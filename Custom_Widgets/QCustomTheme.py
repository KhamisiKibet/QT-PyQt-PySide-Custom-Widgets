import os
import re
import json
import sys

from qtpy.QtWidgets import QApplication, QPushButton, QLabel, QTabWidget, QCheckBox, QToolBox, QWidget
from qtpy.QtGui import QPalette, QCursor
from qtpy.QtCore import QRect, Signal, QObject, QSettings

from Custom_Widgets.Theme import setNewIcon, setNewPixmap, setNewTabIcon, setNewToolBoxIcon
from Custom_Widgets.QCustomCheckBox import QCustomCheckBox

# Monkey patching QPushButton class to add setNewIcon method
QPushButton.iconUrl = None
QPushButton.setNewIcon = setNewIcon

QCheckBox.iconUrl = None
QCheckBox.setNewIcon = setNewIcon

QCustomCheckBox.iconUrl = None
QCustomCheckBox.setNewIcon = setNewIcon


QLabel.piximapUrl = None
QLabel.setNewPixmap = setNewPixmap

QTabWidget.setNewTabIcon = setNewTabIcon
QToolBox.setNewItemIcon = setNewToolBoxIcon

class QCustomTheme(QObject):
    # Define a class-level signal
    onThemeChanged = Signal()

    def __init__(self):
        super().__init__()
        # self.onThemeChanged.connect(print("theme changed"))
        self._theme = "default"
    
    @property
    def theme(self):
        settings = QSettings()
        theme = settings.value("THEME")
        if theme:
            self._theme = theme
        return self._theme
    
    def setTheme(self, value):
        self._theme = value
        settings = QSettings()
        settings.setValue("THEME", value)
        
        self.onThemeChanged.emit()  # Emit the signal when theme is modified

    def themeChanged(self):
        # Emit the signal from the instance
        self.onThemeChanged.emit()

    @staticmethod
    def isAppDarkThemed():
        app = QApplication.instance()
        if app is None:
            raise RuntimeError("QApplication instance is required.")
        
        palette = app.palette()
        
        # Extract the background color of the application palette
        background_color = palette.color(QPalette.Window)
        
        # Calculate luminance using the YIQ color space formula
        luminance = (0.299 * background_color.red() + 0.587 * background_color.green() + 0.114 * background_color.blue()) / 255
        
        # Determine if the background color is considered dark or light
        if luminance < 0.5:
            return True  # Dark theme
        else:
            return False  # Light theme
        
    @staticmethod
    def getCurrentScreen():
        """ get current screen """
        cursorPos = QCursor.pos()

        for s in QApplication.screens():
            if s.geometry().contains(cursorPos):
                return s

        return None

    @staticmethod
    def getCurrentScreenGeometry(avaliable=True):
        """ get current screen geometry """
        screen = QCustomTheme.getCurrentScreen() or QApplication.primaryScreen()

        # this should not happen
        if not screen:
            return QRect(0, 0, 1920, 1080)

        return screen.availableGeometry() if avaliable else screen.geometry()
    
    @staticmethod
    def readJsonFile(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    
    @staticmethod
    def applyIcons(self, folder=None, ui_file_name = None):
        settings = QSettings()
        if not folder:
            folder = settings.value("ICONS-COLOR").replace("#", "")
        current_script_folder = os.path.dirname(os.path.realpath(sys.argv[0]))
        jsonFilesFolder = os.path.abspath(os.path.join(current_script_folder, "generated-files/json"))
        if not os.path.exists(jsonFilesFolder):
            os.makedirs(jsonFilesFolder)
        
        # Case insensitive version of the regular expression pattern
        prefix_to_remove = re.compile(r'icons(.*?)icons', re.IGNORECASE)

        # Define a list of widget classes and their corresponding setter methods
        widget_classes = {
            "QPushButton": "setNewIcon",
            "QCheckBox": "setNewIcon",
            "QCustomCheckBox": "setNewIcon",
            "QWidget": None,  # No specific setter method for QWidget
            "QLabel": "setNewPixmap"        }

        # Iterate over each JSON file in the folder
        for jsonFile in os.listdir(jsonFilesFolder):
            if jsonFile.endswith(".json"):
                if ui_file_name:
                    # if json filename matches ui filename(remove json extension)
                    json_filename_without_extension = os.path.splitext(jsonFile)[0]
                    if json_filename_without_extension == ui_file_name:
                        jsonFilePath = os.path.join(jsonFilesFolder, jsonFile)
                    else:
                        continue
                else:
                    jsonFilePath = os.path.join(jsonFilesFolder, jsonFile)

                # Read the JSON file
                widget_data = QCustomTheme.readJsonFile(jsonFilePath)

                # Iterate over each widget class in the dictionary
                for widget_class, setter_method in widget_classes.items():
                    # Get the list of widget info for the current class
                    widgets_info = widget_data.get(widget_class, [])

                    # Iterate over each widget info
                    for widget_info in widgets_info:
                        widget_name = widget_info.get("name", "")
                        icon_url = widget_info.get("icon", "") if widget_info.get("icon", "") else widget_info.get("pixmap", "")

                        # Adjust the icon URL
                        icon_url = re.sub(prefix_to_remove, 'icons/'+folder, icon_url)

                        abs_icon_url = os.path.abspath(os.path.join(current_script_folder, icon_url))

                        # Check if the icon URL is valid and the widget exists in the UI
                        if abs_icon_url != "default_icon_url" and hasattr(self.ui, str(widget_name)):
                            widget = getattr(self.ui, str(widget_name))

                            # Check if the widget is of the current class and if there's a setter method defined
                            if isinstance(widget, globals()[widget_class]) and setter_method:
                                # Call the setter method to apply the icon/pixmap
                                getattr(widget, setter_method)(abs_icon_url)
                            
                            # Handle QTabWidget separately
                            elif widget_class == "QWidget" and "QTabWidget" in widget_info:
                                parent_name = widget_info.get("QTabWidget", "")
                                parent = getattr(self.ui, str(parent_name))

                                if isinstance(parent, QTabWidget):
                                    parent.setNewTabIcon(widget_name, abs_icon_url)
                            
                            # Handle QToolBox separately
                            elif widget_class == "QWidget" and "QToolBox" in widget_info:
                                parent_name = widget_info.get("QToolBox", "")
                                parent = getattr(self.ui, str(parent_name))

                                if isinstance(parent, QToolBox):
                                    parent.setNewItemIcon(widget_name, abs_icon_url)
