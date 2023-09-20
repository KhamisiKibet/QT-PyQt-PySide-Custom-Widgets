# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceeTwLAy.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QScrollArea, QSizePolicy, QSlider,
    QTabWidget, QVBoxLayout, QWidget)

from Custom_Widgets.AnalogGaugeWidget import AnalogGaugeWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 431)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gauge_container = QWidget(self.centralwidget)
        self.gauge_container.setObjectName(u"gauge_container")
        self.gridLayout_4 = QGridLayout(self.gauge_container)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_5 = QWidget(self.gauge_container)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.widget = AnalogGaugeWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(300, 300))
        self.widget.setMaximumSize(QSize(600, 600))
        self.widget.setBaseSize(QSize(300, 300))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.widget)


        self.gridLayout_4.addWidget(self.widget_5, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.gauge_container)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.widget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_28.setFont(font)

        self.verticalLayout_7.addWidget(self.label_28)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.widget_15 = QWidget(self.widget1)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_8 = QVBoxLayout(self.widget_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Parameter = QTabWidget(self.widget_15)
        self.Parameter.setObjectName(u"Parameter")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_16 = QGridLayout(self.tab_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.scrollArea = QScrollArea(self.tab_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 350, 367))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.InnenRadiusSlider = QSlider(self.widget_2)
        self.InnenRadiusSlider.setObjectName(u"InnenRadiusSlider")
        self.InnenRadiusSlider.setMaximum(1000)
        self.InnenRadiusSlider.setValue(0)
        self.InnenRadiusSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.InnenRadiusSlider, 2, 1, 1, 1)

        self.GaugeStartSlider = QSlider(self.widget_2)
        self.GaugeStartSlider.setObjectName(u"GaugeStartSlider")
        self.GaugeStartSlider.setMaximum(360)
        self.GaugeStartSlider.setValue(0)
        self.GaugeStartSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.GaugeStartSlider, 3, 1, 1, 1)

        self.lcdInnerRadius = QLCDNumber(self.widget_2)
        self.lcdInnerRadius.setObjectName(u"lcdInnerRadius")
        self.lcdInnerRadius.setFrameShape(QFrame.NoFrame)
        self.lcdInnerRadius.setFrameShadow(QFrame.Plain)
        self.lcdInnerRadius.setLineWidth(0)
        self.lcdInnerRadius.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdInnerRadius, 2, 2, 1, 1)

        self.offsetSlider = QSlider(self.widget_2)
        self.offsetSlider.setObjectName(u"offsetSlider")
        self.offsetSlider.setMinimum(-360)
        self.offsetSlider.setMaximum(360)
        self.offsetSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.offsetSlider, 5, 1, 1, 1)

        self.lcdGaugeOffset = QLCDNumber(self.widget_2)
        self.lcdGaugeOffset.setObjectName(u"lcdGaugeOffset")
        self.lcdGaugeOffset.setFrameShape(QFrame.NoFrame)
        self.lcdGaugeOffset.setFrameShadow(QFrame.Plain)
        self.lcdGaugeOffset.setLineWidth(0)
        self.lcdGaugeOffset.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdGaugeOffset, 5, 2, 1, 1)

        self.GaugeSizeSlider = QSlider(self.widget_2)
        self.GaugeSizeSlider.setObjectName(u"GaugeSizeSlider")
        self.GaugeSizeSlider.setMaximum(360)
        self.GaugeSizeSlider.setValue(0)
        self.GaugeSizeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.GaugeSizeSlider, 4, 1, 1, 1)

        self.ActualValueSlider = QSlider(self.widget_2)
        self.ActualValueSlider.setObjectName(u"ActualValueSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ActualValueSlider.sizePolicy().hasHeightForWidth())
        self.ActualValueSlider.setSizePolicy(sizePolicy3)
        self.ActualValueSlider.setMaximum(200)
        self.ActualValueSlider.setValue(0)
        self.ActualValueSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.ActualValueSlider, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lcdGaugeStart = QLCDNumber(self.widget_2)
        self.lcdGaugeStart.setObjectName(u"lcdGaugeStart")
        self.lcdGaugeStart.setFrameShape(QFrame.NoFrame)
        self.lcdGaugeStart.setFrameShadow(QFrame.Plain)
        self.lcdGaugeStart.setLineWidth(0)
        self.lcdGaugeStart.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdGaugeStart, 3, 2, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.lcdGaugeValue = QLCDNumber(self.widget_2)
        self.lcdGaugeValue.setObjectName(u"lcdGaugeValue")
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        self.lcdGaugeValue.setFont(font1)
        self.lcdGaugeValue.setFrameShape(QFrame.NoFrame)
        self.lcdGaugeValue.setFrameShadow(QFrame.Plain)
        self.lcdGaugeValue.setLineWidth(0)
        self.lcdGaugeValue.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdGaugeValue, 0, 2, 1, 1)

        self.lcdGaugeSize = QLCDNumber(self.widget_2)
        self.lcdGaugeSize.setObjectName(u"lcdGaugeSize")
        self.lcdGaugeSize.setFrameShape(QFrame.NoFrame)
        self.lcdGaugeSize.setFrameShadow(QFrame.Plain)
        self.lcdGaugeSize.setLineWidth(0)
        self.lcdGaugeSize.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdGaugeSize, 4, 2, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.OuterRadiusSlider = QSlider(self.widget_2)
        self.OuterRadiusSlider.setObjectName(u"OuterRadiusSlider")
        self.OuterRadiusSlider.setMaximum(1000)
        self.OuterRadiusSlider.setValue(0)
        self.OuterRadiusSlider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.OuterRadiusSlider, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lcdOuterRadius = QLCDNumber(self.widget_2)
        self.lcdOuterRadius.setObjectName(u"lcdOuterRadius")
        self.lcdOuterRadius.setFrameShape(QFrame.NoFrame)
        self.lcdOuterRadius.setFrameShadow(QFrame.Plain)
        self.lcdOuterRadius.setLineWidth(0)
        self.lcdOuterRadius.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcdOuterRadius, 1, 2, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.CB_ShowBarGraph = QCheckBox(self.widget_3)
        self.CB_ShowBarGraph.setObjectName(u"CB_ShowBarGraph")
        self.CB_ShowBarGraph.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_ShowBarGraph, 0, 1, 1, 1)

        self.CB_fineGrid = QCheckBox(self.widget_3)
        self.CB_fineGrid.setObjectName(u"CB_fineGrid")
        self.CB_fineGrid.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_fineGrid, 3, 1, 1, 1)

        self.CB_ValueText = QCheckBox(self.widget_3)
        self.CB_ValueText.setObjectName(u"CB_ValueText")
        self.CB_ValueText.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_ValueText, 2, 0, 1, 1)

        self.CB_CenterPoint = QCheckBox(self.widget_3)
        self.CB_CenterPoint.setObjectName(u"CB_CenterPoint")
        self.CB_CenterPoint.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_CenterPoint, 2, 1, 1, 1)

        self.CB_barGraph = QCheckBox(self.widget_3)
        self.CB_barGraph.setObjectName(u"CB_barGraph")
        self.CB_barGraph.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_barGraph, 0, 0, 1, 1)

        self.CB_Grid = QCheckBox(self.widget_3)
        self.CB_Grid.setObjectName(u"CB_Grid")
        self.CB_Grid.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_Grid, 3, 0, 1, 1)

        self.CB_Needle = QCheckBox(self.widget_3)
        self.CB_Needle.setObjectName(u"CB_Needle")
        self.CB_Needle.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_Needle, 4, 0, 1, 1)

        self.CB_ScaleText = QCheckBox(self.widget_3)
        self.CB_ScaleText.setObjectName(u"CB_ScaleText")
        self.CB_ScaleText.setChecked(True)

        self.gridLayout_6.addWidget(self.CB_ScaleText, 4, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_3, 0, Qt.AlignTop)

        self.ActualValue = QLCDNumber(self.scrollAreaWidgetContents)
        self.ActualValue.setObjectName(u"ActualValue")
        self.ActualValue.setFrameShape(QFrame.NoFrame)
        self.ActualValue.setFrameShadow(QFrame.Sunken)
        self.ActualValue.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_3.addWidget(self.ActualValue, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_16.addWidget(self.scrollArea, 3, 0, 1, 1)

        self.Parameter.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_15 = QGridLayout(self.tab)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 240, 784))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_10 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_2 = QVBoxLayout(self.widget_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_10)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_2 = QGridLayout(self.widget_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.lcdNumber_Red_Needle = QLCDNumber(self.widget_9)
        self.lcdNumber_Red_Needle.setObjectName(u"lcdNumber_Red_Needle")
        self.lcdNumber_Red_Needle.setFont(font1)
        self.lcdNumber_Red_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_Needle.setLineWidth(0)
        self.lcdNumber_Red_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Red_Needle, 0, 2, 1, 1)

        self.GreenSlider_Needle = QSlider(self.widget_9)
        self.GreenSlider_Needle.setObjectName(u"GreenSlider_Needle")
        self.GreenSlider_Needle.setMaximum(255)
        self.GreenSlider_Needle.setValue(50)
        self.GreenSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.GreenSlider_Needle, 1, 1, 1, 1)

        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.lcdNumber_Green_Needle = QLCDNumber(self.widget_9)
        self.lcdNumber_Green_Needle.setObjectName(u"lcdNumber_Green_Needle")
        self.lcdNumber_Green_Needle.setFont(font1)
        self.lcdNumber_Green_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_Needle.setLineWidth(0)
        self.lcdNumber_Green_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Green_Needle, 1, 2, 1, 1)

        self.lcdNumber_Blue_Needle = QLCDNumber(self.widget_9)
        self.lcdNumber_Blue_Needle.setObjectName(u"lcdNumber_Blue_Needle")
        self.lcdNumber_Blue_Needle.setFont(font1)
        self.lcdNumber_Blue_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_Needle.setLineWidth(0)
        self.lcdNumber_Blue_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Blue_Needle, 2, 2, 1, 1)

        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.BlueSlider_Needle = QSlider(self.widget_9)
        self.BlueSlider_Needle.setObjectName(u"BlueSlider_Needle")
        self.BlueSlider_Needle.setMaximum(255)
        self.BlueSlider_Needle.setValue(50)
        self.BlueSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.BlueSlider_Needle, 2, 1, 1, 1)

        self.TrancSlider_Needle = QSlider(self.widget_9)
        self.TrancSlider_Needle.setObjectName(u"TrancSlider_Needle")
        self.TrancSlider_Needle.setMaximum(255)
        self.TrancSlider_Needle.setValue(255)
        self.TrancSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.TrancSlider_Needle, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_Needle = QLCDNumber(self.widget_9)
        self.lcdNumber_Trancparency_Needle.setObjectName(u"lcdNumber_Trancparency_Needle")
        self.lcdNumber_Trancparency_Needle.setFont(font1)
        self.lcdNumber_Trancparency_Needle.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_Needle.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_Needle.setLineWidth(0)
        self.lcdNumber_Trancparency_Needle.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_Trancparency_Needle, 3, 2, 1, 1)

        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.RedSlider_Needle = QSlider(self.widget_9)
        self.RedSlider_Needle.setObjectName(u"RedSlider_Needle")
        self.RedSlider_Needle.setMaximum(255)
        self.RedSlider_Needle.setValue(50)
        self.RedSlider_Needle.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.RedSlider_Needle, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_9, 3, 0, 1, 1)

        self.label_32 = QLabel(self.widget_4)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_3.addWidget(self.label_32, 0, 0, 1, 1)

        self.theme_comboBox = QComboBox(self.widget_4)
        self.theme_comboBox.addItem("")
        self.theme_comboBox.setObjectName(u"theme_comboBox")

        self.gridLayout_3.addWidget(self.theme_comboBox, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.label_29 = QLabel(self.widget_10)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_2.addWidget(self.label_29)

        self.widget_6 = QWidget(self.widget_10)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_9 = QGridLayout(self.widget_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_10 = QGridLayout(self.widget_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_16 = QLabel(self.widget_8)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_10.addWidget(self.label_16, 1, 0, 1, 1)

        self.lcdNumber_Red_NeedleDrag = QLCDNumber(self.widget_8)
        self.lcdNumber_Red_NeedleDrag.setObjectName(u"lcdNumber_Red_NeedleDrag")
        self.lcdNumber_Red_NeedleDrag.setFont(font1)
        self.lcdNumber_Red_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Red_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Red_NeedleDrag, 0, 2, 1, 1)

        self.GreenSlider_NeedleDrag = QSlider(self.widget_8)
        self.GreenSlider_NeedleDrag.setObjectName(u"GreenSlider_NeedleDrag")
        self.GreenSlider_NeedleDrag.setMaximum(255)
        self.GreenSlider_NeedleDrag.setValue(50)
        self.GreenSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.GreenSlider_NeedleDrag, 1, 1, 1, 1)

        self.label_17 = QLabel(self.widget_8)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_10.addWidget(self.label_17, 3, 0, 1, 1)

        self.lcdNumber_Green_NeedleDrag = QLCDNumber(self.widget_8)
        self.lcdNumber_Green_NeedleDrag.setObjectName(u"lcdNumber_Green_NeedleDrag")
        self.lcdNumber_Green_NeedleDrag.setFont(font1)
        self.lcdNumber_Green_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Green_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Green_NeedleDrag, 1, 2, 1, 1)

        self.lcdNumber_Blue_NeedleDrag = QLCDNumber(self.widget_8)
        self.lcdNumber_Blue_NeedleDrag.setObjectName(u"lcdNumber_Blue_NeedleDrag")
        self.lcdNumber_Blue_NeedleDrag.setFont(font1)
        self.lcdNumber_Blue_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Blue_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Blue_NeedleDrag, 2, 2, 1, 1)

        self.label_18 = QLabel(self.widget_8)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_10.addWidget(self.label_18, 2, 0, 1, 1)

        self.BlueSlider_NeedleDrag = QSlider(self.widget_8)
        self.BlueSlider_NeedleDrag.setObjectName(u"BlueSlider_NeedleDrag")
        self.BlueSlider_NeedleDrag.setMaximum(255)
        self.BlueSlider_NeedleDrag.setValue(50)
        self.BlueSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.BlueSlider_NeedleDrag, 2, 1, 1, 1)

        self.TrancSlider_NeedleDrag = QSlider(self.widget_8)
        self.TrancSlider_NeedleDrag.setObjectName(u"TrancSlider_NeedleDrag")
        self.TrancSlider_NeedleDrag.setMaximum(255)
        self.TrancSlider_NeedleDrag.setValue(255)
        self.TrancSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.TrancSlider_NeedleDrag, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_NeedleDrag = QLCDNumber(self.widget_8)
        self.lcdNumber_Trancparency_NeedleDrag.setObjectName(u"lcdNumber_Trancparency_NeedleDrag")
        self.lcdNumber_Trancparency_NeedleDrag.setFont(font1)
        self.lcdNumber_Trancparency_NeedleDrag.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_NeedleDrag.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_NeedleDrag.setLineWidth(0)
        self.lcdNumber_Trancparency_NeedleDrag.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_10.addWidget(self.lcdNumber_Trancparency_NeedleDrag, 3, 2, 1, 1)

        self.label_19 = QLabel(self.widget_8)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_10.addWidget(self.label_19, 0, 0, 1, 1)

        self.RedSlider_NeedleDrag = QSlider(self.widget_8)
        self.RedSlider_NeedleDrag.setObjectName(u"RedSlider_NeedleDrag")
        self.RedSlider_NeedleDrag.setMaximum(255)
        self.RedSlider_NeedleDrag.setValue(50)
        self.RedSlider_NeedleDrag.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.RedSlider_NeedleDrag, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget_8, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.label_30 = QLabel(self.widget_10)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_2.addWidget(self.label_30)

        self.widget_7 = QWidget(self.widget_10)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_11 = QGridLayout(self.widget_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_12 = QGridLayout(self.widget_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lcdNumber_Green_Scale = QLCDNumber(self.widget_11)
        self.lcdNumber_Green_Scale.setObjectName(u"lcdNumber_Green_Scale")
        self.lcdNumber_Green_Scale.setFont(font1)
        self.lcdNumber_Green_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_Scale.setLineWidth(0)
        self.lcdNumber_Green_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Green_Scale, 1, 2, 1, 1)

        self.RedSlider_Scale = QSlider(self.widget_11)
        self.RedSlider_Scale.setObjectName(u"RedSlider_Scale")
        self.RedSlider_Scale.setMaximum(255)
        self.RedSlider_Scale.setValue(50)
        self.RedSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.RedSlider_Scale, 0, 1, 1, 1)

        self.label_20 = QLabel(self.widget_11)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_12.addWidget(self.label_20, 1, 0, 1, 1)

        self.BlueSlider_Scale = QSlider(self.widget_11)
        self.BlueSlider_Scale.setObjectName(u"BlueSlider_Scale")
        self.BlueSlider_Scale.setMaximum(255)
        self.BlueSlider_Scale.setValue(50)
        self.BlueSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.BlueSlider_Scale, 2, 1, 1, 1)

        self.lcdNumber_Blue_Scale = QLCDNumber(self.widget_11)
        self.lcdNumber_Blue_Scale.setObjectName(u"lcdNumber_Blue_Scale")
        self.lcdNumber_Blue_Scale.setFont(font1)
        self.lcdNumber_Blue_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_Scale.setLineWidth(0)
        self.lcdNumber_Blue_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Blue_Scale, 2, 2, 1, 1)

        self.TrancSlider_Scale = QSlider(self.widget_11)
        self.TrancSlider_Scale.setObjectName(u"TrancSlider_Scale")
        self.TrancSlider_Scale.setMaximum(255)
        self.TrancSlider_Scale.setValue(255)
        self.TrancSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.TrancSlider_Scale, 3, 1, 1, 1)

        self.GreenSlider_Scale = QSlider(self.widget_11)
        self.GreenSlider_Scale.setObjectName(u"GreenSlider_Scale")
        self.GreenSlider_Scale.setMaximum(255)
        self.GreenSlider_Scale.setValue(50)
        self.GreenSlider_Scale.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.GreenSlider_Scale, 1, 1, 1, 1)

        self.lcdNumber_Trancparency_Scale = QLCDNumber(self.widget_11)
        self.lcdNumber_Trancparency_Scale.setObjectName(u"lcdNumber_Trancparency_Scale")
        self.lcdNumber_Trancparency_Scale.setFont(font1)
        self.lcdNumber_Trancparency_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_Scale.setLineWidth(0)
        self.lcdNumber_Trancparency_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Trancparency_Scale, 3, 2, 1, 1)

        self.label_21 = QLabel(self.widget_11)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_12.addWidget(self.label_21, 3, 0, 1, 1)

        self.label_23 = QLabel(self.widget_11)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_12.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_22 = QLabel(self.widget_11)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_12.addWidget(self.label_22, 2, 0, 1, 1)

        self.lcdNumber_Red_Scale = QLCDNumber(self.widget_11)
        self.lcdNumber_Red_Scale.setObjectName(u"lcdNumber_Red_Scale")
        self.lcdNumber_Red_Scale.setFont(font1)
        self.lcdNumber_Red_Scale.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_Scale.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_Scale.setLineWidth(0)
        self.lcdNumber_Red_Scale.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_12.addWidget(self.lcdNumber_Red_Scale, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.widget_11, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_13 = QGridLayout(self.widget_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_14 = QGridLayout(self.widget_13)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_24 = QLabel(self.widget_13)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_14.addWidget(self.label_24, 1, 0, 1, 1)

        self.lcdNumber_Red_Display = QLCDNumber(self.widget_13)
        self.lcdNumber_Red_Display.setObjectName(u"lcdNumber_Red_Display")
        self.lcdNumber_Red_Display.setFont(font1)
        self.lcdNumber_Red_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Red_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Red_Display.setLineWidth(0)
        self.lcdNumber_Red_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Red_Display, 0, 2, 1, 1)

        self.GreenSlider_Display = QSlider(self.widget_13)
        self.GreenSlider_Display.setObjectName(u"GreenSlider_Display")
        self.GreenSlider_Display.setMaximum(255)
        self.GreenSlider_Display.setValue(50)
        self.GreenSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.GreenSlider_Display, 1, 1, 1, 1)

        self.label_25 = QLabel(self.widget_13)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_14.addWidget(self.label_25, 3, 0, 1, 1)

        self.lcdNumber_Green_Display = QLCDNumber(self.widget_13)
        self.lcdNumber_Green_Display.setObjectName(u"lcdNumber_Green_Display")
        self.lcdNumber_Green_Display.setFont(font1)
        self.lcdNumber_Green_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Green_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Green_Display.setLineWidth(0)
        self.lcdNumber_Green_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Green_Display, 1, 2, 1, 1)

        self.lcdNumber_Blue_Display = QLCDNumber(self.widget_13)
        self.lcdNumber_Blue_Display.setObjectName(u"lcdNumber_Blue_Display")
        self.lcdNumber_Blue_Display.setFont(font1)
        self.lcdNumber_Blue_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Blue_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Blue_Display.setLineWidth(0)
        self.lcdNumber_Blue_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Blue_Display, 2, 2, 1, 1)

        self.label_26 = QLabel(self.widget_13)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_14.addWidget(self.label_26, 2, 0, 1, 1)

        self.BlueSlider_Display = QSlider(self.widget_13)
        self.BlueSlider_Display.setObjectName(u"BlueSlider_Display")
        self.BlueSlider_Display.setMaximum(255)
        self.BlueSlider_Display.setValue(50)
        self.BlueSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.BlueSlider_Display, 2, 1, 1, 1)

        self.TrancSlider_Display = QSlider(self.widget_13)
        self.TrancSlider_Display.setObjectName(u"TrancSlider_Display")
        self.TrancSlider_Display.setMaximum(255)
        self.TrancSlider_Display.setValue(255)
        self.TrancSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.TrancSlider_Display, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_Display = QLCDNumber(self.widget_13)
        self.lcdNumber_Trancparency_Display.setObjectName(u"lcdNumber_Trancparency_Display")
        self.lcdNumber_Trancparency_Display.setFont(font1)
        self.lcdNumber_Trancparency_Display.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_Display.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_Display.setLineWidth(0)
        self.lcdNumber_Trancparency_Display.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_14.addWidget(self.lcdNumber_Trancparency_Display, 3, 2, 1, 1)

        self.label_27 = QLabel(self.widget_13)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_14.addWidget(self.label_27, 0, 0, 1, 1)

        self.RedSlider_Display = QSlider(self.widget_13)
        self.RedSlider_Display.setObjectName(u"RedSlider_Display")
        self.RedSlider_Display.setMaximum(255)
        self.RedSlider_Display.setValue(50)
        self.RedSlider_Display.setOrientation(Qt.Horizontal)

        self.gridLayout_14.addWidget(self.RedSlider_Display, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.widget_13, 1, 0, 1, 1)

        self.label_31 = QLabel(self.widget_12)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_13.addWidget(self.label_31, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_12)


        self.verticalLayout_4.addWidget(self.widget_10)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_15.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.Parameter.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_3 = QScrollArea(self.tab_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 350, 245))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_14 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_7 = QGridLayout(self.widget_14)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_12 = QLabel(self.widget_14)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)

        self.lcdMinVal = QLCDNumber(self.widget_14)
        self.lcdMinVal.setObjectName(u"lcdMinVal")
        self.lcdMinVal.setFont(font1)
        self.lcdMinVal.setFrameShape(QFrame.NoFrame)
        self.lcdMinVal.setFrameShadow(QFrame.Plain)
        self.lcdMinVal.setLineWidth(0)
        self.lcdMinVal.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdMinVal, 0, 2, 1, 1)

        self.MaxValueSlider = QSlider(self.widget_14)
        self.MaxValueSlider.setObjectName(u"MaxValueSlider")
        self.MaxValueSlider.setMaximum(1100)
        self.MaxValueSlider.setSingleStep(10)
        self.MaxValueSlider.setValue(1100)
        self.MaxValueSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MaxValueSlider, 1, 1, 1, 1)

        self.label_13 = QLabel(self.widget_14)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 3, 0, 1, 1)

        self.lcdMaxVal = QLCDNumber(self.widget_14)
        self.lcdMaxVal.setObjectName(u"lcdMaxVal")
        self.lcdMaxVal.setFont(font1)
        self.lcdMaxVal.setFrameShape(QFrame.NoFrame)
        self.lcdMaxVal.setFrameShadow(QFrame.Plain)
        self.lcdMaxVal.setLineWidth(0)
        self.lcdMaxVal.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdMaxVal, 1, 2, 1, 1)

        self.lcdScalaCount = QLCDNumber(self.widget_14)
        self.lcdScalaCount.setObjectName(u"lcdScalaCount")
        self.lcdScalaCount.setFont(font1)
        self.lcdScalaCount.setFrameShape(QFrame.NoFrame)
        self.lcdScalaCount.setFrameShadow(QFrame.Plain)
        self.lcdScalaCount.setLineWidth(0)
        self.lcdScalaCount.setSegmentStyle(QLCDNumber.Flat)
        self.lcdScalaCount.setProperty("intValue", 10)

        self.gridLayout_7.addWidget(self.lcdScalaCount, 2, 2, 1, 1)

        self.label_14 = QLabel(self.widget_14)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 2, 0, 1, 1)

        self.MainGridSlider = QSlider(self.widget_14)
        self.MainGridSlider.setObjectName(u"MainGridSlider")
        self.MainGridSlider.setMinimum(1)
        self.MainGridSlider.setMaximum(20)
        self.MainGridSlider.setValue(10)
        self.MainGridSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MainGridSlider, 2, 1, 1, 1)

        self.TrancSlider_2 = QSlider(self.widget_14)
        self.TrancSlider_2.setObjectName(u"TrancSlider_2")
        self.TrancSlider_2.setMaximum(255)
        self.TrancSlider_2.setValue(255)
        self.TrancSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.TrancSlider_2, 3, 1, 1, 1)

        self.lcdNumber_Trancparency_2 = QLCDNumber(self.widget_14)
        self.lcdNumber_Trancparency_2.setObjectName(u"lcdNumber_Trancparency_2")
        self.lcdNumber_Trancparency_2.setFont(font1)
        self.lcdNumber_Trancparency_2.setFrameShape(QFrame.NoFrame)
        self.lcdNumber_Trancparency_2.setFrameShadow(QFrame.Plain)
        self.lcdNumber_Trancparency_2.setLineWidth(0)
        self.lcdNumber_Trancparency_2.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdNumber_Trancparency_2, 3, 2, 1, 1)

        self.label_15 = QLabel(self.widget_14)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)

        self.MinValueSlider = QSlider(self.widget_14)
        self.MinValueSlider.setObjectName(u"MinValueSlider")
        self.MinValueSlider.setMaximum(100)
        self.MinValueSlider.setValue(0)
        self.MinValueSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MinValueSlider, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_14, 0, Qt.AlignTop)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_8.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.Parameter.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.Parameter)


        self.verticalLayout_6.addWidget(self.widget_15)


        self.horizontalLayout_2.addWidget(self.widget1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Parameter.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AnalogGaugeWidget_Demo", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ANALOG GAUGE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"OuterRadius", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gauge Size", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gauge Start", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"InnenRadius", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.CB_ShowBarGraph.setText(QCoreApplication.translate("MainWindow", u"Show BarGraph", None))
        self.CB_fineGrid.setText(QCoreApplication.translate("MainWindow", u"Show fine Scale Grid", None))
        self.CB_ValueText.setText(QCoreApplication.translate("MainWindow", u"Show Display", None))
        self.CB_CenterPoint.setText(QCoreApplication.translate("MainWindow", u"Show Center Point", None))
        self.CB_barGraph.setText(QCoreApplication.translate("MainWindow", u"Disable BarGraph Marker", None))
        self.CB_Grid.setText(QCoreApplication.translate("MainWindow", u"Show Scale Grid", None))
        self.CB_Needle.setText(QCoreApplication.translate("MainWindow", u"Show Needle", None))
        self.CB_ScaleText.setText(QCoreApplication.translate("MainWindow", u"Show Scale Text", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Needle Color", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Gauge Theme", None))
        self.theme_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))

        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Needle Color On Drag", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Scale Text Color", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Trancparency", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Value Text Label Color", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Max Value", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Additional", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Grid Divider", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Min Value", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Min, Max Ranges", None))
    # retranslateUi

