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

from Custom_Widgets.Qss.SvgToPngIcons import *


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

def create_requirements_file(required_packages, file_path="requirements.txt"):
    """
    Create a requirements.txt file with the specified package names and versions.

    Args:
        required_packages (list): List of required packages with optional versions.
        file_path (str, optional): Path to the requirements.txt file. Defaults to "requirements.txt".
    """
    # Write the package names to the requirements.txt file
    with open(file_path, "w") as file:
        for package in required_packages:
            file.write(package + "\n")


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

    # Check if any file or folder other than the logs folder exists
    if any(entry.is_file() or (entry.is_dir() and entry.name != "logs") for entry in os.scandir()):
        print(os.scandir(currentDir))
        print(colored(textwrap.dedent("""
        ## EXITING BECAUSE THE FOLDER IS NOT EMPTY
        Please select an empty folder"""), "red"))

        exit()
    
    # Check ui file
    ui_path = os.path.abspath(os.path.join(os.getcwd(), 'ui/interface.ui'))
    if not os.path.exists(os.path.abspath(os.path.join(os.getcwd(), 'ui'))):
        os.mkdir(os.path.abspath(os.path.join(os.getcwd(), 'ui')))
    if not os.path.exists(ui_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/uis/interface.ui')), os.path.join(os.getcwd(),"ui"))  

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

    

    print(textwrap.dedent("""
    # PLEASE ENTER YOUR ICONS COLOR BELOW:
    You can input the color HEX value (e.g., #ffffff)
    or the color string value (e.g., white).
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

    

    print(textwrap.dedent(f"""
    # NOW ENTER ICONS COLOR FOR QT DESIGNER APP:
    NOTE: This is for design purposes only. If your Qt Designer app 
    has a dark theme, enter a light icons color (e.g., "white").
    If Qt Designer has a light theme, enter a dark icons color (e.g., "black").
    Default value will be set to {iconsColor}.
    """))

    while True:
        qtIconsColor = input(textwrap.dedent("Enter icons color: "))
        if qtIconsColor.isspace() or qtIconsColor == "":
            qtIconsColor = iconsColor
            break
        if not QColor().isValidColor(qtIconsColor):
            print(colored(textwrap.dedent(qtIconsColor+ " is not a valid color"), "red"))
            continue
        if query_yes_no(colored(textwrap.dedent("Your icons color is " + str(qtIconsColor) + ". Save the color and continue?"), "blue")):
            break
    
    qt_normal_color = color_to_hex(qtIconsColor)
    

    print(textwrap.dedent(f"""
    # THIS IS FOR YOUR APP THEME:
    NOTE: Background color, text color, and accent color will be used to create your app stylesheet.
    """))

    while True:
        bgColor = input(textwrap.dedent("Enter app background color: "))
        if bgColor.isspace() or bgColor == "":
            print(colored(textwrap.dedent("Background color can not be empty"), "red"))
            continue
        if not QColor().isValidColor(bgColor):
            print(colored(textwrap.dedent(bgColor+ " is not a valid color"), "red"))
            continue
        if query_yes_no(colored(textwrap.dedent("Your app background color is " + str(bgColor) + ". Save the color and continue?"), "blue")):
            break

    bgColor = color_to_hex(bgColor)

    while True:
        txtColor = input(textwrap.dedent("Enter app text color: "))
        if txtColor.isspace() or txtColor == "":
            print(colored(textwrap.dedent("Text color can not be empty"), "red"))
            continue
        if not QColor().isValidColor(txtColor):
            print(colored(textwrap.dedent(txtColor+ " is not a valid color"), "red"))
            continue
        if query_yes_no(colored(textwrap.dedent("Your app text color is " + str(txtColor) + ". Save the color and continue?"), "blue")):
            break

    txtColor = color_to_hex(txtColor)

    while True:
        accColor = input(textwrap.dedent("Enter app accent color: "))
        if accColor.isspace() or accColor == "":
            print(colored(textwrap.dedent("Accent color can not be empty"), "red"))
            continue
        if not QColor().isValidColor(accColor):
            print(colored(textwrap.dedent(accColor+ " is not a valid color"), "red"))
            continue
        if query_yes_no(colored(textwrap.dedent("Your app accent color is " + str(accColor) + ". Save the color and continue?"), "blue")):
            break

    accColor = color_to_hex(accColor)

    # Generate py from ui
    call(["Custom_Widgets", "--convert-ui", "ui", "--qt-library", appQtBinding])

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
    APP THEME USING THE QSETTINGS CLASS:

    The required values are application name, organization name, and domain name.
    If left empty, your app name will be used. You can change this later
    from the JSON stylesheet file inside your project.
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
    json_path = os.path.abspath(os.path.join(os.getcwd(), 'json-styles/style.json'))
    if not os.path.exists(os.path.abspath(os.path.join(os.getcwd(), 'json-styles'))):
        os.mkdir(os.path.abspath(os.path.join(os.getcwd(), 'json-styles')))
    if not os.path.exists(json_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/json/style.json')), os.path.join(os.getcwd(), 'json-styles')) 
      
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
                appSettings = settings['AppSettings']
                appSettings["OrginizationName"] = str(appName)
                appSettings["ApplicationName"] = str(organizationName)
                appSettings["OrginizationDormain"] = str(domainName)
                
                themeSettings = settings['ThemeSettings']
                for theme_setting in themeSettings:
                    customThemes = theme_setting['CustomTheme']
                    for customTheme in customThemes:
                        customTheme["Background-color"] = str(bgColor)
                        customTheme["Text-color"] = str(txtColor)
                        customTheme["Accent-color"] = str(accColor)
                        customTheme["Icons-color"] = str(normal_color)


        f.seek(0)  
        json.dump(data, f, indent=2)
        f.truncate()


    print(textwrap.dedent("JSON stylesheet file created"))

    # Requirements
    required_packages = [
        appQtBinding,
        "QT-PyQt-PySide-Custom-Widgets"
    ]
    create_requirements_file(required_packages)

    print(textwrap.dedent("Successfully created requirements.txt"))

    # Check README file 
    readme_path = os.path.abspath(os.path.join(os.getcwd(), 'README.md'))
    if not os.path.exists(readme_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/md/README.md')), os.getcwd()) 

    print(textwrap.dedent("Successfully created README.md"))

    print(textwrap.dedent("Creating the icons (png) files"))
    print(textwrap.dedent(f"\nGenerating icons for your app. Icons color: {iconsColor}"))
    NewIconsGenerator.generateIcons(progress_callback, normal_color, "", normal_color.replace("#", ""))
    print(textwrap.dedent(f"\nGenerating icons for Qt Designer app. Icons color: {qtIconsColor}"))
    NewIconsGenerator.generateIcons(progress_callback, qt_normal_color, "", "Icons", createQrc = True)
    print(textwrap.dedent("Icons have been created"))

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

    4. Your default app icons are located inside the qss/Icons folder.

    [The following is important only if you decide to use the theme maker]

    5. The default QSASS and qss stylesheet are also inside the qss folder.

    6. Put you own style (CSS or SCSS) inside the qss/defaultStyle.scss file.
    This style will override the default theme style. 

    7. The qss/_variables.scss contains your theme variables

    """))

    print(colored(textwrap.dedent("You can also leave this window open as you work on your project. To preview your app just click enter. The UI and QRC file will be automatically converted for you!"), "yellow"))


    while True:
        if not query_yes_no(colored(textwrap.dedent("Run the created project or exit the project wizard? Type yes to run the app or no to exit the wizard"), "blue")):
            break
        else:
            # Generate py from ui
            call(["Custom_Widgets", "--convert-ui", "ui", "--qt-library", appQtBinding])

            print(textwrap.dedent("""
            RUNNING YOUR PROJECT
            """))
            call(["python", "main.py"])

    exit()