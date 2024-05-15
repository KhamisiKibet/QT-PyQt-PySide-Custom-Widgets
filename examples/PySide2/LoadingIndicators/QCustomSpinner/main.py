# coding:utf-8
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from Custom_Widgets.QCustomLoadingIndicators import QCustomSpinner


class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.vBoxLayout = QVBoxLayout(self)
        self.hBoxLayout = QHBoxLayout()

        self.spinner = QCustomSpinner(lineWidth=10, lineColor="#FF0000", animationType="Bounce")
        # self.spinner = QCustomSpinner()
        self.spinner.setMinimumSize(50, 50)
        self.spinner.setMaximumSize(50, 50)

        self.vBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addWidget(self.spinner, 0, Qt.AlignHCenter)
        self.resize(400, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()