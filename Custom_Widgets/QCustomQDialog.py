# coding:utf-8
from qtpy.QtCore import QEasingCurve, QPropertyAnimation, Qt, QEvent, Signal
from qtpy.QtGui import QColor, QResizeEvent, QPalette, QPaintEvent, QPainter, QMouseEvent
from qtpy.QtWidgets import (QDialog, QGraphicsDropShadowEffect, QStyleOption, QStyle, QApplication,
                             QGraphicsOpacityEffect, QWidget)

from Custom_Widgets.components.python.ui_dialog import Ui_Form
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
        
class QCustomQDialog(QDialog, Ui_Form):
    accepted = Signal()
    rejected = Signal()
    
    title = None
    description = None
    # Add some padding if needed
    padding = 0
    margin = 60 #for drop shadow effect
    borderRadius = 0
    windowMovable = False
    animationDuration = 500
    
    maskWidget = None

    def __init__(self, showForm=None, parent=None, addWidget=None, **kwargs):
        QDialog.__init__(self, parent)  # Initialize QDialog parent class
        Ui_Form.__init__(self)  # Initialize Ui_Form parent class
        
        self.window().installEventFilter(self)

        self.setupUi(self)
        
        self.mask_widget = MaskWidget(parent)
        self.mask_widget.hide()
        self.mask_widget.setParent(self.parent())
        self.mask_widget.lower()
        
        # Customize modal based on kwargs
        if 'title' in kwargs:
            self.titleLabel.setText(str(kwargs['title']))
        else:
            # set title to app title
            # self.setTitle(QApplication.instance().applicationName())
            self.titleLabel.hide() 
            
        if 'description' in kwargs:
            self.descriptionLabel.setText(str(kwargs['description']))
        else:
            self.descriptionLabel.hide()  
        
        if 'padding' in kwargs:
            self.padding = int(kwargs['padding'])
            
        if 'yesButtonIcon' in kwargs:
            self.yesButton.setIcon(kwargs['yesButtonIcon'])
            
        if 'cancelButtonIcon' in kwargs:
            self.cancelButton.setIcon(kwargs['cancelButtonIcon'])
            
        if 'yesButtonText' in kwargs:
            self.yesButton.setText(kwargs['yesButtonText'])
            
        if 'cancelButtonText' in kwargs:
            self.cancelButton.setText(kwargs['cancelButtonText'])
            
        if 'animationDuration' in kwargs:
            self.animationDuration = kwargs['animationDuration']
        
        if 'showYesButton' in kwargs:
            if not kwargs['showYesButton']:
                self.hideYesButton()
                
        if 'showCancelButton' in kwargs:
            if not kwargs['showCancelButton']:
                self.hideCancelButton()
        
        if 'setModal' in kwargs:
            if kwargs['setModal']:
                self.setModal(True)
            else:
                self.setModal(False)
            
        if 'frameless' in kwargs and kwargs['frameless']:
            self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            
            if 'windowMovable' in kwargs and kwargs['windowMovable']:
                self.setMovable(True)
                self.titleBar.mousePressEvent = self.mousePressEvent
                self.titleBar.mouseMoveEvent = self.mouseMoveEvent
                self.titleBar.mouseReleaseEvent = self.mouseReleaseEvent

        self.shownForm = None       
        if showForm:
            self.form = LoadForm(showForm)
            self.verticalLayout_2.addWidget(self.form) 
            try:
                #older versions
                self.form.form =  self.form.ui 
                self.shownForm =  self.form.ui  
            except:
                self.shownForm = None
        
        if addWidget:
            self.addWidget(addWidget)

        self.yesButton.clicked.connect(self.__onYesButtonClicked)
        self.cancelButton.clicked.connect(self.__onCancelButtonClicked)
        self.yesButton.setAttribute(Qt.WA_LayoutUsesWidgetRect)
        self.cancelButton.setAttribute(Qt.WA_LayoutUsesWidgetRect)
        
        self.yesButton.setFocus()
        self.setShadowEffect()
    
    def addWidget(self, widget):
        self.verticalLayout_2.addWidget(widget) 
    
    def setShadowEffect(self, blurRadius=60, offset=(0, 10), color=QColor(0,0,0,100)):
        shadowEffect = QGraphicsDropShadowEffect(self.widget)
        shadowEffect.setBlurRadius(blurRadius)
        shadowEffect.setOffset(*offset)
        shadowEffect.setColor(color)
        # self.widget.setGraphicsEffect(None)
        self.widget.setGraphicsEffect(shadowEffect)
            
    def setMovable(self, movable: bool):
        self.windowMovable = movable

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if hasattr(self, 'offset'):
            if self.windowFlags() & Qt.FramelessWindowHint:
                self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if hasattr(self, 'offset'):
            del self.offset

    def __onCancelButtonClicked(self):
        self.reject()
        # self.rejected.emit()

    def __onYesButtonClicked(self):
        self.accept()
        # self.accepted.emit()

    def hideYesButton(self):
        self.yesButton.hide()

    def hideCancelButton(self):
        self.cancelButton.hide()
    
    def paintEvent(self, e: QPaintEvent):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.drawRoundedRect(rect, 6, 6)
        
    def showEvent(self, e):
        self.checkAppTheme()
        if not self.maskWidget:
            self.maskWidget = MaskWidget(parent=self.parent())
            c = 0 if self.isDark() else 255
            self.maskWidget.setStyleSheet(f'background:rgba({c}, {c}, {c}, .7)')
        
        self.maskWidget.show()
        """ fade in """
        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)
        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(0)
        opacityAni.setEndValue(1)
        opacityAni.setDuration(self.animationDuration)
        opacityAni.setEasingCurve(QEasingCurve.InSine)
        opacityAni.finished.connect(opacityEffect.deleteLater)
        opacityAni.start()
        super().showEvent(e)
            
    
    def hideEvent(self, e):
        super().hideEvent(e)
        try:
            self.maskWidget.hide()
        except:
            pass

    def done(self, code):
        """ fade out """
        self.setGraphicsEffect(None)
        opacityEffect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacityEffect)
        opacityAni = QPropertyAnimation(opacityEffect, b'opacity', self)
        opacityAni.setStartValue(.9)
        opacityAni.setEndValue(0)
        opacityAni.setDuration(self.animationDuration)
        opacityAni.setEasingCurve(QEasingCurve.OutSine)
        opacityAni.finished.connect(lambda: QDialog.done(self, code))
        opacityAni.start()
        
        if self.maskWidget:
            self.mask_widget.hide()
            self.maskWidget.deleteLater()
            self.maskWidget = None

    def resizeEvent(self, e):
        # Calculate the size hint based on the content
        self.verticalLayout.setContentsMargins(self.margin, self.margin, self.margin, self.margin)
        content_size = self.layout().sizeHint()
        self.setMinimumSize(content_size.width() + self.padding, content_size.height() + self.padding)
        self.adjustSize()

        self.checkAppTheme()

    def checkAppTheme(self):
        # icons
        if self.shownForm:
            if self.form.defaultTheme != QCustomTheme().theme:
                # theme changed
                self.form.applyThemeIcons()

    def eventFilter(self, obj, e: QEvent):
        if obj is self.window():
            if e.type() == QEvent.Resize:
                re = QResizeEvent(e)
                self.resize(re.size())

        return super().eventFilter(obj, e)
    
    def isDark(self):
        palette = self.palette()
        background_color = palette.color(QPalette.Window)
        # Calculate the luminance of the background color
        luminance = 0.2126 * background_color.red() + 0.7152 * background_color.green() + 0.0722 * background_color.blue()

        # Determine if the background color is dark or light
        if luminance < 128:
            # Dark background
            return True
        else:
            # Light background
            return False
        
class MaskWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Make the widget fill the entire main window
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(self.parent().geometry() if parent else QApplication.primaryScreen().geometry())
                
        self.hide()
        
        if parent:
            parent.installEventFilter(self)
            # parent.resizeEvent = self.resizeEvent
            # parent.moveEvent = self.moveEvent
            
    def resizeEvent(self, event):
        if self.parent():
            parent_width = self.parent().width()
            parent_height = self.parent().height()
            self.setGeometry(0, 0, parent_width, parent_height)

    def moveEvent(self, event):
        if self.parent():
            parent_width = self.parent().width()
            parent_height = self.parent().height()
            self.setGeometry(0, 0, parent_width, parent_height)

    def eventFilter(self, obj, event):
        if obj == self.parent():
            if event.type() == QEvent.Resize:
                parent_width = self.parent().width()
                parent_height = self.parent().height()
                self.setGeometry(0, 0, parent_width, parent_height)
        return super().eventFilter(obj, event)
    
    def paintEvent(self, e: QPaintEvent):
        super().paintEvent(e)
        
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        
    def deleteLater(self):
        try:
            if self.parent():
                self.parent().destroyed.disconnect(self.onParentDestroyed)
            super().deleteLater()
        except:
            pass

    def onParentDestroyed(self):
        self.deleteLater()

    def showEvent(self, event):
        if self.parent():
            self.parent().destroyed.connect(self.onParentDestroyed)
        super().showEvent(event)

