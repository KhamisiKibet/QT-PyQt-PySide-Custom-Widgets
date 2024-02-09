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
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

########################################################################
## CUSTOM QCheckBox
########################################################################
class QCustomCheckBox(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setCursor(Qt.PointingHandCursor)

        # Check if a QApplication instance already exists
        if QApplication.instance():
            app = QApplication.instance()
        else:
            app = QApplication([])


        # Get the default palette
        palette = app.palette()
            
        # Get the default background color
        bgColor = palette.color(QPalette.Window)
        # Get the default text color (assuming this is your "circle_color")
        circleColor = palette.color(QPalette.Text)
        # Get the default highlight color (assuming this is your "active_color")
        activeColor = palette.color(QPalette.Highlight)

        # COLORS
        self.bgColor = bgColor
        self.circleColor = circleColor
        self.activeColor = activeColor

        # Animation
        self.animationEasingCurve = QEasingCurve.OutBounce
        self.animationDuration = 300

        self.pos = 3
        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(self.animationEasingCurve)
        self.animation.setDuration(self.animationDuration)
        self.stateChanged.connect(self.setup_animation)

        # Create a QLabel to display the text
        self.label = QLabel(self)
        # self.label.setContentsMargins(0, 0, 0, 0)  # Set contents margins to 0 to remove spacing
        self.label.setWordWrap(True)

        # Initialize icon
        self.icon = QIcon()
        self._iconSize = QSize(2, 2)  # Default icon size

    def setIcon(self, icon):
        self.icon = icon
        self.update()
    
    def setIconSize(self, size):
        """
        Set the size of the icon for the checkbox.

        Parameters:
            size (QSize): The size of the icon.
        """
        self._iconSize = size
        self.update()

    ########################################################################
    # Customize QCustomCheckBox
    ########################################################################
    def customizeQCustomCheckBox(self, **customValues):
        if "bgColor" in customValues:
            self.bgColor = customValues["bgColor"]
        
        if "circleColor" in customValues:
            self.circleColor = customValues["circleColor"]

        if "activeColor" in customValues:
            self.activeColor = customValues["activeColor"]

        if "animationEasingCurve" in customValues:
            self.animationEasingCurve = customValues["animationEasingCurve"]
            self.animation.setEasingCurve(self.animationEasingCurve)

        if "animationDuration" in customValues:
            self.animationDuration = customValues["animationDuration"]
            self.animation.setDuration(self.animationDuration)

        self.update()


    def resizeEvent(self, event):
        super().resizeEvent(event)

        # Update checkbox size
        # Update label position and width
        icon_size = self._iconSize.width()
        label_margin = 5  # Adjust the margin between the icon and the label

        label_width = self.width() - (self.height() * 2.1 + icon_size + label_margin)  # Calculate the width of the label area
        label_height = self.height()  # Use the height of the checkbox for the label height

        label_x = self.height() * 2.1 + icon_size + label_margin  # Calculate the x position of the label
        label_y = (self.height() - label_height) / 2  # Center the label vertically within the checkbox area

        self.label.setGeometry(label_x, label_y, label_width, label_height)
        self.label.adjustSize()


    def setText(self, text):
        super().setText(text)
        self.label.setText(text)

    @Property(float)
    def position(self):
        return self.pos

    @position.setter
    def position(self, pos):
        self.pos = pos
        self.update()

    # START STOP ANIMATION
    def setup_animation(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.height() + 2)
        else:
            self.animation.setEndValue(0)
        self.animation.start()
    
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # SET PEN
        p.setPen(Qt.NoPen)

        # DRAW RECT
        rect = QRect(0, 0, self.height() * 2.2, self.height())

        # Define margins
        margin = 3

        if not self.isChecked():
            p.setBrush(QColor(self.bgColor))
            p.drawRoundedRect(0, 0, self.height() * 2.1, self.height(), self.height() * .5, self.height() * .5)

            p.setBrush(QColor(self.circleColor))
            p.drawEllipse(self.pos, 0, self.height(), self.height())
        else:
            p.setBrush(QColor(self.activeColor))
            p.drawRoundedRect(0, 0, self.height() * 2.1, self.height(), self.height() * .5, self.height() * .5)

            p.setBrush(QColor(self.circleColor))
            p.drawEllipse(self.pos, 0, self.height(), self.height())

        # DRAW ICON (Optional)
        if not self.icon.isNull():
            icon_size = self.height() * 0.7 if self.icon.availableSizes() else QSize(16, 16)  
            pixmap = self.icon.pixmap(self._iconSize)
            # Adjust horizontal position to add margin between checkbox and icon
            icon_x = self.height() * 2.1 + margin
            icon_y = (self.height() - self._iconSize.height()) / 2  # Center the icon vertically within the checkbox area
            p.drawPixmap(icon_x, icon_y, pixmap)

        p.end()
