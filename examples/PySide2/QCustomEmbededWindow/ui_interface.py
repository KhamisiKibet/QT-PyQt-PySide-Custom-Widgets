# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacejmMwVK.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 430, 526))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(200, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 862, 33))
        self.menumenu = QMenu(self.menubar)
        self.menumenu.setObjectName(u"menumenu")
        self.menunew_menu = QMenu(self.menubar)
        self.menunew_menu.setObjectName(u"menunew_menu")
        self.menuanother_menu = QMenu(self.menubar)
        self.menuanother_menu.setObjectName(u"menuanother_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.menunew_menu.menuAction())
        self.menubar.addAction(self.menuanother_menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add embeded window", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"left bar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Right bar", None))
        self.menumenu.setTitle(QCoreApplication.translate("MainWindow", u"menu", None))
        self.menunew_menu.setTitle(QCoreApplication.translate("MainWindow", u"new menu", None))
        self.menuanother_menu.setTitle(QCoreApplication.translate("MainWindow", u"another menu", None))
    # retranslateUi

