# QT-PyQt-PySide-Custom-Widgets - Custom Progress Bar / Form Progress Indicator
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![Custom Qt Progress Bar](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/progressbar.png?raw=true)

# Custom Progress Bar / Form Progress Indicator

QT-PyQt-PySide-Custom-Widgets offers a simple way you can add a custom progress bar to your user interface.
The progress bar can be used to indicate the progress of activities such as background tasks or form filling progress and status.

This guide will show you how to add this progress bar to the user interface.

To view some examples of these progess bars, run the following code from your terminal/command line or inside a python file:

```python
# VIEW PROGRESS BAR EXAMPLES
from Custom_Widgets.ProgressIndicator import test
test.main()
```

## Adding Custom Progress Bar / Form Progress Indicator To The User Interface

### Step 1:
Open QT Designer app, create the "Main Window".

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/6.png?raw=true)

### Step 2:
Add "QWidget" container to your "centralwidget" or a container of your choice.

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/7.png?raw=true)

Set the width and height of your widget, alternatively you can set the layout of the container, in this case it is the "centralwidget" 

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/8.png?raw=true)

### Step 3:
Right click on the "widget" the click "promote to". The promote window will appear.
In "Base Class Name" select "QWidget"
In "Promoted class name" field enter "FormProgressIndicator"
In "Header file" enter "Custom_Widgets.widgets.h"
Then Click on "Add" buton

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/9.png?raw=true)

Check the "Global Include" check mark,

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/10.png?raw=true)

Now select the promoted class you just added then click on "Promote" button,

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/11.png?raw=true)


Save the UI file then generate the interface pyhon code. 

This is the UI code, you can copy it and save it as "interface.ui", then open it in QT Designer:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>469</width>
    <height>448</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="FormProgressIndicator" name="widget" native="true"/>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>469</width>
     <height>30</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>FormProgressIndicator</class>
   <extends>QWidget</extends>
   <header location="global">Custom_Widgets.widgets.h</header>
   <container>1</container>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>


```
This is how my user interface pyhon code looks like, you can copy it, create a file and name it "ui_interface.py":

```python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceBmpbGI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.widgets import FormProgressIndicator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 448)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = FormProgressIndicator(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi


```

### Step 4:

Create the "main.py" file, then import the user interace. 
This is my "main.py" file:

```python
########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
from PySide2.QtCore import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        ########################################################################


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  

```

If you run "main.py", you will get something like this:

![Qt Custom Progress Bar Default Look](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/12.png?raw=true)




