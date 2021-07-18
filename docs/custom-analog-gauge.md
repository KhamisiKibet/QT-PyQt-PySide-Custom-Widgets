# QT-PyQt-PySide-Custom-Widgets - Analog Gauge
This module will be soon available for Pip installations, please check back later.

Continue reading...

![Custom Analog Gauge](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/qt-pyqt-pyside-analog-gauge.png?raw=true)

# PyQt/PySide Analog Gauge Meter

## Download

Download the source code plus examples below
[Download](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/tree/main/examples/AnalogGaugeMeterWidget)  


## PyQT
For pyqt5 users click here to download the "analoggaugewidget.py" file and put it in 
the main root directory of your project folder.

## PySide
PySide6/2 guide coming soon, Please check back later

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

# Support this work on Patreon 
[Patreon](https://www.patreon.com/spinntv)  



# READ MORE
## Navigation
[HOME](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/)  
[Customize and Animate QStacked Widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html)  
[Customize and Animate QPushButton](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html) 
[Customize QMainWindow](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html)  
[Customize slide menu widgets](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)




