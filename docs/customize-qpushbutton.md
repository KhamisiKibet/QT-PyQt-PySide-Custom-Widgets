# QT-PyQt-PySide-Custom-Widgets - Customizing QPushButtons
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![Custom QPushButtons](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/qpushbutton.png?raw=true)

# Customizing QPushButtons

The following steps will show you how to customize the look and animation of your QPushButtons. 

## 1. Create QPushButton object/widget.
You can create a QPushButton object directly from your python file or use the QT Designer app. 

From Python file:
```python 
	
# CREATE BUTTON
myButton = QPushButton(parent)
# Button name
myButton.setObjectName(u"myButton")
# Add button to layout(if you have a layout)
myLayout.addWidget(myButton)

```
From QT Designer App
Create the main window 
Drag drop QpushButton widgets to the main container 
Save the UI file
Export the Python Code (Example shown below)

![QT Designer App](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/1.png?raw=true)

## 2 Import QT-PyQt-PySide-Custom-Widgets
Import QT-PyQt-PySide-Custom-Widgets to any python file containing the QPushButton widget you want to customize.
```python
	
# IMPORT QT-PyQt-PySide-Custom-Widgets 
from Custom_Widgets.widgets import *

```
If you created your user interface using QT Designer, remember to also import  QT-PyQt-PySide-Custom-Widgets to the user interface python file everytime you update the interface file from QT Designer.

![user interface file](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/2.png?raw=true)

## 3 Styling QPushButton
Using QT-PyQt-PySide-Custom-Widgets, you can style your buttons using a JSon file directly from your python file.

### A. Applying QPushButton Style from a python file
##### Theme 

QT-PyQt-PySide-Custom-Widgets has 13 preset themes that you can apply to your button as shown below:

```python
# Appy pre-set theme to your button
# Theme number can range from 1 to 13
myButton.setObjectTheme(2) #theme number 2

```
You can also create your own custom button theme by passing the colors of your choice as shown:

```python
# Appy custom theme to your button
# Pass two colors of your choice
myButton.setObjectCustomTheme("#fff", "#000")

```
Hint: Pass two different colors if you want to apply a background gradient to your button as 	   shown above.
	  Pass two similar colors if you want your button to have a uniform background color as shown below.

```python
# Appy custom theme to your button
# Pass two colors of your choice
# Uniform background color(white)
myButton.setObjectCustomTheme("#fff", "#fff")

```

### Animate QPushButton background and border
After applying your button theme, you can chose to animate the backround color, border or both.

Animation trigger event:

```python
myButton.setObjectAnimateOn("hover") #Animate on hover
# OR
myButton.setObjectAnimateOn("click") #Animate on click

```

Animation Easing Curve:
```python
myButton._animation.setEasingCurve(QtCore.QEasingCurve.InOutElastic)
# Read more about QT animation easing curve on their website
```

The default backround color and border will be animated during the animation process. In case you want to apply a different style to your button during the animation process then do add the following statement:

```python
# Apply red and yellow gradient during the animation
applyCustomAnimationThemeStyle(myButton, "red", "yellow")
```

You can also select a different preset theme to be applied to the button during the animation process:

```python
# Apply theme 2 colors to your button during the animation
applyAnimationThemeStyle(myButton, 2)
```
Apply the default button style that will be applied during and after the animation.

```python
myButton.setObjectDefaultStyle("your css style")
```

Set the style that will be applied to the button only after the animation is over.

```python
myButton.setObjectFallBackStyle("you css style")
```

#### QPushButton Icon 

QT-PyQt-PySide-Custom-Widgets uses iconify library to apply and animate button icons. In case you had not installed Iconify library then it should have been installed alongside QT-PyQt-PySide-Custom-Widgets library.

The following video will help you understand more about Iconify and how to get Icon Names from Iconify browser. Click on the image below to start watch.

[![Iconify Video](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/3.png?raw=true)](https://youtu.be/y9qQXn836K0)

Apply button icon:

```python
# Apply button icon
iconify(
    myButton, #button name
    icon = "font-awesome:solid:cloud-download-alt" #icon
)
```
Changing Icon Color:

```python
# Apply button icon
iconify(
    myButton, #button name
    color= "#fff" #color
)
```

Changing Icon Size:

```python
# Apply button icon
iconify(
    myButton, #button name
    size = 64,  #icon size
)
```

Animate buton icon:
You can choose to animate the button icon on hover or click events. There are two types of icon animations: breathe
				 spinn
	
Animate on hover:

```python
# Apply button icon
iconify(
    myButton, #button name
    animateOn = "hover", #Animate button on click
    animation = "spin" #Spin animation
)
```

Animate on click:

```python
# Apply button icon
iconify(
    myButton, #button name
    animateOn = "click", #Animate button on click
    animation = "breathe" #Breathe animation
)
```
The full Iconfy statement can be written as follows:
```python
iconify(
	# Button name must be passed
    myButton, 
    # Optional values
    icon = "font-awesome:solid:cloud-download-alt", 
    color = "orange", 
    size = 64, 
    animation = "spin", 
    animateOn = "click"
)
```

#### QPushButton Shadow
You can apply and animate button shadows using QT-PyQt-PySide-Custom-Widgets extension.
	
Apply Shadow:
```python
applyButtonShadow(
    myButton, #button name
    color= "#fff" #shadow color
)

```

Shadow blur radius:
```python
applyButtonShadow(
    myButton, #button name
    blurRadius = 100 #shadow blur radius
)

```

Shadow x and y offset:
```python
applyButtonShadow(
    myButton, #button name
    # Default value is zero
    xOffset = 5, #x-offset
    yOffset = 5 #y-offset
)

```

Animate shadow:
```python
applyButtonShadow(
    myButton, #button name
    # Default value is false
    animateShadow = True #Animate button shadow
)

```

Choose an even to animate the shadow(hover or click)
```python
applyButtonShadow(
    myButton, #button name
    # Default value is hover
    applyShadowOn= "click"  #Animate button shadow on click
)

```

Change animation duration
```python
applyButtonShadow(
    myButton, #button name
    # Default value is hover
    animateShadowDuration = 1000,  #Animate duration(1 sec)
)

```

The full QPushButton shadow statement can be written as follows:
```python
applyButtonShadow(
    myButton, 
    color= "#fff", 
    applyShadowOn= "hover", 
    animateShadow = True, 
    blurRadius = 100, 
    animateShadowDuration = 500,
    xOffset = 0,
    yOffset = 0
)

```

### A. Applying QPushButton Style from a json file
The easiest way to style your QPushButtons using QT-PyQt-PySide-Custom-Widgets is to use a Json file.

Create a Json file inside your project folder, name it "style.json".
Follow the following steps to style your buttons:

Create a button object that will contain a list of all the buttons you want to style.

```json
{
	"buttons": [
		{
			"name": "button1"
		},
		{
			"name": "button2"
		},
		{
			"name": "button3"
		}
	]
}
```
Now assuming your UI has a QPushButton named "myButton",

##### Apply Theme 
We are going to apply the pre-set theme number "2" to "myButton".

```json
{
	"buttons": [
		{
			"name": "myButton",
			"theme": "2"
		}
	]
}
```
You can also apply the custom theme of your choice by passing two colors.

```json
{
	"buttons": [
		{
			"name": "myButton",
			"customTheme": [
				{
				"color1": "#000",
				"color2": "rgb(37, 150, 190)"
				}
			]
		}
	]
}
```

Set the default style that will be applied to the button during and after the animation process.

```json
{
	"buttons": [
		{
			"name": "myButton",
			"defaultStyle": [
				"border-style: solid;",
				"border-width: 2px;",
			    "border-radius: 3px;",
				"color: #d3dae3;",
				"padding: 5px;"
			]
		}
	]
}
```

Set the style that will be applied the button after the animation is done playing.

```json
{
	"buttons": [
		{
			"name": "myButton",
			"fallBackStyle": [
				"background-color: green"
			]
		}
	]
}
```

#### Animate button background and border
The default value is "both", which will animate the backround color and border.

Animate border alone:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"animation": "border"
		}
	]
}
```

Animate background alone:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"animation": "background"
		}
	]
}
```

The default trigger event for animation is hover.
Animate on click event:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"animateOn": "click"
		}
	]
}
```

Animate on hover event:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"animateOn": "hover"
		}
	]
}
```

Set the background and border style animation duration.

```json
{
	"buttons": [
		{
			"name": "myButton",
			"animationDuration": 1000
		}
	]
}
```

#### Apply button icon and icon animation

Select icon:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"iconify": [
				{
					"icon": "dash:admin-generic"
				}
			]
		}
	]
}
```

Set icon color:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"iconify": [
				{
					"color": "white"
				}
			]
		}
	]
}
```

Set icon size:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"iconify": [
				{
					"size": 32
				}
			]
		}
	]
}
```

Set icon animation(spin or breathe):

```json
{
	"buttons": [
		{
			"name": "myButton",
			"iconify": [
				{
					"animation": "breathe"
				}
			]
		}
	]
}
```

Set icon animation trigger event (click or hover):

```json
{
	"buttons": [
		{
			"name": "myButton",
			"iconify": [
				{
					"animateOn": "hover"
				}
			]
		}
	]
}
```

Full Iconify Json object:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"iconify": [
				{
					"icon": "dash:admin-generic",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "hover"
				}
			]
		}
	]
}
```

#### Apply an animate button shadow

Set shadow color:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"color": "white"
				}
			]
		}
	]
}
```
Set shadow blur radius:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"blurRadius": 100
				}
			]
		}
	]
}
```
Set shadow x and y offset:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"xOffset": 2,
					"yOffset": 2
				}
			]
		}
	]
}
```

Animate shadow:
The default value is False


```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"animateShadow": true
				}
			]
		}
	]
}
```

Set shadow animation trigger event:
If left empty or not specified, the shadow will be applied on button object creation.

Apply shadow on click:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"applyShadowOn": "click"
				}
			]
		}
	]
}
```

Apply shadow on hover:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"applyShadowOn": "hover"
				}
			]
		}
	]
}
```

Set the shadow animation duration:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"animateShadowDuration": 500
				}
			]
		}
	]
}
```

Full json shadow stylesheet:

```json
{
	"buttons": [
		{
			"name": "myButton",
			"shadow":[
				{
					"color": "white",
					"animateShadow": true,
					"applyShadowOn": "hover",
					"animateShadowDuration": 500,
					"blurRadius": 100,
					"xOffset": 2,
					"yOffset": 2
				}
			]
		}
	]
}
```

#### Loading the json style from "style.json" file to the UI

To apply the Json stylesheet to your button, use:
```python
loadJsonStyle(myButton) #Apply button style from json
```
The above statement only applies the syle to ne button. If you want to apply the style to multiple buttons, you can use the for-loop.
For example, assuming that you have a group of QPushButton inside a QFrame called "myFrame",
you can apply the style to all buttona as follows:

```python
######################################################################
## APPLY BUTTON STYLE FROM JSON FILE
########################################################################
# Load the stylesheet for all buttons inside myFrame
for w in myFrame.findChildren(QPushButton):
    # load the stylesheet for button w from the json file
    loadJsonStyle(w) 
    # check if the button stylesheet was found inside the Json file
    if not w.wasThemed:
        # If no style was found, you can apply another style
        applyAnimationThemeStyle(w, 2) #Apply theme 2 to the button
        # OR
        # Appply your own custom theme
        applyCustomAnimationThemeStyle(w, "red", "yellow") #Apply custom theme to the button
```

Another way you can apply the JSon style to multiple buttons is by creating a python list object containing the names of all buttons.

```python
######################################################################
## APPLY BUTTON STYLE FROM JSON FILE
########################################################################
# Create a list containint all the buttons you want to style
myButtons = [myButton1, myButton2, myButton3, ...]
# Load the stylesheet for all buttons in the list
for w in myButtons:
    # load the stylesheet for button w from the json file
    loadJsonStyle(w) 
    # check if the button stylesheet was found inside the Json file
    if not w.wasThemed:
        # If no style was found, you can apply another style
        applyAnimationThemeStyle(w, 2) #Apply theme 2 to the button
        # OR
        # Appply your own custom theme
        applyCustomAnimationThemeStyle(w, "red", "yellow") #Apply custom theme to the button
```

## Json Stylesheet Sample
This is a Json style example. Replace the button names with your own button names.

```json
{
	"buttons": [
		{
			"name": "pushButton",
			"customTheme": [
				{
				"color1": "#2596be",
				"color2": "rgb(37, 150, 190)"
				}
			],
			"iconify": [
				{
					"icon": "dash:admin-generic",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "hover"
				}
			]
		},
		{
			"name": "pushButton_2",
			"theme": "2",
			"animateOn": "click",
			"shadow":[
				{
					"color": "white",
					"applyShadowOn": "click",
					"animateShadow": true,
					"animateShadowDuration": 500,
					"blurRadius": 100
				}
			],
			"iconify": [
				{
					"icon": "feather:loader",
					"color": "white",
					"size": 32,
					"animation": "spin",
					"animateOn": "hover"
				}
			]
		},
		{
			"name": "pushButton_3",
			"theme": "3",
			"animation": "border",
			"animateOn": "hover",
			"iconify": [
				{
					"icon": "font-awesome:brands:amazon",
					"color": "white",
					"size": 32,
					"animation": "spin",
					"animateOn": "click"
				}
			],
			"shadow":[
				{
					"color": "white",
					"animateShadow": true,
					"animateShadowDuration": 500,
					"blurRadius": 100,
					"xOffset": 2,
					"yOffset": 2
				}
			]
		},
		{
			"name": "pushButton_4",
			"theme": "4",
			"animation": "background",
			"iconify": [
				{
					"icon": "font-awesome:brands:google-play",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "click"
				}
			]
		},
		{
			"name": "pushButton_5",
			"theme": "5",
			"animationDuration": 1000,
			"iconify": [
				{
					"icon": "font-awesome:brands:bitcoin",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "click"
				}
			],
			"shadow":[
				{
					"color": "#2596BE",
					"applyShadowOn": "hover",
					"animateShadow": true,
					"animateShadowDuration": 500,
					"blurRadius": 100,
					"xOffset": 0,
					"yOffset": 0
				}
			]
		},
		{
			"name": "pushButton_6",
			"theme": "6",
			"animationEasingCurve": "InSine",
			"animateOn": "click",
			"iconify": [
				{
					"icon": "font-awesome:brands:grav",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "click"
				}
			]
		},
		{
			"name": "pushButton_7",
			"theme": "7",
			"animation": "border",
			"fallBackStyle": [
				"background-color: green"
			],
			"defaultStyle": [
				"border-style: solid;",
				"border-width: 2px;",
			    "border-radius: 3px;",
				"color: #d3dae3;",
				"padding: 5px;"
			],
			"iconify": [
				{
					"icon": "font-awesome:brands:node",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "hover"
				}
			]
		},
		{
			"name": "pushButton_8",
			"theme": "8",
			"animationEasingCurve": "OutInBack",
			"animationDuration": 1000,
			"iconify": [
				{
					"icon": "font-awesome:solid:heart",
					"color": "red",
					"size": 32,
					"animation": "spin",
					"animateOn": "click"
				}
			]
		},
		{
			"name": "pushButton_9",
			"theme": "9",
			"animation": "border",
			"iconify": [
				{
					"icon": "material-design:youtube",
					"color": "red",
					"size": 32,
					"animation": "spin",
					"animateOn": "hover"
				}
			]
		}

	]
}
```

# These Videos will help you understand more:

[CUSTOMIZE QPUSH BUTTON ANIMATIONS SHADOW  BORDER  BACKGROUND  ICON  MODERN GUI  DESIGN](https://youtu.be/qwShmLzYv4s)


[Animate QPushButton  Install Font Libraries  Using ICONIFY Library  Pyqt  PySide  Modern GUI](https://youtu.be/y9qQXn836K0)

# Full Source Code Sample

1) Create a project folder.
2) Inside this filder, create a file and name it "main.py".
3) Copy and paste the following code into "main.py" file.

```python
########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################
"""
READ ME:
I made an extension of the QPushButton class to help make button
customization a animation easier
The QPushButton custom class is in Custom_Widgets.widgets.py, you can go
through it but only change it if youre sure of what youre doing

You can fully customize the buttons in the UI through the style.json file.


name (the name of the button)
theme (theme number from 1 to 13)
customTheme (pass in your custom theme colors -color1 and color2- if the like the look of the available themes)
animateOn (the event that will trigger the button animation- hover or click- event)
animation (the part of the butttom you want to animate - border, background or both)
animationDuration (the time your animation should take playing)
animationEasingCurve (the easing curve for the anomation, google QT animation easing curve)
fallBackStyle (the style that should be applied to the button once the animation is done playing)
defaultStyle (the style that will be applied alongside the animation style)
iconify (pass in the iconify icon style:  
    name = name of the icon
    color = color of the icon
    size = size of the icon
    animateOn = event that should trigger icon animation (hover, click or all)
)

If no JSon value was passed for a particular button, the default stylesheet will be applied the button.

CHECK THE FOR-LOOP BELOW ON MAINWINDOW CLASS ON HOW TO APPLY STYLE FROM JSON FILE



You can also customize the buttons from inside your mainwindow class using the folowing statements:

Set theme
button.setObjectTheme(themeNumber)
Set custom theme
button.setObjectCustomTheme(color, color)
Set animation trigger event
button.setObjectAnimateOn("click" or "hover")
Pass the style that should be applied to the button once the animation is over
button.setObjectFallBackStyle(Stylesheet)
Set the style sheet that will be applied alongside the animation style and fallBack style
button.setObjectDefaultStyle(Stylesheet)
Set the animation easing curve
button._animation.setEasingCurve(QtCore easing curve)

IMPORTANT
If you need to apply the theme to the UI file generated by QT Designer, you should also import the Custom_Widgets.widgets to the UI, check ui_interface.py

"""
########################################################################
## IMPORTS
########################################################################
import sys
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from PySide2.QtCore import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT CUSTOM BUTTONS FILE
# Because ill be frequently updating this package,
# run "pip install --upgrade QT-PyQt-PySide-Custom-Widgets"
# to install any updates
from Custom_Widgets.widgets import *
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

        ######################################################################
        ## UNCOMMENT/COMMENT THE COMMENTED STATEMENTS TO SEE THEIR EFFECTS
        ########################################################################

        ######################################################################
        ## APPLY STYLE FROM JSON FILE
        ########################################################################
        # loadJsonStyle(self.ui.pushButton_2)
        for w in self.ui.widget.findChildren(QPushButton):
            # print(w.objectName())

            ########################################################################
            # load the stylesheet for button w from the json file
            ########################################################################
            loadJsonStyle(w)

            ########################################################################
            # check if the stylesheet was found 
            ########################################################################
            # if no style was found, apply the default style from the animation theme
            ########################################################################

            # if not w.wasThemed:
            	########################################################################
                # w is the button
                # 9 is the theme
                ########################################################################
                # applyAnimationThemeStyle(w, 2)

                ########################################################################
                # OR
                ########################################################################
                # Appply your own custom theme
                ########################################################################
                # applyCustomAnimationThemeStyle(w, "red", "yellow")
                # print(w)

        ########################################################################
        # Create new button
        ########################################################################
        # button = QPushButton("name")
        # button.setText("Login")
        # button.setObjectTheme(2)
        # self.ui.gridLayout.addWidget(button, 2, 1, 1, 1)

        ########################################################################
        # UNCOMMENT THE STATEMENTS BELOW TO SEE THEIR EFFECTS
        ########################################################################
        # self.ui.pushButton.setObjectTheme(1)
        # self.ui.pushButton_2.setObjectTheme(2)
        # self.ui.pushButton_3.setObjectTheme(3)
        # self.ui.pushButton_4.setObjectTheme(4)
        # self.ui.pushButton_5.setObjectTheme(5)
        # self.ui.pushButton_6.setObjectTheme(6)
        # self.ui.pushButton_7.setObjectTheme(11)
        # self.ui.pushButton_5.setObjectTheme(10)
        # self.ui.pushButton.setObjectCustomTheme("#fff", "#000")
        # self.ui.pushButton.setObjectAnimateOn("hover")
        # self.ui.pushButton_7.setObjectAnimateOn("click")
        # self.ui.pushButton._animation.setEasingCurve(QtCore.QEasingCurve.InOutElastic)

        ########################################################################
        # STYLE APPLIED AFTER THE ANIMATION IS COMPLETE
        ########################################################################
        # self.ui.pushButton.setObjectFallBackStyle("""
        # border-style: solid;
        # border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #FF4200, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);
        # border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #FF4200, stop:0.5 #FF4200, stop:0.6 #C0DB50, stop:1 #C0DB50);
        # border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF4200, stop:0.3 #FF4200, stop:0.7 #100E19, stop:1 #100E19);
        # border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
        # border-width: 5px;
        # border-radius: 1px;
        # color: #d3dae3;
        # padding: 2px;
        # background-color: #100E19;
        # """)  

        ########################################################################
        # STYLE APPLIED ALONSIDE ANIMATION THEME STYLE AND FALLBACK STYLE
        ########################################################################
        # self.ui.pushButton.setObjectDefaultStyle(
        #     """
        #         border-radius:5px;
        #         border-width: 10px;
        #         color: #d3dae3;
        #         padding: 5px;
        #     """)   

        ########################################################################
        # Apply button icon
        ########################################################################
        # iconify(
            # self.ui.pushButton, 
            # icon = "font-awesome:solid:cloud-download-alt", 
            # color = "orange", 
            # size = 64, 
            # animation = "spin", 
            # animateOn = "click"
            # )

        ########################################################################
        # Apply button shadow
        ########################################################################
        # applyButtonShadow(
        #     self.ui.pushButton_4, 
        #     color= "#fff", 
        #     applyShadowOn= "hover", 
        #     animateShadow = True, 
        #     blurRadius = 100, 
        #     animateShadowDuration = 500,
        #     xOffset = 0,
        #     yOffset = 0
        #     )



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

4) Create "ui_interface.py" inside your project folder, copy and paste the following code. This is the user interface generated by QT Designer.
NOTE: I also imported "Custom_Widgets.widgets" into this file because the buttons we will be styling are in this file.

```python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacenkDuTt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

########################################################################
# IMPORT CUSTOM BUTTONS FILE
from Custom_Widgets.widgets import *
########################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(584, 331)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0))\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.widget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#55ffff;\">Q</span><span style=\" font-size:18pt; font-style:italic; text-decoration: underline; color:#ffffff;\">BUTTON</span><span style=\" font-size:18pt;\"> CUS</span><span style=\" font-size:24pt; font-weight:600; color:#55ffff;\">T</span><span style=\" font-size:18pt;\">O</span><span style=\" font-size:18pt; font-weight:600;\">MIZ</span><span style=\" font-size:18pt;\">ATION</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Loading", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Amazon", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PlayStore", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"BitCoin", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Surf", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"NodeJs", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Show Love", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Subscribe", None))
    # retranslateUi


```

5) Create "style.json" file which will be used for styling the buttons. Copy and paste the following code inside "style.json" file.

```python
{
	"buttons": [
		{
			"name": "pushButton",
			"customTheme": [
				{
				"color1": "#2596be",
				"color2": "rgb(37, 150, 190)"
				}
			],
			"iconify": [
				{
					"icon": "dash:admin-generic",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "hover"
				}
			]
		},
		{
			"name": "pushButton_2",
			"theme": "2",
			"animateOn": "click",
			"shadow":[
				{
					"color": "white",
					"applyShadowOn": "click",
					"animateShadow": true,
					"animateShadowDuration": 500,
					"blurRadius": 100
				}
			],
			"iconify": [
				{
					"icon": "feather:loader",
					"color": "white",
					"size": 32,
					"animation": "spin",
					"animateOn": "hover"
				}
			]
		},
		{
			"name": "pushButton_3",
			"theme": "3",
			"animation": "border",
			"animateOn": "hover",
			"iconify": [
				{
					"icon": "font-awesome:brands:amazon",
					"color": "white",
					"size": 32,
					"animation": "spin",
					"animateOn": "click"
				}
			],
			"shadow":[
				{
					"color": "white",
					"animateShadow": true,
					"animateShadowDuration": 500,
					"blurRadius": 100,
					"xOffset": 2,
					"yOffset": 2
				}
			]
		},
		{
			"name": "pushButton_4",
			"theme": "4",
			"animation": "background",
			"iconify": [
				{
					"icon": "font-awesome:brands:google-play",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "click"
				}
			]
		},
		{
			"name": "pushButton_5",
			"theme": "5",
			"animationDuration": 1000,
			"iconify": [
				{
					"icon": "font-awesome:brands:bitcoin",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "click"
				}
			],
			"shadow":[
				{
					"color": "#2596BE",
					"applyShadowOn": "hover",
					"animateShadow": true,
					"animateShadowDuration": 500,
					"blurRadius": 100,
					"xOffset": 0,
					"yOffset": 0
				}
			]
		},
		{
			"name": "pushButton_6",
			"theme": "6",
			"animationEasingCurve": "InSine",
			"animateOn": "click",
			"iconify": [
				{
					"icon": "font-awesome:brands:grav",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "click"
				}
			]
		},
		{
			"name": "pushButton_7",
			"theme": "7",
			"animation": "border",
			"fallBackStyle": [
				"background-color: green"
			],
			"defaultStyle": [
				"border-style: solid;",
				"border-width: 2px;",
			    "border-radius: 3px;",
				"color: #d3dae3;",
				"padding: 5px;"
			],
			"iconify": [
				{
					"icon": "font-awesome:brands:node",
					"color": "white",
					"size": 32,
					"animation": "breathe",
					"animateOn": "hover"
				}
			]
		},
		{
			"name": "pushButton_8",
			"theme": "8",
			"animationEasingCurve": "OutInBack",
			"animationDuration": 1000,
			"iconify": [
				{
					"icon": "font-awesome:solid:heart",
					"color": "red",
					"size": 32,
					"animation": "spin",
					"animateOn": "click"
				}
			]
		},
		{
			"name": "pushButton_9",
			"theme": "9",
			"animation": "border",
			"iconify": [
				{
					"icon": "material-design:youtube",
					"color": "red",
					"size": 32,
					"animation": "spin",
					"animateOn": "hover"
				}
			]
		}

	]
}
```

6) Optional step: If you want to see how the user interface looks like in QT Designer and maybe modify it, create a file, name it "interface.ui", copy and paste the following code inside "interface.ui" file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>584</width>
    <height>331</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="styleSheet">
    <string notr="true">#centralwidget{
	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.965686, y2:1, stop:0.0147059 rgba(85, 255, 255, 100), stop:0.0539216 rgba(57, 72, 85, 255), stop:0.0931373 rgba(26, 33, 39, 255), stop:0.455882 rgba(26, 33, 39, 255), stop:0.661765 rgba(0, 0, 0, 0), stop:0.676471 rgba(66, 75, 82, 255), stop:0.843137 rgba(66, 75, 82, 0))
}</string>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item alignment="Qt::AlignTop">
     <widget class="QLabel" name="label">
      <property name="styleSheet">
       <string notr="true"/>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:24pt; font-weight:600; color:#55ffff;&quot;&gt;Q&lt;/span&gt;&lt;span style=&quot; font-size:18pt; font-style:italic; text-decoration: underline; color:#ffffff;&quot;&gt;BUTTON&lt;/span&gt;&lt;span style=&quot; font-size:18pt;&quot;&gt; CUS&lt;/span&gt;&lt;span style=&quot; font-size:24pt; font-weight:600; color:#55ffff;&quot;&gt;T&lt;/span&gt;&lt;span style=&quot; font-size:18pt;&quot;&gt;O&lt;/span&gt;&lt;span style=&quot; font-size:18pt; font-weight:600;&quot;&gt;MIZ&lt;/span&gt;&lt;span style=&quot; font-size:18pt;&quot;&gt;ATION&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
      <property name="textFormat">
       <enum>Qt::RichText</enum>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QWidget" name="widget" native="true">
      <property name="sizePolicy">
       <sizepolicy hsizetype="Preferred" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <layout class="QGridLayout" name="gridLayout">
       <item row="0" column="0">
        <widget class="QPushButton" name="pushButton">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>Settings</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QPushButton" name="pushButton_2">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>Loading</string>
         </property>
        </widget>
       </item>
       <item row="0" column="2">
        <widget class="QPushButton" name="pushButton_3">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>Amazon</string>
         </property>
        </widget>
       </item>
       <item row="1" column="0">
        <widget class="QPushButton" name="pushButton_4">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>PlayStore</string>
         </property>
        </widget>
       </item>
       <item row="1" column="1">
        <widget class="QPushButton" name="pushButton_5">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>BitCoin</string>
         </property>
        </widget>
       </item>
       <item row="1" column="2">
        <widget class="QPushButton" name="pushButton_6">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>Surf</string>
         </property>
        </widget>
       </item>
       <item row="2" column="0">
        <widget class="QPushButton" name="pushButton_7">
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>NodeJs</string>
         </property>
        </widget>
       </item>
       <item row="2" column="1">
        <widget class="QPushButton" name="pushButton_8">
         <property name="text">
          <string>Show Love</string>
         </property>
        </widget>
       </item>
       <item row="2" column="2">
        <widget class="QPushButton" name="pushButton_9">
         <property name="text">
          <string>Subscribe</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

```

7) RUN "main.py"...


# Navigation
[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) [Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html)

