########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinntv.com
# EMAIL: info@spinntv.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
from subprocess import call
import cairosvg
import codecs
import shutil
import json
from urllib.parse import urlparse

########################################################################
## IMPORT PYSIDE2 OR PYSIDE6
########################################################################
# if 'PySide2' in sys.modules:
#     from PySide2.QtCore import QUrl
#     from PySide2.QtGui import QColor

# elif 'PySide6' in sys.modules:
#     from PySide6.QtCore import QUrl
#     from PySide6.QtGui import QColor

# else:
#     raise Exception("PySide2 or PySide6 is required, please install it!")

########################################################################
## MODULE UPDATED TO USE QTPY
########################################################################
from qtpy.QtCore import QUrl
from qtpy.QtGui import QColor

from . Qss.colorsystem import *


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush() 


def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

def generateIcons(iconsColor = "#fff"):  
    # Files folder
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Qss/icons/original_svg')
    list_of_files = []

    svg_color = "#fff"
    normal_color = iconsColor

    focused_color = adjust_lightness(normal_color, 1.5)
    disabled_color = adjust_lightness(normal_color, .5)


    iconsFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/Icons'))


    print("Generating icons for your theme, please wait. This may take long\n")

    for root, dirs, files in os.walk(filename):
        for file in files:
            list_of_files.append(os.path.join(root,file))

    totalIcons = len(list_of_files)

    for name in list_of_files:
        # Create normal icons
        with codecs.open(name, encoding='utf-8', errors='ignore') as f:
            content = f.read()

            newSVG = content.replace(svg_color, normal_color)
            newBytes = str.encode(newSVG)

            name_2 =  os.path.basename(urlparse(name).path).replace(".svg", ".png")
            filename = os.path.abspath(os.path.join(iconsFolder, name_2))

            if not os.path.exists(iconsFolder):
                os.makedirs(iconsFolder)

            if not os.path.exists(filename):                
                try:
                    cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                except Exception as e:
                    print(e)
                    

        # Create focus icons
        with codecs.open(name, encoding='utf-8', errors='ignore') as f:
            content = f.read()

            newSVG = content.replace(svg_color, focused_color)
            newBytes = str.encode(newSVG)

            name_2 =  os.path.basename(urlparse(name).path).replace(".svg", "_focus.png")
            filename = os.path.abspath(os.path.join(iconsFolder, name_2))

            if not os.path.exists(iconsFolder):
                os.makedirs(iconsFolder)

            if not os.path.exists(filename):
                try:
                    cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                except Exception as e:
                    print(e)
    

        # Create disabled icons
        with codecs.open(name, encoding='utf-8', errors='ignore') as f:
            content = f.read()

            newSVG = content.replace(svg_color, disabled_color)
            newBytes = str.encode(newSVG)

            name_2 =  os.path.basename(urlparse(name).path).replace(".svg", "_disabled.png")
            filename = os.path.abspath(os.path.join(iconsFolder, name_2))
            
            if not os.path.exists(iconsFolder):
                os.makedirs(iconsFolder)

            if not os.path.exists(filename):
                try:
                    cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                except Exception as e:
                    print(e)
                
        progress(int((list_of_files.index(name)/totalIcons) * 100), 100)

    print("\nCreating the resources (py) file")
    # Check resource file
    resource_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/QSS_Resources.qrc'))
    if not os.path.exists(resource_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'QSS_Resources.qrc')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))  
    py_resource_path = resource_path.replace(".qrc", ".py")
    py_resource_path = py_resource_path.replace("QSS/", "")
    py_resource_path = py_resource_path.replace("QSS\\", "") #for win
    py_resource_path = py_resource_path.replace("QSS_Resources", "QSS_Resources_rc")
    # Convert qrc to py
    try:
        os.system('pyrcc5 '+'"'+resource_path+'" -o "'+py_resource_path+'"')
    except Exception as e:
        raise e  

    print("Resources (py) file created")





# Current Directory
currentDir = os.getcwd()
print("""
########################################################################
## SPINN DESIGN CODE
# THE CUSTOM WIDGETS MODULE FOR QT
# PROJECT MAKER
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinntv.com
# EMAIL: info@spinntv.com
########################################################################

########################################################################
## INITIALIZING A NEW PROJECT TO:
########################################################################
    """)
print(currentDir)

# Check if the folder is empty
if any(os.scandir(currentDir)):
    print("""
########################################################################
## EXITING BECAUSE THE FOLDER IS NOT EMPTY
########################################################################
Please select an empty folder
        """)
    exit()

print("""

########################################################################

    """)
print("Creating resources folder")

qcss_folder = os.path.abspath(os.path.join(os.getcwd(), 'QSS'))
if not os.path.exists(qcss_folder):
    os.makedirs(qcss_folder)

print("Resources folder created")

print("Creating (qrc) resource file")
# Check resource file
resource_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/QSS_Resources.qrc'))
if not os.path.exists(resource_path):   
    shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Qss/QSS_Resources.qrc')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))

print("Resource (qrc) file created")

print("Creating the main (UI) interface file")
# Check ui file
resource_path = os.path.abspath(os.path.join(os.getcwd(), 'interface.ui'))
if not os.path.exists(resource_path):   
    shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/uis/interface.ui')), os.getcwd())  


print("Main (UI) interface file created")

print("Creating the main (py) python file")
# Check main file
resource_path = os.path.abspath(os.path.join(os.getcwd(), 'main.py'))
if not os.path.exists(resource_path):   
    shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/python/main.py')), os.getcwd())  

print("Main (py) python file created")

print("Creating the icons (png) files")

print("""

########################################################################
PLEASE ENTER YOUR ICONS COLOR BELOW:
########################################################################
You can pass the color HEX value such as #fff
or the color string value like white

    """)

while True:
    iconsColor = input("Enter icons color: ")
    if iconsColor.isspace() or iconsColor == "":
        print("Icons color can not be empty")
        print("!!!!!!")
        continue
    if not QColor().isValidColor(iconsColor):
        print(iconsColor, "is not a valid color")
        print("!!!!!!")
        continue
    if query_yes_no("Your icons color is " + str(iconsColor) + ". Save the color and continue?"):
        break

generateIcons(iconsColor)

print("Icons have been created")

print("Creating UI (py) file")
# Check ui(py) file
resource_path = os.path.abspath(os.path.join(os.getcwd(), 'ui_interface.py'))
if not os.path.exists(resource_path):   
    shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/python/ui_interface.py')), os.getcwd())  

print("UI (py) file has been created")


print("Creating the JSON stylesheet file")

print("""

########################################################################
PLEASE FILL IN THE REQUIRED DATA BELOW:
########################################################################

    """)

while True:
    appName = input("Enter your app name: ")
    if appName.isspace() or appName == "":
        print("App name can not be empty")
        print("!!!!!!")
        continue
    if query_yes_no("Your app name is " + appName + ". Save the name and continue?"):
        break

print("""

########################################################################
THE FOLLOWING VALUES WILL BE USED TO SAVE YOUR APP CONFIGURATIONS SUCH AS
APP APP THEME USING THE QSETTINGS CLASS

The required value are application name, organisation name and domain name.
If left empty, your app name will be used, you can change this later
from the JSON stylesheet file inside your project
########################################################################

    """)

while True:
    organizationName = input("Please enter the your organization name (Optional): ")
    if organizationName.isspace() or organizationName == "":
        organizationName = appName+" Company"
        break
    if query_yes_no("Your organization name is " + organizationName + ". Save the organization name and continue?"):
        break

while True:
    domainName = input("Please enter the your domain name. Please enter a URL i.e domain.org (Optional): ")
    if domainName.isspace() or domainName == "":
        domainName = appName+".org"
        break
    # if not QUrl(domainName).isValid():
    #     print("Invalid URL: %s", domainName, " Domain name must be a URL like domain.org")
    #     continue
    if query_yes_no("Your domain name is " + domainName + ". Save the domain name and continue?"):
        break


# Check json file
json_path = os.path.abspath(os.path.join(os.getcwd(), 'style.json'))
if not os.path.exists(json_path):   
    shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/json/style.json')), os.getcwd())  

with open(json_path, 'r+') as f:
    data = json.load(f)
    print(data)
    if "QMainWindow" in data:
        for QMainWindow in data["QMainWindow"]:
            # Set window tittle
            QMainWindow["tittle"] = appName

    ########################################################################
    ## QSETTINGS
    ########################################################################
    if "QSettings" in data:
        for settings in data["QSettings"]:
            if "AppSettings" in settings:
                appSettings = settings['AppSettings']

                appSettings["OrginizationName"] = str(appName)
                
                appSettings["ApplicationName"] = str(organizationName)
                    
                appSettings["OrginizationDormain"] = str(domainName)

    f.seek(0)  
    json.dump(data, f, indent=4)
    f.truncate()


print("JSON stylesheet file created")

print("""

########################################################################
CONGRATULATIONS! YOUR PROJECT HAS BEEN CREATED.

WHAT NEXT??

1. Open the interface.ui file inside your project folder using QT designer.
This is your main inteface file.

2. Put your app customization/style inside the JSON style.json file.
Read more here on how to use the custom widgets module 
https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets

3. Run the main.py file to view your app. Get more tutorials 
here on how to create awsome QT Apps with python 
https://www.youtube.com/spinnTv

4. Your default app icons are located inside the QSS/Icons folder.

[The following is important only if you decide to use the theme maker]

5. The default QSASS and QSS stylesheet are also inside the QSS folder.

6. Put you own style (CSS or SCSS) inside the QSS/defaultStyle.scss file.
This style will override the default theme style. 

7. The QSS/_variables.scss contains your theme variables

########################################################################

    """)


while True:
    if not query_yes_no("Run the created project or exit the project wizard? Type yes to run the app or no to exit the wizard"):
        break
    else:
        print("""

########################################################################
RUNNING YOUR PROJECT
########################################################################
        """)
        call(["python", "main.py"])


exit()
