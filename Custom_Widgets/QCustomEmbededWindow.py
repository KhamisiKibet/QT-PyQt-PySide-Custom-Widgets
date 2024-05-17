########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

#                 qtpy Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #

import random
from qtpy.QtCore import Qt, QRect, Signal, QEasingCurve, QPropertyAnimation, QSize
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QGraphicsDropShadowEffect, QPushButton, QStyleOption, QStyle, QGraphicsOpacityEffect
from qtpy.QtGui import QColor, QPainter, QPen, QBrush, QPaintEvent

from Custom_Widgets.QCustomTheme import QCustomTheme

class LoadForm(QWidget):
    def __init__(self, form):
        super().__init__()
        # self.ui = Ui_Form()
        self.ui = form
        self.ui.setupUi(self)

        # Check the module name where ui is loaded from
        ui_module_name = form.__module__.split('.')[-1]

        # Replace "ui_" with empty string only at the start
        if ui_module_name.startswith("ui_"):
            self.ui_module_name = ui_module_name[len("ui_"):]

        self.applyThemeIcons()
        
    def applyThemeIcons(self):
        self.customTheme = QCustomTheme()
        self.customTheme.applyIcons(self, ui_file_name=self.ui_module_name)

        self.defaultTheme = self.customTheme.theme

    def paintEvent(self, e: QPaintEvent):
        super().paintEvent(e)
        
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

class QCustomEmbededWindow(QWidget):

    closed = Signal()

    def __init__(self, parent, pos=None, title="New window", icon=None, borderRadius = 10, headerHeight = 25, animationDuration = 500, showForm = None, addWidget = None):
        super().__init__(parent)

        self.borderRadius = borderRadius
        self.setTitle(title)
        self.headerHeight = headerHeight
        self.animationDuration = animationDuration

        self.customTheme = QCustomTheme()

        if pos is None:
            pos = (random.randint(0, self.parent().width()-285), random.randint(0, self.parent().height()-190))
        self.setMinimumSize(285, 100)
        self.setGeometry(pos[0], pos[1], 285, 190)

        self.pressed = None
        self.pressed_pos = None

        self.ly = QVBoxLayout()
        self.ly.setContentsMargins(0, 0, 0, 0)
        self.ly.setAlignment(Qt.AlignTop)
        self.setLayout(self.ly)

        self.header = QWidget()
        self.header.setObjectName("header")
        self.header.setFixedHeight(self.headerHeight)
        self.header_lyt = QHBoxLayout()
        self.header_lyt.setContentsMargins(5, 5, 5, 5)
        self.header_lyt.setSpacing(5)
        self.header_lyt.setAlignment(Qt.AlignTop)
        self.header.setLayout(self.header_lyt)

        self.icon_label = QLabel()
        if icon:
            self.icon_label.setPixmap(icon.pixmap(16, 16))
            self.icon_label.setFixedSize(16, 16)
            self.header_lyt.addWidget(self.icon_label, alignment=Qt.AlignVCenter)

        self.contentwdt = QWidget()
        self.contentwdt.setObjectName("content-area")
        self.content = QVBoxLayout()
        self.contentwdt.setLayout(self.content)

        self.ly.addWidget(self.header)
        self.ly.addWidget(self.contentwdt)

        self.ttl = QLabel(self.title())

        self.close_btn = QPushButton()
        # get default icon:
        self.closeIcon = self.style().standardIcon(QStyle.SP_TitleBarCloseButton).pixmap(QSize(32, 32))
        self.close_btn.setIcon(self.closeIcon)
        self.close_btn.setObjectName("close-button")
        self.close_btn.setFixedSize(self.headerHeight, self.headerHeight)

        self.content_visible = True
        self.last_height = None

        @self.close_btn.clicked.connect
        def slot():
            self.close()
            self.closed.emit()

        self.deta_btn = QPushButton()
        self.shadeIcon = self.style().standardIcon(QStyle.SP_TitleBarShadeButton).pixmap(QSize(32, 32))
        self.unShadeIcon = self.style().standardIcon(QStyle.SP_TitleBarUnshadeButton).pixmap(QSize(32, 32))
        self.deta_btn.setIcon(self.shadeIcon)
        self.deta_btn.setObjectName("hide-button")
        self.deta_btn.setFixedSize(self.headerHeight, self.headerHeight)
        self.deta_btn.clicked.connect(self.showHideContent)
            
        self.header_lyt.addSpacing(10)
        self.header_lyt.addWidget(self.ttl, alignment=Qt.AlignVCenter)
        self.header_lyt.addWidget(self.deta_btn, alignment=Qt.AlignVCenter|Qt.AlignRight)
        self.header_lyt.addWidget(self.close_btn, alignment=Qt.AlignVCenter)

        if showForm:
            self.form = LoadForm(showForm)
            self.addWidget(self.form) 
            try:
                #older versions
                self.form.form =  self.form.ui 
                self.shownForm =  self.form.ui  
            except:
                self.shownForm = None
        
        if addWidget:
            self.addWidget(addWidget) 

    def addWidget(self, widget):
        self.content.addWidget(widget)

    def animateHeight(self, startHeight, endHeight):
        self.animation = QPropertyAnimation(self, b'maximumHeight')
        self.animation.setDuration(self.animationDuration)
        self.animation.setStartValue(startHeight)
        self.animation.setEndValue(endHeight)
        self.animation.setEasingCurve(QEasingCurve.InSine)
        self.animation.start()

    def showHideContent(self):
        if self.content_visible:
            self.content_visible = False
            self.deta_btn.setIcon(self.unShadeIcon)
            self.contentwdt.hide()
            self.animateHeight(self.height(), 0)
        else:
            self.content_visible = True
            self.contentwdt.show()
            self.deta_btn.setIcon(self.shadeIcon)
        
        self.adjustSizeToContent()

    def showEvent(self, e):
        self.adjustSizeToContent()

        """ fade in """
        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)
        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(0)
        opacityAni.setEndValue(1)
        opacityAni.setDuration(self.animationDuration)
        opacityAni.setEasingCurve(QEasingCurve.InSine)
        opacityAni.finished.connect(lambda: self.raiseWidget(opacityAni))
        opacityAni.start()
        super().showEvent(e)

    def raiseWidget(self, opacityEffect):
        self.setShadow()
        self.raise_()

        opacityEffect.deleteLater()
    
    def adjustSizeToContent(self):
        self.adjustSize()
        # Calculate the size hint based on the content
        content_size = self.layout().sizeHint()
        # Add some padding if needed
        padding = 0
        if content_size.width() < 285:
            self.setMinimumSize(285 + padding, content_size.height() + padding)
        else:
            self.setMinimumSize(content_size.width() + padding, content_size.height() + padding)
        self.last_height = self.height()

    def setShadow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QColor(255, 255, 255, 110) if self.customTheme.isAppDarkThemed() else QColor(0, 0, 0, 110))
        self.shadow.setOffset(0, 2)
        self.setGraphicsEffect(self.shadow)

    def __repr__(self):
        return f"<Custom.QCustomEmbededWindow(parent={self.parent()})>"

    def setTitle(self, text):
        self.titleTxt = text

    def title(self):
        return self.titleTxt
    

    def setControlsVisible(self, b):
        if not b:
            self.close_btn.hide()
            self.deta_btn.hide()

        else:
            self.close_btn.show()
            self.deta_btn.show()

    def update(self, *args, **kwargs):
        self.adjustSizeToContent()
        self.anim.update()
        super().update(*args, **kwargs)

    def mousePressEvent(self, event):
        self.startpos = self.pos()
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and event.y() <= self.headerHeight:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

            self.raise_()

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

    def paintEvent(self, event: QPaintEvent):
        super().paintEvent(event)
        
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        painter.end()
