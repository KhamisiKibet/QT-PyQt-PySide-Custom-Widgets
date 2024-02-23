# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infoZkmWVU.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from qtpy.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from qtpy.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(444, 79)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.iconlabel = QLabel(self.frame)
        self.iconlabel.setObjectName(u"iconlabel")
        self.iconlabel.setMinimumSize(QSize(20, 20))
        self.iconlabel.setMaximumSize(QSize(20, 20))
        self.iconlabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.iconlabel, 0, Qt.AlignLeft)

        self.titlelabel = QLabel(self.frame)
        self.titlelabel.setObjectName(u"titlelabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlelabel.sizePolicy().hasHeightForWidth())
        self.titlelabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.titlelabel.setFont(font)
        self.titlelabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.titlelabel)

        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")
        icon = QIcon(QIcon.fromTheme(u"application-exit"))
        self.closeButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.closeButton, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.bodyLabel = QLabel(self.frame_2)
        self.bodyLabel.setObjectName(u"bodyLabel")
        self.bodyLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.bodyLabel)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iconlabel.setText("")
        self.titlelabel.setText(QCoreApplication.translate("Form", u"Title", None))
        self.closeButton.setText("")
        self.bodyLabel.setText(QCoreApplication.translate("Form", u"Body", None))
    # retranslateUi



