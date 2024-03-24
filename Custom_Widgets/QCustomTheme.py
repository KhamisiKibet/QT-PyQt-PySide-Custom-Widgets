from qtpy.QtWidgets import QApplication
from qtpy.QtGui import QPalette, QCursor
from qtpy.QtCore import QRect, Signal, QObject

class QCustomTheme(QObject):
    # Define a class-level signal
    onThemeChanged = Signal()

    def __init__(self):
        super().__init__()
        # self.onThemeChanged.connect(print("theme changed"))

    def themeChanged(self):
        # Emit the signal from the instance
        self.onThemeChanged.emit()

    @staticmethod
    def isAppDarkThemed():
        app = QApplication.instance()
        if app is None:
            raise RuntimeError("QApplication instance is required.")
        
        palette = app.palette()
        
        # Extract the background color of the application palette
        background_color = palette.color(QPalette.Window)
        
        # Calculate luminance using the YIQ color space formula
        luminance = (0.299 * background_color.red() + 0.587 * background_color.green() + 0.114 * background_color.blue()) / 255
        
        # Determine if the background color is considered dark or light
        if luminance < 0.5:
            return True  # Dark theme
        else:
            return False  # Light theme
        
    @staticmethod
    def getCurrentScreen():
        """ get current screen """
        cursorPos = QCursor.pos()

        for s in QApplication.screens():
            if s.geometry().contains(cursorPos):
                return s

        return None

    @staticmethod
    def getCurrentScreenGeometry(avaliable=True):
        """ get current screen geometry """
        screen = QCustomTheme.getCurrentScreen() or QApplication.primaryScreen()

        # this should not happen
        if not screen:
            return QRect(0, 0, 1920, 1080)

        return screen.availableGeometry() if avaliable else screen.geometry()
