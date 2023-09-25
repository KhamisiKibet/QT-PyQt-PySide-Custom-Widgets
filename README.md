![Pink Minimalist Photo Grid Photography YouTube Thumbnail (1)](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/assets/82152373/a222096a-742e-42b4-ad72-15a99db6bfe2)

# QT-PyQt-PySide-Custom-Widgets
Awesome custom widgets made for QT Desktop Applications. Simplify your UI development process. These widgets can be used in QT Designer then imported to PySide code.

# Installation 
First time installer:
```
pip install QT-PyQt-PySide-Custom-Widgets
```

Upgrade/install the latest version:
```
pip install --upgrade QT-PyQt-PySide-Custom-Widgets
```

# Testing
The examples folder in this repository contains a few code examples you can use to test and learn about the custom widgets.

Progress indicator example:
![Custom Progress bar](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot.png?raw=true)

# What is new?
## Version 0.6.2:
- Added support for loading multiple ``JSON Stylesheets``
    By default, the json file named ``style.json`` will be loaded, so no need to specify. The file must me inside the root directory of your project, ``json`` directory, or ``jsonstyles`` directory inside your project folder for it to be automatically loaded.
    
    If you have multiple JSON stylesheet files, then you can apply them to your GUI like this:
    ```python
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui, jsonFiles = {
            "mystyle.json",
            "mydirectory/myJsonStyle.json"
            })
        ########################################################################
    ```
    This feature is helpful especially when you have multiple windows files that will share only some parts of the stylesheet shuch app app title, settings etc.
    
- Toggle logs:
    You can now switch app logs on or off.
    This can be done from a python file:
    ```python
    # Show Logs
    self.showCustomWidgetsLogs = True
    ```
    ```python
    # Hide Logs
    self.showCustomWidgetsLogs = False
    ```
    From the JSON file:
    ```json
    {
    "ShowLogs": true,
    ```
    ```json
    {
    "ShowLogs": false,
    ```

## Version 0.6.8:
- Added full support for `pyside6`

# How to use it.

Documentation:

- Available custom widgets:
    - `AnalogGaugeWidget` - A digital analog widget using just a single `QWidget`. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-analog-gauge.html)
    - `QCustomCheckBox` - Customize and animate `QCheckBox`. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/qt-custom-qcheckbox.html)
    - `QCustomProgressIndicator` - Create a beautiful modern progress indicator for multiple tasks. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-progress-bar.html)
    - `QCustomQPushButton` - Customize and animate `QPushButton` with preset themes and use `iconify` to animate the icons. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qpushbutton.html)
    - `QCustomQSlider` - Easily move the slider to the current clicked position of a `QSlider`. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/qt-custom-qslider.html)
    - `QCustomQStackedWidget` - Add beautiful transition animations and navigate through `QStackedWidget`. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qstacked-widgets.html)
    - `QCustomSlideMenu` - Expand and collapse the size of your `QWidgets` i.e side menu, popup notifications, floating widgets etc. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/custom-slide-menu-widgets.html)
    - `QMainWindow` - Apply custom window title bar and navigation. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/customize-qmainwindow.html)

- Other extra functions:
    - `ProjectMaker / project wizard` - Used for creating a `Qt-Python` project on an empty folder. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/project-maker.html)
    - `QCards` - Apply the same syle ie `drop-shadow effect` to a group of `QFrame`, `QWidget` etc. Best for creating dashboard cards. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/qt-cards.html)
    - `QCustomQPushButtonGroup` - Create a group of `QPushButton`s with different `stylesheet`s for the current `active` or `clicked` button and other innactive buttons. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/qpushbutton-group.html)
    - `Qt Theme Engine` - Beautify your app. This feature will create multiple themes for QT for Python apps. [Read more](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/docs/qt-theme-engine.html)
    - `QSettings` - Easily save your app configurations that will be remembered even after restarting the app ie app theme from Qt Theme Engine`. [Watch the tutorial](https://youtu.be/mkBwInKhBsA)

- Read the full documentation [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/) 

- Or watch the tutorial videos [here](https://www.youtube.com/watch?v=21Qt9p_F7Ts&list=PLJ8t3BKaQLhPKj9Mx08WAwvz7TGskefbK)

# Sample Images
Analog Gauge Widget

![Analog Gauge Widget](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/analog_qt_widget.png?raw=true)

Responsive Animated GUI

![Resposive PyQt PySide GUI](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/responsive-qt-gui-python-intarface.png?raw=true)

Animated QStacked Widget

![Custom QStacked Widgets](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/qstacked.png?raw=true)

