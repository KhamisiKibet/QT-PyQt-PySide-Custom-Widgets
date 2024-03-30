# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emojiPickerhQOwbX.ui'
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
from qtpy.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(230, 163)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_line_edit = QLineEdit(Form)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.verticalLayout.addWidget(self.search_line_edit)

        self.emoji_scroll_area = QScrollArea(Form)
        self.emoji_scroll_area.setObjectName(u"emoji_scroll_area")
        self.emoji_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 210, 84))
        self.emoji_scroll_area_vlayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.emoji_scroll_area_vlayout.setSpacing(5)
        self.emoji_scroll_area_vlayout.setObjectName(u"emoji_scroll_area_vlayout")
        self.emoji_scroll_area_vlayout.setContentsMargins(5, 5, 5, 5)
        self.emoji_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.emoji_scroll_area)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.emoji_information_hlayout = QHBoxLayout(self.widget)
        self.emoji_information_hlayout.setSpacing(0)
        self.emoji_information_hlayout.setObjectName(u"emoji_information_hlayout")
        self.emoji_information_hlayout.setContentsMargins(0, 0, 0, 0)
        self.emoji_image_label = QLabel(self.widget)
        self.emoji_image_label.setObjectName(u"emoji_image_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.emoji_image_label.sizePolicy().hasHeightForWidth())
        self.emoji_image_label.setSizePolicy(sizePolicy1)
        self.emoji_image_label.setMinimumSize(QSize(24, 24))
        self.emoji_image_label.setMaximumSize(QSize(24, 24))

        self.emoji_information_hlayout.addWidget(self.emoji_image_label)

        self.emoji_name_label = QLabel(self.widget)
        self.emoji_name_label.setObjectName(u"emoji_name_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.emoji_name_label.sizePolicy().hasHeightForWidth())
        self.emoji_name_label.setSizePolicy(sizePolicy2)
        self.emoji_name_label.setFont(font)

        self.emoji_information_hlayout.addWidget(self.emoji_name_label)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.search_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"Search Emoji", None))
        self.emoji_image_label.setText("")
        self.emoji_name_label.setText("")
        pass
    # retranslateUi

