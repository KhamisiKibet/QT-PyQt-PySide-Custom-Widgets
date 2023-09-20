# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacetOYTLz.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 471)
        MainWindow.setMaximumSize(QSize(800, 471))
        MainWindow.setStyleSheet(u"*{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color:  #fff;\n"
"}\n"
"#centralwidget, #widget{\n"
"    background-color: #283a4d;\n"
"}\n"
"#frame_4, #frame_5, #frame_8, #frame_9, #frame_12{\n"
"	border-bottom: 1px solid  #17222d;\n"
"	border-radius: 10px;\n"
"}\n"
"#label_24{\n"
"	border: 1px solid #17222d;\n"
"	border-radius: 25px;\n"
"}\n"
"#frame_15{\n"
"	border-bottom: 1px solid #17222d;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 471))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.helpBtn = QPushButton(self.frame)
        self.helpBtn.setObjectName(u"helpBtn")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.helpBtn)

        self.show_hide_exit_prompt = QPushButton(self.frame)
        self.show_hide_exit_prompt.setObjectName(u"show_hide_exit_prompt")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_hide_exit_prompt.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.show_hide_exit_prompt)


        self.horizontalLayout_3.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.exitPrompt = QCustomSlideMenu(self.centralwidget)
        self.exitPrompt.setObjectName(u"exitPrompt")
        self.exitPrompt.setMinimumSize(QSize(788, 0))
        self.exitPrompt.setMaximumSize(QSize(788, 0))
        self.verticalLayout_2 = QVBoxLayout(self.exitPrompt)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.widget_2 = QWidget(self.exitPrompt)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.close_exit_prompt = QPushButton(self.widget_2)
        self.close_exit_prompt.setObjectName(u"close_exit_prompt")

        self.horizontalLayout_5.addWidget(self.close_exit_prompt, 0, Qt.AlignHCenter)

        self.exit = QPushButton(self.widget_2)
        self.exit.setObjectName(u"exit")

        self.horizontalLayout_5.addWidget(self.exit, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.exitPrompt, 0, Qt.AlignRight|Qt.AlignTop)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMinimumSize(QSize(788, 279))
        self.horizontalLayout_2 = QHBoxLayout(self.main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.widget_3 = QWidget(self.main)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 491, 396))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomQStackedWidget(self.scrollAreaWidgetContents)
        self.mainPages.setObjectName(u"mainPages")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.horizontalLayout_7 = QHBoxLayout(self.loginPage)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.loginPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(300, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/images/images/2.png"))
        self.label_10.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_10)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.loginPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 50))
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setPixmap(QPixmap(u":/icons/Icons/user.png"))
        self.label_5.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.loginResponse = QLabel(self.frame_3)
        self.loginResponse.setObjectName(u"loginResponse")
        self.loginResponse.setEnabled(True)
        font1 = QFont()
        font1.setItalic(True)
        font1.setUnderline(True)
        self.loginResponse.setFont(font1)
        self.loginResponse.setAlignment(Qt.AlignCenter)
        self.loginResponse.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.loginResponse)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.loginUsername = QLineEdit(self.frame_4)
        self.loginUsername.setObjectName(u"loginUsername")

        self.horizontalLayout_9.addWidget(self.loginUsername)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.showHideLoginPass = QPushButton(self.frame_5)
        self.showHideLoginPass.setObjectName(u"showHideLoginPass")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/eye-off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showHideLoginPass.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.showHideLoginPass)

        self.loginPassword = QLineEdit(self.frame_5)
        self.loginPassword.setObjectName(u"loginPassword")
        self.loginPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_10.addWidget(self.loginPassword)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.submitLogin = QPushButton(self.frame_3)
        self.submitLogin.setObjectName(u"submitLogin")

        self.verticalLayout_7.addWidget(self.submitLogin)

        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        font2 = QFont()
        font2.setUnderline(True)
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_18)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.signUpBtn = QPushButton(self.frame_6)
        self.signUpBtn.setObjectName(u"signUpBtn")

        self.horizontalLayout_8.addWidget(self.signUpBtn)


        self.verticalLayout_7.addWidget(self.frame_6)


        self.horizontalLayout_7.addWidget(self.frame_3)

        self.mainPages.addWidget(self.loginPage)
        self.signUpPage = QWidget()
        self.signUpPage.setObjectName(u"signUpPage")
        self.horizontalLayout_14 = QHBoxLayout(self.signUpPage)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.signUpPage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(300, 300))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/images/images/1.png"))
        self.label_16.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_16)


        self.horizontalLayout_14.addWidget(self.frame_11)

        self.frame_7 = QFrame(self.signUpPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(300, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 50))
        self.label_11.setMaximumSize(QSize(50, 50))
        self.label_11.setPixmap(QPixmap(u":/icons/Icons/user.png"))
        self.label_11.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)

        self.registerResponse = QLabel(self.frame_7)
        self.registerResponse.setObjectName(u"registerResponse")
        self.registerResponse.setFont(font1)
        self.registerResponse.setAlignment(Qt.AlignCenter)
        self.registerResponse.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.registerResponse)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon2)

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.signup_username = QLineEdit(self.frame_8)
        self.signup_username.setObjectName(u"signup_username")

        self.horizontalLayout_11.addWidget(self.signup_username)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_9.addWidget(self.label_14)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.show_hide_signup_password = QPushButton(self.frame_9)
        self.show_hide_signup_password.setObjectName(u"show_hide_signup_password")
        self.show_hide_signup_password.setIcon(icon3)

        self.horizontalLayout_12.addWidget(self.show_hide_signup_password)

        self.signup_password = QLineEdit(self.frame_9)
        self.signup_password.setObjectName(u"signup_password")
        self.signup_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_12.addWidget(self.signup_password)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.show_hide_signup_conf_password = QPushButton(self.frame_12)
        self.show_hide_signup_conf_password.setObjectName(u"show_hide_signup_conf_password")
        self.show_hide_signup_conf_password.setIcon(icon3)

        self.horizontalLayout_15.addWidget(self.show_hide_signup_conf_password)

        self.signup_conf_password = QLineEdit(self.frame_12)
        self.signup_conf_password.setObjectName(u"signup_conf_password")
        self.signup_conf_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_15.addWidget(self.signup_conf_password)


        self.verticalLayout_9.addWidget(self.frame_12)

        self.signup_btn = QPushButton(self.frame_7)
        self.signup_btn.setObjectName(u"signup_btn")

        self.verticalLayout_9.addWidget(self.signup_btn)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.loginBtn = QPushButton(self.frame_10)
        self.loginBtn.setObjectName(u"loginBtn")

        self.horizontalLayout_13.addWidget(self.loginBtn)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.horizontalLayout_14.addWidget(self.frame_7)

        self.mainPages.addWidget(self.signUpPage)
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.horizontalLayout_20 = QHBoxLayout(self.homePage)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.homePage)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(300, 300))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/images/images/3.png"))
        self.label_20.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_20)


        self.horizontalLayout_20.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.homePage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(300, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_21 = QLabel(self.frame_14)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 50))
        self.label_21.setMaximumSize(QSize(50, 50))
        self.label_21.setPixmap(QPixmap(u":/icons/Icons/unlock.png"))
        self.label_21.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_22, 0, Qt.AlignTop)

        self.appDetails = QLabel(self.frame_14)
        self.appDetails.setObjectName(u"appDetails")
        self.appDetails.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.appDetails)

        self.logoutBtn = QPushButton(self.frame_14)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/log-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon4)

        self.verticalLayout_12.addWidget(self.logoutBtn)


        self.horizontalLayout_20.addWidget(self.frame_14, 0, Qt.AlignVCenter)

        self.mainPages.addWidget(self.homePage)
        self.networkErrorPage = QWidget()
        self.networkErrorPage.setObjectName(u"networkErrorPage")
        self.verticalLayout_14 = QVBoxLayout(self.networkErrorPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_25 = QLabel(self.networkErrorPage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(250, 250))
        self.label_25.setMaximumSize(QSize(250, 250))
        self.label_25.setPixmap(QPixmap(u":/images/images/4.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.label_27 = QLabel(self.networkErrorPage)
        self.label_27.setObjectName(u"label_27")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_27.setFont(font3)
        self.label_27.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_27)

        self.label_29 = QLabel(self.networkErrorPage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_29)

        self.tryAgain = QPushButton(self.networkErrorPage)
        self.tryAgain.setObjectName(u"tryAgain")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/loader.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tryAgain.setIcon(icon5)

        self.verticalLayout_14.addWidget(self.tryAgain, 0, Qt.AlignHCenter)

        self.mainPages.addWidget(self.networkErrorPage)

        self.verticalLayout_6.addWidget(self.mainPages)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.scrollArea)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.userAccount = QCustomSlideMenu(self.main)
        self.userAccount.setObjectName(u"userAccount")
        self.userAccount.setMinimumSize(QSize(300, 267))
        self.userAccount.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.userAccount)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.userAccount)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.scrollArea_2 = QScrollArea(self.userAccount)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 300, 379))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.userAccountPages = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.userAccountPages.setObjectName(u"userAccountPages")
        self.loginAccount = QWidget()
        self.loginAccount.setObjectName(u"loginAccount")
        self.verticalLayout_5 = QVBoxLayout(self.loginAccount)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.loginAccount)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignBottom)

        self.label_23 = QLabel(self.loginAccount)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 100))
        self.label_23.setMaximumSize(QSize(100, 100))
        self.label_23.setPixmap(QPixmap(u":/icons/Icons/lock.png"))
        self.label_23.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_23, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.userAccountPages.addWidget(self.loginAccount)
        self.loggedAccountDetails = QWidget()
        self.loggedAccountDetails.setObjectName(u"loggedAccountDetails")
        self.verticalLayout_13 = QVBoxLayout(self.loggedAccountDetails)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.loggedAccountDetails)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_24 = QLabel(self.frame_15)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(50, 50))
        self.label_24.setMaximumSize(QSize(50, 50))
        self.label_24.setPixmap(QPixmap(u":/icons/Icons/user.png"))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_24)

        self.username = QLabel(self.frame_15)
        self.username.setObjectName(u"username")
        self.username.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.username)


        self.verticalLayout_13.addWidget(self.frame_15, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.loggedAccountDetails)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.app_id = QLabel(self.frame_16)
        self.app_id.setObjectName(u"app_id")
        self.app_id.setWordWrap(True)

        self.gridLayout.addWidget(self.app_id, 0, 1, 1, 1)

        self.app_key = QLabel(self.frame_16)
        self.app_key.setObjectName(u"app_key")
        self.app_key.setWordWrap(True)

        self.gridLayout.addWidget(self.app_key, 1, 1, 1, 1)

        self.label_26 = QLabel(self.frame_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setWordWrap(True)

        self.gridLayout.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_28 = QLabel(self.frame_16)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setWordWrap(True)

        self.gridLayout.addWidget(self.label_28, 1, 0, 1, 1)

        self.label_30 = QLabel(self.frame_16)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setWordWrap(True)

        self.gridLayout.addWidget(self.label_30, 2, 0, 1, 1)

        self.key_date = QLabel(self.frame_16)
        self.key_date.setObjectName(u"key_date")
        self.key_date.setWordWrap(True)

        self.gridLayout.addWidget(self.key_date, 2, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_16, 0, Qt.AlignTop)

        self.logoutUser = QPushButton(self.loggedAccountDetails)
        self.logoutUser.setObjectName(u"logoutUser")
        self.logoutUser.setIcon(icon4)

        self.verticalLayout_13.addWidget(self.logoutUser, 0, Qt.AlignHCenter)

        self.userAccountPages.addWidget(self.loggedAccountDetails)

        self.verticalLayout_4.addWidget(self.userAccountPages)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)


        self.horizontalLayout_2.addWidget(self.userAccount)


        self.verticalLayout.addWidget(self.main)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout = QHBoxLayout(self.footer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.footer)
        self.pushButton.setObjectName(u"pushButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.label_19 = QLabel(self.footer)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout.addWidget(self.label_19, 0, Qt.AlignRight)

        self.checkBox = QCheckBox(self.footer)
        self.checkBox.setObjectName(u"checkBox")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/box.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox.setIcon(icon7)

        self.horizontalLayout.addWidget(self.checkBox)

        self.show_hide_user_account = QPushButton(self.footer)
        self.show_hide_user_account.setObjectName(u"show_hide_user_account")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_hide_user_account.setIcon(icon8)

        self.horizontalLayout.addWidget(self.show_hide_user_account, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)
        self.userAccountPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QT App Settings Session", None))
        self.helpBtn.setText("")
        self.show_hide_exit_prompt.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Exit the app?", None))
        self.close_exit_prompt.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.label_10.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.loginResponse.setText(QCoreApplication.translate("MainWindow", u"Please login below.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.pushButton_2.setText("")
        self.loginUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.showHideLoginPass.setText("")
        self.loginPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.submitLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Forgot Password?", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Not registered?", None))
        self.signUpBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_16.setText("")
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.registerResponse.setText(QCoreApplication.translate("MainWindow", u"Register below", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.pushButton_7.setText("")
        self.signup_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.show_hide_signup_password.setText("")
        self.signup_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.show_hide_signup_conf_password.setText("")
        self.signup_conf_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.signup_btn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Already registered?", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"WELCOME", None))
        self.appDetails.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Username</span>: Username</p><p align=\"center\"><span style=\" font-weight:600;\">App ID:</span> ID</p><p align=\"center\"><span style=\" font-weight:600;\">APP Key</span>: Key</p><p align=\"center\"><span style=\" font-weight:600;\">Expiry Date</span>: Date</p></body></html>", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_25.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Network Error!", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"You need internet connection to login. Please check your connection then try again.", None))
        self.tryAgain.setText(QCoreApplication.translate("MainWindow", u"Try again", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logged Account", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Please Login Or Sign Up", None))
        self.label_23.setText("")
        self.label_24.setText("")
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.app_id.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.app_key.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Application ID", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Application Key", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Key Expiry Date", None))
        self.key_date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.logoutUser.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Light/Dark Theme", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.show_hide_user_account.setText("")
    # retranslateUi

