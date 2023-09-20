# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceiewPRG.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(441, 261)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_3 = QCustomCheckBox(self.frame)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_2 = QCustomCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox = QCustomCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox 1", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox 2", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox 3", None))
    # retranslateUi

