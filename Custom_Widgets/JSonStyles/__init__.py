# JSON FOR READING THE JSON STYLESHEET
import json
import os
import re

from qtpy.QtCore import *
from qtpy import QtWidgets, QtGui, QtCore
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from Custom_Widgets.FileMonitor import QSsFileMonitor
from Custom_Widgets.QCustomQPushButtonGroup import QCustomQPushButtonGroup
from Custom_Widgets.QCustomQPushButton import applyAnimationThemeStyle, applyButtonShadow, iconify, applyCustomAnimationThemeStyle, applyStylesFromColor
from Custom_Widgets.QPropertyAnimation import returnAnimationEasingCurve, returnQtDirection

from Custom_Widgets.Qss.colorsystem import CreateColorVariable
from Custom_Widgets.Log import *


## Read JSON stylesheet
def loadJsonStyle(self, ui, update = False, **jsonFiles):
    # START THREAD
    self.customWidgetsThreadpool = QThreadPool()
    # Show Logs
    self.showCustomWidgetsLogs = True
    self.checkForMissingicons = True
    self.ui = ui
    self.jsonStyleSheets = []  # List to store loaded JSON style sheets
    self.jsonStyleData = {}

    if not jsonFiles:
        json_file_paths = ["style.json", "json/style.json", "jsonstyles/style.json"]
        for file_path in json_file_paths:
            if os.path.isfile(file_path):
                with open(file_path) as file:
                    data = json.load(file)
                    self.jsonStyleData.update(data)  # Update existing data with new data
                    self.jsonStyleSheets.append(file_path)

    else:
        for file in jsonFiles.get('jsonFiles', []):
            # Construct the absolute path to the file
            jsonFile = os.path.abspath(os.path.join(os.getcwd(), file))
            if os.path.isfile(jsonFile):
                with open(jsonFile) as jsonFile:
                    data = json.load(jsonFile)
                    # APPLY JSON STYLESHEET
                    # self = QMainWindow class
                    # self.ui = Ui_MainWindow / user interface class
                    self.jsonStyleData.update(data)  # Update existing data with new data
                    self.jsonStyleSheets.append(file)
            else:
                logError(self, "Error loading your JSON files: '{}' does not exist".format(file))

    applyJsonStyle(self, update = update)


## Apply JSon stylesheet
def applyJsonStyle(self, update = False):
    data = self.jsonStyleData
    ## Show logs
    if "ShowLogs" in data:
        if data["ShowLogs"]:
            # Show Logs
            self.showCustomWidgetsLogs = True
        else:
            # Hide Logs
            self.showCustomWidgetsLogs = False

    ## Live QSS compiler
    if "LiveCompileQss" in data:
        if data["LiveCompileQss"]:
            if not hasattr(self, 'qss_watcher') and not hasattr(self, 'liveCompileQss'):
                self.liveCompileQss = True
                QSsFileMonitor.start_qss_file_listener(self)
            
        else:
            self.liveCompileQss = False
            # QSsFileMonitor.stop_qss_file_listener(self)

    # Generate missing icons including qt designer icons
    if "CheckForMissingicons" in data:
        if data["CheckForMissingicons"]:
            self.checkForMissingicons = data["CheckForMissingicons"]
        else:
            self.checkForMissingicons = False


    ## QSETTINGS
    if "QSettings" in data:
        for settings in data['QSettings']:
            if "AppSettings" in settings:
                appSettings = settings['AppSettings']
                if "OrginizationName" in appSettings and len(str(appSettings["OrginizationName"])) > 0:
                    self.orginazationName = str(appSettings["OrginizationName"])
                else:
                    self.orginazationName = ""

                if "ApplicationName" in settings['AppSettings'] and len(str(appSettings["ApplicationName"])) > 0:
                    self.applicationName = str(appSettings["ApplicationName"])

                else:
                    self.applicationName = ""


                if "OrginizationDormain" in settings['AppSettings'] and len(str(appSettings["OrginizationDormain"])) > 0:
                    self.orginazationDomain = str(appSettings["OrginizationDormain"]).replace(" ", "")
                else:
                    self.orginazationDomain = ""

            if "ThemeSettings" in settings:
                for themeSettings in settings['ThemeSettings']:
                    if "CustomTheme" in themeSettings:
                        # Create themes
                        if not hasattr(self.ui, "themes"):
                            setattr(self.ui, "themes", [])
                        themes = getattr(self.ui, "themes")

                        for customTheme in themeSettings['CustomTheme']:
                            if "Theme-name" in customTheme and len(str(customTheme['Theme-name'])) > 0:
                                theme_name = str(customTheme['Theme-name'])

                                if not hasattr(self.ui, theme_name):
                                    setattr(self.ui, theme_name, Object())
                                
                                theme = getattr(self.ui, theme_name)
                                theme.name = theme_name

                                if "Background-color" in customTheme and len(str(customTheme['Background-color'])) > 0:
                                    setattr(theme, "backgroundColor", str(customTheme['Background-color']))
                                else:
                                    theme.backgroundColor = ""

                                if "Text-color" in customTheme and len(str(customTheme['Text-color'])) > 0:
                                    theme.textColor = str(customTheme['Text-color'])

                                else:
                                    theme.textColor = ""

                                if "Accent-color" in customTheme and len(str(customTheme['Accent-color'])) > 0:
                                    theme.accentColor = str(customTheme['Accent-color'])

                                else:
                                    theme.accentColor = ""

                                if "Icons-color" in customTheme and len(str(customTheme['Icons-color'])) > 0:
                                    theme.iconsColor = str(customTheme['Icons-color'])

                                else:
                                    theme.iconsColor = ""

                                if "Default-Theme" in customTheme and bool(customTheme['Default-Theme']) == True:
                                    # THEME = settings.value("THEME")
                                    setngs = QSettings()
                                    if setngs.contains("THEME") and setngs.contains("THEME") is not None:
                                        theme.defaultTheme = False
                                    else:
                                        theme.defaultTheme = True

                                else:
                                    theme.defaultTheme = False

                                if "Create-icons" in customTheme and bool(customTheme['Create-icons']) == False:
                                    theme.createNewIcons = False
                                else:
                                    theme.createNewIcons = True

                                themes.append(theme)

        if not hasattr(self.ui, "DARK"):
            setattr(self.ui, "DARK", Object())
            darkTheme = getattr(self.ui, "DARK")
            darkTheme.name = "DARK"
            darkTheme.defaultTheme = False
            darkTheme.createNewIcons = True
            themes.append(darkTheme)
        if not hasattr(self.ui, "LIGHT"):
            setattr(self.ui, "LIGHT", Object())
            lightTheme = getattr(self.ui, "LIGHT")
            lightTheme.name = "LIGHT"
            lightTheme.defaultTheme = False
            lightTheme.createNewIcons = True
            themes.append(lightTheme)

        # QAppSettings.updateAppSettings(self)
            
    if update:
        CreateColorVariable.CreateVariables(self)

    ## QCARDS
    if "QCard" in data:
        for QCard in data['QCard']:
            if "cards" in QCard:
                for card in QCard['cards']:

                    if "shadow" in QCard:
                        if hasattr(self.ui, str(card)):
                            cardWidget = getattr(self.ui, str(card))
                            effect = QtWidgets.QGraphicsDropShadowEffect(cardWidget)
                            for shadow in QCard['shadow']:
                                if "color" in shadow and len(str(shadow["color"])) > 0:
                                    effect.setColor(QColor(self.getThemeVariableValue(str(shadow["color"]))))
                                else:
                                    effect.setColor(QColor(0,0,0,0))
                                if "blurRadius" in shadow and int(shadow["blurRadius"]) > 0:
                                    effect.setBlurRadius(int(shadow["blurRadius"]))
                                else:
                                    effect.setBlurRadius(0)
                                if "xOffset" in shadow and int(shadow["xOffset"]) > 0:
                                    effect.setXOffset(int(shadow["xOffset"]))
                                else:
                                    effect.setXOffset(0)
                                if "yOffset" in shadow and int(shadow["yOffset"]) > 0:
                                    effect.setYOffset(int(shadow["yOffset"]))
                                else:
                                    effect.setYOffset(0)

                            cardWidget.setGraphicsEffect(effect)

    ## BUTTON GROUPS
    # Add Class To PushButtons
    QPushButton.getButtonGroup = QCustomQPushButtonGroup.getButtonGroup
    QPushButton.getButtonGroupActiveStyle = QCustomQPushButtonGroup.getButtonGroupActiveStyle
    QPushButton.getButtonGroupNotActiveStyle = QCustomQPushButtonGroup.getButtonGroupNotActiveStyle
    QPushButton.getButtonGroupButtons = QCustomQPushButtonGroup.getButtonGroupButtons
    QPushButton.getButtonGroupActiveStyle = QCustomQPushButtonGroup.getButtonGroupActiveStyle
    QPushButton.setButtonGroupActiveStyle = QCustomQPushButtonGroup.setButtonGroupActiveStyle

    if "QPushButtonGroup" in data:
        grp_count = 0
        for QPushButtonGroup in data['QPushButtonGroup']:
            if "Buttons" in QPushButtonGroup:
                grp_count += 1
                for button in QPushButtonGroup["Buttons"]:
                    if hasattr(self.ui, str(button)):
                        btn = getattr(self.ui, str(button))
                        btn.groupParent = self
                        if not hasattr(btn, "active"):
                            if "ActiveButton" in QPushButtonGroup and QPushButtonGroup["ActiveButton"] == button:
                                btn.active = True
                            else:
                                btn.active = False

                        if not btn.metaObject().className() == "QPushButton" and not btn.metaObject().className() == "QPushButtonThemed":
                            raise Exception("Error: "+str(button)+" is not a QPushButton object.")
                        setattr(btn, "group", grp_count)

                        if not hasattr(self, "group_btns_"+str(grp_count)):
                            setattr(self, "group_btns_"+str(grp_count), [])

                        getattr(self, "group_btns_"+str(grp_count)).append(btn)

                        if not update:
                            btn.clicked.connect(self.checkButtonGroup)
                    else:
                        raise Exception("Error: Button named "+str(button)+" was not found.")
                        


            activeStyle = ""
            notActiveStyle = ""
            if "Style" in QPushButtonGroup:
                for style in QPushButtonGroup["Style"]:
                    if "Active" in style:
                        activeStyle = self.styleVariablesFromTheme(style['Active'])
                    if "NotActive" in style:
                        notActiveStyle = self.styleVariablesFromTheme(style['NotActive'])

                # getattr(self, "group_btns_"+str(grp_count))[0].active = True
                setattr(self, "group_active_"+str(grp_count), activeStyle)
                setattr(self, "group_not_active_"+str(grp_count), notActiveStyle)

                if update:
                    self.checkButtonGroup(button = btn)



    ## ANALOG GAUGE WIDGET
    if "AnalogGaugeWidget" in data:
        for AnalogGaugeWidget in data['AnalogGaugeWidget']:
            if "name" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["name"])) > 0:
                if hasattr(self.ui, str(AnalogGaugeWidget["name"])):
                    gaugeWidget = getattr(self.ui, str(AnalogGaugeWidget["name"]))

                    if not gaugeWidget.metaObject().className() == "AnalogGaugeWidget":
                        raise Exception("Error: "+str(AnalogGaugeWidget["name"])+" is not a AnalogGaugeWidget object")

                    if "units" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["units"])) > 0:
                        # Set gauge units
                        gaugeWidget.units = str(AnalogGaugeWidget["units"])

                    if "minValue" in AnalogGaugeWidget:
                        # Set gauge min value
                        gaugeWidget.minValue = int(AnalogGaugeWidget["minValue"])


                    if "maxValue" in AnalogGaugeWidget:
                        # Set gauge max value
                        gaugeWidget.maxValue = int(AnalogGaugeWidget["maxValue"])

                    if "scalaCount" in AnalogGaugeWidget:
                        # Set scala count
                        gaugeWidget.scalaCount = int(AnalogGaugeWidget["scalaCount"])

                    if "startValue" in AnalogGaugeWidget:
                        # Set start value
                        gaugeWidget.updateValue(int(AnalogGaugeWidget["startValue"]))

                    if "gaugeTheme" in AnalogGaugeWidget:
                        # Set gauge theme
                        gaugeWidget.setGaugeTheme(int(AnalogGaugeWidget["gaugeTheme"]))

                    if "offsetAngle" in AnalogGaugeWidget:
                        # Set offset angle
                        gaugeWidget.updateAngleOffset(int(AnalogGaugeWidget["offsetAngle"]))

                    if "innerRadius" in AnalogGaugeWidget:
                        # Set inner radius
                        gaugeWidget.setGaugeColorInnerRadiusFactor(int(AnalogGaugeWidget["innerRadius"]))

                    if "outerRadius" in AnalogGaugeWidget:
                        # Set outer radius
                        gaugeWidget.setGaugeColorOuterRadiusFactor(int(AnalogGaugeWidget["outerRadius"]))

                    if "scaleStartAngle" in AnalogGaugeWidget:
                        # Set start angle
                        gaugeWidget.setScaleStartAngle(int(AnalogGaugeWidget["scaleStartAngle"]))


                    if "totalScaleAngle" in AnalogGaugeWidget:
                        # Set total scale angle
                        gaugeWidget.setTotalScaleAngleSize(int(AnalogGaugeWidget["totalScaleAngle"]))

                    if "enableBarGraph" in AnalogGaugeWidget:
                        # Set enable bar graph
                        gaugeWidget.setEnableBarGraph(bool(AnalogGaugeWidget["enableBarGraph"]))

                    if "enableValueText" in AnalogGaugeWidget:
                        # Set enable text value
                        gaugeWidget.setEnableValueText(bool(AnalogGaugeWidget["enableValueText"]))

                    if "enableNeedlePolygon" in AnalogGaugeWidget:
                        # Set enable needle polygon
                        gaugeWidget.setEnableNeedlePolygon(bool(AnalogGaugeWidget["enableNeedlePolygon"]))

                    if "enableCenterPoint" in AnalogGaugeWidget:
                        # Set enable needle center
                        gaugeWidget.setEnableCenterPoint(bool(AnalogGaugeWidget["enableCenterPoint"]))


                    if "enableScaleText" in AnalogGaugeWidget:
                        # Set enable scale text
                        gaugeWidget.setEnableScaleText(bool(AnalogGaugeWidget["enableScaleText"]))

                    if "enableScaleBigGrid" in AnalogGaugeWidget:
                        # Set enable big scale grid
                        gaugeWidget.setEnableBigScaleGrid(bool(AnalogGaugeWidget["enableScaleBigGrid"]))

                    if "enableScaleFineGrid" in AnalogGaugeWidget:
                        # Set enable big scale grid
                        gaugeWidget.setEnableFineScaleGrid(bool(AnalogGaugeWidget["enableScaleFineGrid"]))

                    if "needleColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["needleColor"])) > 0:
                        # Set needle color
                        gaugeWidget.NeedleColor = QColor(self.getThemeVariableValue(str(AnalogGaugeWidget["needleColor"])))
                        gaugeWidget.NeedleColorReleased = QColor(self.getThemeVariableValue(str(AnalogGaugeWidget["needleColor"])))


                    if "needleColorOnDrag" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["needleColorOnDrag"])) > 0:
                        # Set needle color on drag
                        gaugeWidget.NeedleColorDrag = QColor(self.getThemeVariableValue(str(AnalogGaugeWidget["needleColorOnDrag"])))

                    if "scaleValueColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["scaleValueColor"])) > 0:
                        # Set value color
                        gaugeWidget.ScaleValueColor = QColor(self.getThemeVariableValue(str(AnalogGaugeWidget["scaleValueColor"])))

                    if "displayValueColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["displayValueColor"])) > 0:
                        # Set display value color
                        gaugeWidget.DisplayValueColor = QColor(self.getThemeVariableValue(str(AnalogGaugeWidget["displayValueColor"])))

                    if "bigScaleColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["bigScaleColor"])) > 0:
                        # Set big scale color
                        gaugeWidget.setBigScaleColor(QColor(self.getThemeVariableValue(str(AnalogGaugeWidget["bigScaleColor"]))))

                    if "fineScaleColor" in AnalogGaugeWidget and len(str(AnalogGaugeWidget["fineScaleColor"])) > 0:
                        # Set fine scale color
                        gaugeWidget.setFineScaleColor(QColor(self.getThemeVariableValue(str(AnalogGaugeWidget["fineScaleColor"]))))

                    if "customGaugeTheme" in AnalogGaugeWidget:
                        # Set custom gauge theme
                        colors = AnalogGaugeWidget['customGaugeTheme']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setCustomGaugeTheme(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2'])),
                                                color3 = self.getThemeVariableValue(str(x['color3']))
                                            )

                                    else:

                                        gaugeWidget.setCustomGaugeTheme(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2']))
                                            )

                                else:

                                    gaugeWidget.setCustomGaugeTheme(
                                            color1 = self.getThemeVariableValue(str(x['color1']))
                                        )

                    if "scalePolygonColor" in AnalogGaugeWidget:
                        # Set scale polygon color
                        colors = AnalogGaugeWidget['scalePolygonColor']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setScalePolygonColor(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2'])),
                                                color3 = self.getThemeVariableValue(str(x['color3']))
                                            )

                                    else:

                                        gaugeWidget.setScalePolygonColor(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2'])),
                                            )

                                else:

                                    gaugeWidget.setScalePolygonColor(
                                            color1 = self.getThemeVariableValue(str(x['color1'])),
                                        )

                    if "needleCenterColor" in AnalogGaugeWidget:
                        # Set needle center color
                        colors = AnalogGaugeWidget['needleCenterColor']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setNeedleCenterColor(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2'])),
                                                color3 = self.getThemeVariableValue(str(x['color3']))
                                            )

                                    else:

                                        gaugeWidget.setNeedleCenterColor(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2'])),
                                            )

                                else:

                                    gaugeWidget.setNeedleCenterColor(
                                            color1 = self.getThemeVariableValue(str(x['color1'])),
                                        )

                    if "outerCircleColor" in AnalogGaugeWidget:
                        # Set outer circle color
                        colors = AnalogGaugeWidget['outerCircleColor']

                        for x in colors:

                            if "color1" in x and len(str(x['color1'])) > 0:
                                if "color2" in x and len(str(x['color2'])) > 0:
                                    if "color3" in x and len(str(x['color3'])) > 0:

                                        gaugeWidget.setOuterCircleColor(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2'])),
                                                color3 = self.getThemeVariableValue(str(x['color3']))
                                            )

                                    else:

                                        gaugeWidget.setOuterCircleColor(
                                                color1 = self.getThemeVariableValue(str(x['color1'])),
                                                color2= self.getThemeVariableValue(str(x['color2'])),
                                            )

                                else:

                                    gaugeWidget.setOuterCircleColor(
                                            color1 = self.getThemeVariableValue(str(x['color1'])),
                                        )

                    if "valueFontFamily" in AnalogGaugeWidget:
                        # Set value font family
                        font = AnalogGaugeWidget['valueFontFamily']

                        for x in font:
                            if "path" in x and len(str(x['path'])) > 0:
                                QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), str(x['path'])) )

                            if "name" in x and len(str(x['name'])) > 0:
                                gaugeWidget.setValueFontFamily(str(x['name']))

                    if "scaleFontFamily" in AnalogGaugeWidget:
                        # Set scale font family
                        font = AnalogGaugeWidget['scaleFontFamily']
                        for x in font:
                            if "path" in x and len(str(x['path'])) > 0:

                                QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), str(x['path'])) )

                            if "name" in x and len(str(x['name'])) > 0:
                                gaugeWidget.setScaleFontFamily(str(x['name']))


                else:
                    raise Exception(str(AnalogGaugeWidget["name"])+" is not a AnalogGaugeWidget, no widget found")

    ## MENUS
    if "QCustomSlideMenu" in data:
        for QCustomSlideMenu in data['QCustomSlideMenu']:
            if "name" in QCustomSlideMenu and len(str(QCustomSlideMenu["name"])) > 0:
                if hasattr(self.ui, str(QCustomSlideMenu["name"])):
                    containerWidget = getattr(self.ui, str(QCustomSlideMenu["name"]))


                    if not containerWidget.metaObject().className() == "QCustomSlideMenu":
                        raise Exception("Error: "+str(QCustomSlideMenu["name"])+" is not a QCustomSlideMenu object")

                    #
                    defaultWidth = 0
                    defaultHeight = 0
                    collapsedWidth = 0
                    collapsedHeight = 0
                    expandedWidth = 0
                    expandedHeight = 0
                    animationDuration = 0
                    collapsingAnimationDuration = 0
                    expandingAnimationDuration = 0
                    animationEasingCurve = returnAnimationEasingCurve("Linear")
                    collapsingAnimationEasingCurve = returnAnimationEasingCurve("Linear")
                    expandingAnimationEasingCurve = returnAnimationEasingCurve("Linear")
                    collapsedStyle = ""
                    expandedStyle = ""
                    buttonObject = ""
                    menuCollapsedIcon = ""
                    menuExpandedIcon = ""
                    menuCollapsedStyle = ""
                    menuExpandedStyle = ""
                    relativeTo = ""
                    position = ""
                    shadowColor = ""
                    shadowBlurRadius = ""
                    shadowXOffset = ""
                    shadowYOffset = ""
                    floatMenu = False
                    autoHide = True

                    if "floatPosition" in QCustomSlideMenu:
                        floatMenu = True
                        if hasattr(self, "floatingWidgets"):
                            self.floatingWidgets.append(containerWidget)
                        else:

                            
                            # Floating widgets
                            
                            self.floatingWidgets = []
                            self.floatingWidgets.append(containerWidget)

                        for floatPosition in QCustomSlideMenu["floatPosition"]:

                            if "relativeTo" in floatPosition:
                                if hasattr(self.ui, floatPosition["relativeTo"]):
                                    relativeTo = getattr(self.ui, str(floatPosition["relativeTo"]))

                                    relativeTo = containerWidget.setParent(relativeTo)
                                else:
                                    relativeTo = floatPosition["relativeTo"]

                            if "position" in floatPosition:
                                position = floatPosition["position"]

                            if "shadow" in floatPosition:
                                for shadow in floatPosition["shadow"]:
                                    if "color" in shadow:
                                        shadowColor = self.getThemeVariableValue(shadow["color"])
                                    if "blurRadius" in shadow:
                                        shadowBlurRadius = shadow["blurRadius"]
                                    if "xOffset" in shadow:
                                        shadowXOffset = shadow["xOffset"]
                                    if "yOffset" in shadow:
                                        shadowYOffset = shadow["yOffset"]

                            if "autoHide" in floatPosition:
                                if floatPosition["position"] == True:
                                    autoHide = True
                                else:
                                    autoHide = False
                            else:
                                autoHide = False

                    if "defaultSize" in QCustomSlideMenu:
                        for defaultSize in QCustomSlideMenu["defaultSize"]:

                            if "width" in defaultSize:
                                defaultWidth = defaultSize["width"]

                            if "height" in defaultSize:
                                defaultHeight = defaultSize["height"]


                    if "collapsedSize" in QCustomSlideMenu:
                        for collapsedSize in QCustomSlideMenu["collapsedSize"]:

                            if "width" in collapsedSize:
                                collapsedWidth = collapsedSize["width"]

                            if "height" in collapsedSize:
                                collapsedHeight = collapsedSize["height"]

                    if "expandedSize" in QCustomSlideMenu:
                        for expandedSize in QCustomSlideMenu["expandedSize"]:

                            if "width" in expandedSize:
                                expandedWidth = expandedSize["width"]

                            if "height" in expandedSize:
                                expandedHeight = expandedSize["height"]

                    if "menuTransitionAnimation" in QCustomSlideMenu:

                        for menuTransitionAnimation in QCustomSlideMenu["menuTransitionAnimation"]:

                            if "animationDuration" in menuTransitionAnimation:
                                animationDuration = menuTransitionAnimation["animationDuration"]
                                collapsingAnimationDuration = menuTransitionAnimation["animationDuration"]
                                expandingAnimationDuration = menuTransitionAnimation["animationDuration"]

                            if "animationEasingCurve" in menuTransitionAnimation:
                                animationEasingCurve = returnAnimationEasingCurve(menuTransitionAnimation["animationEasingCurve"])
                                collapsingAnimationEasingCurve = returnAnimationEasingCurve(menuTransitionAnimation["animationEasingCurve"])
                                expandingAnimationEasingCurve = returnAnimationEasingCurve(menuTransitionAnimation["animationEasingCurve"])

                            if "whenCollapsing" in menuTransitionAnimation:
                                for whenCollapsing in menuTransitionAnimation["whenCollapsing"]:
                                    if "animationDuration" in whenCollapsing:
                                        collapsingAnimationDuration = whenCollapsing["animationDuration"]

                                    if "animationEasingCurve" in whenCollapsing:
                                        collapsingAnimationEasingCurve = returnAnimationEasingCurve(whenCollapsing["animationEasingCurve"])


                            if "whenExpanding" in menuTransitionAnimation:
                                for whenExpanding in menuTransitionAnimation["whenExpanding"]:
                                    if "animationDuration" in whenExpanding:
                                        expandingAnimationDuration = whenExpanding["animationDuration"]

                                    if "animationEasingCurve" in whenExpanding:
                                        expandingAnimationEasingCurve = returnAnimationEasingCurve(whenExpanding["animationEasingCurve"])


                    if "menuContainerStyle" in QCustomSlideMenu:
                        for menuContainerStyle in QCustomSlideMenu["menuContainerStyle"]:
                            if "whenMenuIsCollapsed" in menuContainerStyle:
                                colSty = ""
                                for collapsedStyle in menuContainerStyle["whenMenuIsCollapsed"]:
                                    colSty +=str(collapsedStyle)

                                if len(colSty) > 0:
                                    collapsedStyle = self.styleVariablesFromTheme(colSty)

                            if "whenMenuIsExpanded" in menuContainerStyle and len(str(menuContainerStyle["whenMenuIsExpanded"])) > 0:
                                expSty = ""
                                for expandedStyle in menuContainerStyle["whenMenuIsExpanded"]:
                                    expSty += str(expandedStyle)

                                if len(expSty) > 0:
                                    expandedStyle = self.styleVariablesFromTheme(expSty)

                    containerWidget.customizeQCustomSlideMenu(
                        defaultWidth = defaultWidth,
                        defaultHeight = defaultHeight,
                        collapsedWidth = collapsedWidth,
                        collapsedHeight = collapsedHeight,
                        expandedWidth = expandedWidth,
                        expandedHeight = expandedHeight,
                        animationDuration = animationDuration,
                        animationEasingCurve = animationEasingCurve,
                        collapsingAnimationDuration = collapsingAnimationDuration,
                        collapsingAnimationEasingCurve = collapsingAnimationEasingCurve,
                        expandingAnimationDuration = expandingAnimationDuration,
                        expandingAnimationEasingCurve = expandingAnimationEasingCurve,
                        collapsedStyle = collapsedStyle,
                        expandedStyle = expandedStyle,
                        floatMenu = floatMenu,
                        relativeTo = relativeTo,
                        position = position,
                        shadowColor = shadowColor,
                        shadowBlurRadius    = shadowBlurRadius,
                        shadowXOffset   = shadowXOffset,
                        shadowYOffset   = shadowYOffset,
                        autoHide = autoHide,
                        update = update
                    )

                    if "toggleButton" in QCustomSlideMenu:
                        for toggleButton in QCustomSlideMenu["toggleButton"]:
                            if "buttonName" in toggleButton and len(str(toggleButton["buttonName"])) > 0:
                                if hasattr(self.ui, str(toggleButton["buttonName"])):

                                    buttonObject = getattr(self.ui, str(toggleButton["buttonName"]))

                                    if "icons" in toggleButton:
                                        for icons in toggleButton["icons"]:
                                            if "whenMenuIsCollapsed" in icons and len(str(icons["whenMenuIsCollapsed"])) > 0:
                                                menuCollapsedIcon = replace_url_prefix(str(icons["whenMenuIsCollapsed"]), "Qss/icons")


                                            if "whenMenuIsExpanded" in icons and len(str(icons["whenMenuIsExpanded"])) > 0:
                                                menuExpandedIcon = replace_url_prefix(str(icons["whenMenuIsExpanded"]), "Qss/icons")



                                    if "style" in toggleButton:
                                        for style in toggleButton["style"]:
                                            if "whenMenuIsCollapsed" in style:
                                                colSty = ""
                                                for collapsedStyle in style["whenMenuIsCollapsed"]:
                                                    colSty += str(collapsedStyle)

                                                if len(colSty) > 0:
                                                    menuCollapsedStyle = self.styleVariablesFromTheme(colSty)


                                            if "whenMenuIsExpanded" in style:
                                                expSty = ""
                                                for collapsedStyle in style["whenMenuIsExpanded"]:
                                                    expSty += str(collapsedStyle)

                                                if len(expSty) > 0:
                                                    menuExpandedStyle = self.styleVariablesFromTheme(expSty)


                                    containerWidget.toggleButton(
                                        buttonName = buttonObject,
                                        iconWhenMenuIsCollapsed = menuCollapsedIcon,
                                        iconWhenMenuIsExpanded = menuExpandedIcon,
                                        styleWhenMenuIsCollapsed = menuCollapsedStyle,
                                        styleWhenMenuIsExpanded = menuExpandedStyle,
                                        update = update
                                    )

                                else:
                                    raise Exception(str(toggleButton["buttonName"])+" toggle button could not be found")
                    if not update:
                        containerWidget.refresh()


                else:
                    raise Exception(str(QCustomSlideMenu["name"])+" is not a QCustomSlideMenu, no widget found")
    ## WINDOWS FLAG
    if "QMainWindow" in data:
        for QMainWindow in data['QMainWindow']:
            if "tittle" in QMainWindow and len(str(QMainWindow["tittle"])) > 0:
                # Set window tittle
                self.setWindowTitle(str(QMainWindow["tittle"]))

            if "icon" in QMainWindow and len(str(QMainWindow["icon"])) > 0:  
                # Set window Icon
                self.setWindowIcon(QtGui.QIcon(str(QMainWindow["icon"])))

            if "frameless" in QMainWindow and QMainWindow["frameless"]:   
                ## # Remove window tittle bar
                self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

            if "transluscentBg" in QMainWindow and QMainWindow["transluscentBg"]:
                ## # Set main background to transparent
                self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            if "sizeGrip" in QMainWindow and len(str(QMainWindow["sizeGrip"])) > 0:
                # Window Size grip to resize window
                if hasattr(self.ui, str(QMainWindow["sizeGrip"])):
                    QSizeGrip(getattr(self.ui, str(QMainWindow["sizeGrip"])))

            if "shadow" in QMainWindow:
                ## # Shadow effect style
                for shadow in QMainWindow["shadow"]:
                    if "centralWidget" in shadow and len(str(shadow['centralWidget'])) > 0:
                        if hasattr(self.ui, str(shadow["centralWidget"])):
                            self.shadow = QGraphicsDropShadowEffect(self)
                            if "color" in shadow and len(str(shadow['color'])) > 0:
                                self.shadow.setColor(QColor(self.getThemeVariableValue(str(shadow['color']))))
                            if "blurRadius" in shadow and int(shadow['blurRadius']) > 0:
                                self.shadow.setBlurRadius(int(shadow['blurRadius']))
                            if "xOffset" in shadow and int(shadow['xOffset']) > 0:
                                self.shadow.setXOffset(int(shadow['xOffset']))
                            else:
                                self.shadow.setXOffset(0)

                            if "yOffset" in shadow and int(shadow['yOffset']) > 0:
                                self.shadow.setYOffset(int(shadow['yOffset']))
                            else:
                                self.shadow.setYOffset(0)
 
                            ## # Appy shadow to central widget
                            getattr(self.ui, str(shadow["centralWidget"])).setGraphicsEffect(self.shadow)



            if "navigation" in QMainWindow:
                for navigation in QMainWindow["navigation"]:
                    if "minimize" in navigation and len(str(navigation["minimize"])) > 0:
                        
                        #Minimize window
                        if hasattr(self.ui, str(navigation["minimize"])):
                            getattr(self.ui, str(navigation["minimize"])).clicked.connect(lambda: self.showMinimized())

                    if "close" in navigation and len(str(navigation["close"])) > 0:
                        
                        #Close window
                        if hasattr(self.ui, str(navigation["close"])):
                            getattr(self.ui, str(navigation["close"])).clicked.connect(lambda: self.close())

                    if "restore" in navigation:
                        
                        #Restore/Maximize window
                        for restore in navigation["restore"]:
                            if "buttonName" in restore and len(str(restore["buttonName"])) > 0:
                                if hasattr(self.ui, str(restore["buttonName"])):
                                    getattr(self.ui, str(restore["buttonName"])).clicked.connect(lambda: self.restore_or_maximize_window())
                                    self.restoreBtn = getattr(self.ui, str(restore["buttonName"]))
                            if "normalIcon" in restore and len(str(restore["normalIcon"])) > 0:
                                self.normalIcon = replace_url_prefix(str(restore["normalIcon"]), "Qss/icons")
                            else:
                                self.normalIcon = ""

                            if "maximizedIcon" in restore and len(str(restore["maximizedIcon"])) > 0:
                                self.maximizedIcon = replace_url_prefix(str(restore["maximizedIcon"]), "Qss/icons")
                            else:
                                self.maximizedIcon = ""

                    if "moveWindow" in navigation and len(str(navigation["moveWindow"])) > 0:
                        # Add click event/Mouse move event/drag event to the top header to move the window
                        if hasattr(self.ui, str(navigation["moveWindow"])):
                            getattr(self.ui, str(navigation["moveWindow"])).mouseMoveEvent = self.moveWindow
                        

                    if "tittleBar" in navigation and len(str(navigation["tittleBar"])) > 0:
                        # Add click event/Mouse move event/drag event to the top header to move the window
                        if hasattr(self.ui, str(navigation["tittleBar"])):
                            getattr(self.ui, str(navigation["tittleBar"])).mouseDoubleClickEvent = self.toggleWindowSize

    if "QPushButton" in data:
        for button in data['QPushButton']:
            if "name" in button and len(button["name"]) > 0:
                # GET BUTTON OBJECT
                if hasattr(self.ui, str(button["name"])):
                    buttonObject = getattr(self.ui, str(button["name"]))
                    # VERIFY IF THE OBJECT IS A BUTTON
                    if not str(buttonObject.metaObject().className()) == "QCustomQPushButton" and not buttonObject.metaObject().className() == "QPushButtonThemed":
                        raise Exception(buttonObject.metaObject().className(), buttonObject, " is not of type QPushButton")

                    buttonObject.wasFound = False
                    buttonObject.wasThemed = False

                    if buttonObject.objectName() == button["name"]:
                        if "theme" in button and len(button["theme"]) > 0:
                            buttonObject.setObjectTheme(button["theme"])

                        if "customTheme" in button and len(button["customTheme"]) > 0:
                            for x in button["customTheme"]:
                                if len(x["color1"]) > 0 and len(x["color1"]) > 0 :
                                    buttonObject.setObjectCustomTheme(self.getThemeVariableValue(x["color1"]), self.getThemeVariableValue(x["color2"]))

                        if "animateOn" in button and len(button["animateOn"]) > 0:
                            buttonObject.setObjectAnimateOn(button["animateOn"])

                        if "animation" in button and len(button["animation"]) > 0:
                            buttonObject.setObjectAnimation(button["animation"])

                        if "animationDuration" in button and int(button['animationDuration']) > 0:
                            buttonObject._animation.setDuration(int(button["animationDuration"]))

                        if "animationEasingCurve" in button and len(button['animationEasingCurve']) > 0:
                            easingCurve = returnAnimationEasingCurve(button['animationEasingCurve'])
                            buttonObject._animation.setEasingCurve(easingCurve)


                        fallBackStyle = ""
                        if "fallBackStyle" in button:
                            for x in button["fallBackStyle"]:
                                fallBackStyle += x

                        defaultStyle = ""
                        if "defaultStyle" in button:
                            for x in button["defaultStyle"]:
                                defaultStyle += x

                        buttonObject.wasThemed = True

                        if len(fallBackStyle) > 0:
                            buttonObject.setObjectFallBackStyle(self.styleVariablesFromTheme(fallBackStyle))

                        if len(defaultStyle) > 0:
                            buttonObject.setObjectDefaultStyle(self.styleVariablesFromTheme(defaultStyle))

                        if len(fallBackStyle) > 0:
                            buttonObject.setStyleSheet(defaultStyle + fallBackStyle)
                        elif "theme" in button and len(button["theme"]) > 0:
                            #
                            applyAnimationThemeStyle(buttonObject, button["theme"])
                        elif "customTheme" in button and len(button["customTheme"]) > 0:
                            for x in button["customTheme"]:
                                if len(x["color1"]) > 0 and len(x["color1"]) > 0 :
                                    applyCustomAnimationThemeStyle(buttonObject, self.getThemeVariableValue(x["color1"]), self.getThemeVariableValue(x["color2"]))
                        else:
                            buttonObject.wasThemed = False

                        ## ICONIFY STYLESHEET
                        if "iconify" in button:
                            for icon in button['iconify']:
                                if "icon" in icon and len(icon['icon']) > 0:
                                    btnIcon = icon['icon']
                                    if "color" in icon and len(icon['color']) > 0:
                                        color = self.getThemeVariableValue(icon['color'])
                                    else:
                                        color = ""

                                    if "size" in icon and int(icon['size']) > 0:
                                        size = icon['size']
                                    else:
                                        size = ""

                                    if "animateOn" in icon and len(icon['animateOn']) > 0:
                                        animateOn = icon['animateOn']
                                    else:
                                        animateOn = ""

                                    if "animation" in icon and len(icon['animation']) > 0:
                                        animation = icon['animation']
                                    else:
                                        animation = ""

                                    iconify(buttonObject, icon = btnIcon, color = color, size = size, animation = animation, animateOn = animateOn)


                        ## BUTTON SHADOW STYLESHEET
                        if "shadow" in button:
                            for shadow in button["shadow"]:
                                if "color" in shadow and len(str(shadow['color'])) > 0:
                                    shadowColor = self.getThemeVariableValue(shadow['color'])
                                else:
                                    shadowColor = ""

                                if "applyShadowOn" in shadow and len(str(shadow['applyShadowOn'])) > 0:
                                    applyShadowOn = shadow['applyShadowOn']
                                else:
                                    applyShadowOn = ""

                                if "animateShadow" in shadow:
                                    animateShadow = shadow['animateShadow']
                                else:
                                    animateShadow = False

                                if "animateShadowDuration" in shadow and int(shadow['animateShadowDuration']) > 0:
                                    animateShadowDuration = shadow['animateShadowDuration']
                                else:
                                    animateShadowDuration = 0

                                if "blurRadius" in shadow and int(shadow['blurRadius']) > 0:
                                    blurRadius = shadow['blurRadius']
                                else:
                                    blurRadius = 0

                                if "xOffset" in shadow and int(shadow['xOffset']) > 0:
                                    xOffset = shadow['xOffset']
                                else:
                                    xOffset = 0

                                if "yOffset" in shadow and int(shadow['yOffset']) > 0:
                                    yOffset = shadow['yOffset']
                                else:
                                    yOffset = 0

                                applyButtonShadow(
                                    buttonObject,
                                    color= shadowColor,
                                    applyShadowOn= applyShadowOn,
                                    animateShadow = animateShadow,
                                    blurRadius = blurRadius,
                                    animateShadowDuration = animateShadowDuration,
                                    xOffset = xOffset,
                                    yOffset = yOffset
                                )

                        buttonObject.wasFound = True

    ## Qstacked Widget
    if "QCustomQStackedWidget" in data:
        for stackedWidget in data['QCustomQStackedWidget']:
            if "name" in stackedWidget and len(str(stackedWidget["name"])) > 0:
                if hasattr(self.ui, str(stackedWidget["name"])):
                    widget = getattr(self.ui, str(stackedWidget["name"]))
                    if widget.objectName() == stackedWidget["name"]:
                        if "transitionAnimation" in stackedWidget:
                            for transitionAnimation in stackedWidget["transitionAnimation"]:
                                if "fade" in transitionAnimation:
                                    for fade in transitionAnimation["fade"]:
                                        if "active" in fade and fade["active"]:
                                            widget.fadeTransition = True
                                            if "duration" in fade and fade["duration"] > 0:
                                                widget.fadeTime = fade["duration"]
                                            if "easingCurve" in fade and len(str(fade["easingCurve"])) > 0:
                                                widget.fadeEasingCurve = returnAnimationEasingCurve(fade["easingCurve"])

                                if "slide" in transitionAnimation:
                                    for slide in transitionAnimation["slide"]:
                                        if "active" in slide and slide["active"]:
                                            widget.slideTransition = True
                                            if "duration" in slide and slide["duration"] > 0:
                                                widget.transitionTime = slide["duration"]
                                            if "easingCurve" in slide and len(str(slide["easingCurve"])) > 0:
                                                widget.transitionEasingCurve = returnAnimationEasingCurve(slide["easingCurve"])
                                            if "direction" in slide and len(str(slide["direction"])) > 0:
                                                widget.transitionDirection = returnQtDirection(slide["direction"])

                        if "navigation" in stackedWidget:
                            for navigation in stackedWidget["navigation"]:
                                if "nextPage" in navigation:
                                    if hasattr(self.ui, str(navigation["nextPage"])):
                                        button = getattr(self.ui, str(navigation["nextPage"]))
                                        button.clicked.connect(lambda: widget.slideToNextWidget())
                                    else:
                                        raise Exception("Unknown button '" +str(button)+ "'. Please check your JSon file")

                                if "previousPage" in navigation:
                                    if hasattr(self.ui, str(navigation["previousPage"])):
                                        button = getattr(self.ui, str(navigation["previousPage"]))
                                        button.clicked.connect(lambda: widget.slideToPreviousWidget())
                                    else:
                                        raise Exception("Unknown button '" +str(button)+ "'. Please check your JSon file")

                                if "navigationButtons" in navigation:
                                    for navigationButton in navigation["navigationButtons"]:
                                        for button in navigationButton:
                                            widgetPage = navigationButton[button]
                                            if not hasattr(self.ui, str(widgetPage)):
                                                raise Exception("Unknown widget '" +str(widgetPage)+ "'. Please check your JSon file")
                                            if not hasattr(self.ui, str(button)):
                                                raise Exception("Unknown button '" +str(button)+ "'. Please check your JSon file")

                                            pushBtn = getattr(self.ui, str(button))
                                            widgetPg = getattr(self.ui, str(widgetPage))
                                            navigationButtons(widget, pushBtn, widgetPg)

    ## QCustomProgressIndicator
    if "QCustomProgressIndicator" in data:
        for QCustomProgressIndicator in data['QCustomProgressIndicator']:
            if "name" in QCustomProgressIndicator and len(str(QCustomProgressIndicator["name"])) > 0:
                if hasattr(self.ui, str(QCustomProgressIndicator["name"])):
                    containerWidget = getattr(self.ui, str(QCustomProgressIndicator["name"]))


                    if not containerWidget.metaObject().className() == "QCustomProgressIndicator":
                        raise Exception("Error: "+str(QCustomProgressIndicator["name"])+" is not a QCustomProgressIndicator widget")
                    
                    if "color" in QCustomProgressIndicator:
                        containerWidget.color = self.getThemeVariableValue(str(QCustomProgressIndicator["color"]))
                        containerWidget.updateFormProgressIndicator(color = containerWidget.color)
                    
                    if "fillColor" in QCustomProgressIndicator:
                        containerWidget.fillColor = self.getThemeVariableValue(str(QCustomProgressIndicator["fillColor"]))
                        containerWidget.updateFormProgressIndicator(fillColor = containerWidget.fillColor)

                    if "warningFillColor" in QCustomProgressIndicator:
                        containerWidget.warningFillColor = self.getThemeVariableValue(str(QCustomProgressIndicator["warningFillColor"]))
                        containerWidget.updateFormProgressIndicator(warningFillColor = containerWidget.warningFillColor)

                    if "errorFillColor" in QCustomProgressIndicator:
                        containerWidget.errorFillColor = self.getThemeVariableValue(str(QCustomProgressIndicator["errorFillColor"]))
                        containerWidget.updateFormProgressIndicator(errorFillColor = containerWidget.errorFillColor)

                    if "successFillColor" in QCustomProgressIndicator:
                        containerWidget.successFillColor = self.getThemeVariableValue(str(QCustomProgressIndicator["successFillColor"]))
                        containerWidget.updateFormProgressIndicator(successFillColor = containerWidget.successFillColor)

                    if "formProgressCount" in QCustomProgressIndicator:
                        containerWidget.formProgressCount = int(QCustomProgressIndicator["formProgressCount"])
                        containerWidget.updateFormProgressIndicator(formProgressCount = containerWidget.formProgressCount)

                    if "formProgressAnimationDuration" in QCustomProgressIndicator:
                        containerWidget.formProgressAnimationDuration = int(QCustomProgressIndicator["formProgressAnimationDuration"])
                        containerWidget.updateFormProgressIndicator(formProgressAnimationDuration = containerWidget.formProgressAnimationDuration)
                    
                    if "formProgressAnimationEasingCurve" in QCustomProgressIndicator:
                        containerWidget.formProgressAnimationEasingCurve = str(QCustomProgressIndicator["formProgressAnimationEasingCurve"])
                        containerWidget.updateFormProgressIndicator(formProgressAnimationEasingCurve = containerWidget.formProgressAnimationEasingCurve)
                    
                    if "height" in QCustomProgressIndicator:
                        containerWidget.height = int(QCustomProgressIndicator["height"])
                        containerWidget.updateFormProgressIndicator(height = containerWidget.height)

                    if "width" in QCustomProgressIndicator:
                        containerWidget.width = int(QCustomProgressIndicator["width"])
                        containerWidget.updateFormProgressIndicator(width = containerWidget.width)
                    
                    if "startPercentage" in QCustomProgressIndicator:
                        containerWidget.startPercentage = int(QCustomProgressIndicator["startPercentage"])
                        containerWidget.updateFormProgressIndicator(startPercentage = containerWidget.startPercentage)

                    if "theme" in QCustomProgressIndicator:
                        containerWidget.theme = int(QCustomProgressIndicator["theme"])
                        containerWidget.selectFormProgressIndicatorTheme(containerWidget.theme)

                    # containerWidget.updateFormProgress(value)

    ## QCustomCheckBox
    if "QCustomCheckBox" in data:
        for QCustomCheckBox in data['QCustomCheckBox']:

            checkBoxes = []

            if "name" in QCustomCheckBox and len(str(QCustomCheckBox["name"])) > 0:
                checkBoxes.append(QCustomCheckBox["name"])

            if "names" in QCustomCheckBox:
                checkBoxes.extend(QCustomCheckBox["names"])

            if checkBoxes:
                for checkBox in checkBoxes:
                    if hasattr(self.ui, str(checkBox)):
                        containerWidget = getattr(self.ui, str(checkBox))


                        if not containerWidget.metaObject().className() == "QCustomCheckBox":
                            raise Exception("Error: "+str(checkBox)+" is not a QCustomCheckBox widget")
                        
                        if "bgColor" in QCustomCheckBox:
                            containerWidget.bgColor = QColor(self.getThemeVariableValue(str(QCustomCheckBox["bgColor"])))
                            containerWidget.customizeQCustomCheckBox(bgColor = containerWidget.bgColor)
                        
                        if "circleColor" in QCustomCheckBox:
                            containerWidget.circleColor = QColor(self.getThemeVariableValue(str(QCustomCheckBox["circleColor"])))
                            containerWidget.customizeQCustomCheckBox(circleColor = containerWidget.circleColor)
                        
                        if "activeColor" in QCustomCheckBox:
                            containerWidget.activeColor = QColor(self.getThemeVariableValue(str(QCustomCheckBox["activeColor"])))
                            containerWidget.customizeQCustomCheckBox(activeColor = containerWidget.activeColor)

                        if "animationEasingCurve" in QCustomCheckBox:
                            containerWidget.animationEasingCurve = returnAnimationEasingCurve(str(QCustomCheckBox["animationEasingCurve"]))
                            containerWidget.customizeQCustomCheckBox(animationEasingCurve = containerWidget.animationEasingCurve)

                        if "animationDuration" in QCustomCheckBox:
                            containerWidget.animationDuration = int(QCustomCheckBox["animationDuration"])
                            containerWidget.customizeQCustomCheckBox(animationDuration = containerWidget.animationDuration)

                    else:
                        raise Exception("Error: "+str(checkBox)+" widget does not exist")
                    
def replace_url_prefix(url, new_prefix):
    pattern = re.compile(r':/[^/]+/')
    return pattern.sub( new_prefix + '/', url, 1)

class Object(object):
    pass

def navigationButtons(stackedWidget, pushButton, widgetPage):
    pushButton.clicked.connect(lambda: stackedWidget.setCurrentWidget(widgetPage))
