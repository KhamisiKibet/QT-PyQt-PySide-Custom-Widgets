from qtpy.QtGui import *
from qtpy.QtWidgets import *

import os

class QPushButtonThemed(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        # store icon url 
        self.iconUrl = None

    def setNewIcon(self, url):
        icon = QIcon(url)
        self.setIcon(icon)

        self.iconUrl = url

class QLabelThemed(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        # store icon url 
        self.piximapUrl = None

    def setNewPixmap(self, url):
        piximap = QPixmap(url)
        self.setPixmap(piximap)

        self.piximapUrl = url

    
