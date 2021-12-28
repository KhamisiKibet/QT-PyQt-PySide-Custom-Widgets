# QT-PyQt-PySide-Custom-Widgets - QT Cards(QCards)
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![QT Cards](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/qt-cards-on-dashboard.png?raw=true)

# QT Cards Widget

The QT-PyQt-PySide-Custom-Widgets provides you with a simpler option to create "card" widgets. 
QCard is simply a group of widdgets that you can apply a uniform drop shadow effects to without having to apply the shadow to individual widgets. This is helpful especilly when creating a dashboard with several "card" widgets.

## Creating QCards
After designing your GUI, inside the root of your project folder, create the "style.json" file which will contain all the values that will customize your GUI.


Inside the "style.json" file create "QCard" main object:

```json
{
	"QCard": [{
	}]
}
```

Pass the group of widgets(widget names) you want to apply the drop shadow graphic effect to:

```json
{
	"QCard": [{
		"cards": [
			"card1",
			"card2",
			"card3",
			"card4"
		]
	}]
}
```

Pass the shadow values:

```json
{
	"QCard": [{
		"cards": [
			"card1",
			"card2",
			"card3",
			"card4"
		],
		"shadow":[
			{
				"color": "#000",
				"blurRadius": 5,
				"xOffset": 0,
				"yOffset": 0
			}
		]
	}]
}
```

Yo can have as many QCard groups as you want:

```json
{
	"QCard": [
		{
			"cards": [
				"card1",
				"card2",
				"card3",
				"card4"
			],
			"shadow":[
				{
					"color": "#000",
					"blurRadius": 5,
					"xOffset": 0,
					"yOffset": 0
				}
			]
		},
		{
		"cards": [
			"card5",
			"card6",
			"card7",
			"card8"
		],
		"shadow":[
			{
				"color": "#555",
				"blurRadius": 20,
				"xOffset": 0,
				"yOffset": 0
			}
		]
	}
	]
}
```

# More

Watch the full video tutorial here https://youtu.be/44IbJnTiKRg

# Navigation

[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) [Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) [Custom Animated Progress Indicator / Progress Bar](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-progress-bar.html)  [Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html) [Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html) [Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)