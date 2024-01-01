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
import subprocess
import cairosvg
import codecs
import shutil
import json
from urllib.parse import urlparse
import argparse

from termcolor import colored  # Install termcolor using: pip install termcolor
import textwrap


########################################################################
## MODULE UPDATED TO USE QTPY
########################################################################
from qtpy.QtCore import QUrl
from qtpy.QtGui import QColor

from . Qss.colorsystem import *


def progress(count, total, status=''):
    bar_len = 30
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

def generateIcons(iconsColor = "#ffffff"):  
    # Files folder
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Qss/icons/original_svg')
    list_of_files = []

    svg_color = "#ffffff"
    normal_color = iconsColor

    focused_color = lighten_color(normal_color)
    disabled_color = darken_color(normal_color, .5)


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
    global resource_path, py_resource_path
    resource_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/QSS_Resources.qrc'))
    if not os.path.exists(resource_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'QSS_Resources.qrc')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))  
    py_resource_path = resource_path.replace(".qrc", ".py")
    py_resource_path = py_resource_path.replace("QSS/", "")
    py_resource_path = py_resource_path.replace("QSS\\", "") #for win
    py_resource_path = py_resource_path.replace("QSS_Resources", "QSS_Resources_rc")

def convert_ui_to_py(ui_path, output_py_path, app_module):
    if app_module == "PySide6":
        subprocess.run(["pyside6-uic", ui_path, "-o", output_py_path])
    elif app_module == "PySide2":
        subprocess.run(["pyside2-uic", ui_path, "-o", output_py_path])
    elif app_module == "PyQt6":
        subprocess.run(["pyuic6", ui_path, "-o", output_py_path])
    elif app_module == "PyQt5":
        subprocess.run(["pyuic5", ui_path, "-o", output_py_path])
    else:
        print(colored(textwrap.dedent(f"Unsupported Qt app module: {app_module}"), "red"))

def convert_qrc_to_py(qrc_path, output_py_path, app_module):
    if app_module == "PySide6":
        subprocess.run(["pyside6-rcc", qrc_path, "-o", output_py_path])
    elif app_module == "PySide2":
        subprocess.run(["pyside2-rcc", qrc_path, "-o", output_py_path])
    elif app_module == "PyQt6":
        subprocess.run(["pyrcc6", qrc_path, "-o", output_py_path])
    elif app_module == "PyQt5":
        subprocess.run(["pyrcc5", qrc_path, "-o", output_py_path])
    else:
        print(colored(textwrap.dedent(f"Unsupported Qt app module: {app_module}"), "red"))


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
    qrc_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/QSS_Resources.qrc'))
    if not os.path.exists(qrc_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Qss/QSS_Resources.qrc')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))
    
    
    # Check ui file
    ui_path = os.path.abspath(os.path.join(os.getcwd(), 'interface.ui'))
    if not os.path.exists(ui_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/uis/interface.ui')), os.getcwd())  

    # App module
    print(textwrap.dedent("""
    #PLEASE ENTER YOUR QT APP MODULE:
    (Default: PySide6) (Options: PySide6, PySide2, PyQt6, PyQt5)
    """))

    global appModule

    while True:
        appModule = input(textwrap.dedent("Enter your app module: "))
        if appModule.isspace() or appModule == "":
            print(colored(textwrap.dedent("QT App module set to PySide6"), "red"))
            appModule = "PySide6"
            break
        if appModule != "PySide6" and appModule != "PySide2" and appModule != "PyQt6" and appModule != "PyQt5":
            print(colored(textwrap.dedent(appModule+ " is not a valid qt app module"), "red"))
            continue
        if query_yes_no(colored(textwrap.dedent("Your QT App module is " + str(appModule) + ".  Continue?"), "blue")):
            break

    # Check main file
    main_py = os.path.abspath(os.path.join(os.getcwd(), 'main.py'))
    if not os.path.exists(main_py):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/python/main.py')), os.getcwd())  

    # Check ui(py) file
    ui_output_py_path = os.path.abspath(os.path.join(os.getcwd(), 'ui_interface.py'))
    if not os.path.exists(ui_output_py_path):   
        shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'components/python/ui_interface.py')), os.getcwd())  

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

    generateIcons(iconsColor)

    # Generate py files from ui and qrc
    convert_ui_to_py(ui_path, ui_output_py_path, appModule)
    convert_qrc_to_py(resource_path, py_resource_path, appModule) 

    print(textwrap.dedent("Icons have been created"))

    print(textwrap.dedent("Creating the JSON stylesheet file"))

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
        data["QtModule"] = appModule
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

    """))

    print(colored(textwrap.dedent("You can also leave this window open as you work on your project. To preview your app just click enter. The UI and QRC file will be automatically converted for you!"), "yellow"))


    while True:
        if not query_yes_no(colored(textwrap.dedent("Run the created project or exit the project wizard? Type yes to run the app or no to exit the wizard"), "blue")):
            break
        else:
            convert_qrc_to_py(resource_path, py_resource_path, appModule) 
            convert_ui_to_py(ui_path, ui_output_py_path, appModule)

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
        print(textwrap.dedent("No valid command provided. Use 'Custom_Widgets --create-project' or 'Custom_Widgets --build-widgets'."))


if __name__ == "__main__":
    run_command()
