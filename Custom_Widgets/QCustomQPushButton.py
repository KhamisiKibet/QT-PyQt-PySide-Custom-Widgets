########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################

from Custom_Widgets import iconify as ico

########################################################################
## MODULE UPDATED TO USE QT.PY
########################################################################
from qtpy.QtCore import QVariantAnimation, QAbstractAnimation, QSize
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QPushButton, QGraphicsDropShadowEffect

class QCustomQPushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        ########################################################################
        ## CREATE ANIMATION
        ########################################################################
        self._animation = QVariantAnimation()
        self._animation.setStartValue(0.00001)
        self._animation.setEndValue(0.9999)
        self._animation.valueChanged.connect(self._animate)
        # self._animation.setEasingCurve(QEasingCurve.OutQuad)

        # DEAFAULT ANIMATION DURATION
        self._animation.setDuration(500)

        self._shadowAnimation = QVariantAnimation()
        self._shadowAnimation.setStartValue(0)
        self._shadowAnimation.setEndValue(10)
        self._shadowAnimation.valueChanged.connect(self._animateShadow)
        # self._shadowAnimation.setEasingCurve(QEasingCurve.OutQuad)

        # DEAFAULT ANIMATION DURATION
        self._shadowAnimation.setDuration(500)

        # DEFAULT COLOR
        self.color1 = None
        self.color2 = None

        # DEFAULT ANIMATION TRIGGER FOR BUTTON IS HOVER EVENT
        self.setObjectAnimatedOn = "hover"

        # DEFAULT ANIMATION TRIGGER FOR BUTTON ICON IS NONE
        self.setIconAnimatedOn = None

        # ANIMATE BORDER AND BACKGROUND BY DEFAULT
        self.setObjectAnimate = "both"

        # SET DEFAULT FALLBACK STYLE TO NINE
        self.fallBackStyle = None

        # SET DEFAULT FALLBACK STYLE TO NONE
        self.defaultStyle = None

        # SET DEFAULT FALLBACK STYLE TO NONE
        self.clickPosition = None

        # SET DEFAULT FALLBACK STYLE TO NONE
        self.mousePosition = None

        # SET DEFAULT SHADOW EVENT TO NONE
        self.applyShadowOn = None



    ########################################################################
    ## BUTTON THEMES
    ########################################################################
    def setObjectTheme(self, theme):
        if str(theme) == "1":
            self.color1 = QColor(9, 27, 27, 25)
            self.color2 = QColor(85, 255, 255, 255)
        elif str(theme) == "2":
            self.color1 = QColor(240, 53, 218)
            self.color2 = QColor(61, 217, 245)
        elif str(theme) == "3":
            self.color1 = QColor("#C0DB50")
            self.color2 = QColor("#100E19")
        elif str(theme) == "4":
            self.color1 = QColor("#FF16EB")
            self.color2 = QColor("#100E19")
        elif str(theme) == "5":
            self.color1 = QColor("#FF4200")
            self.color2 = QColor("#100E19")
        elif str(theme) == "6":
            self.color1 = QColor("#000046")
            self.color2 = QColor("#1CB5E0")
        elif str(theme) == "7":
            self.color1 = QColor("#EB5757")
            self.color2 = QColor("#000000")
        elif str(theme) == "8":
            self.color1 = QColor("#FF8235")
            self.color2 = QColor("#30E8BF")
        elif str(theme) == "9":
            self.color1 = QColor("#20002c")
            self.color2 = QColor("#cbb4d4")
        elif str(theme) == "10":
            self.color1 = QColor("#C33764")
            self.color2 = QColor("#1D2671")
        elif str(theme) == "11":
            self.color1 = QColor("#ee0979")
            self.color2 = QColor("#ff6a00")
        elif str(theme) == "12":
            self.color1 = QColor("#242424")
            self.color2 = QColor("#FA0000")
        elif str(theme) == "13":
            self.color1 = QColor("#25395f")
            self.color2 = QColor("#55ffff")

        else:
            raise Exception("Unknown theme '" +str(theme)+ "'")



    ########################################################################
    ## SET BUTTON THEME
    ########################################################################
    def setObjectCustomTheme(self, color1, color2):
        self.color1 = QColor(color1)
        self.color2 = QColor(color2)

    ########################################################################
    ## SET BUTTON ANIMATION
    ########################################################################
    def setObjectAnimation(self, animation):
        self.setObjectAnimate = str(animation)

    ########################################################################
    ## SET BUTTON ANIMATION EVENT TRIGGER
    ########################################################################
    def setObjectAnimateOn(self, trigger):
        self.setObjectAnimatedOn = trigger
        if str(trigger) == "click":
            self._animation.setDuration(200)
        else:
            self._animation.setDuration(500)

    ########################################################################
    ## SET BUTTON STYLESHEET TO BE AOOLIED AFTER ANIMATION IS OVER
    ########################################################################
    def setObjectFallBackStyle(self, style):
        self.fallBackStyle = str(style)

    ########################################################################
    ## SET BUTTON DEFAULT STYLESHEET THAT WILL BE ADDED ALONGSIDE ANIMATION
    ## STYLE
    ########################################################################
    def setObjectDefaultStyle(self, style):
        self.defaultStyle = str(style)

    ########################################################################
    ## SET BUTTON BUTTON HOVER IN EVENT
    ########################################################################
    def enterEvent(self, event):
        self.mousePosition = "over"
        if self.setObjectAnimatedOn  == "hover" or self.setObjectAnimatedOn is None:
            self._animation.setDirection(QAbstractAnimation.Forward)
            self._animation.start()
        #
        if self.setIconAnimatedOn == "hover":
            if hasattr(self, 'anim'):
                self.anim.start()
        if self.applyShadowOn == "hover":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QAbstractAnimation.Forward)
                self._shadowAnimation.start()

            else:
                self.setGraphicsEffect(self.shadow)

        super().enterEvent(event)

    ########################################################################
    ## SET BUTTON HOVER OUT EVENT
    ########################################################################
    def leaveEvent(self, event):
        self.mousePosition = "out"
        if self.setObjectAnimatedOn  == "hover" or self.setObjectAnimatedOn is None:
            self._animation.setDirection(QAbstractAnimation.Backward)
            self._animation.start()
            self._animation.finished.connect(lambda: self.applyDefaultStyle())

        if self.applyShadowOn == "hover":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QAbstractAnimation.Backward)
                self._shadowAnimation.start()
                self._shadowAnimation.finished.connect(lambda: self.removeButtonShadow())
                # disconnect(self._shadowAnimation.finished, self.removeButtonShadow())

        super().leaveEvent(event)


    ########################################################################
    ## SET BUTTON MOUSE PRESS 'DOWN' EVENT
    ########################################################################
    def mousePressEvent(self, event):
        self.clickPosition = "down"
        if self.setObjectAnimatedOn  == "click":
            self._animation.setDirection(QAbstractAnimation.Forward)
            self._animation.start()
        #
        if self.setIconAnimatedOn == "click":
            if hasattr(self, 'anim'):
                self.anim.start()
        if self.applyShadowOn == "click":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QAbstractAnimation.Forward)
                self._shadowAnimation.start()
            else:
                self.setGraphicsEffect(self.shadow)

        super().mousePressEvent(event)

    ########################################################################
    ## SET BUTTON MOUSE PRESS 'UP' EVENT
    ########################################################################
    def mouseReleaseEvent(self, event):
        self.clickPosition = "up"
        if self.setObjectAnimatedOn  == "click":
            self._animation.setDirection(QAbstractAnimation.Backward)
            self._animation.start()
            self._animation.finished.connect(lambda: self.applyDefaultStyle())
        if self.applyShadowOn == "click":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QAbstractAnimation.Backward)
                self._shadowAnimation.start()
                self._shadowAnimation.finished.connect(lambda: self.removeButtonShadow())
            else:
                self.setGraphicsEffect(self.shadow)
        super().mouseReleaseEvent(event)

    def doNothing(self):
        pass


    ########################################################################
    ## REMOVE BUTTON SHADOW
    ##
    ########################################################################
    def removeButtonShadow(self):
        # self.shadow.setBlurRadius(0)
        #######################################################################
        ## # Appy shadow to button
        ########################################################################
        self.setGraphicsEffect(self.shadow)

    ########################################################################
    ## APPLY BUTTON STYLESHEET AFTER ANIMATION IS OVER
    ## AND STOP ICON ANIMATIONS
    ########################################################################
    def applyDefaultStyle(self):
        if self.mousePosition == "out" or self.clickPosition == "up":
            if self.fallBackStyle is None:
                pass
            else:
                if self.defaultStyle is not None:
                    self.setStyleSheet(str(self.defaultStyle + self.fallBackStyle))
                else:
                    self.setStyleSheet(str(self.fallBackStyle))

            if hasattr(self, 'anim'):
                if (self.setIconAnimatedOn == "click" and self.clickPosition == "up") or (self.setIconAnimatedOn == "hover" and self.mousePosition == "out"):
                    try:
                        self.anim.stop()
                    except Exception as e:
                        pass

    ########################################################################
    ## ANIMATE BUTTON BACKGROUND AND BORDER
    ########################################################################
    def _animate(self, value):
        color_stop = 1
        if self.defaultStyle is not None:
            qss = str(self.defaultStyle)
        else:
            qss = """

            """

        if self.color1 is not None or self.color2 is not None:
            grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop:{value} {color2}, stop: 1.0 {color1});".format(
                color1=self.color1.name(), color2=self.color2.name(), value=value
            )


            style = """
                border-top-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop: """+str(value)+"""  """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name())+""");
                border-bottom-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop: """+str(value)+""" """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name())+""");
                border-right-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:"""+str(value)+"""  """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name())+""");
                border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop: """+str(value)+""" """+str(self.color1.name())+""", stop: """+str(color_stop)+"""  """+str(self.color2.name()) +""");

            """

            if self.setObjectAnimate == "border":
                qss += style
            elif self.setObjectAnimate == "background":
                qss += grad
            else:
                qss += grad
                qss += style

            self.setStyleSheet(qss)


    ########################################################################
    ## ANIMATE BUTTON SHADOW
    ########################################################################
    def _animateShadow(self, value):
        # Animate the transition
        self.shadow.setBlurRadius(value)
        #######################################################################
        ## # Appy shadow to button
        ########################################################################
        self.setGraphicsEffect(self.shadow)


########################################################################
##
########################################################################

def iconify(buttonObject, **iconCustomization):
    if "icon" in iconCustomization and len(iconCustomization['icon']) > 0:
        buttonObject.buttonIcon = ico.Icon(iconCustomization['icon'])

        if "color" in iconCustomization and len(iconCustomization['color']) > 0:
            buttonObject.buttonIcon = ico.Icon(iconCustomization['icon'], color=QColor(iconCustomization['color']))

        if "animation" in iconCustomization and len(iconCustomization['animation']) > 0:
            if iconCustomization['animation'] == "spin":
                buttonObject.anim = ico.anim.Spin()
            elif iconCustomization['animation'] == "breathe":
                buttonObject.anim = ico.anim.Breathe()
            elif iconCustomization['animation'] == "breathe and spin" or iconCustomization['animation'] == "spinn and breathe":
                buttonObject.anim = ico.anim.Spin() + ico.anim.Breathe()
            else:
                raise Exception("Unknown value'" +iconCustomization['animation']+ "' for ico.animation(). Supported animations are 'spinn' and 'breathe'")

            buttonObject.buttonIcon = ico.Icon(iconCustomization['icon'], color=QColor(iconCustomization['color']), anim=buttonObject.anim)

        buttonObject.buttonIcon.setAsButtonIcon(buttonObject)

        if "size" in iconCustomization and int(iconCustomization['size']) > 0:
            buttonObject.setIconSize(QSize(int(iconCustomization['size']), int(iconCustomization['size'])))

        if "animateOn" in iconCustomization and len(str(iconCustomization['animateOn'])) > 0:
            if "animation" in iconCustomization and len(str(iconCustomization['animation'])) > 0:
                if iconCustomization['animateOn'] == "all":
                    buttonObject.anim.start()
                elif iconCustomization['animateOn'] == "hover":
                    buttonObject.setIconAnimatedOn = "hover"
                elif iconCustomization['animateOn'] == "click":
                    buttonObject.setIconAnimatedOn = "click"

            else:
                raise Exception("Please specify the button icon animation. Supported signature is 'animation': 'spinn' or 'animation': 'breathe'")
    else:
        raise Exception("Failed to create the icon, please define the icon image i.e icon = 'icon.image'")


#######################################################################
## # APPLY BUTTON SHADOW
########################################################################
def applyButtonShadow(buttonObject, **shadowCustomization):
    buttonObject.shadow = QGraphicsDropShadowEffect(buttonObject)

    if "blurRadius" in shadowCustomization and int(shadowCustomization['blurRadius']) > 0:
        buttonObject.shadow.setBlurRadius(int(shadowCustomization['blurRadius']))
        buttonObject._shadowAnimation.setEndValue(int(shadowCustomization['blurRadius']))
    else:
        buttonObject.shadow.setBlurRadius(10)

    if "xOffset" in shadowCustomization and int(shadowCustomization['xOffset']) > 0:
        buttonObject.shadow.setXOffset(int(shadowCustomization['xOffset']))
    else:
        buttonObject.shadow.setXOffset(0)

    if "yOffset" in shadowCustomization and int(shadowCustomization['yOffset']) > 0:
        buttonObject.shadow.setYOffset(int(shadowCustomization['yOffset']))
    else:
        buttonObject.shadow.setYOffset(0)

    if "color" in shadowCustomization:
        buttonObject.shadow.setColor(QColor(shadowCustomization['color']))

    if "applyShadowOn" in shadowCustomization and len(str(shadowCustomization['applyShadowOn'])) > 0:
        if shadowCustomization['applyShadowOn'] == "hover":
            buttonObject.applyShadowOn = "hover"
        elif shadowCustomization['applyShadowOn'] == "click":
            buttonObject.applyShadowOn = "click"
        else:
            raise Exception("Unknown event "+str(shadowCustomization['applyShadowOn'])+". Can not apply button shadow. Supported signature 'hover' or 'click'")

        if "animateShadow" in shadowCustomization and shadowCustomization['animateShadow'] == True:
            buttonObject.animateShadow = True
            if "animateShadowDuration" in shadowCustomization and int(shadowCustomization['animateShadowDuration']) > 0:
                buttonObject._shadowAnimation.setDuration(int(shadowCustomization['animateShadowDuration']))
        else:
            buttonObject.animateShadow = False

    else:

        #######################################################################
        ## # Appy shadow to central widget
        ########################################################################
        buttonObject.setGraphicsEffect(buttonObject.shadow)


########################################################################
## APPLY ANIMATION THEME STYLESHEET (IF NO JSON STYLE WAS  FOUND)
########################################################################
def applyAnimationThemeStyle(buttonObject, theme):
    buttonObject.setObjectTheme(theme)

    color1 = buttonObject.color1
    color2 = buttonObject.color2

    applyStylesFromColor(buttonObject, color1, color2)


def applyCustomAnimationThemeStyle(buttonObject, color1, color2):
    if len(color1) > 0 and len(color2) > 0 :
        buttonObject.setObjectCustomTheme(color1, color2)
        color1 = buttonObject.color1
        color2 = buttonObject.color2

        applyStylesFromColor(buttonObject, color1, color2)


    else:
        raise Exception("Please enter valid colors for your custom theme. Supported signature applyCustomAnimationThemeStyle(buttonObject, color1, color2)")

def applyStylesFromColor(buttonObject, color1, color2):
        if buttonObject.defaultStyle is not None:
            qss = buttonObject.defaultStyle
        else:
            qss = ""

        grad = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 {color1}, stop: 0 {color2}, stop: 1.0 {color1});".format(color1=color1.name(), color2=color2.name())

        style = """
            border-top-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.466, stop: 0  """+str(color1.name())+""", stop: 1  """+str(color2.name())+""");
            border-bottom-color: qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop: 0 """+str(color1.name())+""", stop: 1  """+str(color2.name())+""");
            border-right-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop: 0  """+str(color1.name())+""", stop: 1  """+str(color2.name())+""");
            border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop: 0 """+str(color1.name())+""", stop: 1  """+str(color2.name()) +""");

        """

        buttonObject.setStyleSheet(qss + grad + style)

        # buttonObject.setObjectFallBackStyle(qss + grad + style)


########################################################################
## ==> END
########################################################################