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

class ArcLoader:
    def __init__(
            self,
            parent=None,
            spacer=0,
            startAngle=270,
            spanAngle=1/16,
            direction=True,
            duration=4000
            ):
        self.parent = parent
        self.spacer = spacer
        self.startAngle = startAngle
        self.fixedStartAngle = self.startAngle
        self.spanAngle = spanAngle
        self.direction = direction
        self.duration = duration

        self.clockWise = True
        self.antiClockWise = False

    def getRotationAnimation(self):
        animation = QVariantAnimation(self.parent)
        animation.setStartValue(self.spacer)
        animation.setEndValue(self.spacer+360*2)
        animation.setDuration(self.duration)
        animation.setEasingCurve(QEasingCurve.InOutSine)
        animation.valueChanged.connect(self.updateSpacer)
        return animation

    def getSpanAngleAnimation(self):
        animation = QVariantAnimation(self.parent)
        animation.setStartValue(1/16)
        animation.setEndValue(1/16+360)
        animation.setDuration(self.duration*.5)
        animation.finished.connect(self.animationFinished)
        animation.valueChanged.connect(self.updateSpanAngle)
        return animation
    
    def getStartAngleAnimation(self):
        animation = QVariantAnimation(self.parent)
        animation.setStartValue(270)
        animation.setEndValue(270+360)
        animation.setDuration(self.duration*.5)
        animation.finished.connect(self.startAnimationFinished)
        animation.valueChanged.connect(self.updateStartAngle)
        return animation
    
    def startAnimationFinished(self):
        self.startAngle = 270
        self.fixedStartAngle = self.startAngle
        self.spanAngle = 1/16
        self.direction = not self.direction

    def startAnimations(self):
        seqGroup = QSequentialAnimationGroup(self.parent)
        if self.direction:
            seqGroup.addAnimation(self.getSpanAngleAnimation())
            seqGroup.addAnimation(self.getStartAngleAnimation())
        else:
            seqGroup.addAnimation(self.getStartAngleAnimation())
            seqGroup.addAnimation(self.getSpanAngleAnimation())
        parGroup = QParallelAnimationGroup(self.parent)
        parGroup.addAnimation(self.getRotationAnimation())
        parGroup.addAnimation(seqGroup)
        parGroup.setLoopCount(10)
        parGroup.start()

    def animationFinished(self):
        self.direction = not self.direction

    def updateStartAngle(self, newValue):
        self.startAngle = newValue
        self.parent.update()

    def updateSpacer(self, newValue):
        self.spacer = newValue
        self.parent.update()
    
    def updateSpanAngle(self, newValue):
        self.spanAngle = newValue
        self.parent.update()

class QCustomArcLoader(QFrame):
    def __init__(
            self, 
            parent=None,
            color=QColor("#ffffff"),
            penWidth=20
            ):
        QFrame.__init__(self, parent=parent)

        self.setFrameShape(QFrame.NoFrame)
        self.setFixedSize(160, 160)
        self.color = color
        self.initPen(penWidth)

        self.arc1 = ArcLoader(self, 0, 270, 1/16, True, 4*1000)
        self.arc1.startAnimations()

    def calculateXR(self, level):
        x = self.pen.width()*level/2
        r = self.width()-self.pen.width()*level
        return x, r
    
    def draw(self):
        x, r = self.calculateXR(1)
        arc = self.arc1
        if arc.direction:
            spanAngle = arc.startAngle-arc.fixedStartAngle+arc.spanAngle
        else: 
            spanAngle = 360-(arc.startAngle-arc.fixedStartAngle)
        if spanAngle < 1/16:
            spanAngle = 1/16
        self.painter.drawArc(x, x, r, r, -(arc.spacer+arc.startAngle)*16, -spanAngle*16) 
        x, r = self.calculateXR(5)
        self.painter.drawArc(x, x, r, r, -(arc.spacer+arc.startAngle)*16, (360-spanAngle)*16) 

    def initPen(self, penWidth):
        self.pen = QPen()
        self.pen.setColor(self.color)
        self.pen.setWidth(penWidth)
        self.pen.setCapStyle(Qt.RoundCap)

    def paintEvent(self, e):
        self.painter = QPainter(self)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setPen(self.pen)
        self.draw()
        self.painter.end()