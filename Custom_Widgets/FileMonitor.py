import sys
import os
import json
from qtpy.QtCore import QObject, QFileSystemWatcher
from qtpy.QtWidgets import QApplication
from termcolor import colored
import xml.etree.ElementTree as ET
from lxml import etree
import re

from Custom_Widgets.Qss.SvgToPngIcons import *

from Custom_Widgets.QAppSettings import QAppSettings

class FileMonitor(QObject):
    def __init__(self, files_to_monitor):
        super().__init__()
        file_folder = os.path.join(os.getcwd(), "generated-files")
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)
        file_folder = os.path.join(os.getcwd(), "generated-files/ui")
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)
        file_folder = os.path.join(os.getcwd(), "generated-files/json")
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)
        file_folder = os.path.join(os.getcwd(), "src")
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)

        self.files_to_monitor = files_to_monitor

        # Create a QFileSystemWatcher for each file
        self.fileSystemWatchers = [QFileSystemWatcher([file]) for file in self.files_to_monitor]

        # Connect the fileChanged signal for each watcher
        for watcher in self.fileSystemWatchers:
            watcher.fileChanged.connect(self.on_file_change)

        self.button_info = []
        self.label_info = []

    def on_file_change(self, path):
        print(f"File {path} has been changed!")
        # Find the index of the changed file
        index = -1
        for i, watcher in enumerate(self.fileSystemWatchers):
            if path in watcher.files():
                index = i
                break

        if index != -1:
            convert_file(path)
    
def convert_file(path):
    # Load the UI file
    tree = etree.parse(path)
    root = tree.getroot()

    # Initialize an empty dictionary to store widget names and their icons
    widget_info = {}

    # Iterate through each element in the UI file
    for element in root.iter():
        if 'name' in element.attrib and (element.attrib['name'] == 'icon' or element.attrib['name'] == "windowIcon"):
            widget = element.getparent()  # Get the parent widget
            widget_class = widget.get('class')  # Get the widget class
            widget_name = widget.get('name')  # Get the widget name
            
            iconset_element = element.find('iconset')

            if iconset_element is not None:
                if 'resource' in iconset_element.attrib:
                    # Extract the QRC file path from the 'resource' attribute
                    qrc_file_path = iconset_element.attrib['resource']
                    # Extract the folder name containing the QRC file
                    qrc_folder = os.path.dirname(qrc_file_path)
                    # Combine with the relative path within the <iconset> tag
                    relative_path = iconset_element.find("normaloff").text
                    icon_url = replace_url_prefix(relative_path, qrc_folder)

                else:
                    icon_url = generate_relative_path(path, iconset_element.find("normaloff").text)
                
                # Check if the widget's parent is a QTabWidget
                parent_widget = widget.getparent()
                if parent_widget.tag == 'widget' and parent_widget.get('class') == 'QTabWidget':
                    # Get the tab name
                    tab_name = parent_widget.get('name')
                    # Add the widget info to the dictionary
                    if widget_class in widget_info:
                        widget_info[widget_class].append({"QTabWidget": tab_name, "name": widget_name, "icon": icon_url})
                    else:
                        widget_info[widget_class] = [{"QTabWidget": tab_name, "name": widget_name, "icon": icon_url}]
                else:
                    # Add the widget info to the dictionary
                    if widget_class in widget_info:
                        widget_info[widget_class].append({"name": widget_name, "icon": icon_url})
                    else:
                        widget_info[widget_class] = [{"name": widget_name, "icon": icon_url}]
        
        if 'name' in element.attrib and element.attrib['name'] == 'pixmap':
            widget = element.getparent()  # Get the parent widget
            widget_class = widget.get('class')  # Get the widget class
            widget_name = widget.get('name')  # Get the widget name
            
            pixmap_element = element.find('pixmap')
            
            if pixmap_element is not None:
                if 'resource' in pixmap_element.attrib:
                    # Extract the QRC file path from the 'resource' attribute
                    qrc_file_path = pixmap_element.attrib['resource']
                    # Extract the folder name containing the QRC file
                    qrc_folder = os.path.dirname(qrc_file_path)
                    # Combine with the relative path within the <pixmap> tag
                    relative_path = pixmap_element.text
                    pixmap_url = replace_url_prefix(relative_path, qrc_folder)
                else:
                    pixmap_url = generate_relative_path(path, pixmap_element.text)

                # Add the widget info to the dictionary
                if widget_class in widget_info:
                    widget_info[widget_class].append({"name": widget_name, "pixmap": pixmap_url})
                else:
                    widget_info[widget_class] = [{"name": widget_name, "pixmap": pixmap_url}]


    # Generate JSON file name from UI name
    base_name, _ = os.path.splitext(os.path.basename(path))
    json_file_name = f"{base_name}.json"

    # Update JSON data for the specific file
    update_json(widget_info, json_file_name)

    replacements_list = [
        # ("widget", "class", "QPushButton", "QPushButtonThemed"),
        # ("widget", "class", "QLabel", "QLabelThemed"),
    ]
    root = replace_attributes_values(path, replacements_list)

def update_json(data, json_file_name):
    # Save the JSON data back to the file
    json_path = os.path.join(os.getcwd(), "generated-files/json/"+json_file_name)
    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

def generate_relative_path(ui_path, relative_url):
    # Determine the directory of the UI file
    ui_dir = os.path.dirname(ui_path)
    
    # Combine UI directory with the relative URL
    abs_path = os.path.abspath(os.path.join(ui_dir, relative_url))
    
    return abs_path

def replace_url_prefix(url, new_prefix):
    pattern = re.compile(r':/[^/]+/')
    url = pattern.sub( new_prefix + '/', url, 1)
    return re.sub(r'^\.\./', '', url)
    
def start_file_listener(file_or_folder, qt_binding="PySide6"):
    if qt_binding is None:
        qt_binding = "PySide6"
    if qt_binding not in ["PySide6", "PySide2", "PyQt6", "PyQt5"]:
        print(colored((str(qt_binding) + " is not a valid Qt binding/API Name"), "red"))
        return

    qtpy.API_NAME = qt_binding
    os.environ['QT_API'] = qt_binding.lower()

    files_to_monitor = []

    if os.path.isfile(file_or_folder):
        # If the provided path is a file, check if it's a .ui file
        if not file_or_folder.lower().endswith(".ui"):
            raise ValueError("The file to monitor must be a .ui file.")
        if not os.path.exists(file_or_folder):
            raise FileNotFoundError(f"The file {file_or_folder} does not exist.")

        files_to_monitor.append(file_or_folder)
        print(f"Monitoring file: {file_or_folder}")

    elif os.path.isdir(file_or_folder):
        # If the provided path is a directory, get all .ui files in the folder
        ui_files = [f for f in os.listdir(file_or_folder) if f.lower().endswith(".ui")]

        if not ui_files:
            print("No .ui files found in the specified folder.")
            return

        print(f"Monitoring files in folder: {file_or_folder}")
        print(f".ui files found: {', '.join(ui_files)}")
        for ui_file in ui_files:
            file_path = os.path.join(file_or_folder, ui_file)
            files_to_monitor.append(file_path)

    else:
        print("Invalid path. Please provide a valid .ui file or folder.")
        return

    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create a FileMonitor instance with the list of files to monitor
    file_monitor = FileMonitor(files_to_monitor)

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
    new_file_name = "new_{}{}".format(base_name, extension)
    new_file_path = os.path.join(os.getcwd(), "generated-files/ui/"+new_file_name)

    # Save the modified XML to the new file
    tree.write(new_file_path, encoding="utf-8", xml_declaration=True)

    # Append custom widgets
    widget_list = [
        ("QPushButton", "QPushButton", "Custom_Widgets.Theme.h", 1),
        ("QLabel", "QLabel", "Custom_Widgets.Theme.h", 1)
    ]
    append_custom_widgets(new_file_path, widget_list)

    ui_output_py_path = os.path.join(os.getcwd(), "src/ui_"+base_name.replace(".ui", "")+".py")
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
    new_file_name = "generated-files/ui/new_{}{}".format(base_name, extension)
    new_file_path = os.path.join(os.path.dirname(ui_file_path), new_file_name)

    # Save the modified XML to the new file
    tree.write(new_file_path, encoding="utf-8", xml_declaration=True)

    return root  # Return the root element after modification


def start_ui_conversion(file_or_folder, qt_binding="PySide6"):
    if qt_binding is None:
        qt_binding = "PySide6"
    if qt_binding not in ["PySide6", "PySide2", "PyQt6", "PyQt5"]:
        print(colored((str(qt_binding) + " is not a valid Qt binding/API Name"), "red"))
        return

    qtpy.API_NAME = qt_binding
    os.environ['QT_API'] = qt_binding.lower()

    files_to_convert = []

    if os.path.isfile(file_or_folder):
        # If the provided path is a file, check if it's a .ui file
        if not file_or_folder.lower().endswith(".ui"):
            raise ValueError("The file to monitor must be a .ui file.")
        if not os.path.exists(file_or_folder):
            raise FileNotFoundError(f"The file {file_or_folder} does not exist.")

        files_to_convert.append(file_or_folder)
        print(f"Converting file: {file_or_folder}")

    elif os.path.isdir(file_or_folder):
        # If the provided path is a directory, get all .ui files in the folder
        ui_files = [f for f in os.listdir(file_or_folder) if f.lower().endswith(".ui")]

        if not ui_files:
            print("No .ui files found in the specified folder.")
            return

        print(f"Converting files in folder: {file_or_folder}")
        print(f".ui files found: {', '.join(ui_files)}")
        for ui_file in ui_files:
            file_path = os.path.join(file_or_folder, ui_file)
            files_to_convert.append(file_path)

    else:
        print("Invalid path. Please provide a valid .ui file or folder.")
        return
    
    file_folder = os.path.join(os.getcwd(), "src")
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
    file_folder = os.path.join(os.getcwd(), "generated-files/ui")
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
    file_folder = os.path.join(os.getcwd(), "generated-files/json")
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)
    
    [convert_file(file) for file in files_to_convert]

    print("Done converting!")


class QSsFileMonitor():
    def __init__(self, parent=None):
        super(QSsFileMonitor, self).__init__(parent)

    def start_qss_file_listener(self):
        if self.liveCompileQss:
            logInfo(self, "Live monitoring Qss/scss/defaultStyle.scss file for changes")
            default_sass_path = os.path.abspath(os.path.join(os.getcwd(), 'Qss/scss/defaultStyle.scss'))

            if os.path.isfile(default_sass_path):
                # Monitor defaultStyle.scss file for changes
                self.qss_watcher = QFileSystemWatcher()
                self.qss_watcher.addPath(default_sass_path)

                # Monitor JSON style sheets for changes
                for json_file in self.jsonStyleSheets:
                    json_file_path = os.path.abspath(os.path.join(os.getcwd(), json_file))
                    if os.path.isfile(json_file_path):
                        self.qss_watcher.addPath(json_file_path)

                        logInfo(self, f"Live monitoring {json_file} for changes")
                    else:
                        logError(self, f"Error: JSON file {json_file} not found")
                
                self.qss_watcher.fileChanged.connect(lambda path=default_sass_path: QSsFileMonitor.qss_file_changed(self, path))

            else:
                logError(self, "Error: Qss/scss/defaultStyle.scss file not found")


    def qss_file_changed(self, file_path):
        logInfo(self, f"File changed: {file_path}")

        # # Check if the file extension is '.json'
        # if file_path.endswith('.json'):
        #     # reload jsons
        #     self.reloadJsonStyles(update = True)
        # else:
        #     # Apply compiled stylesheet
        #     QAppSettings.updateAppSettings(self)

        QAppSettings.updateAppSettings(self)

    def stop_qss_file_listener(self):
        if hasattr(self, 'qss_watcher'):
            # Disconnect the fileChanged signal from the qss_file_changed slot
            self.qss_watcher.fileChanged.disconnect(QSsFileMonitor.qss_file_changed)
            self.qss_watcher.deleteLater()
            del self.qss_watcher



    
