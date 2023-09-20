# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceArehuJ.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(605, 367)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.myStackedWidget = QCustomQStackedWidget(self.centralwidget)
        self.myStackedWidget.setObjectName(u"myStackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 90, 171, 131))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.myStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 100, 241, 191))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #000;")
        self.myStackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 90, 211, 151))
        self.label_3.setFont(font)
        self.myStackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.myStackedWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nxt = QPushButton(self.frame)
        self.nxt.setObjectName(u"nxt")

        self.horizontalLayout.addWidget(self.nxt)

        self.page1 = QPushButton(self.frame)
        self.page1.setObjectName(u"page1")

        self.horizontalLayout.addWidget(self.page1)

        self.page2 = QPushButton(self.frame)
        self.page2.setObjectName(u"page2")

        self.horizontalLayout.addWidget(self.page2)

        self.prev = QPushButton(self.frame)
        self.prev.setObjectName(u"prev")

        self.horizontalLayout.addWidget(self.prev)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        self.nxt.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.page1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.page2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.prev.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
    # retranslateUi

