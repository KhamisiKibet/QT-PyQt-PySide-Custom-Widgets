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

# Nav
[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/)

