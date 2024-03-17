########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os

########################################################################
## MODULE UPDATED TO USE QT.PY
########################################################################
from qtpy.QtCore import QVariantAnimation, QEasingCurve, QSize, QRect, Qt
from qtpy.QtGui import QPaintEvent
from qtpy.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QSizePolicy, QGridLayout
# from qtpy import  QtCore

from Custom_Widgets.QPropertyAnimation import returnAnimationEasingCurve

import warnings

########################################################################
## FORM PROGRESS INDICATOR
########################################################################
class QCustomProgressIndicator(QWidget):
    def __init__(self, parent=None):
        super(QCustomProgressIndicator, self).__init__(parent)
        # Try to add layout if does not exist
        try:
            self.progressIndicatorLayout = QVBoxLayout(self)
            self.progressIndicatorLayout.setSpacing(0)
            self.progressIndicatorLayout.setContentsMargins(0, 0, 0, 0)
        except Exception:
            pass 
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
        self.formProgressAnimation = QVariantAnimation()
        self.formProgressAnimation.valueChanged.connect(self.updateFormProgress)
        self.formProgressAnimation.setEasingCurve(QEasingCurve.OutQuad)

        # DEAFAULT ANIMATION DURATION
        self.formProgressAnimation.setDuration(500)
        # self.formProgressAnimation.setDirection(QtCore.QAbstractAnimation.Forward)

        self.createFormProgressIndicator()

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
        else:
            raise Exception("Error: QCustomProgressIndicator theme number ranges from 1 to 5, "+str(themeNumber)+" was passed instead.")




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
                    getattr(self, '_'+str(x)).setStyleSheet("""
                        color: """+self.color+""";
                        background-color: """+self.warningFillColor+""";
                        border-radius: """+str(int(self.formProgressHeight / 3))+""";

                    """)
                    getattr(self, '_'+str(x)).setText(u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"> ! </span><span style=\" font-weight:600; vertical-align:super;\"> "+str(x)+" </span></p></body></html>")
                    getattr(self, '_'+str(x)).setToolTip(u"Warning!")

            elif hasattr(self, 'step_'+str(x)+"_success") and getattr(self, 'step_'+str(x)+"_success"):
                if hasattr(self, '_'+str(x)):
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
        self.progressIndicator.setFrameShape(QFrame.StyledPanel)
        self.progressIndicator.setFrameShadow(QFrame.Raised)
        self.progressIndicatorBg = QFrame(self.progressIndicator)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressIndicatorBg.sizePolicy().hasHeightForWidth())
        self.progressIndicatorBg.setSizePolicy(sizePolicy1)
        self.progressIndicatorBg.setFrameShape(QFrame.StyledPanel)
        self.progressIndicatorBg.setFrameShadow(QFrame.Raised)
        self.progressIndicatorFront = QFrame(self.progressIndicator)

        self.progressIndicatorFront.setFrameShape(QFrame.StyledPanel)
        self.progressIndicatorFront.setFrameShadow(QFrame.Raised)
        self.progressIndicatorFrontGridLayout = QGridLayout(self.progressIndicatorFront)
        self.progressIndicatorFrontGridLayout.setSpacing(0)
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


        try:
            self.progressIndicatorVerticalLayout = QVBoxLayout(self.progressIndicator)
            self.progressIndicatorVerticalLayout.setSpacing(0)
            self.progressIndicatorVerticalLayout.setContentsMargins(0, 0, 0, 0)
            # self.progressIndicatorVerticalLayout.addWidget(self.progressIndicator)
            return self.progressIndicatorVerticalLayout
        except Exception:
            return self.progressIndicator

        # return self.progressIndicator


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

class Test:
    def main(self):
        warnings.warn(
            "To test the custom widgets please check the examples folder on github.\n"
            "Deprecated imports. Please update your import statements:\n"
            "For more information, refer to the documentation"
            "https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets"
            "or contact support."
        )

########################################################################
## END
########################################################################