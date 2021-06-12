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

![user interface file](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/1.png?raw=true)

## 3 Styling QPushButton
Using QT-PyQt-PySide-Custom-Widgets, you can style your buttons using a JSon file directly from your python file.

### A. Applying QPushButton Style from a python file
##### Theme 

# Installation Testing
Run the following code to see if the installation was successful.

```python
	# Run this from your terminal or create a python file, 
	# paste this code, then run
	from Custom_Widgets.ProgressIndicator import test
	test.main()

```

You should see the following interface:
![alt text](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot.png?raw=true)

# How to use it.
Read the full documentation plus video guides [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/)
