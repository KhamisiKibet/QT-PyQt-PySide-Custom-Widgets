import sys
import os
import json
from qtpy.QtCore import *
from qtpy.QtWidgets import QApplication
from termcolor import colored
import xml.etree.ElementTree as ET
import re

from . Qss.SvgToPngIcons import *

class FileMonitor(QObject):
    def __init__(self, file_to_monitor):
        super().__init__()
        theme_folder = os.path.join(os.getcwd(), "QSS/Theme")
        if not os.path.exists(theme_folder):
            os.makedirs(theme_folder)

        self.file_to_monitor = file_to_monitor
        self.json_file = "QSS/Theme/resources.json"
        self.fileSystemWatcher = QFileSystemWatcher([self.file_to_monitor])
        self.fileSystemWatcher.fileChanged.connect(self.on_file_change)

        self.button_info = []
        self.label_info = []

    def on_file_change(self, path):
        print(f"File {path} has been changed!")
        
        replacements_list = [
            ("widget", "class", "QPushButton", "QPushButtonThemed"),
            ("widget", "class", "QLabel", "QLabelThemed"),
            
        ]

        root = replace_attributes_values(path, replacements_list)

        self.update_json(root)

    def update_json(self, root):
        button_tag = "widget"
        button_attribute = "class"
        button_value = "QPushButtonThemed"

        label_tag = "widget"
        label_attribute = "class"
        label_value = "QLabelThemed"

        # Find all QPushButton elements with the specified tag and class
        buttons = root.findall(".//{}[@class='{}']".format(button_tag, button_value))

        # Find all QLabel elements with the specified tag and class
        labels = root.findall(".//{}[@class='{}']".format(label_tag, label_value))

        # Extract button names and icon URLs
        button_data = []

        for button in buttons:
            button_name = button.get("name")
            iconset_element = button.find(".//iconset")

            if iconset_element is not None and 'resource' in iconset_element.attrib:
                # Extract the QRC file path from the 'resource' attribute
                qrc_file_path = iconset_element.attrib['resource']
                # Extract the folder name containing the QRC file
                qrc_folder = os.path.dirname(qrc_file_path)
                # Combine with the relative path within the <iconset> tag
                relative_path = iconset_element.find("normaloff").text
                icon_url = self.replace_url_prefix(relative_path, qrc_folder)
            else:
                # Handle the case where icon_element is None
                icon_url = "default_icon_url"  # Set a default value or handle it as needed

            button_data.append({"name": button_name, "icon": icon_url})

        # Extract label names and pixmap URLs
        label_data = []

        for label in labels:
            label_name = label.get("name")
            pixmap_element = label.find(".//pixmap")

            if pixmap_element is not None and 'resource' in pixmap_element.attrib:
                # Extract the QRC file path from the 'resource' attribute
                qrc_file_path = pixmap_element.attrib['resource']
                # Extract the folder name containing the QRC file
                qrc_folder = os.path.dirname(qrc_file_path)
                # Combine with the relative path within the <pixmap> tag
                relative_path = pixmap_element.text
                pixmap_url = self.replace_url_prefix(relative_path, qrc_folder)
            else:
                # Handle the case where pixmap_element is None
                pixmap_url = "default_pixmap_url"  # Set a default value or handle it as needed

            label_data.append({"name": label_name, "pixmap": pixmap_url})

        # Remove entries for buttons and labels that no longer exist
        existing_button_names = {entry["name"] for entry in self.button_info}
        existing_label_names = {entry["name"] for entry in self.label_info}
        
        # Update the JSON data for buttons
        self.button_info = button_data

        # Update the JSON data for labels
        self.label_info = label_data

        # Save the JSON data back to the file
        with open(self.json_file, "w") as json_file:
            json.dump({"buttons": self.button_info, "labels": self.label_info}, json_file, indent=2)


    def replace_url_prefix(self, url, new_prefix):
        pattern = re.compile(r':/[^/]+/')
        return pattern.sub( new_prefix + '/', url, 1)


def start_file_listener(file_to_monitor, qt_binding = "PySide6"):

    if qt_binding is None:
        qt_binding = "PySide6"
    if qt_binding not in ["PySide6", "PySide2", "PyQt6", "PyQt5"]:
        print(colored((str(qt_binding) + " is not a valid Qt binding/API Name"), "red"))
        return
    
    qtpy.API_NAME = qt_binding
    os.environ['QT_API'] = qt_binding.lower()
    
    if not file_to_monitor.lower().endswith(".ui"):
        raise ValueError("The file to monitor must be a .ui file.")

    if not os.path.exists(file_to_monitor):
        raise FileNotFoundError(f"The file {file_to_monitor} does not exist.")

    app = QApplication(sys.argv)  # Create a QApplication instance
    print(f"Monitoring file: {file_to_monitor}")
    file_monitor = FileMonitor(file_to_monitor)
    sys.exit(app.exec_())  # Start the application event loop

def replace_attributes_values(ui_file_path, replacements):
    # Parse the XML file
    tree = ET.parse(ui_file_path)
    root = tree.getroot()

    # Find and remove the <resources> element
    resources_elements = root.findall(".//resources")
    for resources_element in resources_elements:
        root.remove(resources_element)

    # Iterate over the replacement specifications
    for tag, attribute, old_value, new_value in replacements:
        # Find all elements with the specified tag
        elements = root.findall(".//{}".format(tag))

        # Replace the attribute value for each matching element
        for element in elements:
            if attribute in element.attrib and element.attrib[attribute] == old_value:
                element.attrib[attribute] = new_value

    # Create a new file name
    base_name, extension = os.path.splitext(os.path.basename(ui_file_path))
    new_file_name = "QSS/Theme/new_{}{}".format(base_name, extension)
    new_file_path = os.path.join(os.path.dirname(ui_file_path), new_file_name)

    # Save the modified XML to the new file
    tree.write(new_file_path, encoding="utf-8", xml_declaration=True)

    # Append custom widgets
    widget_list = [
        ("QPushButtonThemed", "QPushButton", "Custom_Widgets.Theme.h", 1),
        ("QLabelThemed", "QLabel", "Custom_Widgets.Theme.h", 1)
    ]
    append_custom_widgets(new_file_path, widget_list)

    ui_output_py_path = os.path.join(os.getcwd(), "ui_"+base_name.replace(".ui", "")+".py")
    NewIconsGenerator.uiToPy(new_file_path, ui_output_py_path)

    return root  # Return the root element after modification


def append_custom_widgets(ui_file_path, widget_list):
    # Parse the existing XML file
    tree = ET.parse(ui_file_path)
    root = tree.getroot()

    # Find the customwidgets section or create it if it doesn't exist
    customwidgets_section = root.find(".//customwidgets")
    if customwidgets_section is None:
        customwidgets_section = ET.Element("customwidgets")
        root.append(customwidgets_section)

    for widget_spec in widget_list:
        widget_class, widget_extends, widget_header, widget_container = widget_spec

        # Check if a customwidget with the specified class already exists
        existing_customwidgets = customwidgets_section.findall(".//customwidget[class='{}']".format(widget_class))
        if existing_customwidgets:
            # Custom widget with the specified class already exists, skip
            continue

        # Create a new customwidget element
        customwidget = ET.Element("customwidget")

        # Add class, extends, header, and container elements to the customwidget
        class_element = ET.SubElement(customwidget, "class")
        class_element.text = widget_class

        extends_element = ET.SubElement(customwidget, "extends")
        extends_element.text = widget_extends

        header_element = ET.SubElement(customwidget, "header", location="global")
        header_element.text = widget_header

        container_element = ET.SubElement(customwidget, "container")
        container_element.text = str(widget_container)

        # Append the new customwidget to the customwidgets section
        customwidgets_section.append(customwidget)

    # Save the modified XML back to the file
    tree.write(ui_file_path, encoding="utf-8", xml_declaration=True)


def remove_resources_tag(ui_file_path):
    # Parse the XML file
    tree = ET.parse(ui_file_path)
    root = tree.getroot()

    # Find and remove the <resources> element
    resources_elements = root.findall(".//resources")
    for resources_element in resources_elements:
        parent = resources_element.getparent()
        parent.remove(resources_element)

    # Create a new file name
    base_name, extension = os.path.splitext(os.path.basename(ui_file_path))
    new_file_name = "QSS/Theme/new_{}{}".format(base_name, extension)
    new_file_path = os.path.join(os.path.dirname(ui_file_path), new_file_name)

    # Save the modified XML to the new file
    tree.write(new_file_path, encoding="utf-8", xml_declaration=True)

    return root  # Return the root element after modification




if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--monitor-ui":
        print("Usage: Custom_Widgets --monitor-ui <file_to_monitor>")
        sys.exit(1)

    try:
        start_file_listener(sys.argv[2])
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
