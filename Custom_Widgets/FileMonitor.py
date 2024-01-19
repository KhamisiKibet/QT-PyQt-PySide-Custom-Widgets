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

    def on_file_change(self, path):
        print(f"File {path} has been changed!")
        tag = "widget"  # Replace with the actual tag name in your UI file
        attribute = "class"
        old_value = "QPushButton"
        new_value = "QPushButtonThemed"

        root = replace_attribute_value(path, tag, attribute, old_value, new_value)

        self.update_json(root)

    def update_json(self, root):
        tag = "widget"
        attribute = "class"
        value = "QPushButtonThemed"

        # Find all elements with the specified tag and class
        buttons = root.findall(".//{}[@class='{}']".format(tag, value))

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

        # Remove entries for buttons that no longer exist
        existing_button_names = {entry["name"] for entry in self.button_info}
        # updated_button_info = [entry for entry in self.button_info if entry["name"] in existing_button_names]

        # Update the JSON data
        self.button_info = button_data

        # Save the JSON data back to the file
        with open(self.json_file, "w") as json_file:
            json.dump(self.button_info, json_file, indent=2)

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

def replace_attribute_value(ui_file_path, tag, attribute, old_value, new_value):
    # Parse the XML file
    tree = ET.parse(ui_file_path)
    root = tree.getroot()

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

    # Append a custom widget
    append_custom_widget(new_file_path, "QPushButtonThemed", "QPushButton", "Custom_Widgets.Theme.h", 1)
    ui_output_py_path = os.path.join(os.getcwd(), "ui_"+base_name.replace(".ui", "")+".py")
    NewIconsGenerator.uiToPy(new_file_path, ui_output_py_path)

    return root  # Return the root element after modification

def append_custom_widget(ui_file_path, widget_class, widget_extends, widget_header, widget_container):
    # Parse the existing XML file
    tree = ET.parse(ui_file_path)
    root = tree.getroot()

    # Find the customwidgets section or create it if it doesn't exist
    customwidgets_section = root.find(".//customwidgets")
    if customwidgets_section is None:
        customwidgets_section = ET.Element("customwidgets")
        root.append(customwidgets_section)

    # Check if a customwidget with the specified class already exists
    existing_customwidgets = customwidgets_section.findall(".//customwidget[class='{}']".format(widget_class))
    if existing_customwidgets:
        # Custom widget with the specified class already exists, skip
        return

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
