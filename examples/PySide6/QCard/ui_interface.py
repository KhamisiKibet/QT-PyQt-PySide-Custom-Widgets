# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceUUzKhr.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 471)
        MainWindow.setStyleSheet(u"\n"
"#centralwidget, #widget_4, #widget_5{\n"
"	background-color: #1f232a;\n"
"}\n"
"QWidget{\n"
"	background-color: rgb(34, 38, 56);\n"
"	border-radius: 30px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.card1 = QWidget(self.widget_4)
        self.card1.setObjectName(u"card1")
        self.verticalLayout_2 = QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.card1)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.card1)

        self.card2 = QWidget(self.widget_4)
        self.card2.setObjectName(u"card2")
        self.horizontalLayout_3 = QHBoxLayout(self.card2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.card2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.card2)

        self.card3 = QWidget(self.widget_4)
        self.card3.setObjectName(u"card3")
        self.horizontalLayout_4 = QHBoxLayout(self.card3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.card3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.card3)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.card4 = QWidget(self.widget_5)
        self.card4.setObjectName(u"card4")
        self.horizontalLayout_7 = QHBoxLayout(self.card4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.card4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.card4)

        self.card5 = QWidget(self.widget_5)
        self.card5.setObjectName(u"card5")
        self.horizontalLayout_6 = QHBoxLayout(self.card5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.card5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)


        self.horizontalLayout_2.addWidget(self.card5)

        self.card6 = QWidget(self.widget_5)
        self.card6.setObjectName(u"card6")
        self.horizontalLayout_5 = QHBoxLayout(self.card6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.card6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.horizontalLayout_2.addWidget(self.card6)


        self.verticalLayout.addWidget(self.widget_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Card 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Card 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Card 3", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Card 4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Card 5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Card 6", None))
    # retranslateUi

