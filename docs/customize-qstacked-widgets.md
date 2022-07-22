# QT-PyQt-PySide-Custom-Widgets - Customizing QStacked Widgets
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![Custom QStacked Widgets](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/qstacked.png?raw=true)

# Customizing QStacked Widgets

The following steps will show you how to customize the look and animation of your QStacked Widgets. 

## 1. Create QStacked Widgets.
You can create a QStacked Widgets directly from your python file or use the QT Designer app. In this demo, we will be using QT Designer app.

### Create user interface containing QStacked Widgets.

![Custom QStacked Widgets QT Designer](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/4.png?raw=true)

- Add the promote class to the QStacked Widget
> Right click on the QStacked then select ``promote to..`` then enter the ``class`` and ``header file`` name as shown below:

![Screenshot_20220722_080559.png](https://www.dropbox.com/s/h35haep9nu4n9ut/Screenshot_20220722_080559.png?dl=0&raw=1)

![Screenshot_20220722_080958.png](https://www.dropbox.com/s/pazrn5kh8tiogb1/Screenshot_20220722_080958.png?dl=0&raw=1)

- Click ``add``, then click ``promote``
 
> To create the above user interface...
Create a folder for your project, "myProject".
Inside this folder, create a file called "interface.ui", and paste the following code in "interface.ui" file. Open the file in QT Designer.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>605</width>
    <height>367</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QCustomStackedWidget" name="myStackedWidget">
      <widget class="QWidget" name="page">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 0, 127);</string>
       </property>
       <widget class="QLabel" name="label">
        <property name="geometry">
         <rect>
          <x>180</x>
          <y>90</y>
          <width>171</width>
          <height>131</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <pointsize>20</pointsize>
         </font>
        </property>
        <property name="text">
         <string>PAGE 1</string>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="page_2">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(85, 255, 255);</string>
       </property>
       <widget class="QLabel" name="label_2">
        <property name="geometry">
         <rect>
          <x>180</x>
          <y>100</y>
          <width>241</width>
          <height>191</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <pointsize>20</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">color: #000;</string>
        </property>
        <property name="text">
         <string>PAGE 2</string>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="page_3">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(25, 25, 25);</string>
       </property>
       <widget class="QLabel" name="label_3">
        <property name="geometry">
         <rect>
          <x>190</x>
          <y>90</y>
          <width>211</width>
          <height>151</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <pointsize>20</pointsize>
         </font>
        </property>
        <property name="text">
         <string>PAGE 3</string>
        </property>
       </widget>
      </widget>
     </widget>
    </item>
    <item>
     <widget class="QFrame" name="frame">
      <property name="frameShape">
       <enum>QFrame::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Raised</enum>
      </property>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QPushButton" name="nxt">
         <property name="text">
          <string>Next</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="page1">
         <property name="text">
          <string>Page 1</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="page2">
         <property name="text">
          <string>Page 2</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="prev">
         <property name="text">
          <string>Previous</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <customwidgets>
  <customwidget>
   <class>QCustomStackedWidget</class>
   <extends>QStackedWidget</extends>
   <header location="global">Custom_Widgets.Widgets.h</header>
   <container>1</container>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
```

- Import your UI python code.
From the QT Designer app, you can generate the user interface python code, but I have already done that for you. So, just create a file inside your project folder, name it "ui_interface.py". Copy and paste the follownig code inside "ui_interface.py".

```python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacedaHCcH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from Custom_Widgets.Widgets import QCustomStackedWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(605, 367)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.myStackedWidget = QCustomStackedWidget(self.centralwidget)
        self.myStackedWidget.setObjectName(u"myStackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 90, 171, 131))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.myStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 100, 241, 191))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #000;")
        self.myStackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 90, 211, 151))
        self.label_3.setFont(font)
        self.myStackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.myStackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nxt = QPushButton(self.frame)
        self.nxt.setObjectName(u"nxt")

        self.horizontalLayout.addWidget(self.nxt)

        self.page1 = QPushButton(self.frame)
        self.page1.setObjectName(u"page1")

        self.horizontalLayout.addWidget(self.page1)

        self.page2 = QPushButton(self.frame)
        self.page2.setObjectName(u"page2")

        self.horizontalLayout.addWidget(self.page2)

        self.prev = QPushButton(self.frame)
        self.prev.setObjectName(u"prev")

        self.horizontalLayout.addWidget(self.prev)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.nxt.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.page1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.page2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.prev.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
    # retranslateUi
```

- Now create a file inside your project folder and name it "main.py". Inside this file, copy and paste the following code.

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
If you run "main.py", your interface should look like this:

![Custom QStacked Widgets QT Designer](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/5.png?raw=true)


## 2. Add Navigations And Animations To QStacked Widgets.
Using QT-PyQt-PySide-Custom-Widgets library, you can easily add navigation functions and animate your Qstacked widgets. This can be achieved directly from your python file or using a JSon file.

### Customize QStacked Widgets from your python file. 

The first step is to import QT-PyQt-PySide-Custom-Widgets library to the python file where you created the QStacked Widgets.

```python
########################################################################
# IMPORT CUSTOM BUTTONS FILE
from Custom_Widgets.Widgets import *
########################################################################
```

#### Adding navigation

QT-PyQt-PySide-Custom-Widgets provides an easy way to navigate through your QStacked widgets.

To navigate to the next widget page:

```python
# myStackedWidget is the name of your stacked widget
# slideToNextWidget() shows the next widget page
myStackedWidget.slideToNextWidget()
```

To navigate to the previous widget page:

```python
# myStackedWidget is the name of your stacked widget
# slideToPreviousWidget() shows the previous widget page
myStackedWidget.slideToPreviousWidget()
```

You can also add click events to your buttons. Assuming you have two buttons named "nxt" and "prev":

```python
# myStackedWidget is the name of your stacked widget
# slideToNextWidget() shows the next widget page
# slideToPreviousWidget() shows the previous widget page
# nxt and prev are navigation buttons
prev.clicked.connect(lambda: myStackedWidget.slideToPreviousWidget())
nxt.clicked.connect(lambda: myStackedWidget.slideToNextWidget())
```

To navigate to a particular page:

```python
# Navigate to page1
myStackedWidget.setCurrentWidget(page1)
```

Navigate to a particular page on button click:

```python
# Navigate to page1 on page1_btn button click
page1_btn.clicked.connect(lambda: myStackedWidget.setCurrentWidget(page1))
```
#### Animating QStacked Widgets

You can add "fade" and "slide" animations to your QStacked widget. You can also fully customize these animations.

##### Fade Animation

Add fade animation to your QStacked widget when transitioning between pages.

```python
########################################################################
## QSTACKWIDGETS FADE ANIMATION
# ######################################################################## 
# Set setFadeTransition to True if you want the pages to fade 
# otherwise set it to False
# The default value is False
myStackedWidget.setFadeTransition(True)
# Set the fade animation duration
myStackedWidget.setFadeSpeed(500)
# Set the fade easing curve
myStackedWidget.setFadeCurve(QtCore.QEasingCurve.Linear)
```

##### Slide Animation

Add slide animation to your QStacked widget when transitioning between pages. Pages can slide horizontally or vertically

```python
########################################################################
## QSTACKWIDGETS SLIDE ANIMATION
# ######################################################################## 
# Set setSlideTransition to True if you want the pages to slide 
# otherwise set it to False
# The default value is False
myStackedWidget.setSlideTransition(True)
# Set the slide animation duration
myStackedWidget.setTransitionSpeed(500)
# Set the slide easing curve
myStackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
```
To slide horizontally:

```python
# Set horizontal page transition between pages
myStackedWidget.setTransitionDirection(QtCore.Qt.Horizontal)
```

To slide vertically:

```python
# Set vertical page transition between pages
myStackedWidget.setTransitionDirection(QtCore.Qt.Vertical)
```

Now lets customize QStacked widget from "main.py" file we created earlier,
Inside this file, copy and paste the following code:

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
from PySide2 import QtCore
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

        ########################################################################
        ## QSTACKWIDGETS NAVIGATION
        ########################################################################
        self.ui.prev.clicked.connect(lambda: self.ui.myStackedWidget.slideToPreviousWidget())
        self.ui.nxt.clicked.connect(lambda: self.ui.myStackedWidget.slideToNextWidget())

        self.ui.page1.clicked.connect(lambda: self.ui.myStackedWidget.setCurrentWidget(self.ui.page))
        self.ui.page2.clicked.connect(lambda: self.ui.myStackedWidget.setCurrentWidget(self.ui.page_2))
        ########################################################################
        ## 
        ########################################################################

        ########################################################################
        ## QSTACKWIDGETS ANIMATION
        # ########################################################################        
        self.ui.myStackedWidget.setTransitionDirection(QtCore.Qt.Vertical)
        self.ui.myStackedWidget.setTransitionSpeed(500)
        self.ui.myStackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
        # ACTIVATE Animation
        self.ui.myStackedWidget.setSlideTransition(True)

        # # Fade animation
        self.ui.myStackedWidget.setFadeSpeed(500)
        self.ui.myStackedWidget.setFadeCurve(QtCore.QEasingCurve.Linear)
        self.ui.myStackedWidget.setFadeTransition(True)
        ########################################################################
        ## 
        ########################################################################

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

RUN "main.py"

### Customize QStacked Widgets from your JSon file. 

The recommended way to customize your QStacked widgets using QT-PyQt-PySide-Custom-Widgets library is through a JSon file. 

Inside your project folder, create a file and name it "style.json". 
Inside this file, create a "QStackedWidget" object which will contain all QStackedWidget names and their custom values.

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget"
		},
		{
			"name":"myStackedWidget_2"
		},
		{
			"name":"myStackedWidget_3"
		}
	]
}
```

#### Adding navigations to QStacked from a JSon file.

Add next("nxt") and previous("prev") button names, which when clicked the QStacked will show the next or previous page from current active page index.

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"navigation":[
				{
					"nextPage":"nxt",
					"previousPage": "prev"
				}
			]
		}
	]
}
```
You can also add other buttons which will navigate to a particular page as shown:
In this example when "page1" button is clicked, "page" page will be shown, when "page2" button is clicked, "page_2" page will be displayed in QStacked widget

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"navigation":[
				{
					"navigationButtons":[
						{
							"page1": "page",
							"page2": "page_2"
						}
					]
				}
			]
		}
	]
}
```

Full navigation exaple will look like this:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"navigation":[
				{
					"nextPage":"nxt",
					"previousPage": "prev",
					"navigationButtons":[
						{
							"page1": "page",
							"page2": "page_2"
						}
					]
				}
			]
		}
	]
}
```

#### Adding transtion animations to QStacked from a JSon file.

Add fade animation:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"fade":[
						{
							"active": true
						}
					]
				}
			]
		}
	]
}
```

Set fade animation duration:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"fade":[
						{
							"duration": 1000
						}
					]
				}
			]
		}
	]
}
```

Set fade animation easing curve:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"fade":[
						{
							"easingCurve": "Linear"
						}
					]
				}
			]
		}
	]
}
```

Full fade animaion customization code will look like this:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"fade":[
						{
							"active": true,
							"duration":1000,
							"easingCurve": "Linear"
						}
					]
				}
			]
		}
	]
}
```

Add Slide animation:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"slide":[
						{
							"active": true
						}
					]
				}
			]
		}
	]
}
```

Set Slide animation duration:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"slide":[
						{
							"duration": 500
						}
					]
				}
			]
		}
	]
}
```

Set Slide animation easing curve:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"slide":[
						{
							"easingCurve": "OutBack"
						}
					]
				}
			]
		}
	]
}
```

##### Set Slide animation easing direction:

Horizontal direction:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"slide":[
						{
							"direction": "horizontal"
						}
					]
				}
			]
		}
	]
}
```

OR vertical direction:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"slide":[
						{
							"direction": "vertical"
						}
					]
				}
			]
		}
	]
}
```

Full slide animaion customization code will look like this:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"slide":[
						{
							"active":true,
							"duration": 500,
							"direction": "horizontal",
							"easingCurve": "OutBack"
						}
					]
				}
			]
		}
	]
}
```

#### The full QStacked JSon customization code:

```json
{
	"QStackedWidget":[
		{
			"name":"myStackedWidget",
			"transitionAnimation":[
				{
					"fade":[
						{
							"active": true,
							"duration":1000,
							"easingCurve": "OutBack"
						}
					],
					"slide":[
						{
							"active":true,
							"duration": 1000,
							"direction": "horizontal",
							"easingCurve": "OutBack"
						}
					]
				}
			],
			"navigation":[
				{
					"nextPage":"nxt",
					"previousPage": "prev",
					"navigationButtons":[
						{
							"page1": "page",
							"page2": "page_2"
						}
					]
				}
			]
	
		}
	]
}
```

## Applying style from JSon file to QStacked widgets

To apply your JSon style from "style.json" to the user inteface, just call loadJsonStyle(ui):

```python
########################################################################
## LOAD QSTACKWIDGETS ANIMATION AND NAVIGATIONS FROM JSON FILE
########################################################################
# ui  is the window class that contains the user interface widgets
loadJsonStyle(self, ui)
```

Now lets apply the JSon stylesheet from "main.py" file we created earlier,
Inside this file, copy and paste the following code:

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

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT CUSTOM WIDGETS MODULE
from Custom_Widgets.Widgets import *
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        ## LOAD QSTACKWIDGETS ANIMATION AND NAVIGATIONS FROM JSON FILE
        ########################################################################
        loadJsonStyle(self, self.ui)
        ########################################################################
        ## 
        ########################################################################

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

RUN "main.py"



# Navigation
[Video Tutorial](https://youtu.be/UHRP5pRZSiU)
[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) 
[Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) 
[Custom Animated Progress Indicator / Progress Bar](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-progress-bar.html)  
[Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html)  
[Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)



