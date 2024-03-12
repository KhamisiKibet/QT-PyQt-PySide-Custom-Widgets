########################################################################
## IMPORTS
########################################################################
import os
import sys

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

def color_to_hex(color):
    """
    Convert a color to its hex representation.

    Parameters:
    - color (str or tuple): Color representation, such as color name (e.g., 'red'),
      hex code (e.g., '#FF0000'), or RGB tuple (e.g., (255, 0, 0)).

    Returns:
    - str: Hex color code.
    """
    if isinstance(color, str):
        # If the input is a color name, convert it to hex
        if color in mc.CSS4_COLORS:
            return mc.CSS4_COLORS[color]
        else:
            # Try to convert named color to hex
            try:
                rgba = mc.to_rgba(color)
                return mc.to_hex(rgba)
            except ValueError:
                raise ValueError(f"Invalid color name: {color}")

    elif isinstance(color, tuple) and len(color) == 3:
        # If the input is an RGB tuple, convert it to hex
        rgba = color + (1.0,)  # Add alpha channel
        return mc.to_hex(rgba)

    else:
        raise ValueError("Invalid color representation")

def lighten_color(hex_color, factor=0.35):
    """
    Lightens a given hex color.

    Parameters:
    - hex_color (str): The hex color code (e.g., "#RRGGBB").
    - factor (float): Lightening factor, where 0 means no change and 1 means white.

    Returns:
    - str: The lightened hex color code.
    """
    hex_color = color_to_hex(hex_color)
    # Convert hex to RGB
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Calculate the lightened color
    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)

    # Convert back to hex
    lightened_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    
    return lightened_color


def darken_color(hex_color, factor=0.35):
    """
    Darkens a given hex color.

    Parameters:
    - hex_color (str): The hex color code (e.g., "#RRGGBB").
    - factor (float): Darkening factor, where 0 means no change and 1 means black.

    Returns:
    - str: The darkened hex color code.
    """
    hex_color = color_to_hex(hex_color)
    # Convert hex to RGB
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    # Calculate the darkened color
    r = int(r * (1 - factor))
    g = int(g * (1 - factor))
    b = int(b * (1 - factor))

    # Convert back to hex
    darkened_color = "#{:02X}{:02X}{:02X}".format(r, g, b)

    return darkened_color

def is_color_dark_or_light(color):
    # Convert color to RGB
    rgb = mc.to_rgba(color)[:3]

    # Calculate relative luminance
    luminance = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]

    # Adjust threshold based on your preference
    threshold = 0.5

    # Check if the color is relatively dark or light
    return "dark" if luminance < threshold else "light"


class Theme:
    def __init__(self, bg_color, txt_color, accent_color, icons_color=""):
        self.bg_color = bg_color
        self.txt_color = txt_color
        self.accent_color = accent_color
        self.icons_color = icons_color

class Dark(Theme):
    def __init__(self):
        super().__init__("#0d1117", "#fff", "#238636", "#fff")

class Light(Theme):
    def __init__(self):
        super().__init__("#fff", "#000", "#00bcff", "#000")


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
                    settings.setValue("THEME", theme.name)
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
        theme = Light()
        
        if THEME == "LIGHT":
            theme = Light()

        elif THEME == "DARK":
            theme = Dark()

        else:
            if not hasattr(self.ui, 'themes'):
                theme = Light()
                
            else:
                for uitheme in self.ui.themes:
                    if uitheme.defaultTheme or uitheme.name == THEME:
                        # generate app theme
                        settings.setValue("THEME", uitheme.name)

                        theme.bg_color = uitheme.backgroundColor
                        theme.txt_color = uitheme.textColor
                        theme.accent_color = uitheme.accentColor
                        theme.icons_color = uitheme.iconsColor

        if is_color_dark_or_light(theme.bg_color) == "light":
            theme.BG_1 = theme.bg_color
            theme.BG_2 = darken_color(theme.bg_color, 0.05)
            theme.BG_3 = darken_color(theme.bg_color, 0.1)
            theme.BG_4 = darken_color(theme.bg_color, 0.15)
            theme.BG_5 = darken_color(theme.bg_color, 0.2)
            theme.BG_6 = darken_color(theme.bg_color, 0.25)

        else:
            theme.BG_1 = theme.bg_color
            theme.BG_2 = adjust_lightness(theme.bg_color, 0.90)
            theme.BG_3 = adjust_lightness(theme.bg_color, 0.80)
            theme.BG_4 = adjust_lightness(theme.bg_color, 0.70)
            theme.BG_5 = adjust_lightness(theme.bg_color, 0.60)
            theme.BG_6 = adjust_lightness(theme.bg_color, 0.50)
            # theme.BG_2 = lighten_color(theme.bg_color, 0.05)
            # theme.BG_3 = lighten_color(theme.bg_color, 0.1)
            # theme.BG_4 = lighten_color(theme.bg_color, 0.15)
            # theme.BG_5 = lighten_color(theme.bg_color, 0.2)
            # theme.BG_6 = lighten_color(theme.bg_color, 0.25)

        if is_color_dark_or_light(theme.txt_color) == "light":
            theme.CT_1 = theme.txt_color
            theme.CT_2 = darken_color(theme.txt_color, 0.2)
            theme.CT_3 = darken_color(theme.txt_color, 0.4)
            theme.CT_4 = darken_color(theme.txt_color, 0.6)
        else:
            theme.CT_1 = theme.txt_color
            theme.CT_2 = lighten_color(theme.txt_color, 0.2)
            theme.CT_3 = lighten_color(theme.txt_color, 0.4)
            theme.CT_4 = lighten_color(theme.txt_color, 0.6)

        if is_color_dark_or_light(theme.txt_color) == "light":
            theme.CA_1 = theme.accent_color
            theme.CA_2 = darken_color(theme.accent_color, .2)
            theme.CA_3 = darken_color(theme.accent_color, .4)
            theme.CA_4 = darken_color(theme.accent_color, .6)
        else:
            theme.CA_1 = theme.accent_color
            theme.CA_2 = lighten_color(theme.accent_color, .2)
            theme.CA_3 = lighten_color(theme.accent_color, .4)
            theme.CA_4 = lighten_color(theme.accent_color, .6)

        if theme.icons_color is not None and theme.icons_color != "":
            folder = theme.icons_color.replace("#", "")
        else:
            folder = theme.accent_color.replace("#", "")
        
        # Add icons folder to search path
        QDir.addSearchPath('theme-icons', os.path.join(os.getcwd(), 'Qss/icons/'))
        theme.ICONS = "theme-icons:"+folder+"/"
            

        # Update global color variables
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
        scss_folder = os.path.abspath(os.path.join(os.getcwd(), 'Qss/scss'))
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

