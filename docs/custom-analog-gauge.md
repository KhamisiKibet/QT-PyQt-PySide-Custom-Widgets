# QT-PyQt-PySide-Custom-Widgets - Analog Gauge

## Install
```
pip install QT-PyQt-PySide-Custom-Widgets

```
Continue reading...

![Custom Analog Gauge](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/qt-pyqt-pyside-analog-gauge.png?raw=true)

# PyQt/PySide Analog Gauge Meter

![Custom Analog Gauge](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/analog_qt_widget.png?raw=true)

## Video Tutorial

[Watch Video tutorial](https://youtu.be/5WHnlRQcUy4)  


## Download

Download the source code plus examples below
[Download](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/tree/main/examples/AnalogGaugeMeterWidget)  


# PyQT
For pyqt5 users click [here](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/tree/main/examples/AnalogGaugeMeterWidget)  to download the "analoggaugewidget.py" file and put it in 
the main root directory of your project folder.

## PyQt5

## Usage 

### Creating Widget
Create a widget with a custom promote class inside QT Designer as shown below:

Add the widget to the UI

![Ading QT Designer Widget](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/25.png?raw=true)

Right click on the widget, select promote. Inside the Promoted Widgets container, enter "AnalogGaugeWidget" as the class name and "analoggaugewidget.h" as the header file name the click on "add".
Check the "Global include" check mark then click on promote.
![Adding QT Designer Promote Widget class](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/26.png?raw=true)

After designing your user interface file (UI), convet it to a PyQt python file

### Customizing Widget

Note: in these example "self.ui.widget" is the widget name from the User Interface file.

#### Set gauge units 

```python
################################################################################################
# Set gauge units
################################################################################################
self.ui.widget.units = "Km/h"

```

#### Set minimum and maximum gauge value

```python
################################################################################################
# Set minimum gauge value
################################################################################################
self.ui.widget.minValue = 0
# OR
self.ui.widget.setMinValue(self.ui.MaxValueSlider.value())
################################################################################################
# Set maximum gauge value
################################################################################################
self.ui.widget.maxValue = 100
# OR
self.ui.widget.setMaxValue(100)

```

#### Set gauge scale divisions

```python
################################################################################################
# Set scale divisions
################################################################################################
self.ui.widget.scalaCount = 10

# OR

self.ui.widget.setScalaCount(10)

```

#### Set scale start position

```python
# Start from the minimum value
# self.ui.widget.updateValue(self.ui.widget.minValue)
# OR
# Start from half/middle value
self.ui.widget.updateValue(int(self.ui.widget.maxValue - self.ui.widget.minValue)/2)

```

#### Select preset widget theme

```python
################################################################################################
# Select gauge theme
################################################################################################
self.ui.widget.setGaugeTheme(8) #theme number range from 0 to 10

```

#### Create your own custom gauge theme

Method coming soon...

#### Set offset angle

```python
self.ui.widget.updateAngleOffset(0)

```

#### Set scale start angle

```python
self.ui.widget.setScaleStartAngle(135)

```

#### Set scale total angle

```python
self.ui.widget.setTotalScaleAngleSize(270)

```

#### Enable/Disable bar graph

```python
# True or False
self.ui.widget.setEnableBarGraph(True)

```

#### Enable/Disable value text

```python
# True or False
self.ui.widget.setEnableValueText(True)

```

#### Enable/Disable center point

```python
# True or False
self.ui.widget.setEnableCenterPoint(True)

```

#### Enable/Disable needle pointer

```python
# True or False
self.ui.widget.setEnableNeedlePolygon(True)

```

#### Enable/Disable scale text

```python
# True or False
self.ui.widget.setEnableScaleText(True)

```

#### Enable/Disable scale polygon

```python
# True or False
self.ui.widget.setEnableScalePolygon(True)

```

#### Enable/Disable big scale

```python
# True or False
self.ui.widget.setEnableBigScaleGrid(True)

```

#### Enable/Disable fine scale

```python
# True or False
self.ui.widget.setEnableFineScaleGrid(True)

```

#### Set gauge color outer radius factor

```python
# 0 - 1000
self.ui.widget.setGaugeColorOuterRadiusFactor(1000)

```

#### Set gauge color inner radius factor

```python
# 0 - 1000
self.ui.widget.setGaugeColorInnerRadiusFactor(0)

```

#### Set needle color

```python
# RGBA int values range from 0- 255
self.ui.widget.setNeedleColor(R=R, G=G, B=B, Transparency=Transparency)

```

#### Set needle color on drag

```python
# RGBA int values range from 0- 255
self.ui.widget.setNeedleColorOnDrag(R=R, G=G, B=B, Transparency=Transparency)

```

#### Set scale value color

```python
# RGBA int values range from 0- 255
self.ui.widget.setScaleValueColor(R=R, G=G, B=B, Transparency=Transparency)

```

#### Set display value/units color

```python
# RGBA int values range from 0- 255
self.ui.widget.setDisplayValueColor(R=R, G=G, B=B, Transparency=Transparency)

```

# PySide

Pyside users need to install the Custom_Widgets module from pip. Run

```cmd
pip install QT-PyQt-PySide-Custom-Widgets
```

Or upgrade it if you had installed it

```cmd
pip install --upgrade QT-PyQt-PySide-Custom-Widgets
```

### Creating Widget

The process is similar to PyQt (above) the only difference is renaming the promote class name and the header file name

Class name: "AnalogGaugeWidget"
Header file name: "Custom_Widgets.AnalogGaugeWidget.h"

![Adding QT Designer Promote Widget class](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/27.png?raw=true)

### Customizing Widget

If you want to customize the gauge widget from your python files, then the process is similar to PyQt (above).
in PySide, you can also customize the widget using a JSon stylesheet.

Create a "style.json" file inside your project folder. Below is the full JSon sample stylesheet. Also watch the video tutorial for the full guide. [Watch the tutorial videos here](https://youtu.be/5WHnlRQcUy4)

## Full JSON stylesheet sample

```json
{
	"AnalogGaugeWidget": [{
		"name": "widget",
		"units": "Mph",
		"minValue": "100",
		"maxValue": "500",
		"scalaCount": "5",
		"startValue": "250",
		"gaugeTheme": "0",
		"offsetAngle": "0",
		"outerRadius": "1000",
		"innerRadius": "900",
		"scaleStartAngle": "135",
		"totalScaleAngle": "270",
		"enableBarGraph": true,
		"enableValueText": true,
		"enableCenterPoint": true,
		"enableNeedlePolygon": true,
		"enableScaleText": true,
		"enableScaleBigGrid": true,
		"enableScaleFineGrid": true,
		"needleColor": "#002523",
		"needleColorOnDrag": "red",
		"scaleValueColor": "#fff",
		"displayValueColor": "#00F6E9",
		"bigScaleColor" : "#005275",
		"fineScaleColor" : "#005275",
		"customGaugeTheme": [{
			"color1": "#002523",
			"color2": "#990008",
			"color3": "#00F6E9"
		}],
		"scalePolygonColor": [{
			"color1": "#002523",
			"color2": "#990008",
			"color3": "#00F6E9"
		}],
		"needleCenterColor": [{
			"color1": "#002523",
			"color2": "#990008",
			"color3": "#00F6E9"
		}],
		"outerCircleColor": [{
			"color1": "#002523",
			"color2": "#0000",
			"color3": "#00F6E9"
		}],
		"valueFontFamily": [{
			"path": "fonts/ds_digital/DS-DIGIB.TTF",
			"name": "DS-Digital"
		}],
		"scaleFontFamily": [{
			"path": "fonts/ds_digital/DS-DIGIB.TTF",
			"name": "DS-Digital"
		}]
	}]
}

```

# Support this work on Patreon 
[Patreon](https://www.patreon.com/spinntv)  



# READ MORE
## Navigation
[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/)  
[Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html)  
[Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) 
[Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html)  
[Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)




