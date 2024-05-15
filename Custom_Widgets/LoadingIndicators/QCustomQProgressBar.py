# coding:utf-8
# Original code: https://github.com/zhiyiYo/PyQt-Fluent-Widgets/tree/PySide6
# Edits and improvements made by Khamisi Kibet
# QT GUI BY SPINN TV(YOUTUBE)
from math import floor

from qtpy.QtCore import (QEasingCurve, Qt, QPropertyAnimation, Property,
                          QParallelAnimationGroup, QSequentialAnimationGroup, QLocale)
from qtpy.QtGui import QPainter, QColor, QPalette
from qtpy.QtWidgets import QProgressBar, QStyleOption, QStyle

from Custom_Widgets.QCustomTheme import QCustomTheme


class QCustomQProgressBar(QProgressBar):
    """ Indeterminate progress bar """

    def __init__(self, parent=None, start=True):
        super().__init__(parent=parent)

        self.customTheme = QCustomTheme()

        self._shortPos = 0
        self._longPos = 0
        self.shortBarAni = QPropertyAnimation(self, b'shortPos', self)
        self.longBarAni = QPropertyAnimation(self, b'longPos', self)

        self._lightBarColor = QColor()
        self._darkBarColor = QColor()

        self._isError = False

        self.aniGroup = QParallelAnimationGroup(self)
        self.longBarAniGroup = QSequentialAnimationGroup(self)

        self.shortBarAni.setDuration(833)
        self.longBarAni.setDuration(1167)
        self.shortBarAni.setStartValue(0)
        self.longBarAni.setStartValue(0)
        self.shortBarAni.setEndValue(1.45)
        self.longBarAni.setEndValue(1.75)
        self.longBarAni.setEasingCurve(QEasingCurve.OutQuad)

        self.aniGroup.addAnimation(self.shortBarAni)
        self.longBarAniGroup.addPause(785)
        self.longBarAniGroup.addAnimation(self.longBarAni)
        self.aniGroup.addAnimation(self.longBarAniGroup)
        self.aniGroup.setLoopCount(-1)

        self.setFixedHeight(4)

        if start:
            self.start()

    def setCustomBarColor(self, light, dark):
        """ set the custom bar color

        Parameters
        ----------
        light, dark: str | Qt.GlobalColor | QColor
            bar color in light/dark theme mode
        """
        self._lightBarColor = QColor(light)
        self._darkBarColor = QColor(dark)
        self.update()

    @Property(float)
    def shortPos(self):
        return self._shortPos

    @shortPos.setter
    def shortPos(self, p):
        self._shortPos = p
        self.update()

    @Property(float)
    def longPos(self):
        return self._longPos

    @longPos.setter
    def longPos(self, p):
        self._longPos = p
        self.update()

    def start(self):
        self.shortPos = 0
        self.longPos = 0
        self.aniGroup.start()
        self.update()

    def stop(self):
        self.aniGroup.stop()
        self.shortPos = 0
        self.longPos = 0
        self.update()

    def isStarted(self):
        return self.aniGroup.state() == QParallelAnimationGroup.Running

    def pause(self):
        self.aniGroup.pause()
        self.update()

    def resume(self):
        self.aniGroup.resume()
        self.update()

    def setPaused(self, isPaused: bool):
        self.aniGroup.setPaused(isPaused)
        self.update()

    def isPaused(self):
        return self.aniGroup.state() == QParallelAnimationGroup.Paused

    def error(self):
        self._isError = True
        self.aniGroup.stop()
        self.update()

    def setError(self, isError: bool):
        self._isError = isError
        if isError:
            self.error()
        else:
            self.start()

    def isError(self):
        return self._isError

    def barColor(self):
        if self.isError():
            return QColor(255, 153, 164) if self.customTheme.isAppDarkThemed() else QColor(196, 43, 28)

        if self.isPaused():
            return QColor(252, 225, 0) if self.customTheme.isAppDarkThemed() else QColor(157, 93, 0)

        return self.palette().color(QPalette.Highlight)

    def paintEvent(self, e):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

        painter.setPen(Qt.NoPen)
        painter.setBrush(self.barColor())

        # draw short bar
        x = int((self.shortPos - 0.4) * self.width())
        w = int(0.4 * self.width())
        r = self.height() / 2
        painter.drawRoundedRect(x, 0, w, self.height(), r, r)

        # draw long bar
        x = int((self.longPos - 0.6) * self.width())
        w = int(0.6 * self.width())
        r = self.height() / 2
        painter.drawRoundedRect(x, 0, w, self.height(), r, r)
