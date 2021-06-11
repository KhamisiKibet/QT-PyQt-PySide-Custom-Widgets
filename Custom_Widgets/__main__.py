########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import iconify as ico #pip install iconify
from iconify.qt import QtGui, QtWidgets, QtCore
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
# JSON FOR READING THE JSON STYLESHEET
import json

class QPushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        ########################################################################
        ## CREATE ANIMATION
        ########################################################################
        self._animation = QtCore.QVariantAnimation()
        self._animation.setStartValue(0.00001)
        self._animation.setEndValue(0.9999)
        self._animation.valueChanged.connect(self._animate)
        # self._animation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        # DEAFAULT ANIMATION DURATION
        self._animation.setDuration(500) 

        self._shadowAnimation = QtCore.QVariantAnimation()
        self._shadowAnimation.setStartValue(0)
        self._shadowAnimation.setEndValue(10)
        self._shadowAnimation.valueChanged.connect(self._animateShadow)
        # self._shadowAnimation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

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
            self.color1 = QtGui.QColor(9, 27, 27, 25)
            self.color2 = QtGui.QColor(85, 255, 255, 255)
        elif str(theme) == "2":
            self.color1 = QtGui.QColor(240, 53, 218)
            self.color2 = QtGui.QColor(61, 217, 245)
        elif str(theme) == "3":
            self.color1 = QtGui.QColor("#C0DB50")
            self.color2 = QtGui.QColor("#100E19")
        elif str(theme) == "4":
            self.color1 = QtGui.QColor("#FF16EB")
            self.color2 = QtGui.QColor("#100E19")
        elif str(theme) == "5":
            self.color1 = QtGui.QColor("#FF4200")
            self.color2 = QtGui.QColor("#100E19")
        elif str(theme) == "6":
            self.color1 = QtGui.QColor("#000046")
            self.color2 = QtGui.QColor("#1CB5E0")
        elif str(theme) == "7":
            self.color1 = QtGui.QColor("#EB5757")
            self.color2 = QtGui.QColor("#000000")
        elif str(theme) == "8":
            self.color1 = QtGui.QColor("#FF8235")
            self.color2 = QtGui.QColor("#30E8BF")
        elif str(theme) == "9":
            self.color1 = QtGui.QColor("#20002c")
            self.color2 = QtGui.QColor("#cbb4d4")
        elif str(theme) == "10":
            self.color1 = QtGui.QColor("#C33764")
            self.color2 = QtGui.QColor("#1D2671")
        elif str(theme) == "11":
            self.color1 = QtGui.QColor("#ee0979")
            self.color2 = QtGui.QColor("#ff6a00")
        elif str(theme) == "12":
            self.color1 = QtGui.QColor("#242424")
            self.color2 = QtGui.QColor("#FA0000")
        elif str(theme) == "13":
            self.color1 = QtGui.QColor("#25395f")
            self.color2 = QtGui.QColor("#55ffff")

        else:
            raise Exception("Unknown theme '" +str(theme)+ "'")



    ########################################################################
    ## SET BUTTON THEME
    ########################################################################
    def setObjectCustomTheme(self, color1, color2):
        self.color1 = QtGui.QColor(color1)
        self.color2 = QtGui.QColor(color2)

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
            self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
            self._animation.start()
        # 
        if self.setIconAnimatedOn == "hover":
            if hasattr(self, 'anim'):
                self.anim.start()
        if self.applyShadowOn == "hover":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Forward)
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
            self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
            self._animation.start()
            self._animation.finished.connect(lambda: self.applyDefaultStyle())

        if self.applyShadowOn == "hover":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Backward)
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
            self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
            self._animation.start()
        # 
        if self.setIconAnimatedOn == "click":
            if hasattr(self, 'anim'):
                self.anim.start()
        if self.applyShadowOn == "click":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Forward)
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
            self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
            self._animation.start()
            self._animation.finished.connect(lambda: self.applyDefaultStyle())
        if self.applyShadowOn == "click":
            if self.animateShadow:
                self._shadowAnimation.setDirection(QtCore.QAbstractAnimation.Backward)
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
        # print(self.setIconAnimatedOn, self.clickPosition, self.mousePosition)
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
                        # print("stopping icon animation")
                        self.anim.stop()
                    except Exception as e:
                        # print(e)
                        pass

    ########################################################################
    ## ANIMATE BUTTON BACKGROUND AND BORDER
    ########################################################################
    def _animate(self, value):
        # print(self, value)
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

            # print(self.color2.name())

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
            buttonObject.buttonIcon = ico.Icon(iconCustomization['icon'], color=QtGui.QColor(iconCustomization['color']))

        if "animation" in iconCustomization and len(iconCustomization['animation']) > 0:
            if iconCustomization['animation'] == "spin":
                buttonObject.anim = ico.anim.Spin()
            elif iconCustomization['animation'] == "breathe":
                buttonObject.anim = ico.anim.Breathe()
            elif iconCustomization['animation'] == "breathe and spin" or iconCustomization['animation'] == "spinn and breathe":
                buttonObject.anim = ico.anim.Spin() + ico.anim.Breathe()
            else:
                raise Exception("Unknown value'" +iconCustomization['animation']+ "' for ico.animation(). Supported animations are 'spinn' and 'breathe'")

            buttonObject.buttonIcon = ico.Icon(iconCustomization['icon'], color=QtGui.QColor(iconCustomization['color']), anim=buttonObject.anim)

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
        print("Failed to create the icon, please define the icon image i.e icon = 'icon.image'")


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
## APPLY ANIMATION THEME STYLESHEET (IF NO STYLE WAS JSON FOUND)
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
        # print(buttonObject, color1.name(), color2.name())


########################################################################
## ==> END
########################################################################      


"""
This is an extension of QStackedWidget which adds transition animation 
And Navigation Functions to
your QStackedWidget widgets
You can customize the animations using a JSon file or Python statements
"""
                              

########################################################################
## QStackedWidget Class
########################################################################
class QStackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super(QStackedWidget, self).__init__(parent)

        ########################################################################
        ## Initialize Default Values
        ########################################################################
        # Fade transition
        self.fadeTransition = False
        # Slide transition
        self.slideTransition = False
        # Default transition direction
        self.transitionDirection = QtCore.Qt.Vertical
        # Default transition animation time
        self.transitionTime = 500
        # Default fade animation time
        self.fadeTime = 500
        # Default transition animation easing curve
        self.transitionEasingCurve = QtCore.QEasingCurve.OutBack
        # Default transition animation easing curve
        self.fadeEasingCurve = QtCore.QEasingCurve.Linear
        # Default current widget index
        self.currentWidget = 0
        # Default next widget index
        self.nextWidget = 0
        # Default widget position
        self._currentWidgetPosition = QtCore.QPoint(0, 0)
        # Default boolean for active widget
        self.widgetActive = False
                            

    ########################################################################
    ## Function to update transition direction
    ########################################################################
    def setTransitionDirection(self, direction):
        self.transitionDirection = direction

    ########################################################################
    ## Function to update transition speed
    ########################################################################
    def setTransitionSpeed(self, speed):
        self.transitionTime = speed

    ########################################################################
    ## Function to update fade speed
    ########################################################################
    def setFadeSpeed(self, speed):
        self.fadeTime = speed

    ########################################################################
    ## Function to update transition easing curve
    ########################################################################
    def setTransitionEasingCurve(self, aesingCurve):
        self.transitionEasingCurve = aesingCurve

    ########################################################################
    ## Function to update fade easing curve
    ########################################################################
    def setFadeCurve(self, aesingCurve):
        self.fadeEasingCurve = aesingCurve

    ########################################################################
    ## Function to update fade animation playing state
    ########################################################################
    def setFadeTransition(self, fadeState):
        if isinstance(fadeState, bool):
            self.fadeTransition = fadeState
        else:
            raise Exception("setFadeTransition() only accepts boolean variables")

    ########################################################################
    ## Function to update slide  playing state
    ########################################################################
    def setSlideTransition(self, slideState):
        if isinstance(slideState, bool):
            self.slideTransition = slideState
        else:
            raise Exception("setSlideTransition() only accepts boolean variables")

    ########################################################################
    ## Function to transition to previous widget
    ########################################################################
    @QtCore.Slot()
    def slideToPreviousWidget(self):
        currentWidgetIndex = self.currentIndex()
        if currentWidgetIndex > 0:
            self.slideToWidgetIndex(currentWidgetIndex - 1)

    ########################################################################
    ## Function to transition to next widget
    ########################################################################
    @QtCore.Slot()
    def slideToNextWidget(self):
        currentWidgetIndex = self.currentIndex()
        if currentWidgetIndex < (self.count() - 1):
            self.slideToWidgetIndex(currentWidgetIndex + 1)


    ########################################################################
    ## Function to transition to a given widget index
    ########################################################################
    def slideToWidgetIndex(self, index):
        if index > (self.count() - 1):
            index = index % self.count()
        elif index < 0:
            index = (index + self.count()) % self.count()
        if self.slideTransition:
            self.slideToWidget(self.widget(index))
        else:
            self.setCurrentIndex(index)

    ########################################################################
    ## Function to transition to a given widget
    ########################################################################
    def slideToWidget(self, newWidget):
        # If the widget is active, exit the function
        if self.widgetActive:
            return

        # Update widget active bool
        self.widgetActive = True

        # Get current and next widget index
        _currentWidgetIndex = self.currentIndex()
        _nextWidgetIndex = self.indexOf(newWidget)

        # If current widget index is equal to next widget index, exit function
        if _currentWidgetIndex == _nextWidgetIndex:
            self.widgetActive = False
            return

        # Get X and Y position of QStackedWidget
        offsetX, offsetY = self.frameRect().width(), self.frameRect().height()
        # Set the next widget geometry
        self.widget(_nextWidgetIndex).setGeometry(self.frameRect())

        # Set left right(horizontal) or up down(vertical) transition
        if not self.transitionDirection == QtCore.Qt.Horizontal:
            if _currentWidgetIndex < _nextWidgetIndex:
                # Down up transition
                offsetX, offsetY = 0, -offsetY
            else:
                # Up down transition
                offsetX = 0
        else:
            # Right left transition
            if _currentWidgetIndex < _nextWidgetIndex:
                offsetX, offsetY = -offsetX, 0
            else:
                # Left right transition
                offsetY = 0

        nextWidgetPosition = self.widget(_nextWidgetIndex).pos()
        currentWidgetPosition = self.widget(_currentWidgetIndex).pos()
        self._currentWidgetPosition = currentWidgetPosition

        # Animate transition
        offset = QtCore.QPoint(offsetX, offsetY)
        self.widget(_nextWidgetIndex).move(nextWidgetPosition - offset)
        self.widget(_nextWidgetIndex).show()
        self.widget(_nextWidgetIndex).raise_()

        anim_group = QtCore.QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        for index, start, end in zip(
            (_currentWidgetIndex, _nextWidgetIndex), 
            (currentWidgetPosition, nextWidgetPosition - offset), 
            (currentWidgetPosition + offset, nextWidgetPosition)
        ):
            animation = QtCore.QPropertyAnimation(
                self.widget(index),
                b"pos",
                duration=self.transitionTime,
                easingCurve=self.transitionEasingCurve,
                startValue=start,
                endValue=end,
            )
            anim_group.addAnimation(animation)

        self.nextWidget = _nextWidgetIndex
        self.currentWidget = _currentWidgetIndex

        self.widgetActive = True
        anim_group.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

        # Play fade animation
        if self.fadeTransition:
            FadeWidgetTransition(self, self.widget(_currentWidgetIndex), self.widget(_nextWidgetIndex))

    ########################################################################
    ## Function to hide old widget and show new widget after animation is done
    ########################################################################
    @QtCore.Slot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.nextWidget)
        self.widget(self.currentWidget).hide()
        self.widget(self.currentWidget).move(self._currentWidgetPosition)
        self.widgetActive = False

    ########################################################################
    ## Function extending the QStackedWidget setCurrentWidget to animate transition
    ########################################################################
    @QtCore.Slot()
    def setCurrentWidget(self, widget):
        currentIndex = self.currentIndex()
        nextIndex = self.indexOf(widget)
        # print(currentIndex, nextIndex)
        if self.currentIndex() == self.indexOf(widget):
            return
        if self.slideTransition:
            self.slideToWidgetIndex(nextIndex)

        if self.fadeTransition:
            self.fader_widget = FadeWidgetTransition(self, self.widget(self.currentIndex()), self.widget(self.indexOf(widget)))
            if not self.slideTransition:
                self.setCurrentIndex(nextIndex)

        if not self.slideTransition and not self.fadeTransition:
            self.setCurrentIndex(nextIndex)


########################################################################
## Fade widget class
########################################################################
class FadeWidgetTransition(QWidget):
    def __init__(self, animationSettings, oldWidget, newWidget):
    
        QWidget.__init__(self, newWidget)
        
        self.oldPixmap = QPixmap(newWidget.size())
        oldWidget.render(self.oldPixmap)
        self.pixmapOpacity = 1.0
        
        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(animationSettings.fadeTime)
        self.timeline.setEasingCurve(animationSettings.fadeEasingCurve)
        self.timeline.start()
        
        self.resize(newWidget.size())
        self.show()
    
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmapOpacity)
        painter.drawPixmap(0, 0, self.oldPixmap)
        painter.end()
    
    def animate(self, value):    
        self.pixmapOpacity = 1.0 - value
        self.repaint()


    
########################################################################
## Read JSon stylesheet
########################################################################
def loadJsonStyle(self):
    file = open('style.json',)
    data = json.load(file)

    buttonObject.wasFound = False
    buttonObject.wasThemed = False

    if "buttons" in data:
        for button in data['buttons']:
            # print(json.dumps(button["fallBackStyle"]))

            if "name" in button and len(button["name"]) > 0:
                if buttonObject.objectName() == button["name"]:
                    if "theme" in button and len(button["theme"]) > 0:
                        buttonObject.setObjectTheme(button["theme"])

                    if "customTheme" in button and len(button["customTheme"]) > 0:
                        for x in button["customTheme"]:
                            # print(x)
                            if len(x["color1"]) > 0 and len(x["color1"]) > 0 :
                                buttonObject.setObjectCustomTheme(x["color1"], x["color2"])

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

                    # print(fallBackStyle)

                    defaultStyle = ""
                    if "defaultStyle" in button:
                        for x in button["defaultStyle"]:
                            defaultStyle += x

                    # print(fallBackStyle)

                    buttonObject.wasThemed = True

                    if len(fallBackStyle) > 0:
                        buttonObject.setObjectFallBackStyle(fallBackStyle)

                    if len(defaultStyle) > 0:
                        buttonObject.setObjectDefaultStyle(defaultStyle)

                    if len(fallBackStyle) > 0:
                        buttonObject.setStyleSheet(defaultStyle + fallBackStyle)
                    elif "theme" in button and len(button["theme"]) > 0:
                        # 
                        applyAnimationThemeStyle(buttonObject, button["theme"])
                    elif "customTheme" in button and len(button["customTheme"]) > 0:
                        for x in button["customTheme"]:
                            if len(x["color1"]) > 0 and len(x["color1"]) > 0 :
                                applyCustomAnimationThemeStyle(buttonObject, x["color1"], x["color2"])
                    else: 
                        buttonObject.wasThemed = False


                    ########################################################################
                    ## ICONIFY STYLESHEET
                    ########################################################################
                    if "iconify" in button:                    
                        for icon in button['iconify']:
                            if "icon" in icon and len(icon['icon']) > 0:
                                btnIcon = icon['icon']
                                if "color" in icon and len(icon['color']) > 0:
                                    color = icon['color']
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


                    ########################################################################
                    ## BUTTON SHADOW STYLESHEET
                    ########################################################################
                    if "shadow" in button:  
                        for shadow in button["shadow"]:
                            if "color" in shadow and len(str(shadow['color'])) > 0:
                                shadowColor = shadow['color']
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

    if "QStackedWidget" in data:
        for stackedWidget in data['QStackedWidget']:
            if "name" in stackedWidget and len(str(stackedWidget["name"])) > 0:
                if hasattr(self, str(stackedWidget["name"])):
                    widget = getattr(self, str(stackedWidget["name"]))                    
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
                                    if hasattr(self, str(navigation["nextPage"])):
                                        button = getattr(self, str(navigation["nextPage"]))
                                        button.clicked.connect(lambda: widget.slideToNextWidget())
                                    else:
                                        print("No button found")

                                if "previousPage" in navigation:
                                    if hasattr(self, str(navigation["previousPage"])):
                                        button = getattr(self, str(navigation["previousPage"]))
                                        button.clicked.connect(lambda: widget.slideToPreviousWidget())
                                    else:
                                        print("No button found")

                                if "navigationButtons" in navigation:
                                    for navigationButton in navigation["navigationButtons"]:
                                        for button in navigationButton:
                                            widgetPage = navigationButton[button]
                                            if not hasattr(self, str(widgetPage)):
                                                raise Exception("Unknown widget '" +str(widgetPage)+ "'. Please check your JSon file")
                                            if not hasattr(self, str(button)):
                                                raise Exception("Unknown button '" +str(button)+ "'. Please check your JSon file")

                                            pushBtn = getattr(self, str(button))
                                            widgetPg = getattr(self, str(widgetPage))
                                            navigationButtons(widget, pushBtn, widgetPg)

########################################################################
## 
########################################################################

########################################################################
## 
########################################################################
def navigationButtons(stackedWidget, pushButton, widgetPage):    
    pushButton.clicked.connect(lambda: stackedWidget.setCurrentWidget(widgetPage))
########################################################################
##
########################################################################

########################################################################
## 
########################################################################
def returnAnimationEasingCurve(easingCurveName):
    if len(str(easingCurveName)) > 0:
        if str(easingCurveName) == "OutQuad":               
            return QtCore.QEasingCurve.OutQuad
        elif str(easingCurveName) == "Linear":              
            return QtCore.QEasingCurve.Linear
        elif str(easingCurveName) == "InQuad":              
            return QtCore.QEasingCurve.InQuad
        elif str(easingCurveName) == "InOutQuad":           
            return QtCore.QEasingCurve.InOutQuad
        elif str(easingCurveName) == "OutInQuad":           
            return QtCore.QEasingCurve.OutInQuad
        elif str(easingCurveName) == "InCubic":           
            return QtCore.QEasingCurve.InCubic
        elif str(easingCurveName) == "OutCubic":           
            return QtCore.QEasingCurve.OutCubic
        elif str(easingCurveName) == "InOutCubic":          
            return QtCore.QEasingCurve.InOutCubic
        elif str(easingCurveName) == "OutInCubic":          
            return QtCore.QEasingCurve.OutInCubic
        elif str(easingCurveName) == "InQuart":          
            return QtCore.QEasingCurve.InQuart
        elif str(easingCurveName) == "OutQuart":          
            return QtCore.QEasingCurve.OutQuart
        elif str(easingCurveName) == "InOutQuart":          
            return QtCore.QEasingCurve.InOutQuart
        elif str(easingCurveName) == "OutInQuart":          
            return QtCore.QEasingCurve.OutInQuart
        elif str(easingCurveName) == "InQuint":          
            return QtCore.QEasingCurve.InQuint
        elif str(easingCurveName) == "OutQuint":          
            return QtCore.QEasingCurve.OutQuint
        elif str(easingCurveName) == "InOutQuint":          
            return QtCore.QEasingCurve.InOutQuint
        elif str(easingCurveName) == "InSine":          
            return QtCore.QEasingCurve.InSine
        elif str(easingCurveName) == "OutSine":          
            return QtCore.QEasingCurve.OutSine
        elif str(easingCurveName) == "InOutSine":          
            return QtCore.QEasingCurve.InOutSine
        elif str(easingCurveName) == "OutInSine":          
            return QtCore.QEasingCurve.OutInSine
        elif str(easingCurveName) == "InExpo":          
            return QtCore.QEasingCurve.InExpo
        elif str(easingCurveName) == "OutExpo":          
            return QtCore.QEasingCurve.OutExpo
        elif str(easingCurveName) == "InOutExpo":          
            return QtCore.QEasingCurve.InOutExpo
        elif str(easingCurveName) == "OutInExpo":          
            return QtCore.QEasingCurve.OutInExpo
        elif str(easingCurveName) == "InCirc":          
            return QtCore.QEasingCurve.InCirc
        elif str(easingCurveName) == "OutCirc":          
            return QtCore.QEasingCurve.OutCirc
        elif str(easingCurveName) == "InOutCirc":          
            return QtCore.QEasingCurve.InOutCirc
        elif str(easingCurveName) == "OutInCirc":          
            return QtCore.QEasingCurve.OutInCirc
        elif str(easingCurveName) == "InElastic":          
            return QtCore.QEasingCurve.InElastic
        elif str(easingCurveName) == "OutElastic":          
            return QtCore.QEasingCurve.OutElastic
        elif str(easingCurveName) == "InOutElastic":        
            return QtCore.QEasingCurve.InOutElastic
        elif str(easingCurveName) == "OutInElastic":        
            return QtCore.QEasingCurve.OutInElastic
        elif str(easingCurveName) == "InBack":        
            return QtCore.QEasingCurve.InBack
        elif str(easingCurveName) == "OutBack":        
            return QtCore.QEasingCurve.OutBack
        elif str(easingCurveName) == "InOutBack":        
            return QtCore.QEasingCurve.InOutBack
        elif str(easingCurveName) == "OutInBack":        
            return QtCore.QEasingCurve.OutInBack
        elif str(easingCurveName) == "InBounce":        
            return QtCore.QEasingCurve.InBounce
        elif str(easingCurveName) == "OutBounce":        
            return QtCore.QEasingCurve.OutBounce
        elif str(easingCurveName) == "InOutBounce":        
            return QtCore.QEasingCurve.InOutBounce
        elif str(easingCurveName) == "OutInBounce":        
            return QtCore.QEasingCurve.OutInBounce
        else:
            raise Exception("Unknown value'" +easingCurveName+ "' for setEasingCurve() on ", animation)
########################################################################
## 
########################################################################

########################################################################
## 
########################################################################
def returnQtDirection(direction):
    if len(str(direction)) > 0:
        if str(direction) == "horizontal":
            return QtCore.Qt.Horizontal
        elif str(direction) == "vertical":
            return QtCore.Qt.Vertical
        else:
            raise Exception("Unknown direction name given ("+direction+"), please use Vertical or Horizontal direction")

    else:
        raise Exception("Empty direction name given, please use Vertical or Horizontal direction")                                    

########################################################################
## END
########################################################################     

########################################################################
## FORM PROGRESS INDICATOR
########################################################################    
class FormProgressIndicator(QWidget):
    def __init__(self, parent=None):
        super(FormProgressIndicator, self).__init__(parent)
        # DEFAULT VALUES
        # Black font color
        self.color = "#000"
        # Blue fill color
        self.fillColor = "#00a4bd"
        # Success color
        self.successFillColor = "#00a4bd"
        # Warning color
        self.warningFillColor = "#ffa500"
        # Error color
        self.errorFillColor = "#ff0000"
        # Progress steps
        self.formProgressCount = 5
        # Progress width
        self.formProgressWidth = 500
        # Progress width
        self.formProgressDefaultWidth = self.formProgressWidth
        # Progress height
        self.formProgressHeight = 30
        # Animation 
        self.formProgressAnimation = QtCore.QVariantAnimation()
        self.formProgressAnimation.valueChanged.connect(self.updateFormProgress)
        self.formProgressAnimation.setEasingCurve(QtCore.QEasingCurve.OutQuad)

        # DEAFAULT ANIMATION DURATION
        self.formProgressAnimation.setDuration(500)
        # self.formProgressAnimation.setDirection(QtCore.QAbstractAnimation.Forward)

        self.createFormProgressIndicator()
        # print(self.createFormProgressIndicator())

    def selectFormProgressIndicatorTheme(self, themeNumber):
        if themeNumber == 1:
            fillColor = "qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))"
            warningFillColor = "qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.5, fx:0.504878, fy:0.51, stop:0.731707 rgba(0, 0, 0, 0), stop:1 rgba(255, 102, 0, 255))"
            errorFillColor = "qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.5, fx:0.504878, fy:0.51, stop:0.731707 rgba(0, 0, 0, 0), stop:1 rgba(255, 0, 0, 255))"
            successFillColor = "qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.5, fx:0.504878, fy:0.51, stop:0.731707 rgba(0, 0, 0, 0), stop:1 rgba(69, 208, 208, 255))"
        elif themeNumber == 2:
            fillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(9, 27, 27, 255), stop:1 rgba(85, 255, 255, 255))"
            warningFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(85, 255, 255, 255))"
            errorFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(85, 255, 255, 255))"
            successFillColor = fillColor
        elif themeNumber == 3:
            self.color = "#fff"
            fillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(38, 59, 99, 255), stop:1 rgba(25, 28, 30, 255))"
            warningFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 150, 3, 255), stop:1 rgba(25, 28, 30, 255))"
            errorFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(25, 28, 30, 255))"
            successFillColor = fillColor
        elif themeNumber == 4:
            self.color = "#fff"
            fillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(38, 59, 99, 255), stop:1 rgba(0, 164, 189, 255))"
            warningFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 143, 30, 255), stop:1 rgba(0, 164, 189, 255))"
            errorFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 164, 189, 255))"
            successFillColor = fillColor
        elif themeNumber == 5:
            self.color = "#000"
            fillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 164, 189, 255))"
            warningFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 85, 0, 255))"
            errorFillColor = "qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 42, 42, 255))"
            successFillColor = fillColor

            


        self.fillColor = fillColor
        self.warningFillColor = warningFillColor
        self.errorFillColor = errorFillColor
        self.successFillColor = successFillColor
            

    def setStepStatus(self, **stepStatus):
        for x in stepStatus:
            if hasattr(self, str(x)):
                if isinstance(stepStatus[x], bool):
                    setattr(self, str(x), stepStatus[x])
                else:
                    raise Exception("setStepStatus() only accepts boolean variables, "+stepStatus[x]+" given instead")
        if "step" in stepStatus and "status" in stepStatus and "value" in stepStatus:
            
            if hasattr(self, "step_"+str(stepStatus["step"])+"_"+str(stepStatus["status"])):
                if isinstance(stepStatus["value"], bool):
                    setattr(self, "step_"+str(stepStatus["step"])+"_"+str(stepStatus["status"]), stepStatus["value"])
                else:
                    raise Exception("setStepStatus() only accepts boolean variables, "+stepStatus["value"]+" given instead")
                
        

    def updateFormProgressIndicator(self, **values):
        if "color" in values and len(str(values['color'])) > 0:
            self.color = values['color']

        if "fillColor" in values and len(str(values['fillColor'])) > 0:
            self.fillColor = values['fillColor']

        if "warningFillColor" in values and len(str(values['warningFillColor'])) > 0:
            self.warningFillColor = values['warningFillColor']

        if "errorFillColor" in values and len(str(values['errorFillColor'])) > 0:
            self.errorFillColor = values['errorFillColor']

        if "successFillColor" in values and len(str(values['successFillColor'])) > 0:
            self.successFillColor = values['successFillColor']

        if "formProgressCount" in values and int(values['formProgressCount']) > 0:
            if values['formProgressCount'] != self.formProgressCount:
                self.formProgressCount = values['formProgressCount']

                for x in self.progressIndicatorFront.findChildren(QLabel):
                    x.setParent(None)
                    self.progressIndicatorFrontGridLayout.removeWidget(x)

                for x in range(1, self.formProgressCount + 1):
                    newLabel = QLabel(self.progressIndicatorFront)
                    newLabel.setObjectName(u"_"+str(x))
                    newLabel.setMinimumSize(QSize((self.formProgressHeight / 3) * 2, (self.formProgressHeight / 3) * 2))
                    newLabel.setMaximumSize(QSize((self.formProgressHeight / 3) * 2, (self.formProgressHeight / 3) * 2))
                    newLabel.setAlignment(Qt.AlignCenter)
                    newLabel.setText(str(x))
                    newLabel.setStyleSheet("""
                            background-color: """+self.fillColor+""";
                            color: """+self.color+""";
                            border-radius: """+str(self.formProgressHeight / 3)+""";

                        """)

                    setattr(self, "_"+str(x), newLabel)
                    setattr(self, "step_"+str(x)+"_error", False)
                    setattr(self, "step_"+str(x)+"_warning", False)
                    setattr(self, "step_"+str(x)+"_success", False)


                    self.progressIndicatorFrontGridLayout.addWidget(newLabel, 0, (x-1), 1, 1)

        if "formProgressAnimationDuration" in values and int(values['formProgressAnimationDuration']) > 0:
            self.formProgressAnimation.setDuration(values['formProgressAnimationDuration'])

        if "formProgressAnimationEasingCurve" in values and len(str(values['formProgressAnimationEasingCurve'])) > 0:
            self.formProgressAnimation.setEasingCurve(returnAnimationEasingCurve(str(values['formProgressAnimationEasingCurve'])))

        if "height" in values and int(values['height']) > 0:
            self.formProgressHeight = int(values['height'])
            self.setMaximumSize(QSize(self.formProgressDefaultWidth, self.formProgressHeight))
            self.setMinimumSize(QSize(self.formProgressDefaultWidth, self.formProgressHeight))

        if "width" in values and int(values['width']) > 0:
            self.formProgressWidth = int(values['width'])
            self.formProgressDefaultWidth = int(values['width'])
            self.setMaximumSize(QSize(self.formProgressDefaultWidth, self.formProgressHeight))
            self.setMinimumSize(QSize(self.formProgressDefaultWidth, self.formProgressHeight))

        if "startPercentage" in values:
            if int(values['startPercentage']) <= 100 and int(values['startPercentage']) >= 0:
                self.formProgressWidth = int(values['startPercentage']) * self.formProgressDefaultWidth / 100
            else:
                raise Exception("Starting percentage should be between 0 to 100")

        self.updateFormProgress(self.formProgressWidth)
        # self.update()



    def animateFormProgress(self, percentage):
        # CURRENT WIDTH PERCENTAGE
        currentWidth = self.progressIndicatorBg.width()
        newWidth = (percentage/100) * self.formProgressDefaultWidth

        self.formProgressAnimation.setStartValue(int(currentWidth))
        self.formProgressAnimation.setEndValue(int(newWidth))
        self.formProgressAnimation.start()

    def updateFormProgress(self, value):
        
        self.formProgressWidth = value
        self.progressIndicatorBg.setMinimumSize(QSize(value, (self.formProgressHeight / 3)))
        self.progressIndicatorBg.setMaximumSize(QSize(value, (self.formProgressHeight / 3)))
        self.progressIndicatorBg.setStyleSheet(u"#progressIndicatorBg{background-color: "+self.fillColor+"; border-radius: "+str(int(self.formProgressHeight / 6))+";}")


        # 
        if self.formProgressDefaultWidth < 1:
           self.formProgressDefaultWidth = self.width() 

        percentageValue = (value/self.formProgressDefaultWidth ) * 100
        stepsPercentage = 100/self.formProgressCount 
        fillEl = int(percentageValue / stepsPercentage)  

        for x in range(1, fillEl + 1):
            if hasattr(self, 'step_'+str(x)+"_error") and getattr(self, 'step_'+str(x)+"_error"):
                if hasattr(self, '_'+str(x)):
                    getattr(self, '_'+str(x)).setStyleSheet("""
                        color: """+self.color+""";
                        background-color: """+self.errorFillColor+""";
                        border-radius: """+str(int(self.formProgressHeight / 3))+""";

                    """)
                    getattr(self, '_'+str(x)).setText(u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"> ✘ </span><span style=\" font-weight:600; vertical-align:super;\"> "+str(x)+" </span></p></body></html>")
                    getattr(self, '_'+str(x)).setToolTip(u"Error!")
                
            elif hasattr(self, 'step_'+str(x)+"_warning") and getattr(self, 'step_'+str(x)+"_warning"):
                if hasattr(self, '_'+str(x)):
                    # print(x, getattr(self, '_'+str(x)))
                    getattr(self, '_'+str(x)).setStyleSheet("""
                        color: """+self.color+""";
                        background-color: """+self.warningFillColor+""";
                        border-radius: """+str(int(self.formProgressHeight / 3))+""";

                    """)
                    getattr(self, '_'+str(x)).setText(u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"> ! </span><span style=\" font-weight:600; vertical-align:super;\"> "+str(x)+" </span></p></body></html>")
                    getattr(self, '_'+str(x)).setToolTip(u"Warning!")

            elif hasattr(self, 'step_'+str(x)+"_success") and getattr(self, 'step_'+str(x)+"_success"):
                if hasattr(self, '_'+str(x)):
                    # print(x, getattr(self, '_'+str(x)))
                    getattr(self, '_'+str(x)).setStyleSheet("""
                        color: """+self.color+""";
                        background-color: """+self.successFillColor+""";
                        border-radius: """+str(int(self.formProgressHeight / 3))+""";

                    """)
                    getattr(self, '_'+str(x)).setText(u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"> ✔ </span><span style=\" font-weight:600; vertical-align:super;\"> "+str(x)+" </span></p></body></html>")
                    getattr(self, '_'+str(x)).setToolTip(u"Success!")

                                      
            else:
                if hasattr(self, '_'+str(x)):
                    getattr(self, '_'+str(x)).setStyleSheet("""
                        color: """+self.color+""";
                        background-color: """+self.fillColor+""";
                        border-radius: """+str(int(self.formProgressHeight / 3))+""";

                    """)
                    getattr(self, '_'+str(x)).setText(str(x))
                    getattr(self, '_'+str(x)).setToolTip(u"Step "+str(x))

        remainingEl = self.formProgressCount - fillEl

        if remainingEl > 0:
            for x in range(fillEl+1, self.formProgressCount + 1):
                if hasattr(self, 'step_'+str(x)+"_error") and not getattr(self, 'step_'+str(x)+"_error") and hasattr(self, 'step_'+str(x)+"_warning") and not getattr(self, 'step_'+str(x)+"_warning"):
                    if hasattr(self, '_'+str(x)):
                        getattr(self, '_'+str(x)).setStyleSheet("""
                            color: """+self.color+""";
                            background-color: transparent;
                            border-radius: """+str(int(self.formProgressHeight / 3))+""";

                        """)



    def createFormProgressIndicator(self):
        self.progressIndicator = QFrame(self)
        self.progressIndicator.setObjectName(u"progressIndicator")
        self.progressIndicator.setFrameShape(QFrame.StyledPanel)
        self.progressIndicator.setFrameShadow(QFrame.Raised)
        self.progressIndicatorBg = QFrame(self.progressIndicator)
        self.progressIndicatorBg.setObjectName(u"progressIndicatorBg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressIndicatorBg.sizePolicy().hasHeightForWidth())
        self.progressIndicatorBg.setSizePolicy(sizePolicy1)
        self.progressIndicatorBg.setFrameShape(QFrame.StyledPanel)
        self.progressIndicatorBg.setFrameShadow(QFrame.Raised)
        self.progressIndicatorFront = QFrame(self.progressIndicator)
        self.progressIndicatorFront.setObjectName(u"progressIndicatorFront")
        
        self.progressIndicatorFront.setFrameShape(QFrame.StyledPanel)
        self.progressIndicatorFront.setFrameShadow(QFrame.Raised)
        self.progressIndicatorFrontGridLayout = QGridLayout(self.progressIndicatorFront)
        self.progressIndicatorFrontGridLayout.setSpacing(0)
        self.progressIndicatorFrontGridLayout.setObjectName(u"progressIndicatorFrontGridLayout")
        self.progressIndicatorFrontGridLayout.setContentsMargins(0, 0, 0, 0)

        for x in range(1, self.formProgressCount + 1):
            newLabel = QLabel(self.progressIndicatorFront)
            newLabel.setObjectName(u"_"+str(x))
            newLabel.setMinimumSize(QSize(int(self.formProgressHeight / 3) * 2, int(self.formProgressHeight / 3) * 2))
            newLabel.setMaximumSize(QSize(int(self.formProgressHeight / 3) * 2, int(self.formProgressHeight / 3) * 2))
            newLabel.setAlignment(Qt.AlignCenter)
            newLabel.setText(str(x))
            newLabel.setStyleSheet("""
                    color: """+self.color+""";
                    background-color: transparent;
                    border-radius: """+str(int(self.formProgressHeight / 3))+""";

                """)

            setattr(self, "_"+str(x), newLabel)
            setattr(self, "step_"+str(x)+"_error", False)
            setattr(self, "step_"+str(x)+"_warning", False)
            setattr(self, "step_"+str(x)+"_success", False)


            self.progressIndicatorFrontGridLayout.addWidget(newLabel, 0, (x-1), 1, 1)

        
        self.progressIndicatorVerticalLayout = QVBoxLayout(self)
        self.progressIndicatorVerticalLayout.setObjectName(u"progressIndicatorVerticalLayout")
        self.progressIndicatorVerticalLayout.setSpacing(0)
        self.progressIndicatorVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressIndicatorVerticalLayout.addWidget(self.progressIndicator)

        return self.progressIndicator


    def paintEvent(self, event: QPaintEvent):
        self.progressIndicatorBg.setMinimumSize(QSize(self.formProgressWidth, int(self.formProgressHeight / 3)))
        self.progressIndicatorBg.setMaximumSize(QSize(self.formProgressWidth, int(self.formProgressHeight / 3)))
        if self.formProgressDefaultWidth < 1:
            self.formProgressDefaultWidth = self.width() 
        
        self.progressIndicatorFront.setMinimumSize(QSize(self.formProgressDefaultWidth, self.formProgressHeight))


        self.progressIndicatorBg.setGeometry(QRect(0, int(self.formProgressHeight / 3), self.formProgressWidth, int(self.formProgressHeight / 3)))

        self.progressIndicatorFront.setGeometry(QRect(0, 0, self.formProgressWidth, int(self.formProgressHeight / 3)))

        for x in self.progressIndicatorFront.findChildren(QLabel):
            x.setMinimumSize(QSize(int(self.formProgressHeight / 3) * 2, int(self.formProgressHeight / 3) * 2))
            x.setMaximumSize(QSize(int(self.formProgressHeight / 3) * 2, int(self.formProgressHeight / 3) * 2))

        self.progressIndicator.setMinimumSize(QSize(self.formProgressDefaultWidth, self.formProgressHeight))
        # self.progressIndicator.setMaximumSize(QSize(self.width(), self.formProgressHeight))
        self.progressIndicator.setStyleSheet(u"background-color: transparent; padding: 0;")

        self.progressIndicatorBg.setStyleSheet(u"background-color: "+self.fillColor+"; border-radius: "+str(int(self.formProgressHeight / 6)))
########################################################################
## END
######################################################################## 

if __name__=="__main__":
    print("Import to your main py file")
        

########################################################################
## END
########################################################################                             
