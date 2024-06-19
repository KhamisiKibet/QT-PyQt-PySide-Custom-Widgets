# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tooltipWbsliR.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(94, 32)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.iconlabel = QLabel(self.frame)
        self.iconlabel.setObjectName(u"iconlabel")
        self.iconlabel.setMinimumSize(QSize(20, 20))
        self.iconlabel.setMaximumSize(QSize(20, 20))
        self.iconlabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.iconlabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.titlelabel = QLabel(self.frame)
        self.titlelabel.setObjectName(u"titlelabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlelabel.sizePolicy().hasHeightForWidth())
        self.titlelabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.titlelabel.setFont(font1)
        self.titlelabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.titlelabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iconlabel.setText("")
        self.titlelabel.setText(QCoreApplication.translate("Form", u"Title", None))
    # retranslateUi

