import cairosvg
import codecs
import os
import sys
import shutil
from urllib.parse import urlparse
from pathlib import Path
import __main__


from . colorsystem import *

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
        svg_color = "#fff"
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
                os.system('pyrcc5 "'+resource_path+'" -o "'+py_resource_path+'"')
                settings.setValue("ICONS-COLOR", normal_color)
            except Exception as e:
                # raise e
                print("error while converting resource file")  
        else:
            ## GENERATE OTHER ICONS
            NewIconsGenerator.generateAllIcons(self, progress_callback) 

    def generateAllIcons(self, progress_callback):
        settings = QSettings()
        # Files folder
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'icons/original_svg')
        list_of_files = []

        svg_color = "#fff"        

        for theme in self.ui.themes:
            THEME = settings.value("THEME")
            # if theme.defaultTheme or theme.name == THEME:
                # continue

            if self.showCustomWidgetsLogs:
                print("Checking icons for "+theme.name)
                

            if hasattr(theme, "iconsColor"):
                if theme.iconsColor != "":
                   normal_color = str(theme.iconsColor)
                else:
                    normal_color = str(theme.accentColor)

            elif THEME == "LIGHT":
                themeProperty = Light()
                if themeProperty.icons_color == "":
                    normal_color = str(themeProperty.accent_color)
                else:
                    normal_color = str(themeProperty.icons_color)
                
            elif THEME == "DARK":
                themeProperty = Dark()
                if themeProperty.icons_color == "":
                    normal_color = str(themeProperty.accent_color)
                else:
                    normal_color = str(themeProperty.icons_color)

            else:
                if self.showCustomWidgetsLogs:
                    print("No icons color specified for theme", theme.name)
                continue
            
            focused_color = adjust_lightness(normal_color, 1.5)
            disabled_color = adjust_lightness(normal_color, .5) 

            iconsFolderName = normal_color.replace("#", "")

            iconsFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/'+iconsFolderName))

            if self.showCustomWidgetsLogs:
                print("Generating missing icons for your theme",  normal_color, "please wait. This may take long")

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

                    if os.path.exists(filename):
                        continue
                    else:
                        if settings.value("ICONS-COLOR") is not None and settings.value("ICONS-COLOR").replace("#", "") == iconsFolderName:
                            continue
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

                    if os.path.exists(filename):
                        continue
                    else:
                        if settings.value("ICONS-COLOR") is not None and settings.value("ICONS-COLOR").replace("#", "") == iconsFolderName:
                            # RENAME FOLDER
                            oldIconsFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/Icons'))

                            if os.path.exists(os.path.join(oldIconsFolder, name_2)):
                                shutil.move(os.path.join(oldIconsFolder, name_2), iconsFolder)
                                continue

                    filename = os.path.abspath(os.path.join(iconsFolder, name_2))
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

                    if os.path.exists(filename):
                        continue
                    else:
                        if settings.value("ICONS-COLOR") is not None and settings.value("ICONS-COLOR").replace("#", "") == iconsFolderName:
                            # RENAME FOLDER
                            oldIconsFolder = os.path.abspath(os.path.join(os.getcwd(), 'QSS/Icons'))

                            if os.path.exists(os.path.join(oldIconsFolder, name_2)):
                                shutil.move(os.path.join(oldIconsFolder, name_2), iconsFolder)
                                continue

                    filename = os.path.abspath(os.path.join(iconsFolder, name_2))
                    try:
                        cairosvg.svg2png(bytestring=newBytes, write_to=filename)
                    except Exception as e:
                        print(e)
                        

                # EMMIT PROGRESS VALUE
                progress_callback.emit(int((list_of_files.index(name)/totalIcons) * 100))


