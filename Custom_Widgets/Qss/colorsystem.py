import os
import sys
from qtpy.QtCore import *
import matplotlib.colors as mc
import colorsys

settings = QSettings()

def adjust_lightness(color, amount=0.5):
    try:
        c = mc.cnames[color]
    except KeyError:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))

    if c[1] > 0:
        adjusted_lightness = c[1] * amount * amount 
    else:
        adjusted_lightness = 1 - (amount * amount)

    adjusted_hue = c[0]
    adjusted_saturation = c[2] 

    rgb = colorsys.hls_to_rgb(adjusted_hue, adjusted_lightness, adjusted_saturation)
    new_color = rgb_to_hex((int(rgb[0] * 250), int(rgb[1] * 250), int(rgb[2] * 250)))

    return new_color


def rgb_to_hex(rgb):
    hex_color = '%02x%02x%02x' % rgb
    return "#" + hex_color

def hex_to_rgb(hex_color):
    hex_color = color_to_hex(hex_color)
    # Remove '#' if present
    hex_color = hex_color.lstrip('#')
    
    # Convert hexadecimal to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    return r, g, b


def color_to_hex(color):
    if isinstance(color, str):
        if color in mc.CSS4_COLORS:
            return mc.CSS4_COLORS[color]
        else:
            try:
                rgba = mc.to_rgba(color)
                return mc.to_hex(rgba)
            except ValueError:
                raise ValueError(f"Invalid color name: {color}")

    elif isinstance(color, tuple) and len(color) == 3:
        rgba = color + (1.0,)
        return mc.to_hex(rgba)

    else:
        raise ValueError("Invalid color representation")

def lighten_color(hex_color, factor=0.35):
    hex_color = color_to_hex(hex_color)
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    r = int(r + (255 - r) * factor)
    g = int(g + (255 - g) * factor)
    b = int(b + (255 - b) * factor)

    lightened_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    
    return lightened_color


def darken_color(hex_color, factor=0.35):
    hex_color = color_to_hex(hex_color)
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)

    r = int(r * (1 - factor))
    g = int(g * (1 - factor))
    b = int(b * (1 - factor))

    darkened_color = "#{:02X}{:02X}{:02X}".format(r, g, b)

    return darkened_color

def is_color_dark_or_light(color):
    rgb = mc.to_rgba(color)[:3]
    luminance = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
    threshold = 0.5
    return "dark" if luminance < threshold else "light"

class Theme:
    def __init__(self, bg_color, txt_color, accent_color, icons_color=""):
        self.bg_color = bg_color
        self.txt_color = txt_color
        self.accent_color = accent_color
        self.icons_color = icons_color

class Dark(Theme):
    def __init__(self):
        super().__init__("#0d1117", "white", "#238636", "white")

class Light(Theme):
    def __init__(self):
        super().__init__("white", "black", "#00bcff", "black")

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

            currentThemeInfo = {"background-color": convert_to_six_digit_hex(theme.bg_color), "text-color": convert_to_six_digit_hex(theme.txt_color), "accent-color": convert_to_six_digit_hex(theme.accent_color), "icons-color": convert_to_six_digit_hex(iconsColor)}

        else:
            for theme in self.ui.themes:
                if theme.defaultTheme or theme.name == THEME:
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
        
        QDir.addSearchPath('theme-icons', os.path.join(os.getcwd(), 'Qss/icons/'))
        theme.ICONS = "theme-icons:"+folder+"/"

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

        bg_rgb_1 = hex_to_rgb(theme.BG_1)
        bg_rgb_2 = hex_to_rgb(theme.BG_2)
        bg_rgb_3 = hex_to_rgb(theme.BG_3)
        bg_rgb_4 = hex_to_rgb(theme.BG_4)
        bg_rgb_5 = hex_to_rgb(theme.BG_5)
        bg_rgb_6 = hex_to_rgb(theme.BG_6)

        txt_rgb_1 = hex_to_rgb(theme.CT_1)
        txt_rgb_2 = hex_to_rgb(theme.CT_2)
        txt_rgb_3 = hex_to_rgb(theme.CT_3)
        txt_rgb_4 = hex_to_rgb(theme.CT_4)

        accent_rgb_1 = hex_to_rgb(theme.CA_1)
        accent_rgb_2 = hex_to_rgb(theme.CA_2)
        accent_rgb_3 = hex_to_rgb(theme.CA_3)
        accent_rgb_4 = hex_to_rgb(theme.CA_4)

        theme.CB1_R, theme.CB1_G, theme.CB1_B = bg_rgb_1[0], bg_rgb_1[1], bg_rgb_1[2]
        theme.CB2_R, theme.CB2_G, theme.CB2_B = bg_rgb_2[0], bg_rgb_2[1], bg_rgb_2[2]
        theme.CB3_R, theme.CB3_G, theme.CB3_B = bg_rgb_3[0], bg_rgb_3[1], bg_rgb_3[2]
        theme.CB4_R, theme.CB4_G, theme.CB4_B = bg_rgb_4[0], bg_rgb_4[1], bg_rgb_4[2]
        theme.CB5_R, theme.CB5_G, theme.CB5_B = bg_rgb_5[0], bg_rgb_5[1], bg_rgb_5[2]
        theme.CB6_R, theme.CB6_G, theme.CB6_B = bg_rgb_6[0], bg_rgb_6[1], bg_rgb_6[2]

        theme.CT1_R, theme.CT1_G, theme.CT1_B = txt_rgb_1[0], txt_rgb_1[1], txt_rgb_1[2]
        theme.CT2_R, theme.CT2_G, theme.CT2_B = txt_rgb_2[0], txt_rgb_2[1], txt_rgb_2[2]
        theme.CT3_R, theme.CT3_G, theme.CT3_B = txt_rgb_3[0], txt_rgb_3[1], txt_rgb_3[2]
        theme.CT4_R, theme.CT4_G, theme.CT4_B = txt_rgb_4[0], txt_rgb_4[1], txt_rgb_4[2]

        theme.CA1_R, theme.CA1_G, theme.CA1_B = accent_rgb_1[0], accent_rgb_1[1], accent_rgb_1[2]
        theme.CA2_R, theme.CA2_G, theme.CA2_B = accent_rgb_2[0], accent_rgb_2[1], accent_rgb_2[2]
        theme.CA3_R, theme.CA3_G, theme.CA3_B = accent_rgb_3[0], accent_rgb_3[1], accent_rgb_3[2]
        theme.CA4_R, theme.CA4_G, theme.CA4_B = accent_rgb_4[0], accent_rgb_4[1], accent_rgb_4[2]


        self.theme.PATH_RESOURCES = theme.ICONS

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
        $CB1_R: {theme.CB1_R};
        $CB1_G: {theme.CB1_G};
        $CB1_B: {theme.CB1_B};
        $CB2_R: {theme.CB2_R};
        $CB2_G: {theme.CB2_G};
        $CB2_B: {theme.CB2_B};
        $CB3_R: {theme.CB3_R};
        $CB3_G: {theme.CB3_G};
        $CB3_B: {theme.CB3_B};
        $CB4_R: {theme.CB4_R};
        $CB4_G: {theme.CB4_G};
        $CB4_B: {theme.CB4_B};
        $CB5_R: {theme.CB5_R};
        $CB5_G: {theme.CB5_G};
        $CB5_B: {theme.CB5_B};
        $CB6_R: {theme.CB6_R};
        $CB6_G: {theme.CB6_G};
        $CB6_B: {theme.CB6_B};
        $COLOR_TEXT_1: {theme.CT_1};
        $COLOR_TEXT_2: {theme.CT_2};
        $COLOR_TEXT_3: {theme.CT_3};
        $COLOR_TEXT_4: {theme.CT_4};
        $CT1_R: {theme.CT1_R};
        $CT1_G: {theme.CT1_G};
        $CT1_B: {theme.CT1_B};
        $CT2_R: {theme.CT2_R};
        $CT2_G: {theme.CT2_G};
        $CT2_B: {theme.CT2_B};
        $CT3_R: {theme.CT3_R};
        $CT3_G: {theme.CT3_G};
        $CT3_B: {theme.CT3_B};
        $CT4_R: {theme.CT4_R};
        $CT4_G: {theme.CT4_G};
        $CT4_B: {theme.CT4_B};
        $COLOR_ACCENT_1: {theme.CA_1};
        $COLOR_ACCENT_2: {theme.CA_2};
        $COLOR_ACCENT_3: {theme.CA_3};
        $COLOR_ACCENT_4: {theme.CA_4};
        $CA1_R: {theme.CA1_R};
        $CA1_G: {theme.CA1_G};
        $CA1_B: {theme.CA1_B};
        $CA2_R: {theme.CA2_R};
        $CA2_G: {theme.CA2_G};
        $CA2_B: {theme.CA2_B};
        $CA3_R: {theme.CA3_R};
        $CA3_G: {theme.CA3_G};
        $CA3_B: {theme.CA3_B};
        $CA4_R: {theme.CA4_R};
        $CA4_G: {theme.CA4_G};
        $CA4_B: {theme.CA4_B};
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

def convert_to_six_digit_hex(color):
    if color.startswith("#"):
        if len(color) == 4:
            color = "#" + color[1]*2 + color[2]*2 + color[3]*2
        elif len(color) == 7:
            pass
        else:
            raise ValueError("Invalid hex color format")
    else:
        try:
            rgb = mc.to_rgb(color)
            color = "#{:02X}{:02X}{:02X}".format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
        except ValueError:
            raise ValueError("Invalid color name")

    return color
