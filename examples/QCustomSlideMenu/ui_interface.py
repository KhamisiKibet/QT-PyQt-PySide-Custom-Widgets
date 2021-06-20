# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceWLSHkW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 356)
        self.my_toggle_button = QWidget(MainWindow)
        self.my_toggle_button.setObjectName(u"my_toggle_button")
        self.my_widget_name = QCustomSlideMenu(self.my_toggle_button)
        self.my_widget_name.setObjectName(u"my_widget_name")
        self.my_widget_name.setGeometry(QRect(220, 60, 261, 211))
        self.my_widget_name.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label = QLabel(self.my_widget_name)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 101, 18))
        self.pushButton = QPushButton(self.my_toggle_button)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 131, 34))
        MainWindow.setCentralWidget(self.my_toggle_button)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"My Widget", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Toggle Button ", None))
    # retranslateUi

