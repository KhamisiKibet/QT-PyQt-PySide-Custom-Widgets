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
