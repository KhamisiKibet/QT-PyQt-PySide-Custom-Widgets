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

Using QT Designer:

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
In "Header file" enter "Custom_Widgets.Widgets.h"
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
   <header location="global">Custom_Widgets.Widgets.h</header>
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

from Custom_Widgets.Widgets import FormProgressIndicator


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


You can also add the custom progress bar to the user interace without using QT Designer app:

### Step 1:

Import the custom progress bar the file where you want to create the progress bar:

```python
# IMPORT CUSTOM PROGRESS BAR / PROGRESS INDICATOR
from Custom_Widgets.Widgets import FormProgressIndicator
```

### Step 2:

Create the progress bar:

```python
myProgressBar = FormProgressIndicator(parentContainer)
myProgressBar.setObjectName(u"widget")
# If you have a layout
myLayout.addWidget(myProgressBar)
```

## Customizing and Animating the Custom Progress bar / Progress Indicator

Use the "updateFormProgressIndicator()" function to customize the progress bar.

### Changing font color:

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set font color
    color = "#000"
)
```

### Changing fill color:

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set fill color
    fillColor = "white"
)
```

### Changing fill color "warning":

The custom progress indicator has different steps, each step status can be set individually. For example, if you have a task that is downloading 5 files, the prigress indicator will have five steps. If file one fails to download, then you can set "step 1" to show an error or warning. 
You can also refer to YouTube video upload Form, each step where the correct video information is passed is marked with a check mark, while any step that has an error is marked with a warning sign.

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set fill color for warnings
    warningFillColor = "purple"
)
```

### Changing fill color "errors":

To mark steps where an error occured,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set fill color for errors
    errorFillColor = "red"
)
```

### Changing fill color "success":

To mark steps that completed successfully,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set fill color for success
    successFillColor = "pink"
)
```

### Changing number of steps:

The default value is 5,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set number of progress steps(default is 5)
    formProgressCount = 7
)
```

### Changing progress animation duration:

The default value is 500,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set progress animation duration
    formProgressAnimationDuration = 200
)
```

### Changing progress animation easing curve:

The default value is Linear,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set progress animation easing curve
    formProgressAnimationEasingCurve = "InOutQuint"
)
```

### Changing progress bar height:

The default value is 60,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set progress container height
    height = 80
)
```

### Changing progress bar width:

The default value is 500,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set progress container width
    width = 550
)
```

### Changing progress starting percentage:

The default value is 0,

```python
# CUSTOMIZE FORM PROGRESS INDICATOR
myProgressBar.updateFormProgressIndicator(
    # Set default progress percentage
    startPercentage = 50 #half
)
```

The full progress bar customization code will look like this:

```python
myProgressBar.updateFormProgressIndicator(
    # Set font color
    color = "#000", 
    # Set fill color
    fillColor = "white", 
    # Set fill color for warnings
    warningFillColor = "purple",
    # Set fill color for errors
    errorFillColor = "red",
    # Set fill color for success
    successFillColor = "pink",
    # Set number of progress steps(default is 5)
    formProgressCount = 10,
    # Set progress animation duration
    formProgressAnimationDuration = 2000, #2seconds
    # Set progress animation easing curve
    formProgressAnimationEasingCurve = "InOutQuint",
    # Set progress container height
    height = 80,
    # Set progress container width
    width = 1000,
    # Set default progress percentage
    startPercentage = 50 #half
)
```

### Applying pre-set progress bar themes:

QT-PyQt-PySide-Custom-Widgets has five progress bar themes wich you can apply to your progress bar instead of passing your own colors.
To apply the progress bar theme:

```python
# Slect progress bar theme (range 1-5)
myProgressBar.selectFormProgressIndicatorTheme(4)

## OR
myProgressBar.updateFormProgressIndicator(
    theme = 4
)
```

### Using custom widget's theme engine:
You can also use the custom widget's theme engine to apply the progressbar theme style. The progressbar will inherit the app theme style:

```python
#Inherit app theme style
myProgressBar.updateFormProgressIndicator(
    inheritTheme = True
)
```

You can also specify the colors you want to apply from your theme

```python
#Inherit app theme colors
myProgressBar.updateFormProgressIndicator(
    # NOTE: only choose one color i.e self.theme.COLOR_TEXT_1, self.theme.COLOR_ACCENT_3, self.theme.COLOR_BACKGROUND_5
    
    # Set font color
    color = self.theme.COLOR_TEXT_1 ... self.theme.COLOR_TEXT_4, 
    # Set fill color
    fillColor = self.theme.COLOR_BACKGROUND_1 ..... self.theme.COLOR_BACKGROUND_6, 
    # Set fill color for warnings
    warningFillColor = self.theme.COLOR_ACCENT_1 ... self.theme.COLOR_ACCENT_4,
    # Set fill color for errors
    errorFillColor = self.theme.COLOR_ACCENT_1 ... self.theme.COLOR_ACCENT_4,
    # Set fill color for success
    successFillColor = self.theme.COLOR_ACCENT_1 ... self.theme.COLOR_ACCENT_4
    
)
```

Read more about the [theme engine here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/qt-theme-engine.html)

### Animating progress bar:

In order to animate the progress bar, you have to change the progress value in terms of percentage.

```python
# Animate progress to 60 percent
myProgressBar.animateFormProgress(60) #60 percent 
```

## Updating Progress Step Status

The progress indicator has four status. The default status in "None". You can update each progress step indidually to indicate the status of that step.

### Setting progress step status to "warning":

```python
# UPDATE THE PROGRESS STEP STATUS
myProgressBar.setStepStatus(
	# Step 2
    step_2_warning = True
)
```

### Setting progress step status to "error":

```python
# UPDATE THE PROGRESS STEP STATUS
myProgressBar.setStepStatus(
	# Step 5
    step_5_error = True
)
```

### Setting progress step status to "success":

```python
# UPDATE THE PROGRESS STEP STATUS
myProgressBar.setStepStatus(
	# Step 3
    step_3_success = True
)
```

Now to upadate multiple step status, you can write something like this:

```python
# UPDATE THE PROGRESS STEP STATUS
self.ui.widget.setStepStatus(
    # Step 5
    step_5_error = True,
    # Step 2
    step_2_warning = True,
    # Step 3
    step_3_success = True
)
```

Another alternative way to update the progress step stays is to use "setStepStatus()" function.

```python
# UPDATE THE PROGRESS STEP STATUS USING setStepStatus()
myProgressBar.setStepStatus(
	# progress step number
	step = 3,
	# Status ["warning", "error", "success"]
	status = "error",
	# Satus value [True, False]
	value = True
)
```

To reset the progress status, use "setStepStatus()" and set the value to "False".

### Reset progress step status:

Reset progress status for step 3:

Warning:

```python
# UPDATE THE PROGRESS STEP STATUS USING setStepStatus()
myProgressBar.setStepStatus(
	# progress step number
	step = 3,
	# Status ["warning", "error", "success"]
	status = "warning",
	# Satus value [True, False]
	value = False
)
```

Error:

```python
# UPDATE THE PROGRESS STEP STATUS USING setStepStatus()
myProgressBar.setStepStatus(
	# progress step number
	step = 3,
	# Status ["warning", "error", "success"]
	status = "error",
	# Satus value [True, False]
	value = False
)
```

Success:

```python
# UPDATE THE PROGRESS STEP STATUS USING setStepStatus()
myProgressBar.setStepStatus(
	# progress step number
	step = 3,
	# Status ["warning", "error", "success"]
	status = "success",
	# Satus value [True, False]
	value = False
)
```

# Add and customize your progress bar using a JSon File.

[Read here on how to generate a project using the project creator](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/project-maker.html). Skip this part if your app already has a "json stylesheet" for the custom widgets.

Once you have created your project, you can customize your progressbar from a json file as shown:

```json
{
   "FormProgressIndicator": [
        {
            "name": "myProgressBar",
            "color": "THEME.COLOR_TEXT_1",
            "fillColor": "THEME.COLOR_BACKGROUND_2",
            "warningFillColor": "THEME.COLOR_ACCENT_3",
            "errorFillColor": "THEME.COLOR_ACCENT_2",
            "successFillColor": "THEME.COLOR_ACCENT_1",
            "formProgressCount": 5,
            "formProgressAnimationDuration": 2000,
            "formProgressAnimationEasingCurve": "OutBack",
            "height": 5,
            "width": 500,
            "startPercentage": 0,
            "theme": 3,
            "inheritTheme": true
        }
    ]
}
```

- "name" : your widget name
- "color": the text color, in this case "THEME.COLOR_TEXT_1" is the theme text color. You can also pass a hex value ie "#fff". This also applies to "fillColor", "warningFillColor", "errorFillColor" and "successFillColor".
- You can also ignore the above colors and apply one of the preset themes(We applied theme 3)
- You can make your progressbar inherit the theme style without specifying a preset theme or theme colors by using "inheritTheme" bool, set it to true. 

Json style for multiple progressbar might look like this:
```json
{
   "FormProgressIndicator": [
        {
            "name": "myProgressBar",
            "color": "THEME.COLOR_TEXT_1",
            "fillColor": "THEME.COLOR_BACKGROUND_2",
            "warningFillColor": "THEME.COLOR_ACCENT_3",
            "errorFillColor": "THEME.COLOR_ACCENT_2",
            "successFillColor": "THEME.COLOR_ACCENT_1",
            "formProgressCount": 5,
            "formProgressAnimationDuration": 2000,
            "formProgressAnimationEasingCurve": "OutBack",
            "height": 5,
            "width": 500,
            "startPercentage": 0
        },
        {
            "name": "myProgressBar2",
            "formProgressCount": 10,
            "formProgressAnimationDuration": 1000,
            "formProgressAnimationEasingCurve": "OutBack",
            "height": 5,
            "width": 600,
            "startPercentage": 10,
            "theme": 3,
        },
        {
            "name": "myProgressBar3",
            "formProgressCount": 5,
            "formProgressAnimationDuration": 2000,
            "formProgressAnimationEasingCurve": "OutBack",
            "height": 5,
            "width": 500,
            "startPercentage": 0,
            "inheritTheme": true
        },
        {
            "name": "myProgressBar4",
            "color": "#fff",
            "fillColor": "#000",
            "warningFillColor": "#E41F1F",
            "errorFillColor": "#E4E41F",
            "successFillColor": "#1FE430",
            "formProgressCount": 5,
            "formProgressAnimationDuration": 2000,
            "formProgressAnimationEasingCurve": "Linear",
            "height": 5,
            "width": 500,
            "startPercentage": 0
        },
    ]
}
```

# Examples

Copy and paste the follong code examples to "main.py" file we created earlier:

Example 1:

![Qt Progress bar example](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/13.png?raw=true)

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


        #######################################################################
        # CUSTOMIZE PROGRESS BAR
        #######################################################################
        self.ui.widget.updateFormProgressIndicator(
            # Set font color
            color = "#000", 
            # Set fill color
            fillColor = "white", 
            # Set fill color for warnings
            warningFillColor = "purple",
            # Set fill color for errors
            errorFillColor = "red",
            # Set fill color for success
            successFillColor = "pink",
            # Set number of progress steps(default is 5)
            formProgressCount = 10,
            # Set progress animation duration
            formProgressAnimationDuration = 2000, #2seconds
            # Set progress animation easing curve
            formProgressAnimationEasingCurve = "InOutQuint",
            # Set progress container height
            height = 80,
            # Set progress container width
            width = 1000,
            # Set default progress percentage
            startPercentage = 50 #half
        )


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

Example 2

![Qt Progress bar example](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/14.png?raw=true)

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


        #######################################################################
        # CUSTOMIZE PROGRESS BAR
        #######################################################################

        # Slect progress bar theme (range 1-5)
        self.ui.widget.selectFormProgressIndicatorTheme(5)

        # Animate progress to 60 percent
        self.ui.widget.animateFormProgress(60) #60 percent 


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

Example 3:

![Qt Progress bar example](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/15.png?raw=true)

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


        #######################################################################
        # CUSTOMIZE PROGRESS BAR
        #######################################################################

        # Slect progress bar theme (range 1-5)
        self.ui.widget.selectFormProgressIndicatorTheme(3)

        # Animate progress to 60 percent
        self.ui.widget.animateFormProgress(100) #60 percent 

        # UPDATE THE PROGRESS STEP STATUS
        self.ui.widget.setStepStatus(
            # Step 5
            step_5_error = True,
            # Step 2
            step_2_warning = True,
            # Step 3
            step_3_success = True
        )


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


# Navigation
[Video Tutorial 1](https://youtu.be/0jw4ZT6mH_w) [Video Tutorial 2](https://youtu.be/CEsUlUD1_sE) [HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/)  [Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html)  [Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) [Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html)  [Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)




