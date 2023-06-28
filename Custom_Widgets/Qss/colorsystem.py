########################################################################
## 
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys

########################################################################
# IMPORT PYSIDE
########################################################################
# if 'PySide2' in sys.modules:
#     from PySide2.QtCore import *
# elif 'PySide6' in sys.modules:
#     from PySide6.QtCore import *

########################################################################
## MODULE UPDATED TO USE QTPY
########################################################################
from qtpy.QtCore import *
########################################################################

import matplotlib.colors as mc
import colorsys
########################################################################
settings = QSettings()

def adjust_lightness(color, amount=0.5):
    try:
        c = mc.cnames[color]
    except KeyError:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    # print(c)

    if c[1] > 0:
        # adjusted_lightness = c[1] * amount
        adjusted_lightness = c[1] * amount * amount 
    else:
        adjusted_lightness = 1 - (amount * amount)
        # adjusted_lightness = 1 - c[1] * amount * amount

    adjusted_hue = c[0]
    # adjusted_lightness = c[1] * amount * amount 
    adjusted_saturation = c[2] 

    rgb = colorsys.hls_to_rgb(adjusted_hue, adjusted_lightness, adjusted_saturation)
    new_color = rgb_to_hex((int(rgb[0] * 250), int(rgb[1] * 250), int(rgb[2] * 250)))

    return new_color


def rgb_to_hex(rgb):
    hex_color = '%02x%02x%02x' % rgb
    return "#" + hex_color

class Theme:
    def __init__(self, bg_color, txt_color, accent_color, icons_color=""):
        self.bg_color = bg_color
        self.txt_color = txt_color
        self.accent_color = accent_color
        self.icons_color = icons_color

        self.BG_1 = adjust_lightness(bg_color, 1)
        self.BG_2 = adjust_lightness(bg_color, 0.95)
        self.BG_3 = adjust_lightness(bg_color, 0.8)
        self.BG_4 = adjust_lightness(bg_color, 0.75)
        self.BG_5 = adjust_lightness(bg_color, 0.6)
        self.BG_6 = adjust_lightness(bg_color, 0.55)

        self.CT_1 = adjust_lightness(txt_color, 1)
        self.CT_2 = adjust_lightness(txt_color, 0.9)
        self.CT_3 = adjust_lightness(txt_color, 0.8)
        self.CT_4 = adjust_lightness(txt_color, 0.7)

        self.CA_1 = adjust_lightness(accent_color, 1)
        self.CA_2 = adjust_lightness(accent_color, 0.9)
        self.CA_3 = adjust_lightness(accent_color, 0.8)
        self.CA_4 = adjust_lightness(accent_color, 0.7)

        self.ICONS = ":/icons/Icons/"

class Dark(Theme):
    def __init__(self):
        super().__init__("#0D0D14", "#fff", "#A8B9BD")

class Light(Theme):
    def __init__(self):
        super().__init__("#fff", "#000", "#00bcff")


########################################################################
## 
########################################################################

########################################################################
## CREATE COLOR VARIABLES
########################################################################
class CreateColorVariable():
    def __init__(self, parent=None):
        super(CreateColorVariable, self).__init__(parent)

    def getCurrentThemeInfo(self):
        settings = QSettings()

        THEME = settings.value("THEME")
                
        currentThemeInfo = {}

        if THEME == "LIGHT":
            theme = Light()
            if theme.icons_color == "":
                iconsColor = theme.accent_color
                theme.icons_color = theme.accent_color
            else:
                iconsColor = theme.icons_color

            currentThemeInfo = {"background-color": theme.bg_color, "text-color": theme.txt_color, "accent-color": theme.accent_color, "icons-color": iconsColor}

        elif THEME == "DARK":
            theme = Dark()
            if theme.icons_color == "":
                iconsColor = theme.accent_color
                theme.icons_color = theme.accent_color
            else:
                iconsColor = theme.icons_color

            currentThemeInfo = {"background-color": theme.bg_color, "text-color": theme.txt_color, "accent-color": theme.accent_color, "icons-color": iconsColor}

        else:
            for theme in self.ui.themes:
                if theme.defaultTheme or theme.name == THEME:
                    # generate app theme
                    settings.setValue("THEME", theme.name);
                    bg_color = theme.backgroundColor
                    txt_color = theme.textColor
                    accent_color = theme.accentColor

                    if theme.createNewIcons:
                        if theme.iconsColor == "":
                            iconsColor = accent_color
                        else:
                            iconsColor = theme.iconsColor
                    else:
                        iconsColor = None

                    currentThemeInfo = {"background-color": bg_color, "text-color": txt_color, "accent-color": accent_color, "icons-color": iconsColor}

        if len(currentThemeInfo) == 0:
            theme = Light()
            if theme.icons_color == "":
                iconsColor = theme.accent_color
            else:
                iconsColor = theme.icons_color

            currentThemeInfo = {"background-color": theme.bg_color, "text-color": theme.txt_color, "accent-color": theme.accent_color, "icons-color": iconsColor}

        return currentThemeInfo
        
    def CreateVariables(self):
        settings = QSettings()
        
        THEME = settings.value("THEME")
        themeFound = False
        if THEME == "LIGHT":
            theme = Light()

        elif THEME == "DARK":
            theme = Dark()

        else:
            for themes in self.ui.themes:
                if themes.defaultTheme or themes.name == THEME:
                    # generate app theme
                    settings.setValue("THEME", themes.name)

                    theme = themes
                    theme.bg_color = themes.backgroundColor
                    theme.txt_color = themes.textColor
                    theme.accent_color = themes.accentColor
                    theme.icons_color = theme.iconsColor
                    themeFound = True

            if not themeFound:
                theme = Light()


            theme.BG_1 = adjust_lightness(theme.bg_color, 1)
            theme.BG_2 = adjust_lightness(theme.bg_color, 0.90)
            theme.BG_3 = adjust_lightness(theme.bg_color, 0.80)
            theme.BG_4 = adjust_lightness(theme.bg_color, 0.70)
            theme.BG_5 = adjust_lightness(theme.bg_color, 0.60)
            theme.BG_6 = adjust_lightness(theme.bg_color, 0.50)

            theme.CT_1 = adjust_lightness(theme.txt_color, 1)
            theme.CT_2 = adjust_lightness(theme.txt_color, 0.9)
            theme.CT_3 = adjust_lightness(theme.txt_color, 0.8)
            theme.CT_4 = adjust_lightness(theme.txt_color, 0.7)

            theme.CA_1 = adjust_lightness(theme.accent_color, 1)
            theme.CA_2 = adjust_lightness(theme.accent_color, .9)
            theme.CA_3 = adjust_lightness(theme.accent_color, .8)
            theme.CA_4 = adjust_lightness(theme.accent_color, .7)

            theme.ICONS = ":/icons/Icons/"

        # Create global color variables
        self.theme = Object()
        self.theme.COLOR_BACKGROUND_1 = theme.BG_1
        self.theme.COLOR_BACKGROUND_2 = theme.BG_2
        self.theme.COLOR_BACKGROUND_3 = theme.BG_3
        self.theme.COLOR_BACKGROUND_4 = theme.BG_4
        self.theme.COLOR_BACKGROUND_5 = theme.BG_5
        self.theme.COLOR_BACKGROUND_6 = theme.BG_6

        self.theme.COLOR_TEXT_1 = theme.CT_1
        self.theme.COLOR_TEXT_2 = theme.CT_2
        self.theme.COLOR_TEXT_3 = theme.CT_3
        self.theme.COLOR_TEXT_4 = theme.CT_4

        self.theme.COLOR_ACCENT_1 = theme.CA_1
        self.theme.COLOR_ACCENT_2 = theme.CA_2
        self.theme.COLOR_ACCENT_3 = theme.CA_3
        self.theme.COLOR_ACCENT_4 = theme.CA_4

        self.theme.PATH_RESOURCES = theme.ICONS

        # scss_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_variables.scss'))
        scss_folder = os.path.abspath(os.path.join(os.getcwd(), 'QSS'))
        if not os.path.exists(scss_folder):
            os.makedirs(scss_folder)

        scss_path = os.path.abspath(os.path.join(scss_folder, '_variables.scss'))
        f = open(scss_path, 'w')
        print(f"""
        //===================================================//
        // FILE AUTO-GENERATED, ANY CHANGES MADE WILL BE LOST //
        //====================================================//
        $COLOR_BACKGROUND_1: {theme.BG_1};
        $COLOR_BACKGROUND_2: {theme.BG_2};
        $COLOR_BACKGROUND_3: {theme.BG_3}; 
        $COLOR_BACKGROUND_4: {theme.BG_4}; 
        $COLOR_BACKGROUND_5: {theme.BG_5}; 
        $COLOR_BACKGROUND_6: {theme.BG_6}; 
        $COLOR_TEXT_1: {theme.CT_1};
        $COLOR_TEXT_2: {theme.CT_2};
        $COLOR_TEXT_3: {theme.CT_3};
        $COLOR_TEXT_4: {theme.CT_4};
        $COLOR_ACCENT_1: {theme.CA_1};
        $COLOR_ACCENT_2: {theme.CA_2};
        $COLOR_ACCENT_3: {theme.CA_3};
        $COLOR_ACCENT_4: {theme.CA_4};
        $OPACITY_TOOLTIP: 230;
        $SIZE_BORDER_RADIUS: 4px;
        $BORDER_1: 1px solid $COLOR_BACKGROUND_1;
        $BORDER_2: 1px solid $COLOR_BACKGROUND_4;
        $BORDER_3: 1px solid $COLOR_BACKGROUND_6;
        $BORDER_SELECTION_3: 1px solid $COLOR_ACCENT_3;
        $BORDER_SELECTION_2: 1px solid $COLOR_ACCENT_2;
        $BORDER_SELECTION_1: 1px solid $COLOR_ACCENT_1;
        $PATH_RESOURCES: '{theme.ICONS}';
        //===================================================//
        // END //
        //====================================================//
        """, file=f)

        f.close()

########################################################################
##
########################################################################
class Object(object):
    pass
