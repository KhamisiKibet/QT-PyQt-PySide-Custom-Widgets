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

# Gallery
![Responsive pyside pyqt GUI](https://www.dropbox.com/scl/fi/v71slvbih1fo8nwjj1bug/Screenshot_20240130_105009.png?rlkey=0t1x2nzelmvysturs16x7iz7k&dl=0&raw=1)

<div class="gallery">
  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot.png?raw=true" alt="Custom Progress Bar">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/18.png?raw=true" alt="Custom Title Bar">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/analog_qt_widget.png?raw=true" alt="Custom Title Bar">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/qt-cards-on-dashboard.png?raw=true" alt="Qt Cards">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Qt-Custom-checkbox.png?raw=true" alt="Qt custom checkbox">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/qt-nav-buttons.png?raw=true" alt="Qt side menu nav">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot_20230923_064515.png?raw=true" alt="Qt custom qpushbutton">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Screenshot_20230923_064515.png?raw=true" alt="Qt custom qpushbutton">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/responsive-qt-gui-python-intarface.png?raw=true" alt="responsive GUI">
  </div>

</div>

![Responsive pyside pyqt GUI](https://github.com/KhamisiKibet/Docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Capture.PNG?raw=true)

<div class="gallery">
  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Capture2.PNG?raw=true" alt="Responsive pyside pyqt GUI">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Capture3.PNG?raw=true" alt="Responsive pyside pyqt GUI">
  </div>

  <div class="gallery-item">
    <img src="https://github.com/KhamisiKibet/docs-QT-PyQt-PySide-Custom-Widgets/blob/main/images/Capture5.PNG?raw=true" alt="Responsive pyside pyqt GUI">
  </div>

</div>

<style>
  .gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between; /* Adjust as needed */
  }

  .gallery-item {
    flex: 1 0 200px; /* Minimum width of 200px for each item */
    margin-bottom: 10px;
    flex-grow: 0;
  }

  .gallery-item img {
    width: 100%;
    height: auto;
    border-radius: 5px;
    max-height: 300px; /* Set maximum height for images */
  }
</style>



# What is new?
## Version 0.6.9:
1. **New project structure:**

To use version 0.6.9 or later, it's best to stick to the project structure outlined below. Alternatively, you can use the ``ProjectMake or project wizard`` tool, which will set up your project with the same structure automatically.
```cmd
project_name/
│
├── README.md
├── requirements.txt
├── main.py
│
├── ui/
│   ├── main_window.ui
│   └── ...
│
├── src/
│   ├── __init__.py
│   ├── utils.py
│   ├── helper_functions.py
│   └── ui_main_window.py  # Automatically generated from main_window.ui
│
├── qss/
│   ├── scss/
│   │   ├── style.scss
│   │   └── ...
│   │
│   └── icons/
│       ├── icon1.png
│       └── ...
│
├── logs/
│   └── custom_widgets.log
│
├── json_styles/
│   ├── style.json
│   └── ...
│
└── generated-files/
    ├── new_files # Automatically generated by Custom Widgets
    └── ...


```

**Description:**

- **README.md:** Description of the project.
- **requirements.txt:** List of Python dependencies required for the project.
- **main.py:** Entry point of the application.
- **ui/:** Directory containing UI-related files.
    - **main_window.ui:** Main window layout file.
    - Other UI-related files.
- **src/:** Source code directory.
    - **_\_init__.py:** Package initialization file.
    - **utils.py:** Utility functions.
    - **helper_functions.py:** Additional helper functions.
    - **ui_main_window.py:** Automatically generated Python code from main_window.ui.
- **qss/:** Directory for Qt Style Sheets (QSS) and icons.
    - **scss/:** SCSS files for styling.
    - **icons/:** Icon images.
- **logs/:** Directory for log files.
    - **custom_widgets.log:** Log file.
- **json_styles/:** Directory for JSON style files.
-   **style.json:** Example JSON style file.
- **generated-files/:** Directory for files auto-generated by the custom widgets module.
    - Example generated files include **UI's** and **JSon** files

This structure allows for automatic conversion of UI files to Python code and placement within the src folder, simplifying the development process for users.

2. **Quick theme engine**.
- Applies new icons on theme change without need to restart your app.
- Faster theme/icons switching.
- The custom widgets module comes with its own icon sets:
    - Feather
    - FontAwesome
    - and Google material design icons.

3. **New custom widgets `logs`.**
- Log file is located inside the "Logs" folder.

4. **Quick `CMD/Terminal` commands:**
- To launch `ProjectMaker / project wizard`, run
```cmd
Custom_Widgets --create-project
```
This will create a `Qt-python` project inside your empty folder, ready to run.
- Easy to convert UI files to py. The cutom widgets `Theme Engine` eliminated the need for `QRC` to `python` file conversion, therefore to generate `UI-Python` files without any errors, use
```cmd
Custom_Widgets --convert-ui ui-path --qt-library your-lib
```
- Monitor changes made to UI file and generate new .py file and other necessary files for the custom widgets
```cmd
Custom_Widgets --monitor-ui ui-path --qt-library your-lib
```
Where: `ui-path` is the UI file path or folder containing UI files.
`your-lib` is `PySide6`, `PySide2`, `PyQt5` or `PyQt6`

> [Updating old GUI app to work with the current Custom Widgets module update](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/Updating-old-GUI-app-to-work-with-the%20current-Custom-Widgets-module-update)

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

Please read the required **project structure** above before proceeding.

## Documentation:

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



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
