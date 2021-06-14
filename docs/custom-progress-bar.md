# QT-PyQt-PySide-Custom-Widgets - Custom Progress Bar / Form Progress Indicator
Am assuming that you have already installed QT-PyQt-PySide-Custom-Widgets library from PyPi, if not, then start reading from [here](https://khamisikibet.github.io/QT-PyQt-PySide-Custom-Widgets/).

![Custom Qt Progress Bar](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/progressbar.png?raw=true)

# Custom Progress Bar / Form Progress Indicator

QT-PyQt-PySide-Custom-Widgets offers a simple way you can add a custom progress bar to your user interface.
The progress bar can be used to indicate the progress of activities such as background tasks or form filling progress and status.

This guide will show you how to add this progress bar to the user interface.

To view some examples of these progess bars, run the following code from your terminal/command line or inside a python file:

```python
# VIEW PROGRESS BAR EXAMPLES
from Custom_Widgets.ProgressIndicator import test
test.main()
```

## Adding Custom Progress Bar / Form Progress Indicator To The User Interface

### Step 1:
Open QT Designer app, create the "Main Window".

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/6.png?raw=true)

### Step 2:
Add "QWidget" container to your "centralwidget" or a container of your choice.

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/7.png?raw=true)

Set the width and height of your widget, alternatively you can set the layout of the container, in this case it is the "centralwidget" 

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/8.png?raw=true)

### Step 3:
Right click on the "widget" the click "promote to". The promote window will appear.
In "Base Class Name" select "QWidget"
In "Promoted class name" field enter "FormProgressIndicator"
In "Header file" enter "Custom_Widgets.widgets.h"
Then Click on "Add" buton

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/9.png?raw=true)

Check the "Global Include" check mark,

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/10.png?raw=true)

Now select the promoted class you just added then click on "Promote" button,

![Qt Designer Create Main Window](https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets/blob/main/images/11.png?raw=true)





