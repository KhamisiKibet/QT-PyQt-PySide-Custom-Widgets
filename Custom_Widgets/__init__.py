## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
import os
import __main__

from Custom_Widgets.Qss import SassCompiler
CompileStyleSheet = SassCompiler.CompileStyleSheet
from Custom_Widgets.Qss.SvgToPngIcons import NewIconsGenerator
from Custom_Widgets.Theme import setNewIcon, setNewPixmap, setNewTabIcon

from qtpy import QtWidgets, QtGui, QtCore
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
from qtpy.QtCore import Signal

import json
import re

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.JSonStyles import loadJsonStyle

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

class QMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.clickPosition = None  # Initialize clickPosition attribute
        self.normalGeometry = self.geometry()

        self.iconsWorker = None
        self.allIconsWorker = None

        QCoreApplication.instance().aboutToQuit.connect(self.stopWorkers)
    
    # Add mouse events to the window
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
        # Hide floating widgets
        cursor = QtGui.QCursor()
        xPos = cursor.pos().x()
        yPos = cursor.pos().y()
        if hasattr(self, "floatingWidgets"):
            for x in self.floatingWidgets:
                if hasattr(x, "autoHide") and x.autoHide:
                    x.collapseMenu()

    # Update restore button icon on maximizing or minimizing window
    def updateRestoreButtonIcon(self):
        settings = QSettings()
        if settings.value("ICONS-COLOR") is not None:
            normal_color = settings.value("ICONS-COLOR")
            icons_folder = normal_color.replace("#", "")

            prefix_to_remove = re.compile(r'^Qss/icons/[^/]+/')
            self.maximizedIcon = re.sub(prefix_to_remove, 'Qss/icons/'+icons_folder+'/', self.maximizedIcon)
            self.normalIcon = re.sub(prefix_to_remove, 'Qss/icons/'+icons_folder+'/', self.normalIcon)

        # If window is maxmized
        if self.isMaximized():
            # Change Iconload
            if len(str(self.maximizedIcon)) > 0:
                # self.restoreBtn.setIcon(QtGui.QIcon(str(self.maximizedIcon)))
                self.restoreBtn.setNewIcon(str(self.maximizedIcon))
        else:
            # Change Icon
            if len(str(self.normalIcon)) > 0:
                # self.restoreBtn.setIcon(QtGui.QIcon(str(self.normalIcon)))
                self.restoreBtn.setNewIcon(str(self.normalIcon))

    def restore_or_maximize_window(self):
        # If window is maximized
        if self.isMaximized():
            self.showNormal()
        else:
            # Save the current window geometry before maximizing
            self.normalGeometry = self.geometry()

            self.showMaximized()

        self.updateRestoreButtonIcon()

    def showNormal(self):
        super().showNormal()

        # Restore the window to its previous position and size
        if hasattr(self, 'normalGeometry'):
            self.setGeometry(self.normalGeometry)
            del self.normalGeometry

    # Function to Move window on mouse drag event on the tittle bar
    def moveWindow(self, e):
        # Detect if the window is  normal size
        if not self.isMaximized(): #Not maximized
            # Move window only when window is normal size
            #if left mouse button is clicked (Only accept left mouse button clicks)
            if e.buttons() == Qt.LeftButton:
                #Move window
                if self.clickPosition is not None:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

            self.normalGeometry = self.geometry()
        # else:
        #     self.showNormal()

    def toggleWindowSize(self, e):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self.updateRestoreButtonIcon()

    ## Check Button Groups
    def checkButtonGroup(self):
        btn = self.sender()
        group = btn.group
        groupBtns = getattr(self, "group_btns_"+str(group))
        active = getattr(self, "group_active_"+str(group))
        notActive = getattr(self, "group_not_active_"+str(group))

        for x in groupBtns:
            if not x == btn:
                x.setStyleSheet(notActive)
                x.active = False

        btn.setStyleSheet(active)
        btn.active = True

    def compileSassTheme(self, progress_callback):
        ## GENERATE NEW ICONS FOR CURRENT THEME
        NewIconsGenerator.generateNewIcons(self, progress_callback)

    def makeAllIcons(self, progress_callback):
        ## GENERATE ALL ICONS FOR ALL THEMES
        NewIconsGenerator.generateAllIcons(self, progress_callback)

    def sassCompilationProgress(self, n):
        pass
        # self.ui.activityProgress.setValue(n)
        
    def readJsonFile(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def applyIcons(self, folder):
        jsonFilesFolder = os.path.abspath(os.path.join(os.getcwd(), "generated-files/json"))
        if not os.path.exists(jsonFilesFolder):
            os.makedirs(jsonFilesFolder)
        prefix_to_remove = re.compile(r'icons(.*?)Icons')

        # Define a list of widget classes and their corresponding setter methods
        widget_classes = {
            "QPushButton": "setNewIcon",
            "QCheckBox": "setNewIcon",
            "QCustomCheckBox": "setNewIcon",
            "QWidget": None,  # No specific setter method for QWidget
            "QLabel": "setNewPixmap",
        }

        # Iterate over each JSON file in the folder
        for jsonFile in os.listdir(jsonFilesFolder):
            if jsonFile.endswith(".json"):
                jsonFilePath = os.path.join(jsonFilesFolder, jsonFile)

                # Read the JSON file
                widget_data = self.readJsonFile(jsonFilePath)

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

                        # Check if the icon URL is valid and the widget exists in the UI
                        if icon_url != "default_icon_url" and hasattr(self.ui, str(widget_name)):
                            widget = getattr(self.ui, str(widget_name))

                            # Check if the widget is of the current class and if there's a setter method defined
                            if isinstance(widget, globals()[widget_class]) and setter_method:
                                # Call the setter method to apply the icon/pixmap
                                getattr(widget, setter_method)(icon_url)
                            
                            # Handle QTabWidget separately
                            elif widget_class == "QWidget" and "QTabWidget" in widget_info:
                                parent_name = widget_info.get("QTabWidget", "")
                                parent = getattr(self.ui, str(parent_name))

                                if isinstance(parent, QTabWidget):
                                    parent.setNewTabIcon(widget_name, icon_url)

    def stopWorkers(self):
        if self.iconsWorker is not None:
            self.iconsWorker.stop()

        if self.allIconsWorker is not None:
            self.allIconsWorker.stop()

def mouseReleaseEvent(self, QMouseEvent):
    cursor = QtGui.QCursor()
    # self.ui.frame.setGeometry(QRect(cursor.pos().x(), cursor.pos().y(), 151, 111))

def navigationButtons(stackedWidget, pushButton, widgetPage):
    pushButton.clicked.connect(lambda: stackedWidget.setCurrentWidget(widgetPage))
