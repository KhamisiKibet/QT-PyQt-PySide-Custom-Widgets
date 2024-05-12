# ///////////////////////////////////////////////////////////////
#
# Copyright 2021 by Parham Oyan and Oleg Frolov
# All rights reserved.
#
# ///////////////////////////////////////////////////////////////
# Edits and improvements made by Khamisi Kibet
# QT GUI BY SPINN TV(YOUTUBE)

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

class RoundedRect:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class QCustom3CirclesLoader(QFrame):
    def __init__(
            self, 
            parent=None,
            color=QColor("#333333"),
            penWidth=20,
            animationDuration=400
            ):
        QFrame.__init__(self, parent=parent)
        
        self.setFrameShape(QFrame.NoFrame)
        self.setFixedSize(140, 140)

        self.color = color
        self.penWidth = penWidth
        self.animationDuration = animationDuration

        self.initRects()
        
        self.startAnimations()
    
    def initRects(self):
        x = self.penWidth/2
        self.rectsList = [
            RoundedRect(x, x, 40, 40),
            RoundedRect(x+80, x, 40, 40),
            RoundedRect(x, x+80, 40, 40)
        ]
    
    def getVariantAnimation(self):
        animation = QVariantAnimation(self)
        animation.setDuration(self.animationDuration)
        animation.setEasingCurve(QEasingCurve.InOutSine)
        return animation

    # ANIMATION INITALIZER METHODS ==============================================================
    
    def initMoveDownAnimation(self):
        self.moveDownGP = QSequentialAnimationGroup(self)

        animation = self.getVariantAnimation()
        animation.setStartValue(40)
        animation.setEndValue(120)
        animation.valueChanged.connect(self.moveDownUpdateH)
        self.moveDownGP.addAnimation(animation)

        animation = self.getVariantAnimation()
        animation.setStartValue(10)
        animation.setEndValue(90)
        animation.valueChanged.connect(self.moveDownUpdateY)
        self.moveDownGP.addAnimation(animation)
    
    def initMoveRightAnimation(self):
        self.moveRightGP = QSequentialAnimationGroup(self)

        animation = self.getVariantAnimation()
        animation.setStartValue(40)
        animation.setEndValue(120)
        animation.valueChanged.connect(self.moveRightUpdateW)
        self.moveRightGP.addAnimation(animation)

        animation = self.getVariantAnimation()
        animation.setStartValue(10)
        animation.setEndValue(90)
        animation.valueChanged.connect(self.moveRightUpdateX)
        self.moveRightGP.addAnimation(animation)

    def initMoveUpAnimation(self):
        self.moveUpGP = QSequentialAnimationGroup(self)

        animation = QVariantAnimation(self)
        animation.setDuration(self.animationDuration)
        animation.setStartValue(90)
        animation.setEndValue(10)
        animation.valueChanged.connect(self.moveUpUpdateY)
        self.moveUpGP.addAnimation(animation)

        animation = self.getVariantAnimation()
        animation.setStartValue(120)
        animation.setEndValue(40)
        animation.valueChanged.connect(self.moveUpUpdateH)
        self.moveUpGP.addAnimation(animation)

    def initMoveLeftAnimation(self):
        self.moveLeftGP = QSequentialAnimationGroup(self)

        animation = self.getVariantAnimation()
        animation.setStartValue(90)
        animation.setEndValue(10)
        animation.valueChanged.connect(self.moveLeftUpdateX)
        self.moveLeftGP.addAnimation(animation)

        animation = self.getVariantAnimation()
        animation.setStartValue(120)
        animation.setEndValue(40)
        animation.valueChanged.connect(self.moveLeftUpdateH)
        self.moveLeftGP.addAnimation(animation)

    # UPDATE METHODS ==============================================================

    def moveDownUpdateH(self, newValue):
        self.rectsList[1].h = newValue
        self.update()
    
    def moveDownUpdateY(self, newValue):
        self.rectsList[1].y = newValue
        self.rectsList[1].h = 130-newValue
        self.update()
    
    def moveRightUpdateW(self, newValue):
        self.rectsList[0].w = newValue
        self.update()

    def moveRightUpdateX(self, newValue):
        self.rectsList[0].x = newValue
        self.rectsList[0].w = 130-newValue
        self.update()

    def moveUpUpdateY(self, newValue):
        self.rectsList[2].y = newValue
        self.rectsList[2].h = 130-newValue
        self.update()

    def moveUpUpdateH(self, newValue):
        self.rectsList[2].h = newValue
        self.update()

    def moveLeftUpdateX(self, newValue):
        self.rectsList[1].x = newValue
        self.rectsList[1].w = 130-newValue
        self.update()

    def moveLeftUpdateH(self, newValue):
        self.rectsList[1].w = newValue
        self.update()

    # START ANIMATIONS METHOD ===========================================================

    def startAnimations(self):
        self.initMoveDownAnimation()
        self.initMoveRightAnimation()
        self.initMoveUpAnimation()
        self.initMoveLeftAnimation()
        gp = QSequentialAnimationGroup(self)
        gp.addAnimation(self.moveDownGP)
        gp.addAnimation(self.moveRightGP)
        gp.addAnimation(self.moveUpGP)
        gp.addAnimation(self.moveLeftGP)
        self.moveLeftGP.finished.connect(self.finished)
        gp.setLoopCount(10)
        gp.start()
    
    def finished(self):
        self.rectsList = [self.rectsList[2], self.rectsList[0], self.rectsList[1]]

    # OVERRIDE PAINT EVENT ==============================================================

    def paintEvent(self, e):
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(self.color)
        pen.setWidth(self.penWidth)
        painter.setPen(pen)
        painter.setRenderHint(QPainter.Antialiasing)
        x = self.penWidth/2
        for rect in self.rectsList:
            painter.drawRoundedRect(rect.x, rect.y, rect.w, rect.h, 20, 20)
        painter.end()