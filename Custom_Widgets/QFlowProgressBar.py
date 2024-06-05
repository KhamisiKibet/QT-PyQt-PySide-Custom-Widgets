from qtpy.QtCore import Qt, QRect, Signal, QPointF, Property, QPropertyAnimation, QEasingCurve
from qtpy.QtGui import QPainter, QPaintEvent, QMouseEvent, QColor, QBrush, QPen, QFont, QFontMetrics, QPolygonF
from qtpy.QtWidgets import QWidget
from typing import List

class QFlowProgressBar(QWidget):
    onStepClicked = Signal(int)  # Define the signal for step clicks

    class Styles:
        Circular = 0
        Flat = 1
        Square = 2
        Breadcrumb = 3
    
    class Direction:
        Up = 0
        Down = 1

    def __init__(self, strDetailList: List[str] = None, style: int = Styles.Circular, parent: QWidget = None,
                 finishedNumberColor: QColor = QColor(255, 255, 255), finishedBackgroundColor: QColor = QColor(0, 136, 254),
                 unfinishedBackgroundColor: QColor = QColor(228, 231, 237), numberFontSize: int = 9, textFontSize: int = 10,
                 currentStep: int = 0, pointerDirection: Direction = Direction.Up,
                 animationDuration: int = 1000, easingCurve: QEasingCurve.Type = QEasingCurve.OutQuad, stepsClickable: bool = True):
        """
        Construct a QFlowProgressBar.

        :param strDetailList: List of detail strings for each step.
        :param style: Style of the progress bar (Circular, Flat, Square, Breadcrumb).
        :param parent: Parent widget.
        :param finishedNumberColor: Color for finished step numbers.
        :param finishedBackgroundColor: Background color for finished steps.
        :param unfinishedBackgroundColor: Background color for unfinished steps.
        :param numberFontSize: Font size for step numbers.
        :param textFontSize: Font size for step descriptions.
        :param currentStep: The current step in the progress bar.
        :param pointerDirection: Pointer direction for flat progressbar.
        :param animationDuration: Duration of the animation in milliseconds.
        :param easingCurve: Easing curve for the animation.
        """
        super().__init__(parent)
        self.barStyle = style
        self.finishedNumberColor = finishedNumberColor
        self.finishedBackgroundColor = finishedBackgroundColor
        self.unfinishedBackgroundColor = unfinishedBackgroundColor
        self.stepIconRects = []
        self.stepMessages = strDetailList if strDetailList else []
        self._currentStep = currentStep

        self.numberFontSize = numberFontSize
        self.textFontSize = textFontSize

        self.pointerDirection = pointerDirection

        self._finishedProgressLength = 0
        self.animationDuration = animationDuration
        self.easingCurve = easingCurve

        self.adjustSize()

        self.animation = QPropertyAnimation(self, b"finishedProgressLength")
        self.animation.setDuration(self.animationDuration)
        self.animation.setEasingCurve(self.easingCurve)

        self.stepsClickable = stepsClickable

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        Mouse release event handler.

        :param event: QMouseEvent object.
        """
        if not self.stepsClickable:
            return
        point = event.pos()
        # print("Mouse click coordinates:", point)  # Debug print
        for index, rect in enumerate(self.stepIconRects):
            if rect.contains(point):
                # print("Step", index + 1, "clicked")  # Debug print
                self.changeCurrentStep(index + 1)
                self.onStepClicked.emit(index)
                break

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.changeCurrentStep(self.getCurrentStep())
        self.adjustSize()
        self.update()


    def paintEvent(self, event: QPaintEvent):
        """
        Paint event handler to draw the progress bar.

        :param event: QPaintEvent object.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.barStyle == self.Styles.Circular or self.barStyle == self.Styles.Square:
            self.drawStyle(painter)
        elif self.barStyle == self.Styles.Flat:
            self.drawFlatStyle(painter)

    def drawStyle(self, painter: QPainter):
        """
        Draw the progress bar with Circular or Square style.

        :param painter: QPainter object.
        """
        numberOfSteps = len(self.stepMessages)
        progressBarLength = int(self.size().width() * 0.9)
        progressBarHeight = int(self.size().height() * 0.1)
        totalStepIconLength = int(progressBarLength * 0.88)
        iconSize = int((totalStepIconLength / (numberOfSteps - 1)) * 0.15)
        iconStep = totalStepIconLength // (numberOfSteps - 1)
        iconStartY = 0

        iconBorderPen = QPen(QBrush(self.getBackgroundColor()), iconSize * 0.1)
        whiteBrush = QBrush(Qt.white)
        fontNumber = QFont()
        fontText = QFont()
        fontNumber.setPointSize(self.numberFontSize)
        fontText.setPointSize(self.textFontSize)
        textSize = self.getDrawTextSize("Sample", fontText)

        # Ensure icon size does not exceed 2/3 of the total height
        maxIconSize = int(self.size().height() * 2 / 3)
        iconSize = min(iconSize, maxIconSize)

        # Ensure icon size plus text height does not exceed total height
        totalHeight = self.size().height()
        maxTotalHeight = totalHeight - textSize.height()
        if iconSize + textSize.height() > totalHeight:
            iconSize = maxTotalHeight

        # Draw background progress bar
        startX = int(self.size().width() * 0.05)
        startY = (iconSize / 2) - (progressBarHeight / 2)

        backgroundBrush = QBrush(self.getBackgroundColor())
        finishedBrush = QBrush(self.getFinishedBackgroundColor())
        emptyPen = QPen(Qt.NoPen)

        painter.setPen(emptyPen)
        painter.setBrush(backgroundBrush)
        painter.drawRoundedRect(startX, startY, progressBarLength, progressBarHeight, progressBarHeight, progressBarHeight)

        # Draw finished progress
        painter.setBrush(finishedBrush)
        painter.drawRoundedRect(startX, startY, self.finishedProgressLength, progressBarHeight, progressBarHeight,
                                progressBarHeight)

        painter.save()
        painter.translate(startX + progressBarLength * 0.05, iconStartY)

        for i in range(numberOfSteps):
            if i < self._currentStep:
                painter.setBrush(finishedBrush)
            else:
                painter.setBrush(whiteBrush)

            currentXOffset = i * iconStep
            painter.setPen(iconBorderPen)

            # Store the bounding rectangle of each step icon
            iconRect = QRect(currentXOffset, 1, iconSize, iconSize)
            clickableRect = QRect(currentXOffset + (iconStep - iconSize) // 2 - (iconSize/2), 1, iconSize, iconSize)
            self.stepIconRects.append(clickableRect)

            if self.barStyle == self.Styles.Circular:
                painter.drawEllipse(iconRect)
            else:
                painter.drawRect(iconRect)

            painter.setFont(fontNumber)
            if i < self._currentStep:
                painter.setPen(QPen(self.getFinishedNumberColor()))

            painter.drawText(currentXOffset, 0, iconSize, iconSize, Qt.AlignCenter, str(i + 1))

            displayText = self.stepMessages[i]
            textSize = self.getDrawTextSize(displayText, fontText)

            textStartX = int((currentXOffset + iconSize * 0.5) - textSize.width() / 2)
            textStartY = int(iconSize + 3)
            painter.setFont(fontText)
            if i < self._currentStep:
                painter.setPen(QPen(self.getFinishedBackgroundColor()))

            painter.drawText(textStartX, textStartY, textSize.width(), textSize.height(), Qt.AlignCenter, displayText)

        painter.restore()

    def drawFlatStyle(self, painter: QPainter):
        """
        Draw progress bar with Flat style and triangle pointer tip.

        :param painter: QPainter object.
        """
        numberOfSteps = len(self.stepMessages)
        progressBarLength = int(self.size().width() * 0.9)
        progressBarHeight = int(self.size().height() * 0.1)
        totalStepIconLength = int(progressBarLength * 0.88)
        iconSize = int((totalStepIconLength / (numberOfSteps - 1)) * 0.15)
        iconStep = totalStepIconLength // (numberOfSteps - 1)
        progressBarGap = progressBarHeight * 1.5

        iconBorderPen = QPen(QBrush(self.getBackgroundColor()), iconSize * 0.1)
        whiteBrush = QBrush(Qt.white)
        fontNumber = QFont()
        fontNumber.setPointSize(self.numberFontSize)
        fontText = QFont()
        fontText.setPointSize(self.textFontSize)
        textSize = self.getDrawTextSize("Sample", fontText)

        # Ensure icon size does not exceed 2/3 of the total height
        maxIconSize = int(self.size().height() * 2 / 3)
        iconSize = min(iconSize, maxIconSize)

        # Ensure icon size plus text height does not exceed total height
        totalHeight = self.size().height()
        maxTotalHeight = totalHeight - (textSize.height() + progressBarHeight + (progressBarGap * 2))
        if (iconSize + textSize.height() + progressBarHeight + (progressBarGap * 2)) > totalHeight:
            iconSize = maxTotalHeight

        textStartY = int(iconSize + progressBarHeight + progressBarGap)

        # Background progress bar
        startX = int(self.size().width() * 0.05)
        startY = int(self.size().height() * 0.15)
        progressBarStartY = startY + iconSize + progressBarGap

        backgroundBrush = QBrush(self.getBackgroundColor())
        finishedBrush = QBrush(self.getFinishedBackgroundColor())
        emptyPen = QPen(Qt.NoPen)
        painter.setPen(emptyPen)
        painter.setBrush(backgroundBrush)
        painter.drawRoundedRect(startX, progressBarStartY, progressBarLength, progressBarHeight, progressBarHeight,
                                progressBarHeight)

        # Draw completed progress
        painter.setBrush(finishedBrush)
        painter.drawRoundedRect(startX, progressBarStartY, self.finishedProgressLength, progressBarHeight,
                                progressBarHeight, progressBarHeight)

        painter.save()
        painter.translate(startX + progressBarLength * 0.05, startY)

        for i in range(numberOfSteps):
            if i < self._currentStep:
                painter.setBrush(finishedBrush)
            else:
                painter.setBrush(whiteBrush)

            currentXOffset = i * iconStep
            painter.setPen(iconBorderPen)

            iconRect = QRect(currentXOffset, 1, iconSize, iconSize)
            clickableRect = QRect(currentXOffset + (iconStep - iconSize) // 2 - (iconSize/2), 1, iconSize, iconSize)
            self.stepIconRects.append(clickableRect)

            painter.drawEllipse(iconRect)

            # Draw triangle pointer tip
            pointerTipWidth = progressBarGap
            pointerTipHeight = progressBarGap 
            painter.setPen(Qt.NoPen)
            if i < self._currentStep:
                painter.setBrush(finishedBrush)
            else:
                painter.setBrush(backgroundBrush)

            if self.pointerDirection == self.Direction.Up:
                pointer = QPolygonF([
                            QPointF(currentXOffset + iconSize / 2 - pointerTipWidth / 2, progressBarStartY - progressBarHeight),
                            QPointF(currentXOffset + iconSize / 2 + pointerTipWidth / 2, progressBarStartY - progressBarHeight),
                            QPointF(currentXOffset + iconSize / 2, 1 - pointerTipHeight + progressBarStartY - progressBarHeight)
                        ])
            else:
                pointer = QPolygonF([QPointF(currentXOffset + iconSize / 2 - pointerTipWidth / 2, 1 + iconSize),
                                QPointF(currentXOffset + iconSize / 2 + pointerTipWidth / 2, 1 + iconSize),
                                QPointF(currentXOffset + iconSize / 2, 1 + iconSize + pointerTipHeight)])

            painter.drawPolygon(pointer)

            painter.setFont(fontNumber)
            if i < self._currentStep:
                painter.setPen(QPen(self.getFinishedNumberColor()))

            painter.drawText(currentXOffset, 0, iconSize, iconSize, Qt.AlignCenter, str(i + 1))

            displayText = self.stepMessages[i]
            textSize = self.getDrawTextSize(displayText, fontText)

            textStartX = int((currentXOffset + iconSize * 0.5) - textSize.width() / 2)

            painter.setFont(fontText)
            if i < self._currentStep:
                painter.setPen(QPen(self.getFinishedBackgroundColor()))
            else:
                painter.setPen(QPen(Qt.black))

            painter.drawText(textStartX, textStartY, textSize.width(), textSize.height(), Qt.AlignCenter, displayText)

        painter.restore()

    def getBackgroundColor(self) -> QColor:
        """
        Get the background color of the progress bar.

        :return: QColor object representing the background color.
        """
        return self.unfinishedBackgroundColor

    def getFinishedBackgroundColor(self) -> QColor:
        """
        Get the color for finished progress bar segments.

        :return: QColor object representing the finished segment color.
        """
        return self.finishedBackgroundColor

    def getFinishedNumberColor(self) -> QColor:
        """
        Get the color for finished numbers in the progress bar.

        :return: QColor object representing the finished number color.
        """
        return self.finishedNumberColor
    
    def getCurrentStep(self):
        """
        CReturn current step

        """
        return self._currentStep
    
    def changeCurrentStep(self, step: int):
        """
        Change the current step of the progress bar.

        :param step: New step to set.
        """
        if step > len(self.stepMessages) or step < 0:
            return
        
        self._currentStep = step
        self.animation.setStartValue(self.finishedProgressLength)

        if step <= 0:
            finishedProgressLength = 0
        else:
            progressBarLength = int(self.size().width() * 0.9)
            iconStep = int((progressBarLength * 0.88) / (len(self.stepMessages) - 1))
            finishedProgressLength = int(progressBarLength * 0.05 + (step - 1) * iconStep + iconStep / 2)
            finishedProgressLength = min(finishedProgressLength, progressBarLength)
        
        self.animation.setEndValue(finishedProgressLength)
        self.animation.start()


    def getDrawTextSize(self, text: str, font: QFont) -> QRect:
        """
        Get the size of the text to be drawn.

        :param text: Text string.
        :param font: QFont object.
        :return: QRect object representing the size of the text.
        """
        metrics = QFontMetrics(font)
        return metrics.boundingRect(text).adjusted(-2, -2, 2, 2)

    def getFinishedProgressLength(self) -> int:
        return self._finishedProgressLength

    def setFinishedProgressLength(self, length: int):
        self._finishedProgressLength = length
        self.update()

    finishedProgressLength = Property(int, getFinishedProgressLength, setFinishedProgressLength)
