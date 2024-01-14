########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
# EMAIL: info@spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
from subprocess import call
import shutil
import json
from urllib.parse import urlparse
import argparse

from termcolor import colored  # Install termcolor using: pip install termcolor
import textwrap

from qtpy.QtCore import Signal

from . Qss.SvgToPngIcons import *


########################################################################
## MODULE UPDATED TO USE QTPY
########################################################################
from qtpy.QtCore import QUrl
from qtpy.QtGui import QColor

from . Qss.colorsystem import *

########################################################################
## WORKER SIGNAL CLASS
########################################################################
class ProjectMakerSignals(QObject):
    progress = Signal(int)

def progress(count, status='Done'):
    bar_len = 30
    total = 100
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

def create_project():
    # Current Directory
    currentDir = os.getcwd()
    print(colored(textwrap.dedent("""
    # PROJECT MAKER
    # YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
    # WEBSITE: spinncode.com
    # EMAIL: info@spinncode.com

    # INITIALIZING A NEW PROJECT TO:"""), "green"))

    print(f"Current Folder: {currentDir}")

    # Check if the folder is empty
    if any(os.scandir(currentDir)):
        print(colored(textwrap.dedent("""
        ## EXITING BECAUSE THE FOLDER IS NOT EMPTY
        Please select an empty folder"""), "red"))

        exit()

    print(textwrap.dedent("Creating resources and folder..."))

    qcss_folder = os.path.abspath(os.path.join(os.getcwd(), 'QSS'))
    if not os.path.exists(qcss_folder):
        os.makedirs(qcss_folder)

    # Check resource file
    # qrc_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/QSS_Resources.qrc'))
    # if not os.path.exists(qrc_path):   
    #     shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Qss/QSS_Resources.qrc')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))
    
    
    # Check ui file
    ui_path = os.path.abspath(os.path.join(os.getcwd(), 'interface.ui'))
    if not os.path.exists(ui_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/uis/interface.ui')), os.getcwd())  

    # App Qt binding/API Name
    print(textwrap.dedent("""
    #PLEASE ENTER YOUR Qt APP Qt binding/API Name:
    (Default: PySide6) (Options: PySide6, PySide2, PyQt6, PyQt5)
    """))

    global appQtBinding

    while True:
        appQtBinding = input(textwrap.dedent("Enter your app Qt binding/API Name: "))
        if appQtBinding.isspace() or appQtBinding == "":
            print(colored(textwrap.dedent("Qt App Qt binding/API Name set to PySide6"), "red"))
            appQtBinding = "PySide6"
            break
        if appQtBinding != "PySide6" and appQtBinding != "PySide2" and appQtBinding != "PyQt6" and appQtBinding != "PyQt5":
            print(colored(textwrap.dedent(appQtBinding+ " is not a valid qt app Qt binding/API Name"), "red"))
            continue
        if query_yes_no(colored(textwrap.dedent("Your Qt App Qt binding/API Name is " + str(appQtBinding) + ".  Continue?"), "blue")):
            break

    # Update Qt Binding
    qtpy.API_NAME = appQtBinding
    os.environ['QT_API'] = appQtBinding.lower()

    # Check main file
    main_py = os.path.abspath(os.path.join(os.getcwd(), 'main.py'))
    if not os.path.exists(main_py):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/python/main.py')), os.getcwd())  

    # # Check ui(py) file
    ui_output_py_path = os.path.abspath(os.path.join(os.getcwd(), 'ui_interface.py'))
    # if not os.path.exists(ui_output_py_path):   
    #     shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/python/ui_interface.py')), os.getcwd())  

    print(textwrap.dedent("Creating the icons (png) files"))

    print(textwrap.dedent("""
    #PLEASE ENTER YOUR ICONS COLOR BELOW:
    You can pass the color HEX value such as #ffffff
    or the color string value like white
    """))

    while True:
        iconsColor = input(textwrap.dedent("Enter icons color: "))
        if iconsColor.isspace() or iconsColor == "":
            print(colored(textwrap.dedent("Icons color can not be empty"), "red"))
            continue
        if not QColor().isValidColor(iconsColor):
            print(colored(textwrap.dedent(iconsColor+ " is not a valid color"), "red"))
            continue
        if query_yes_no(colored(textwrap.dedent("Your icons color is " + str(iconsColor) + ". Save the color and continue?"), "blue")):
            break

    signals = ProjectMakerSignals()
    progress_callback = signals.progress
    signals.progress.connect(progress)

    # Create colors
    normal_color = color_to_hex(iconsColor)
    focused_color = lighten_color(normal_color)
    disabled_color = darken_color(normal_color, .5)

    iconsFolderName = normal_color.replace("#", "")

    print(textwrap.dedent(f"\nGenerating normal icons for color: {iconsColor}"))
    NewIconsGenerator.generateIcons(progress_callback, normal_color, "", "Icons", createQrc = True)
    # print(textwrap.dedent(f"\nGenerating fucused icons for color: {iconsColor}"))
    # NewIconsGenerator.generateIcons(progress_callback, focused_color, "_focus", iconsFolderName)
    # print(textwrap.dedent(f"\nGenerating disabled icons for color: {iconsColor}"))
    # NewIconsGenerator.generateIcons(progress_callback, disabled_color, "_disabled", iconsFolderName)

    # Move icons
    # print(textwrap.dedent("\nMoving icons to Icons folder") )
    # destinationFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/Icons'))
    # sourceFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/'+iconsFolderName))
    # NewIconsGenerator.moveIcons(sourceFolder, destinationFolder)

    print(textwrap.dedent("Icons have been created"))

    # print(textwrap.dedent("\nCreating the resources (py) file"))
    # # Check resource file
    # qrcFile, pyDest = NewIconsGenerator.checkQrc()
    # # Convert qrc to py 
    # NewIconsGenerator.qrcToPy(qrcFile, pyDest)

    # Generate py from ui
    NewIconsGenerator.uiToPy(ui_path, ui_output_py_path)

    print(textwrap.dedent("\nCreating the JSON stylesheet file"))

    print(textwrap.dedent(f"""
    #PLEASE FILL IN THE REQUIRED DATA BELOW:
    Default value will be set to {os.path.basename(os.getcwd())}
    """))

    while True:
        appName = input(textwrap.dedent("Enter your app name: "))
        if appName.isspace() or appName == "":
            appName = os.path.basename(os.getcwd())
            
        if query_yes_no(colored(textwrap.dedent("Your app name is " + appName + ". Save the name and continue?"), "blue")):
            break

    print(textwrap.dedent("""
    THE FOLLOWING VALUES WILL BE USED TO SAVE YOUR APP CONFIGURATIONS SUCH AS
    APP THEME USING THE QSETTINGS CLASS

    The required value are application name, organisation name and domain name.
    If left empty, your app name will be used, you can change this later
    from the JSON stylesheet file inside your project
    """))

    while True:
        organizationName = input(textwrap.dedent("Please enter the your organization name (Optional): "))
        if organizationName.isspace() or organizationName == "":
            organizationName = appName+" Company"
            break
        if query_yes_no(colored(textwrap.dedent("Your organization name is " + organizationName + ". Save the organization name and continue?"), "blue")):
            break

    while True:
        domainName = input(textwrap.dedent("Please enter the your domain name. Please enter a URL i.e domain.org (Optional): "))
        if domainName.isspace() or domainName == "":
            domainName = appName+".org"
            break
        # if not QUrl(domainName).isValid():
        #     print("Invalid URL: %s", domainName, " Domain name must be a URL like domain.org")
        #     continue
        if query_yes_no(colored(textwrap.dedent("Your domain name is " + domainName + ". Save the domain name and continue?"), "blue")):
            break


    # Check json file
    json_path = os.path.abspath(os.path.join(os.getcwd(), 'style.json'))
    if not os.path.exists(json_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/json/style.json')), os.getcwd())  

    with open(json_path, 'r+') as f:
        data = json.load(f)
        # print(data)
        data["QtBinding"] = appQtBinding
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


    print(textwrap.dedent("JSON stylesheet file created"))

    print(textwrap.dedent("""

    CONGRATULATIONS! YOUR PROJECT HAS BEEN CREATED.

    WHAT NEXT??

    1. Open the interface.ui file inside your project folder using Qt designer.
    This is your main inteface file.

    2. Put your app customization/style inside the JSON style.json file.
    Read more here on how to use the custom widgets module 
    https://github.com/KhamisiKibet/Qt-PyQt-PySide-Custom-Widgets

    3. Run the main.py file to view your app. Get more tutorials 
    here on how to create awsome Qt Apps with python 
    https://www.youtube.com/spinnTv

    4. Your default app icons are located inside the QSS/Icons folder.

    [The following is important only if you decide to use the theme maker]

    5. The default QSASS and QSS stylesheet are also inside the QSS folder.

    6. Put you own style (CSS or SCSS) inside the QSS/defaultStyle.scss file.
    This style will override the default theme style. 

    7. The QSS/_variables.scss contains your theme variables

    """))

    print(colored(textwrap.dedent("You can also leave this window open as you work on your project. To preview your app just click enter. The UI and QRC file will be automatically converted for you!"), "yellow"))


    while True:
        if not query_yes_no(colored(textwrap.dedent("Run the created project or exit the project wizard? Type yes to run the app or no to exit the wizard"), "blue")):
            break
        else:
            # Convert qrc to py 
            # NewIconsGenerator.qrcToPy(qrcFile, pyDest)
            NewIconsGenerator.uiToPy(ui_path, ui_output_py_path)

            print(textwrap.dedent("""
            RUNNING YOUR PROJECT
            """))
            call(["python", "main.py"])

    exit()

def run_command():
    parser = argparse.ArgumentParser(description='Custom Widgets Project Maker')
    parser.add_argument('--create-project', action='store_true', help='Create a new project')
    parser.add_argument('--build-widgets', action='store_true', help='Build custom widgets')

    args = parser.parse_args()

    if args.create_project:
        create_project()
    else:
        print(textwrap.dedent("No valid command provided. Use 'Custom_Widgets --create-project'."))


if __name__ == "__main__":
    run_command()
