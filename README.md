[![GitHub](https://img.shields.io/github/license/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets?logo=Github)](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/master/LICENSE) [![GitHub top language](https://img.shields.io/github/languages/top/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets?logo=github)](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets?logo=github)](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets) [![GitHub issues](https://img.shields.io/github/issues/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets?logo=github)](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/issues)

![Custom Widgets Art](https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/custom_widgets_art.png?raw=true)

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
![Custom Progress bar](https://github.com/KhamisiKibet/Docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot.png?raw=true)

# What is new?
## Version 0.6.9:
Quick `CMD/Terminal` commands:
- To launch `ProjectMaker / project wizard`, run
```cmd
Custom_Widgets --create-project
```
This will create a `Qt-python` project inside your empty folder, ready to run.
- Easy to convert UI files to py. The cutom widgets `Theme Engine` eliminated the need for `QRC` to `python` file conversion, therefore to generate `UI-Python` files without any errors, use
```cmd
Custom_Widgets --convert-ui ui-path --qt-library your-lib
```
Where: `ui-path` is the UI file pathe or folder containing UI files.
`your-lib` is `PySide6`, `PySide2`, `PyQt5` or `PyQt6`
- Monitor changes made to UI file and generate new .py file and other necessary files for the custom widgets
```cmd
Custom_Widgets --monitor-ui ui-path --qt-library your-lib
```

Also now you can change the app theme and apply new icons without restarting the app. The custom widgets modulecomes with itw own icon sets:
- Feather
- FontAwesome
- and Google material design icons.

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
    - `AnalogGaugeWidget` - A digital analog widget using just a single `QWidget`. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-analog-gauge)
    - `QCustomCheckBox` - Customize and animate `QCheckBox`. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-qcheckbox)
    - `QCustomProgressIndicator` - Create a beautiful modern progress indicator for multiple tasks. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-progress-bar)
    - `QCustomQPushButton` - Customize and animate `QPushButton` with preset themes and use `iconify` to animate the icons. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-qpushbutton)
    - `QCustomQSlider` - Easily move the slider to the current clicked position of a `QSlider`. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-qslider)
    - `QCustomQStackedWidget` - Add beautiful transition animations and navigate through `QStackedWidget`. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-qstacked-widgets)
    - `QCustomSlideMenu` - Expand and collapse the size of your `QWidgets` i.e side menu, popup notifications, floating widgets etc. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-slide-menu-widgets)
    - `QMainWindow` - Apply custom window title bar and navigation. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-qmainwindow)

- Other extra functions:
    - `ProjectMaker / project wizard` - Used for creating a `Qt-Python` project on an empty folder. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/project-maker)
    - `QCards` - Apply the same syle ie `drop-shadow effect` to a group of `QFrame`, `QWidget` etc. Best for creating dashboard cards. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/qt-cards)
    - `QCustomQPushButtonGroup` - Create a group of `QPushButton`s with different `stylesheet`s for the current `active` or `clicked` button and other innactive buttons. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/qpushbutton-group)
    - `Qt Theme Engine` - Beautify your app. This feature will create multiple themes for QT for Python apps. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/qt-theme-engine)
    - `QSettings` - Easily save your app configurations that will be remembered even after restarting the app ie app theme from Qt Theme Engine`. [Watch the tutorial](https://youtu.be/mkBwInKhBsA)

- Or watch the tutorial videos [here](https://www.youtube.com/watch?v=21Qt9p_F7Ts&list=PLJ8t3BKaQLhPKj9Mx08WAwvz7TGskefbK)

# Sample Images
Analog Gauge Widget

![Analog Gauge Widget](https://github.com/KhamisiKibet/Docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/analog_qt_widget.png?raw=true)

Responsive Animated GUI

![Resposive PyQt PySide GUI](https://github.com/KhamisiKibet/Docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/responsive-qt-gui-python-intarface.png?raw=true)

Animated QStacked Widget

![Custom QStacked Widgets](https://github.com/KhamisiKibet/Docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/qstacked.png?raw=true)
