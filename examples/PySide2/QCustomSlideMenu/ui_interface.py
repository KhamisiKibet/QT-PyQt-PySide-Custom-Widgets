# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXXawCe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(479, 368)
        MainWindow.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.my_toggle_button = QPushButton(self.centralwidget)
        self.my_toggle_button.setObjectName(u"my_toggle_button")
        self.my_toggle_button.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.my_toggle_button.setIcon(icon)

        self.verticalLayout_3.addWidget(self.my_toggle_button)

        self.widget = QCustomSlideMenu(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.my_toggle_button.setText(QCoreApplication.translate("MainWindow", u"Toggle Button", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"My Responsive Widget", None))
    # retranslateUi

