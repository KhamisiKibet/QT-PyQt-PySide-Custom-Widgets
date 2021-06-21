# QT-PyQt-PySide-Custom-Widgets - Custom QMainWindow
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![Custom Qt Progress Bar](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/19.png?raw=true)

# Customize Your QMainWindow

QT-PyQt-PySide-Custom-Widgets offers an easy way to add a custom title bar to application main window.
This is done through "style.json" file. 

# Steps to add a custom windows title bar to your QMainWindow

## Step 1:

Open QT Designer, design your app main widow. Add a custom tittle bar with custom navigation buttons. These buttons are:

	1. Minimize button - If you want your window to be minimizable.
	2. Close button - If you want your window to be closable.
	3. Restore button - If you want your window size to be maximized or restored.

You can also add a QFrame to the bottom right corner of your app window which will be used as a "Size Grip" to resize the window.

I designed the simple window below:

![Custom Title Bar QT DESIGNER](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/16.png?raw=true)

The source code to the above UI can be downloaded [here](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/tree/main/examples/QMainWindow).

## Step 2:

Create "main.py" file, import the UI file, then import QT-PyQt-PySide-Custom-Widgets;

```python
########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *


########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################
.....########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *


########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
```

If you run "main.py", you will get the window with the default title bar:

![Default Title Bar QT DESIGNER](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/17.png?raw=true)


## Step 3:

Create "style.json" file inside your project folder. Inside this file create the "QMainWindow" object which will contain a list of values to customize the main window.

```json
{
	"QMainWindow":[
	]
}
```

## Step 4:

Customize your main window title bar from "style.json" file

### Set window title

```json
{
	"QMainWindow":[
		{
			"tittle":"My Window"
		}
	]
}
```

### Set window icon

```json
{
	"QMainWindow":[
		{
			"icon":":/icons/icons/github.svg"
		}
	]
}
```

### Set window to frameless / Remove default title bar

```json
{
	"QMainWindow":[
		{
			"frameless": true
		}
	]
}
```

### Set window background to transluscent

```json
{
	"QMainWindow":[
		{
			"transluscentBg": true
		}
	]
}
```

### Set window size grip widget

```json
{
	"QMainWindow":[
		{
			"sizeGrip": "size_grip"
		}
	]
}
```

### Apply background shadow to the central widget of the main window

"centralWidget" holds the name of the central widget containing all the main window widgets

```json
{
	"QMainWindow":[
		{
			"shadow":[
				{
					"color": "#555",
					"blurRadius": 20,
					"xOffset": 0,
					"yOffset": 0,
					"centralWidget": "centralwidget"
				}
			]
		}
	]
}
```

### Add custom navigation butttons

Minimize button

```json
{
	"QMainWindow":[
		{
			"navigation":[
				{
					"minimize":"minimize_window_button"
				}
			]
		}
	]
}
```

Close button

```json
{
	"QMainWindow":[
		{
			"navigation":[
				{
					"close": "close_window_button",
				}
			]
		}
	]
}
```

Restore / Maximize button

"buttonName" = name of the button,
"maximizedIcon" = button icon when the window is in its normal size
"normalIcon" = button icon when the window is in maximum size

```json
{
	"QMainWindow":[
		{
			"navigation":[
				{
					"restore":[
						{	
							"buttonName": "restore_window_button",
							"normalIcon": ":/icons/icons/maximize-2.svg",
							"maximizedIcon": ":/icons/icons/minimize-2.svg"
						}
					]
				}
			]
		}
	]
}
```

Drag / Move window widget

A widget that will be used to drag the app window

```json
{
	"QMainWindow":[
		{
			"navigation":[
				{
					"moveWindow": "header_frame"
				}
			]
		}
	]
}
```

The title bar

This is the widget or frame which when double clicked will maximize the window if the window is in normal size or show the normal window size if the window is maximized

```json
{
	"QMainWindow":[
		{
			"navigation":[
				{
					"tittleBar": "header_frame"
				}
			]
		}
	]
}
```

So, the full json style sheet for QMainWindow will look like this:

```json
{
	"QMainWindow":[
		{
			"tittle":"My Window",
			"icon":":/icons/icons/github.svg",
			"frameless": true,
			"transluscentBg": true,
			"sizeGrip": "size_grip",
			"shadow":[
				{
					"color": "#fff",
					"blurRadius": 20,
					"xOffset": 0,
					"yOffset": 0,
					"centralWidget": "centralwidget"
				}
			],
			"navigation":[
				{
					"minimize":"minimize_window_button",
					"close": "close_window_button",
					"restore":[
						{	
							"buttonName": "restore_window_button",
							"normalIcon": ":/icons/icons/maximize-2.svg",
							"maximizedIcon": ":/icons/icons/minimize-2.svg"
						}
					],
					"moveWindow": "header_frame",
					"tittleBar": "header_frame"
				}
			]
		}
	]
}
```

## Apply JSon Stylesheet 

To apply the above Json stylesheet to the main window jus call "loadJsonStyle()" function.

So the "main.py" file will look like this:

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
import os
from PySide2 import *


########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        ########################################################################

        self.show()


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
```
This is the final results:

![Custom Title Bar QT DESIGNER](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/18.png?raw=true)

Watch this video for the full tutorial:
[Video](https://youtu.be/li7esLMuFhE)

# Navigation
[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) [Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html) [Custom Animated Progress Indicator / Progress Bar](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-progress-bar.html) [Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) [Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)




 

