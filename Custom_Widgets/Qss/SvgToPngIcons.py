# -*- coding: utf-8 -*-

import os

# FIX: DLL import issues
def set_dll_search_path():
    # Python 3.8 no longer searches for DLLs in PATH, so we have to add
    # everything in PATH manually. Note that unlike PATH add_dll_directory
    # has no defined order, so if there are two cairo DLLs in PATH we
    # might get a random one.
    if os.name != "nt" or not hasattr(os, "add_dll_directory"):
        return
    for p in os.environ.get("PATH", "").split(os.pathsep):
        try:
            os.add_dll_directory(p)
        except OSError:
            pass


set_dll_search_path()

import cairosvg
import codecs
import subprocess
import shutil
from urllib.parse import urlparse
import __main__

from Custom_Widgets.Qss.colorsystem import *
import qtpy
from qtpy.QtCore import *

from Custom_Widgets.Log import *

from PySide6.QtGui import QColor

class NewIconsGenerator(QObject):
    def __init__(self, arg):
        super(NewIconsGenerator, self).__init__()
        self.arg = arg

    def getAllFolders(base_folder):
        all_folders = []
        for root, dirs, files in os.walk(base_folder):
            for dir_name in dirs:
                folder_path = os.path.relpath(os.path.join(root, dir_name), base_folder)
                all_folders.append(folder_path)
        return all_folders

    def getAllSvgFiles(base_folder):
        svg_files = []
        for file_name in os.listdir(base_folder):
            if file_name.lower().endswith('.svg'):
                file_path = os.path.join(base_folder, file_name)
                svg_files.append(file_path)
        return svg_files
    
    def generateIcons(progress_callback, iconsColor, suffix, iconsFolder="", createQrc=False, output_width=None, output_height=None):
        # Base folder
        base_folder = os.path.dirname(__file__)
        icons_folder_base = os.path.join(base_folder, 'icons')

        svg_color = "#ffffff"

        # Get a list of all folders inside 'icons'
        folders = NewIconsGenerator.getAllFolders(icons_folder_base)
        new_icon_made = False
        qrc_content = f'<RCC>\n'

        qrc_folder_path = os.path.abspath(os.path.join(os.getcwd(), f'Qss/icons'))
        
        for folder in folders:
            qrc_prefix = (folder+suffix).replace("/", "_")
            qrc_prefix = (folder+suffix).replace("\\", "_")
            qrc_content += f'  <qresource prefix="{qrc_prefix}">\n'
            
            icons_folder_path = os.path.abspath(os.path.join(os.getcwd(), f'Qss/icons/{iconsFolder}/{folder}'))

            if not os.path.exists(icons_folder_path):
                os.makedirs(icons_folder_path)

            folder_path = os.path.join(icons_folder_base, folder)
            list_of_files = NewIconsGenerator.getAllSvgFiles(folder_path)
            total_icons = len(list_of_files)

            for index, file_path in enumerate(list_of_files):
                file_name = os.path.basename(urlparse(file_path).path).replace(".svg", f"{suffix}.png")
                output_path = os.path.abspath(os.path.join(icons_folder_path, file_name))

                qrc_content += f'    <file>icons/{folder}/{file_name}</file>\n'
                progress_callback.emit(int((index / total_icons) * 100))

                if os.path.exists(output_path):
                    continue

                try:
                    with codecs.open(file_path, encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                        new_svg = content.replace(svg_color, iconsColor)
                        new_bytes = str.encode(new_svg)

                        if output_height is not None and output_width is not None:
                            cairosvg.svg2png(bytestring=new_bytes, write_to=output_path, output_width=output_width, output_height=output_height)
                        
                        else:
                            cairosvg.svg2png(bytestring=new_bytes, write_to=output_path)

                        new_icon_made = True

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

            qrc_content += f'  </qresource>\n'

        qrc_content += f'</RCC>\n'
        qrc_file_path = os.path.abspath(os.path.join(qrc_folder_path, f'{suffix}_icons.qrc'))

        if (createQrc and new_icon_made) or not os.path.exists(qrc_file_path):
            NewIconsGenerator.createQrcFile(qrc_content, qrc_file_path)
            # Convert qrc to py 
            # qrc_output_path = qrc_file_path.replace(".qrc", "_rc.py")
            # qrc_output_path = qrc_output_path.replace("Qss/", "") #linux
            # qrc_output_path = qrc_output_path.replace("Qss\\", "") #windows
            # NewIconsGenerator.qrcToPy(qrc_file_path, qrc_output_path)

    def generateNewIcons(self, progress_callback): 
        # Icons color
        color = CreateColorVariable.getCurrentThemeInfo(self)
        normal_color = str(color["icons-color"])
        
        settings = QSettings()
        if not settings.value("ICONS-COLOR") == normal_color and color["icons-color"] is not None:
            logInfo(self, ("Current icons color ", settings.value("ICONS-COLOR"), "New icons color", normal_color))
            logInfo(self, "Generating icons for your theme, please wait. This may take long")
            
            settings.setValue("ICONS-COLOR", normal_color)
            iconsFolderName = normal_color.replace("#", "")
            self.themeEngine.applyIcons(self, folder=iconsFolderName)

            if not self.checkForMissingicons:
                # emit 100% progress
                progress_callback.emit(100)
                return 
            # Create normal icons
            NewIconsGenerator.generateIcons(progress_callback, normal_color, "", iconsFolderName, createQrc = False)

            logInfo(self, ("DONE: Current icons color ", settings.value("ICONS-COLOR")))
                

    def generateAllIcons(self, progress_callback):
        if not self.checkForMissingicons:
            # emit 100% progress
            progress_callback.emit(100)
            return
        
        themes = self.ui.themes
        def get_theme_color(theme):
            if hasattr(theme, "iconsColor") and theme.iconsColor != "":
                return theme.iconsColor
            if hasattr(theme, "accentColor") and theme.accentColor != "":
                return theme.accentColor
            return ""

        for theme in themes:
            color = get_theme_color(theme)
            try:
                if color == "" or color == settings.value("ICONS-COLOR"):
                    continue
            except:
                pass

            logInfo(self, f"Checking icons for {theme.name} theme. Icons color: {color}")

            iconsFolderName = color.replace("#", "")
            NewIconsGenerator.generateIcons(progress_callback, color, "", iconsFolderName)
        
        # then make icons for qt designer
        logInfo(self, f"Checking icons for qt designer app.")
        if settings.value("DESIGNER-ICONS-COLOR") is not None:
            NewIconsGenerator.generateIcons(progress_callback, settings.value("DESIGNER-ICONS-COLOR"), "", "icons", createQrc=True, output_width=24, output_height=24)
        else:
            NewIconsGenerator.generateIcons(progress_callback, "#000", "", "icons", createQrc=True, output_width=24, output_height=24)

    def createQrcFile(contents, filePath):
        # Save QRC content to a file
        with open(filePath, 'w', encoding='utf-8') as qrc_file:
            qrc_file.write(contents)

        # print(f'QRC file generated: {filePath}')
    
    def qrcToPy(qrcFile, pyFile):
        """
        Convert a Qt Resource Collection (qrc) file to a Python file.

        Parameters:
        - qrc_file (str): Path to the input qrc file.
        - py_file (str): Path to the output py file.
        """
        try:
            if qtpy.API_NAME == "PyQt5":
                rcc_command = 'pyrcc5'
            elif qtpy.API_NAME == "PyQt6":
                rcc_command = 'pyrcc6'
            elif qtpy.API_NAME == "PySide2":
                rcc_command = 'pyside2-rcc'
            elif qtpy.API_NAME == "PySide6":
                rcc_command = 'pyside6-rcc'
            else:
                raise Exception("Error: Unknown QT binding/API Name", qtpy.API_NAME)

            print(f'{rcc_command} "{qrcFile}" -o "{pyFile}"')
            subprocess.run(f'{rcc_command} "{qrcFile}" -o "{pyFile}"')
            
        except Exception as e:
            print("Error converting qrc to py:", e)

    def uiToPy(uiFile, pyFile):
        """
        Convert a Qt UI file to a Python file.

        Parameters:
        - uiFile (str): Path to the input UI file.
        - pyFile (str): Path to the output Python file.
        """
        try:
            if qtpy.API_NAME == "PyQt5":
                pyuic_command = 'pyuic5'
            elif qtpy.API_NAME == "PyQt6":
                pyuic_command = 'pyuic6'
            elif qtpy.API_NAME == "PySide2":
                pyuic_command = 'pyside2-uic'
            elif qtpy.API_NAME == "PySide6":
                pyuic_command = 'pyside6-uic'
            else:
                raise Exception("Error: Unknown Qt binding/API Name", qtpy.API_NAME)

            os.system(f'{pyuic_command} "{uiFile}" -o "{pyFile}"')

        except Exception as e:
            print("Error converting ui to py:", e)

    def renameFolder(old_name, new_name):
        try:
            # Check if the destination directory exists
            if os.path.exists(new_name):
                # Remove the destination directory if it exists
                shutil.rmtree(new_name)

            # Rename the folder
            os.rename(old_name, new_name)
        except Exception as e:
            pass





