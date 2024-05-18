# coding:utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from Custom_Widgets.QCustomLoadingIndicators import QCustomSpinner


class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()

        self.spinner = QCustomSpinner(lineWidth=10, lineColor="#FF0000", animationType="Bounce")
        self.spinner2 = QCustomSpinner(lineColor="#000", animationType="Smooth")
        self.spinner.setMinimumSize(100, 100)
        self.spinner.setMaximumSize(100, 100)
        self.spinner2.setMinimumSize(100, 100)
        self.spinner2.setMaximumSize(100, 100)

        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addWidget(self.spinner, 0, Qt.AlignHCenter)
        self.vBoxLayout.addWidget(self.spinner2, 0, Qt.AlignHCenter)
        self.resize(400, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()