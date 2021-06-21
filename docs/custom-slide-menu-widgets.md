# QT-PyQt-PySide-Custom-Widgets - Custom Progress Bar / Form Progress Indicator
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![Custom Qt Progress Bar](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/responsive-qt-gui-python-intarface.png?raw=true)

# Custom Responsive PyQt/PySide/Qt Interface With Animated Transition

I mainly build this custom QT class to help user interface designers easily add "Side" menus to their GUI, but after some testing I realized that this extension can actually be used to buld very beautiful responsive user interfaces using QT Designer, Pyside/PyQt and Python.

So this guide will help you learn on how to use QT-PyQt-PySide-Custom-Widgets to build a responsive and animated user interface.

This functionality is available in QT-PyQt-PySide-Custom-Widgets Version 0.1.8 and above: 
[Install or Update QT-PyQt-PySide-Custom-Widgets](https://pypi.org/project/QT-PyQt-PySide-Custom-Widgets/).

## GUI Design In QT Designer.

If you want your widget to be customized using the custom widgets class:

==> Add the widget to your UI

![Qt Designer add widget](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/20.png?raw=true)

==> Promote the widget class

Right click on your widget, then click on promote to. 

![Qt Designer add widget](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/21.png?raw=true)

==> Enter the promote class and header file

Inside the promote classes widget,
========> under base class name select "QWidget" 
========> under promote class name enter "QCustomSlideMenu" 
========> under header file name enter "Custom_Widgets.Widgets.h" 
========> check the "Global Include" check box
========> click on "add"

![Qt Designer add widget class](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/22.png?raw=true)

========> now click on "Promote"

Under object inspector your widget should look like this:

![Qt Designer add widget inspector](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/23.png?raw=true)

Now save the UI(User interface) and generate the UI python code

Now you can be able to customize and animate this widget transition directly from your python file or using a JSon file.

## Customizing The Responsive Widget Using the JSon File

Inside the root of your project folder, create the "style.json" file which will contain all the values that will animate and customize this widget.

This is how my project folder looks like:

![Python project folder](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/24.png?raw=true)

Inside the "style.json" file create "QCustomSlideMenu" mein object:

```json
{
	"QCustomSlideMenu": [{
	}]
}
```
### Pass the name of your widget:

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name"
	}]
}
```

Please NOTE that all other JSon values are OPTIONAL, the only value that you must pass for your widget to be customizedis the widget name. 
If you dont pass any JSon style, the default style will be applied to these widgets.

### Enter widget size:

Enter integer value or "auto", in "auto" size the widget will expand or contract depending on the available window size

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"defaultSize": [{
			"width": 250,
			"height": "auto"
		}]
	}]
}
```

### Enter widget size when minimized/collapsed:

This is the minimum size that will be applied to the the widget when it is fully minimized.
The "auto" value applies "0" width or height to the widget

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"collapsedSize": [{
			"width": 250,
			"height": "auto"
		}]
	}]
}
```

### Enter widget size when maximized/expanded:

This is the maximum size that will be applied to the the widget when it is fully maximized.
The "auto" value applies the full available width or height to the widget

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"expandedSize": [{
			"width": 250,
			"height": "auto"
		}]
	}]
}
```

### Match widget size with parent:

You can also use "parent" instead of auto to give your widget a fixed size that matches the parent size. 

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"defaultSize": [{
			"width": "parent",
			"height": "auto"
		}],
		"collapsedSize": [{
			"width": "parent",
			"height": "auto"
		}],
		"expandedSize": [{
			"width": "parent",
			"height": "auto"
		}]
	}]
}
```

The above widget will have a fixed width that matches the parent witdth even when minimized or maximized.

### Enter widget style when maximized/expanded or minimized/collapsed:

You can pass the style that will be applied to the widget when it is collapsed or expanded

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"menuContainerStyle": [{
			"whenMenuIsCollapsed": [
				"border: 2px solid transparent"
			],
			"whenMenuIsExpanded": [
				"border: 2px solid rgb(9, 5, 13); background-color: rgb(9, 5, 13;"
			]
		}]
	}]
}
```

### Customizing the widget transition animation:

Change the animation duration and the animation easing curve

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"menuTransitionAnimation": [{
			"animationDuration": 2000,
			"animationEasingCurve": "Linear"
		}]
	}]
}
```

This will be applied to both expanding and minimizing transitions

If you want each transition to have different animation properties, then do the following:

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"menuTransitionAnimation": [{
			"whenCollapsing": [{
				"animationDuration": 500,
				"animationEasingCurve": "Linear"
			}],
			"whenExpanding": [{
				"animationDuration": 500,
				"animationEasingCurve": "OutInBack"
			}]
		}]
	}]
}
```


### Adding the "toggle" button

Assuming that you want your widget to be expanded or minimized, then you can add a "QPushButton" which when clicked will minimize or expand your widget.

##### Adding the button name:


```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"toggleButton": [{
			"buttonName": "my_toggle_button"
		}]
	}]
}
```

#### Adding button icons:

You can also add button icons which will be used to indicate if the associated widget is minimized or expanded

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"toggleButton": [{
			"buttonName": "my_toggle_button",
			"icons": [{
				"whenMenuIsCollapsed": ":/icons/icons/align-left.svg",
				"whenMenuIsExpanded": ":/icons/icons/chevron-left.svg"
			}]
		}]
	}]
}
```
#### Adding button styles:

If you want to apply defferent styles to your button when the widget is minimized or maximized then you can use the "style" object as shown:

```json
{
	"QCustomSlideMenu": [{
		"name": "my_widget_name",
		"toggleButton": [{
			"buttonName": "my_toggle_button",
			"style": [{
				"whenMenuIsCollapsed": [
					"border: 2px solid transparent"
				],
				"whenMenuIsExpanded": [
					"border: 2px solid rgb(9, 5, 13)"
				]
			}]
		}]
	}]
}
```

## Apply the JSon stylesheet:

To apply the JSon stylesheet just call the following function from your "main" python file:

```python
########################################################################
# APPLY JSON STYLESHEET
########################################################################
# self = QMainWindow class
# self.ui = Ui_MainWindow / user interface class
loadJsonStyle(self, self.ui)
########################################################################
```

## An Example of the full JSon Style object:

```json
{
	"QCustomSlideMenu": [{
		"name": "menu_widget",
		"defaultSize": [{
			"width": 250,
			"height": "auto"
		}],
		"collapsedSize": [{
			"width": 0,
			"height": 0
		}],
		"expandedSize": [{
			"width": 200,
			"height": "auto"
		}],
		"toggleButton": [{
			"buttonName": "open_close_side_bar_btn",
			"icons": [{
				"whenMenuIsCollapsed": ":/icons/icons/align-left.svg",
				"whenMenuIsExpanded": ":/icons/icons/chevron-left.svg"
			}],
			"style": [{
				"whenMenuIsCollapsed": [
					"border: 2px solid transparent"
				],
				"whenMenuIsExpanded": [
					"border: 2px solid rgb(9, 5, 13)"
				]
			}]
		}],
		"menuTransitionAnimation": [{
			"animationDuration": 2000,
			"animationEasingCurve": "Linear",
			"whenCollapsing": [{
				"animationDuration": 500,
				"animationEasingCurve": "Linear"
			}],
			"whenExpanding": [{
				"animationDuration": 500,
				"animationEasingCurve": "OutInBack"
			}]
		}],
		"menuContainerStyle": [{
			"whenMenuIsCollapsed": [
				"border: 2px solid transparent"
			],
			"whenMenuIsExpanded": [
				"border: 2px solid rgb(9, 5, 13); background-color: rgb(9, 5, 13)"
			]
		}]
	}]
}
```


## Customizing The Responsive Widget From Your Python File:

### Customize the container:

Change multiple values...

```python
########################################################################
# CUSTOMIZE YOUR "MENU" / CONTAINER WIDGET
########################################################################
my_widget.customizeQCustomSlideMenu(
    ########################################################################
    # THESE VALUES ARE OPTIONAL
    # ONLY PASS THE VALUES YOU WANT TO CHANGE
    ########################################################################
    # CHANGE THE DEFAULT WIDGET SIZE ON APP STARTUP
    defaultWidth = 500,
    defaultHeight = 500,
    # CHANGE THE WIDGET SIZE WHEN CALLAPSED/MINIMIZED
    collapsedWidth = 0,
    collapsedHeight = 0,
    # CHANGE THE WIDGET SIZE WHEN EXPANDED/MAXIMIZED
    expandedWidth = 500,
    expandedHeight = 500,
    # CHANGE THE DEFAULT ANIMATION DURATION AND EASING CURVE
    # BY DEFAULT IT WILL BE APPLIED THE WIDGET IS EXPANDED OR COLLAPSED
    animationDuration = 500,
    animationEasingCurve = QtCore.QEasingCurve.Linear,
    # CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS COLLAPSING
    collapsingAnimationDuration = 500,
    collapsingAnimationEasingCurve = QtCore.QEasingCurve.Linear,
    # CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS EXPANDING
    expandingAnimationDuration = 500,
    expandingAnimationEasingCurve = QtCore.QEasingCurve.Linear,
    # PASS THE STYLESHEET THAT WILL BE APPLIED TO THE WIDGET WHEN EXPANDED OR COLLAPSED
    collapsedStyle = "",
    expandedStyle = ""
)
```

or change single values

```python
########################################################################
# CHANGE SINGLE VALUES OF YOUR "MENU" / CONTAINER WIDGET
########################################################################
# CHANGE THE WIDGET SIZE WHEN CALLAPSED/MINIMIZED
my_widget.collapsedWidth = 0
my_widget.collapsedHeight = 0

# CHANGE THE WIDGET SIZE WHEN EXPANDED/MAXIMIZED
my_widget.expandedWidth = 500
my_widget.expandedHeight = 500

# CHANGE THE DEFAULT ANIMATION DURATION AND EASING CURVE
# BY DEFAULT IT WILL BE APPLIED THE WIDGET IS EXPANDED OR COLLAPSED
my_widget.animationDuration = 500
my_widget.animationEasingCurve = QtCore.QEasingCurve.Linear

# CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS COLLAPSING
my_widget.collapsingAnimationDuration = 1000
my_widget.collapsingAnimationEasingCurve = QtCore.QEasingCurve.OutBack

# CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS EXPANDING
my_widget.expandingAnimationDuration = 2000
my_widget.expandingAnimationEasingCurve = QtCore.QEasingCurve.OutQuad

# PASS THE STYLESHEET THAT WILL BE APPLIED TO THE WIDGET WHEN EXPANDED OR COLLAPSED
my_widget.collapsedStyle = ""
my_widget.expandedStyle = ""
```
### Animate the widget:

You can bind these animation functions to a button event or function call. 

```python
########################################################################
# ANIMATE YOUR "MENU" / CONTAINER WIDGET
########################################################################
# TOGGLE WIDGET SIZE
# EXPAND THE WIDGET IF IT IS CURRENTLY COLLAPSED 
# OR
# COLLAPSE THE WIDGET IF IT IS CURRENTLY EXPANDED
my_widget.slideMenu()

# COLLAPSE WIDGET SIZE
my_widget.collapseMenu()

# EXPAND WIDGET SIZE
my_widget.expandMenu()
```

# More

Watch the full video tutorial here [COMING SOON...]

Download the source code [here](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/tree/main/examples/QCustomSlideMenu) 

# Navigation

[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) [Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) [Custom Animated Progress Indicator / Progress Bar](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-progress-bar.html)  [Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html) [Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html)









