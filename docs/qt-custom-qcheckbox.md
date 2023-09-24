# QT-PyQt-PySide-Custom-Widgets 

## Install the custom widgets
```
pip install QT-PyQt-PySide-Custom-Widgets

```

![Qt Custom checkbox](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/Qt-Custom-checkbox.png?raw=true)

# QT Custom Check Box(Switch) widget.

Create a beautiful and animated modern `QCheckBox` or switch using the QT-PyQt-PySide-Custom-Widgets.


## Download

[Download](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/tree/main/examples) an example.

## Creating the check box

- Open `Qt Designer`, add `QCheckBox` to the UI.

![Qt Custom checkbox](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot_20230924_023708.png?raw=true)

- Right click on the check box, select `Promoted widgets...`
- From the promote widgets form:
	- Under "Base class name" select `QCheckBox`
	- Under "Promote class name" enter `QCustomCheckBox`
	- Under "Header file" enter `Custom_Widgets.QCustomCheckBox.h`

- Then click on `promote`.

![QT Designer App](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot_20230924_024306.png?raw=true)

- Generate your UI python code.

## Styling QCheckBox
Using QT-PyQt-PySide-Custom-Widgets, you can style your checkbox using a JSon file or directly from your python file.

### A. Applying QCheckBox Style from a python file

```python
########################################################################
# Customize QCustomCheckBox
########################################################################
self.ui.checkBox.customizeQCustomCheckBox(
    bgColor = "#c3c3c3",
    circleColor = "#fff",
    activeColor = "#17a8e3",
    animationEasingCurve = QEasingCurve.Linear,
    animationDuration = 200
)

```

- "self.ui.checkBox" is the checkbox widget
- "customizeQCustomCheckBox" is the function call to customize the widget. 
- `bgColor`: checkbox background color
- `circleColor`: checkbox circle color
- `activeColor`: checkbox background color when swiched on
- `animationEasingCurve`: checkbox transition animation easing curve
- `animationDuration`: checkbox transition animation duration

### B. Applying QCheckBox Style from a json file

- Create a json file inside your project filder
- Pass the `QCustomCheckBox` object as shown:

```json
{
	"QCustomCheckBox":[
		{
			"name":"checkBox_3",
			"bgColor":"#2e3739",
			"circleColor":"#1dbf73",
			"activeColor":"#7b7b7b",
			"animationEasingCurve":"InOutCubic",
			"animationDuration":500
		}
	]
}
```

To apply the json stylesheet:

- Import the custom widgets module:

```python
########################################################################
# IMPORT CUSTOM WIDGETS MODULE
from Custom_Widgets import *
########################################################################

```
- Call the `loadJsonStyle` function from your main window class

```python
########################################################################
## LOAD STYLE FROM JSON FILE
########################################################################
loadJsonStyle(self, self.ui, jsonFiles = {
    "JsonStyle/style.json"
})
########################################################################
## 
########################################################################

```

# Navigation
- [HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) 

- [Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html) 

- [Custom Animated Progress Indicator / Progress Bar](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-progress-bar.html) 

- [Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html)   
 
- [Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)