import cairosvg
import codecs
import os
import sys
import shutil
import importlib
import random
import string
from urllib.parse import urlparse
from pathlib import Path
import __main__



from . colorsystem import *
import qtpy
from qtpy.QtCore import *

settings = QSettings()

class NewIconsGenerator():
    """docstring for NewIconsGenerator"""
    def __init__(self, arg):
        super(NewIconsGenerator, self).__init__()
        self.arg = arg

    def generateNewIcons(self, progress_callback):  
        settings = QSettings()

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'icons/original_svg')
        list_of_files = []

        color = CreateColorVariable.getCurrentThemeInfo(self)
        svg_color = "#ffffff"
        normal_color = str(color["icons-color"])
        
        focused_color = adjust_lightness(normal_color, 1.5)
        disabled_color = adjust_lightness(normal_color, .5)

        iconsFolderName = normal_color.replace("#", "")
        iconsFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/'+iconsFolderName))
        # 
        oldIconsFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/Icons'))

        if settings.value("ICONS-COLOR") is None:        
            variablesFile = CreateColorVariable.getCurrentThemeInfo(self)
            oldIconsDestinationFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/'+variablesFile['icons-color'].replace("#", "")))
        else:
            oldIconsDestinationFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/'+settings.value("ICONS-COLOR").replace("#", "")))

        if not settings.value("ICONS-COLOR") == normal_color and color["icons-color"] is not None:
            if self.showCustomWidgetsLogs:
                print("Current icons color ", settings.value("ICONS-COLOR"), "New icons color", normal_color)
                print("Generating icons for your theme, please wait. This may take long")

            for root, dirs, files in os.walk(filename):
                for file in files:
                    list_of_files.append(os.path.join(root,file))

            totalIcons = len(list_of_files)

            for name in list_of_files:
                # Move old icons
                name_2 =  os.path.basename(urlparse(name).path).replace(".svg", ".png")
                if os.path.exists(os.path.join(oldIconsFolder, name_2)) and not os.path.exists(os.path.join(oldIconsDestinationFolder, name_2)):
                    shutil.move(os.path.join(oldIconsFolder, name_2), oldIconsDestinationFolder)

                name_2 =  os.path.basename(urlparse(name).path).replace(".svg", "_focus.png")
                if os.path.exists(os.path.join(oldIconsFolder, name_2)) and not os.path.exists(os.path.join(oldIconsDestinationFolder, name_2)):
                    shutil.move(os.path.join(oldIconsFolder, name_2), oldIconsDestinationFolder)

                name_2 =  os.path.basename(urlparse(name).path).replace(".svg", "_disabled.png")
                if os.path.exists(os.path.join(oldIconsFolder, name_2)) and not os.path.exists(os.path.join(oldIconsDestinationFolder, name_2)):
                    shutil.move(os.path.join(oldIconsFolder, name_2), oldIconsDestinationFolder)

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
                            # Convert each SVG icon to png
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
                            # Convert each SVG icon to png
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
                            # Convert each SVG icon to png
                            cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                        except Exception as e:
                            print(e)
                        

                # EMMIT PROGRESS VALUE
                progress_callback.emit(int((list_of_files.index(name)/totalIcons) * 100))


            source_dir = iconsFolder
            target_dir = oldIconsFolder
            
            if not os.path.isdir(source_dir):
                # Delete the file if it exists
                if os.path.exists(source_dir):
                    os.remove(source_dir)
                # Create a new directory
                try:
                    os.mkdir(source_dir)
                except OSError as e:
                    print(f"Creation of the directory {source_dir} failed: {e}")
                
            file_names = os.listdir(source_dir)

            if not os.path.exists(oldIconsFolder):
                os.makedirs(oldIconsFolder)
            else:
                if not os.path.exists(oldIconsFolder):
                    os.makedirs(oldIconsFolder)

            filesMoved = 0   
            for file_name in file_names:
                if os.name == 'nt':
                    shutil.copy(os.path.join(source_dir, file_name), target_dir)
                else:
                    try:
                        shutil.move(os.path.join(source_dir, file_name), target_dir)
                    except Exception as e:
                        shutil.copy(os.path.join(source_dir, file_name), target_dir)
                    

                filesMoved += 1
                # EMMIT PROGRESS VALUE
                progress_callback.emit(int((filesMoved/totalIcons) * 100))


            # Check resource file
            resource_path = os.path.abspath(os.path.join(os.getcwd(), 'QSS/QSS_Resources.qrc'))
            if not os.path.exists(resource_path):   
                shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'QSS_Resources.qrc')), os.path.abspath(os.path.join(os.getcwd(), 'QSS')))  
            py_resource_path = resource_path.replace(".qrc", ".py")
            py_resource_path = py_resource_path.replace("QSS/", "") #linux
            py_resource_path = py_resource_path.replace("QSS\\", "") #windows
            py_resource_path = py_resource_path.replace("QSS_Resources", "QSS_Resources_rc")
            # Convert qrc to py
            try:
                settings.setValue("ICONS-COLOR", normal_color)
                if qtpy.API_NAME == "PyQt5":
                    os.system('pyrcc5 "'+resource_path+'" -o "'+py_resource_path+'"')
                if qtpy.API_NAME == "PyQt6":
                    os.system('pyrcc6 "'+resource_path+'" -o "'+py_resource_path+'"')
                elif qtpy.API_NAME == "PySide2":
                    os.system('pyside2-rcc "'+resource_path+'" -o "'+py_resource_path+'"')
                elif qtpy.API_NAME == "PySide6":
                    os.system('pyside6-rcc "'+resource_path+'" -o "'+py_resource_path+'"')
                else:
                    raise Exception("Error: Uknown QT binding/API Name", qtpy.API_NAME)
                

                settings.setValue("ICONS-COLOR", normal_color)
            except Exception as e:
                # raise e
                print("error while converting resource file")  

            # Reload resources:
            resource_module = "QSS_Resources_rc"  # Replace with your resource module name
            # NewIconsGenerator.reload_resources(self, resource_module)

        else:
            ## GENERATE OTHER ICONS
            NewIconsGenerator.generateAllIcons(self, progress_callback) 

    def reload_resources(self, resource_module):
        # Generate a random name for the new resource file
        random_name = ''.join(random.choices(string.ascii_lowercase, k=8))
        new_resource_file = f"QSS_Resources_rc_{random_name}.py"

        # Copy the resource.py file to the new name
        os.rename("QSS_Resources_rc.py", new_resource_file)

        # Delete any old resource files in the directory
        for file in os.listdir():
            if file.startswith("QSS_Resources_rc_") and file.endswith(".py") and file != new_resource_file:
                os.remove(file)

        # Import the new resource module
        resource_module = importlib.import_module(new_resource_file[:-3])

        print("resource loaded")

    def generateAllIcons(self, progress_callback):
        settings = QSettings()
        svg_color = "#ffffff"
        dirname = os.path.dirname(__file__)
        original_svg_folder = os.path.join(dirname, 'icons/original_svg')
        themes = self.ui.themes

        def get_theme_color(theme):
            if hasattr(theme, "iconsColor") and theme.iconsColor:
                return theme.iconsColor
            return theme.accentColor

        def create_icon_set(color, suffix):
            new_color = adjust_lightness(color, 1.1 if suffix == "" else 1.0)
            for name in list_of_files:
                with codecs.open(name, encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    new_svg = content.replace(svg_color, new_color)
                    new_bytes = str.encode(new_svg)

                    name_2 = os.path.basename(urlparse(name).path).replace(".svg", f"_{suffix}.png")
                    filename = os.path.abspath(os.path.join(icons_folder, name_2))

                    if os.path.exists(filename):
                        continue

                    try:
                        cairosvg.svg2png(bytestring=new_bytes, write_to=filename)
                    except Exception as e:
                        print(e)

        list_of_files = []
        total_icons = 0

        for theme in themes:
            if self.showCustomWidgetsLogs:
                print(f"Checking icons for {theme.name}")

            color = get_theme_color(theme)
            focused_color = adjust_lightness(color, 1.1)
            disabled_color = adjust_lightness(color, 0.2)
            icons_folder_name = color.replace("#", "")
            icons_folder = os.path.abspath(os.path.join(os.getcwd(), f'QSS/{icons_folder_name}'))

            if self.showCustomWidgetsLogs:
                print(f"Generating missing icons for your theme {color}. Please wait. This may take long")

            for root, dirs, files in os.walk(original_svg_folder):
                list_of_files.extend([os.path.join(root, file) for file in files])

            total_icons += len(list_of_files)

            for suffix in ("", "focus", "disabled"):
                create_icon_set(color, suffix)

                if settings.value("ICONS-COLOR") and settings.value("ICONS-COLOR").replace("#", "") == icons_folder_name:
                    # RENAME FOLDER
                    old_icons_folder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/Icons'))
                    for name in list_of_files:
                        name_2 = os.path.basename(urlparse(name).path).replace(".svg", f"_{suffix}.png")
                        if os.path.exists(os.path.join(old_icons_folder, name_2)):
                            shutil.move(os.path.join(old_icons_folder, name_2), icons_folder)

                # EMIT PROGRESS VALUE
                progress_callback.emit(int((total_icons / len(list_of_files)) * 100))



