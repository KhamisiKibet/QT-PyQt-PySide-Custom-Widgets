########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################

########################################################################
## MODULE UPDATED TO USE QT.PY
########################################################################
from qtpy.QtCore import Qt, QEasingCurve, QPoint, Slot, QParallelAnimationGroup, QPropertyAnimation, QAbstractAnimation, QTimeLine
from qtpy.QtGui import QPainter, QPixmap
from qtpy.QtWidgets import QStackedWidget, QWidget


"""
This is an extension of QStackedWidget which adds transition animation
And Navigation Functions to
your QStackedWidget widgets
You can customize the animations using a JSon file or Python statements
"""


########################################################################
## QStackedWidget Class
########################################################################
class QCustomQStackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(QCustomQStackedWidget, self).__init__(parent)

        ########################################################################
        ## Initialize Default Values
        ########################################################################
        # Fade transition
        self.fadeTransition = False
        # Slide transition
        self.slideTransition = False
        # Default transition direction
        self.transitionDirection = Qt.Vertical
        # Default transition animation time
        self.transitionTime = 500
        # Default fade animation time
        self.fadeTime = 500
        # Default transition animation easing curve
        self.transitionEasingCurve = QEasingCurve.OutBack
        # Default transition animation easing curve
        self.fadeEasingCurve = QEasingCurve.Linear
        # Default current widget index
        self.currentWidget = 0
        # Default next widget index
        self.nextWidget = 0
        # Default widget position
        self._currentWidgetPosition = QPoint(0, 0)
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
    @Slot()
    def slideToPreviousWidget(self):
        currentWidgetIndex = self.currentIndex()
        if currentWidgetIndex > 0:
            self.slideToWidgetIndex(currentWidgetIndex - 1)

    ########################################################################
    ## Function to transition to next widget
    ########################################################################
    @Slot()
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
        if not self.transitionDirection == Qt.Horizontal:
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
        offset = QPoint(offsetX, offsetY)
        self.widget(_nextWidgetIndex).move(nextWidgetPosition - offset)
        self.widget(_nextWidgetIndex).show()
        self.widget(_nextWidgetIndex).raise_()

        anim_group = QParallelAnimationGroup(
            self, finished=self.animationDoneSlot
        )

        for index, start, end in zip(
            (_currentWidgetIndex, _nextWidgetIndex),
            (currentWidgetPosition, nextWidgetPosition - offset),
            (currentWidgetPosition + offset, nextWidgetPosition)
        ):
            animation = QPropertyAnimation(
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
        anim_group.start(QAbstractAnimation.DeleteWhenStopped)

        # Play fade animation
        if self.fadeTransition:
            FadeWidgetTransition(self, self.widget(_currentWidgetIndex), self.widget(_nextWidgetIndex))

    ########################################################################
    ## Function to hide old widget and show new widget after animation is done
    ########################################################################
    @Slot()
    def animationDoneSlot(self):
        self.setCurrentIndex(self.nextWidget)
        self.widget(self.currentWidget).hide()
        self.widget(self.currentWidget).move(self._currentWidgetPosition)
        self.widgetActive = False

    ########################################################################
    ## Function extending the QStackedWidget setCurrentWidget to animate transition
    ########################################################################
    @Slot()
    def setCurrentWidget(self, widget):
        currentIndex = self.currentIndex()
        nextIndex = self.indexOf(widget)
        if self.currentIndex() == self.indexOf(widget):
            return
        if self.slideTransition:
            self.slideToWidgetIndex(nextIndex)

        if self.fadeTransition:
            FadeWidgetTransition(self, self.widget(self.currentIndex()), self.widget(self.indexOf(widget)))
        
            # if not self.slideTransition:
            #     self.setCurrentIndex(0)
            
        if not self.slideTransition and not self.fadeTransition:
            self.setCurrentIndex(nextIndex)

########################################################################
## Fade widget class
########################################################################
class FadeWidgetTransition(QWidget):
    def __init__(self, animationSettings, oldWidget, newWidget):
        QWidget.__init__(self, animationSettings.widget(0))

        self.oldPixmap = QPixmap(oldWidget.size())
        oldWidget.render(self.oldPixmap)
        self.pixmapOpacity = 1

        self.animationSettings = animationSettings
        self.newWidget = newWidget

        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animateOldWidget)
        self.timeline.finished.connect(self.animationFinished)
        self.timeline.setDuration(animationSettings.fadeTime)
        self.timeline.setEasingCurve(animationSettings.fadeEasingCurve)
        self.timeline.start()
        
        self.resize(oldWidget.size())
        self.show()

        if not animationSettings.slideTransition:
            animationSettings.setCurrentIndex(0)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # painter.setOpacity(self.pixmapOpacity)
        try:
            painter.setOpacity(self.pixmapOpacity)
        except Exception:
            self.pixmapOpacity = 1
            # painter.setOpacity(self.pixmapOpacity)

        
        painter.drawPixmap(0, 0, self.oldPixmap)
        painter.end()

    def animateOldWidget(self, value):
        self.pixmapOpacity = 1.0 - value
        self.repaint()

    def animationFinished(self):
        self.close()
        FadeOutWidgetTransition(self.animationSettings, self.animationSettings.widget(0), self.newWidget)

class FadeOutWidgetTransition(QWidget):
    def __init__(self, animationSettings, oldWidget, newWidget):
        QWidget.__init__(self, newWidget)

        self.oldPixmap = QPixmap(oldWidget.size())
        oldWidget.render(self.oldPixmap)
        self.pixmapOpacity = 1

        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animateOldWidget)
        self.timeline.finished.connect(self.animationFinished)
        self.timeline.setDuration(animationSettings.fadeTime)
        self.timeline.setEasingCurve(animationSettings.fadeEasingCurve)
        self.timeline.start()
        
        self.resize(oldWidget.size())
        self.show()

        if not animationSettings.slideTransition:
            nextIndex = animationSettings.indexOf(newWidget)
            animationSettings.setCurrentIndex(nextIndex)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmapOpacity)
        painter.drawPixmap(0, 0, self.oldPixmap)
        painter.end()

    def animateOldWidget(self, value):
        self.pixmapOpacity = 1.0 - value
        self.repaint()

    def animationFinished(self):
        self.close()
    
