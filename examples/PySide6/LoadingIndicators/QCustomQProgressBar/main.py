# coding:utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from Custom_Widgets.QCustomLoadingIndicators import QCustomQProgressBar


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.vBoxLayout = QVBoxLayout(self)
    
        self.inProgressBar = QCustomQProgressBar(self)
        self.button = QPushButton("Pause")

        self.vBoxLayout.addWidget(self.inProgressBar)
        self.vBoxLayout.addWidget(self.button, 0, Qt.AlignHCenter)
        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.resize(400, 400)

        self.button.clicked.connect(self.onButtonClicked)

    def onButtonClicked(self):
        if self.inProgressBar.isStarted():
            self.inProgressBar.pause()
            self.button.setText('Play')
        else:
            self.inProgressBar.resume()
            self.button.setText("Pause")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()