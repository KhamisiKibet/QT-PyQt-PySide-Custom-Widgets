# ///////////////////////////////////////////////////////////////
#
# https://www.youtube.com/watch?v=daVpOpvsCKQ&t=20s
# All rights reserved.
#
# ///////////////////////////////////////////////////////////////
# Edits and improvements made by Khamisi Kibet
# QT GUI BY SPINN TV(YOUTUBE)

import math
import time

from perlin_noise import PerlinNoise as Noise
from typing import Optional

from qtpy.QtCore import QVariantAnimation, QPointF, QRect, QSize
from qtpy.QtGui import (QPainter, Qt, QPaintEvent, QColor, QBrush,
                           QPainterPath, QFont)
from qtpy.QtWidgets import QFrame, QWidget


class QCustomPerlinLoader(QFrame):
    def __init__(self, parent: Optional[QWidget] = None,
                size: QSize = QSize(600, 600),
                message: str = "LOADING...",
                color = QColor("white"),
                fontFamily = "Ebrima",
                fontSize = 30,
                rayon: int = 200,
                duration: int = 60 * 1000,
                noiseOctaves: float = 0.8,
                noiseSeed: int = int(time.time()),
                backgroundColor: QColor = QColor("transparent"),
                circleColor1: QColor = QColor("#ff2e63"),
                circleColor2: QColor = QColor("#082e63"),
                circleColor3: QColor = QColor(57, 115, 171, 100)) -> None:
        QFrame.__init__(self, parent)

        self.setFrameShape(QFrame.NoFrame)
        self.setFixedSize(size)

        self.start = 0
        self.step = 1
        self.rayon = rayon
        self.duration = duration
        self.message = message
        self.color = color
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.backgroundColor = backgroundColor
        self.circleColor1 = circleColor1
        self.circleColor2 = circleColor2
        self.circleColor3 = circleColor3

        self.animation: Optional[QVariantAnimation] = None
        self.noise_generator1 = Noise(octaves=noiseOctaves, seed=noiseSeed)
        self.noise_generator2 = Noise(octaves=noiseOctaves, seed=noiseSeed + 1)
        self.noise_generator3 = Noise(octaves=noiseOctaves, seed=noiseSeed + 3)
        self.start_animation()

    def start_animation(self) -> None:
        self.animation = QVariantAnimation(self)
        self.animation.setDuration(self.duration)
        self.animation.setStartValue(self.start)
        self.animation.setEndValue(5000)
        self.animation.valueChanged.connect(self.update_start_angle)
        self.animation.start()

    def update_start_angle(self, new_value: float) -> None:
        self.start = new_value
        self.update()

    def get_deformed_point(self, angle: float, noise_generator: Noise) -> QPointF:
        radian_angle = math.radians(angle)
        _x = math.cos(radian_angle)
        _y = math.sin(radian_angle)
        offset = self.start / 100
        noise = noise_generator([_x + offset, _y + offset])
        c = self.rayon * (1 + noise/2.5)
        point = QPointF(_x * c, _y * c)
        return point

    def draw_deformed_circles(self, painter: QPainter) -> None:
        painter.save()

        painter.translate(self.rect().center())

        path1 = QPainterPath()
        path2 = QPainterPath()
        path3 = QPainterPath()

        angle = 1
        path1.moveTo(self.get_deformed_point(angle, self.noise_generator1))
        path2.moveTo(self.get_deformed_point(angle, self.noise_generator2))
        path3.moveTo(self.get_deformed_point(angle, self.noise_generator3))

        while angle < 360:
            path1.lineTo(self.get_deformed_point(angle, self.noise_generator1))
            path2.lineTo(self.get_deformed_point(angle, self.noise_generator2))
            path3.lineTo(self.get_deformed_point(angle, self.noise_generator3))
            angle += self.step

        painter.drawPath(path1)
        painter.setBrush(QBrush(self.circleColor1))
        painter.drawPath(path2)
        painter.setBrush(QBrush(self.circleColor2))
        painter.drawPath(path2.intersected(path1))
        painter.setBrush(QBrush(self.circleColor3))
        painter.drawPath(path3.intersected(path2))

        painter.restore()

    def draw_message(self, painter: QPainter) -> None:
        font = QFont(self.fontFamily, self.fontSize)
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 10)
        painter.setFont(font)

        painter.setPen(self.color)
        flags = Qt.AlignHCenter | Qt.AlignVCenter
        painter.drawText(self.rect(), flags, self.message)

    def paintEvent(self, e: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(self.backgroundColor))
        painter.setPen(Qt.NoPen)

        _rect = QRect(0, 0, 400, 400)
        _rect.moveCenter(self.rect().center())
        painter.drawRoundedRect(_rect, 100, 100)
        self.draw_deformed_circles(painter)
        self.draw_message(painter)

        painter.end()
