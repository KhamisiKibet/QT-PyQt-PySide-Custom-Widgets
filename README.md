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
# Quick `CMD/Terminal` commands:
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

# Testing
The examples folder in this repository contains a few code examples you can use to test and learn about the custom widgets.

# How to use it.

Please read the required [**project structure**](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/new-features#version-069) and other important updates [here](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/new-features) before proceeding.

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
    - `QCustomModals` - Provides custom modal dialogs for PySide/PyQt applications. It includes various types of modal dialogs such as `Information`, `Success`, `Warning`, `Error`, and `Custom modals`. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-modals)
    - `QDraggableWidget` - Provides custom draggable widget functionality for PyQt/PySide applications. It includes two main classes: `QDragItem` and `QDragWidget`. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/qdragable-widgets)


- Other extra functions:
    - `ProjectMaker / project wizard` - Used for creating a `Qt-Python` project on an empty folder. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/project-maker)
    - `QCards` - Apply the same syle ie `drop-shadow effect` to a group of `QFrame`, `QWidget` etc. Best for creating dashboard cards. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/qt-cards)
    - `QCustomQPushButtonGroup` - Create a group of `QPushButton`s with different `stylesheet`s for the current `active` or `clicked` button and other innactive buttons. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/qpushbutton-group)
    - `Qt Theme Engine` - Beautify your app. This feature will create multiple themes for QT for Python apps. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/other-functions/qt-theme-engine)
    - `QSettings` - Easily save your app configurations that will be remembered even after restarting the app ie app theme from Qt Theme Engine`. [Watch the tutorial](https://youtu.be/mkBwInKhBsA)
    - `JSON Stylesheet Cheatsheet` - JSON stylesheet is used to customize the appearance and behavior of PyQt/PySide custom widgets in the QT-PyQt-PySide-Custom-Widgets module. [Read more](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/json-stylesheet-cheatsheet)


- Or watch the tutorial videos [here](https://www.youtube.com/watch?v=21Qt9p_F7Ts&list=PLJ8t3BKaQLhPKj9Mx08WAwvz7TGskefbK)

# Credits

## Support 💖

Thanks to all supporters on [YouTube](https://youtube.com/spinntv), [Patreon](https://www.patreon.com/spinntv) and other platforms.

If you find this project valuable and would like to contribute to its development and maintenance, you can support us on [Patreon](https://www.patreon.com/spinntv). Your sponsorship means a lot and is greatly appreciated!💖

## Contributors
Thanks to all the [contributors](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/contributors) involved in the development of the project!

<a href="https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=KhamisiKibet/QT-PyQt-PySide-Custom-Widgets" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

## App gallery
A list of modern GUI's made using the custom widgets module. [View](https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/gallery)

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
