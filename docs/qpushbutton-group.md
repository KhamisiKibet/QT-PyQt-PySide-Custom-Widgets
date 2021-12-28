# QT-PyQt-PySide-Custom-Widgets - QPushButtonGroup(QT Grouped Buttons)
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![QT Grouped Buttons](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/qt-nav-buttons.png?raw=true)

# QT Grouped Navigation Buttons

With QT-PyQt-PySide-Custom-Widgets, you can group navigation bittons together. The aim of this functionality is to apply a new style the clicked QPushButton in a group(Active button), an apply a different style to the rest of the QPushButtons in a group(Inactive button)

## Grouping the buttons
After designing your GUI, inside the root of your project folder, create the "style.json" file which will contain all the values that will customize your GUI.


Inside the "style.json" file create "QPushButtonGroup" main object:

```json
{
	"QPushButtonGroup": [{
	}]
}
```

Pass the name of the buttons belonging to the same group:

```json
{
	"QPushButtonGroup": [{
		"Buttons": [
			"pushButton",
			"pushButton_2",
			"pushButton_3",
			"pushButton_4"
		]
	}]
}
```

Pass the style that will be applied to the active and the inactive buttons:

```json
{
	"QPushButtonGroup": [{
		"Buttons": [
			"pushButton",
			"pushButton_2",
			"pushButton_3",
			"pushButton_4"
		],
		"Style":[{
			"Active": "background-color: #015371;",
			"NotActive": "background-color: transparent;"
		}]
	}]
}
```

You can have as many button groups as you want:

```json
{
	"QPushButtonGroup": [
		{
			"Buttons": [
				"pushButton",
				"pushButton_2",
				"pushButton_3",
				"pushButton_4"
			],
			"Style":[{
				"Active": "background-color: #015371;",
				"NotActive": "background-color: transparent;"
			}]
		},
		{
			"Buttons": [
				"pushButton_5",
				"pushButton_6",
				"pushButton_7",
				"pushButton_8"
			],
			"Style":[{
				"Active": "background-color: #fff; border-radius: 0px;",
				"NotActive": "background-color: #000; border-radius: 20px;"
			}]
		},
	]
}
```

# More

Watch the full video tutorial here https://youtu.be/fPgwQJUFPIw


# Navigation

[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) [Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) [Custom Animated Progress Indicator / Progress Bar](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-progress-bar.html)  [Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html) [Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html) [Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)