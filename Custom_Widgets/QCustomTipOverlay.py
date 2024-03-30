# coding:utf-8
from enum import Enum
from typing import Union

from qtpy.QtCore import Qt, QPoint, QObject, QPointF, QTimer, QPropertyAnimation, QEvent, QSize, Signal
from qtpy.QtGui import QPainter, QColor, QPainterPath, QIcon, QPolygonF, QPixmap, QImage, QPaintEvent, QCursor
from qtpy.QtWidgets import QWidget, QGraphicsDropShadowEffect, QStyle, QStyleOption, QApplication

from Custom_Widgets.QCustomTheme import QCustomTheme

from Custom_Widgets.components.python.ui_info import Ui_Form

class LoadForm(QWidget):
    def __init__(self, form):
        super().__init__()
        # self.ui = Ui_Form()
        self.form = form
        self.form.setupUi(self)

class QCustomTipOverlay(QWidget, Ui_Form):
    """ QCustomOvelay """
    closed = Signal()
    def __init__(self, title: str = "", description: str = "", icon: Union[QIcon, str] = None,
               image: Union[str, QPixmap, QImage] = None, isClosable=False, target: Union[QWidget, QPoint] = None,
               parent=None, aniType="pull-up", deleteOnClose=True, duration=1000, tailPosition="bottom-center", showForm = None, addWidget=None,
               closeIcon: Union[QIcon, str] = None, toolFlag = False):

        super().__init__()
        self.setupUi(self)
        if parent:
            self.setParent(parent)
        self.target = target
        self.duration = duration
        self.deleteOnClose = deleteOnClose
        self.title = title
        self.description = description
        self.icon = icon
        self.image = image
        self.isClosable = isClosable
        self.aniType = aniType
        self.tailPosition = tailPosition

        self.icon = icon
        self.title = title
        self.image = image
        self.description = description

        self.showForm = showForm
        self.widget = addWidget

     
        self.closeIcon = closeIcon
        self.closeButton.setStyleSheet("background-color: transparent")
        self.closeButton.clicked.connect(self._fadeOut)

        self.layout().setContentsMargins(20, 20, 20, 20)
        self.manager = QCustomTipOverlayManager.make(self.tailPosition)
        
        self.setIcon(self.icon)
        self.setCloseIcon(self.closeIcon)
        self.setTitle(self.title)
        self.setDescription(self.description)
        self.loadForm(self.showForm)
        self.addWidget(self.widget)
        self.setClosable(self.isClosable)
        self.moveButton()

        # Connect the signal to a slot
        try:
            self.parent().themeEngine.onThemeChanged.connect(self.handleThemeChanged)
        except:
            pass

        self.opacityAni = QPropertyAnimation(self, b'windowOpacity', self)

        # self.setShadowEffect()
        if toolFlag:
            self.setWindowFlags(self.windowFlags() | Qt.Popup | Qt.Tool | Qt.FramelessWindowHint)
        else:
            self.setWindowFlags(self.windowFlags() | Qt.Popup | Qt.FramelessWindowHint)
        
        self.setAttribute(Qt.WA_TranslucentBackground) 

        if parent and parent.window():
            parent.window().installEventFilter(self)

        self.setStyleSheet("#frame{background-color: transparent; padding: 10px;}")
    
    def handleThemeChanged(self):
        self.setIcon(None)
        self.setIcon(self.icon)
        self.setCloseIcon(None)
        self.setCloseIcon(self.closeIcon)
    
    def _fadeOut(self):
        """ fade out """
        self.opacityAni.setDuration(500)
        self.opacityAni.setStartValue(1)
        self.opacityAni.setEndValue(0)
        self.opacityAni.finished.connect(self.close)
        self.opacityAni.start()

    def showEvent(self, e):
        self.adjustSizeToContent()
        self.raise_()
        
        if self.duration >= 0:
            QTimer.singleShot(self.duration, self._fadeOut)
        
        self.opacityAni.setDuration(500)
        self.opacityAni.setStartValue(0)
        self.opacityAni.setEndValue(1)
        self.opacityAni.start()
        super().showEvent(e)

    def closeEvent(self, e):
        self._fadeOut()
        if self.deleteOnClose:
            self.deleteLater()

        super().closeEvent(e)
        self.closed.emit()

    def eventFilter(self, obj, e: QEvent):
        # if self.parent() and obj is self.parent().window():
        if e.type() in [QEvent.Resize, QEvent.WindowStateChange, QEvent.Move, QEvent.Paint]:
            self.adjustSizeToContent()

        return super().eventFilter(obj, e)
    
    def paintEvent(self, e: QPaintEvent):
        super().paintEvent(e)
        # Move the widget to the position determined by the animation manager
        # self.move(self.manager.position(self))

        self.painter = QPainter(self)
        self.painter.setRenderHints(QPainter.Antialiasing)
        self.painter.setPen(Qt.NoPen)

        # opt = QStyleOption()
        # opt.initFrom(self)
        # self.style().drawPrimitive(QStyle.PE_Widget, opt, self.painter, self)
        
        # Set the brush color to the parent's background color if a parent is set
        if self.parent():
            self.painter.setBrush(self.parent().palette().window())
        else:
            self.painter.setBrush(self.palette().window())

        w, h = self.width(), self.height()
        margins = self.layout().contentsMargins()

        self.path = QPainterPath()
        self.path.addRoundedRect(margins.left()/2, margins.top()/2, w - margins.right(), h - margins.bottom(), 8, 8)
        
        self.manager.draw(self, self.painter, self.path)

        self.moveButton()

        self.painter.end()

    def setIcon(self, icon):
        self.iconlabel.show()
        if isinstance(icon, QIcon):
            pixmap = icon.pixmap(QSize(32, 32))
            self.iconlabel.setPixmap(pixmap)
        elif isinstance(icon, str):
            # Assuming icon is a path to an image file
            pixmap = QPixmap(icon).scaled(QSize(32, 32))
            self.iconlabel.setPixmap(pixmap)
        else:
            self.iconlabel.hide()
    
    def setCloseIcon(self, iconFile):
        if isinstance(iconFile, QIcon):
            self.closeButton.setIcon(self.closeIcon)
        elif isinstance(iconFile, str):
            icon = QIcon()
            icon.addFile(iconFile, QSize(32, 32), QIcon.Normal, QIcon.Off)
            self.closeButton.setIcon(icon)
        else:
            icon = self.style().standardIcon(QStyle.SP_TitleBarCloseButton).pixmap(QSize(32, 32))
            self.closeButton.setIcon(icon)

    def setDescription(self, description):
        self.description = description
        if not self.description:
            self.bodyLabel.hide()
            return
        self.bodyLabel.setText(description)
        self.adjustSizeToContent()
    
    def setTitle(self, title):
        self.title = title
        if not self.title:
            self.titlelabel.hide()
            return
        self.titlelabel.setText(title)
        self.adjustSizeToContent()

    def loadForm(self, form):
        self.showForm = form
        # load form
        if self.showForm:
            self.form = LoadForm(self.showForm)
            self.layout().addWidget(self.form) 
        
    def addWidget(self, widget):
        self.widget = widget
        if self.widget:
            self.layout().addWidget(self.widget) 
    
    def adjustSizeToContent(self):
        # Adjust the size to fit the content
        self.adjustSize()

        self.move(self.manager.position(self))

        self.update()

    def setClosable(self, clossable: bool = True):
        self.isClosable = clossable
        if clossable:
            self.closeButton.show()
        else:
            self.closeButton.hide()

    def moveButton(self):
        # Move the button to the calculated position
        margins = self.layout().contentsMargins()
        x, y = margins.right() * 4, margins.top() / 2
        w, h = self.width(), self.height()
        self.closeButton.setParent(self)
        self.closeButton.setLayout(None)
        self.closeButton.move(w - x, y)


class QCustomTipOverlayManager(QObject):
    """ QCustomOvelay manager """
    managers = {}
    def __init__(self):
        super().__init__()

    @classmethod
    def register(tipOverlay, name):
        """Register menu animation manager"""
        def wrapper(Manager):
            if name not in tipOverlay.managers:
                tipOverlay.managers[name] = Manager

            return Manager

        return wrapper

    @classmethod
    def make(tipOverlay, position: str):
        """Create info bar manager according to the display position"""
        if position not in tipOverlay.managers:
            raise ValueError(f'`{position}` is an invalid animation type.')

        return tipOverlay.managers[position]()

@QCustomTipOverlayManager.register("top-center")
class TopTailQCustomQToolTipManager(QCustomTipOverlayManager):
    """ Top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w/2 - margins.right()/2, margins.top()/2), QPointF(w/2, 1), QPointF(w/2 + margins.right()/2, margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width()/2, target.height()))

        self.margins = tipOverlay.layout().contentsMargins()

        x = pos.x() - tipOverlay.width() / 2 + self.margins.right()
        y = pos.y()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("bottom-center")
class BottomTailQCustomQToolTipManager(QCustomTipOverlayManager):
    """ Bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w/2 - margins.right()/2, h - margins.top()/2), QPointF(w/2, h - 1), QPointF(w/2 + margins.right()/2, h - margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width()/2, 0))

        self.margins = tipOverlay.layout().contentsMargins()

        x = pos.x() - tipOverlay.width() / 2 + self.margins.right()
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("left-center")
class LeftTailQCustomQToolTipManager(QCustomTipOverlayManager):
    """ Left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(margins.right()/2, h/2 - margins.top()/2), QPointF(1, h/2), QPointF(margins.right()/2, h/2 + margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        margins = tipOverlay.layout().contentsMargins()

        pos = target.mapToGlobal(QPoint(target.width(), target.height()/2))
        x = pos.x()
        y = pos.y() - tipOverlay.height()/2
        return QPoint(x, y)

@QCustomTipOverlayManager.register("right-center")
class RightTailQCustomQToolTipManager(QCustomTipOverlayManager):
    """ Left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - margins.right()/2, h/2 - margins.top()/2), QPointF(w - 1, h/2), QPointF(w - margins.right()/2, h/2 + margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, target.height()/2))

        x = pos.x() - tipOverlay.width()
        y = pos.y() - tipOverlay.height()/2 
        return QPoint(x, y)

@QCustomTipOverlayManager.register("top-left")
class TopLeftTailQCustomQToolTipManager(TopTailQCustomQToolTipManager):
    """ Top left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
                
        path.addPolygon(
            QPolygonF([QPointF(20, margins.top()/2), QPointF(27, 0), QPointF(34, margins.top()/2)]))
        

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, target.height()))

        x = pos.x() 
        y = pos.y()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("top-right")
class TopRightTailQCustomQToolTipManager(TopTailQCustomQToolTipManager):
    """ Top right tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - 20, margins.top()/2), QPointF(w - 27, 1), QPointF(w - 34, margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))

        x = pos.x() - tipOverlay.width()
        y = pos.y()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("bottom-left")
class BottomLeftTailQCustomQToolTipManager(BottomTailQCustomQToolTipManager):
    """ Bottom left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(20, h - margins.top()/2), QPointF(27, h - 1), QPointF(34, h - margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, 0))
        x = pos.x()
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("bottom-right")
class BottomRightTailQCustomQToolTipManager(BottomTailQCustomQToolTipManager):
    """ Bottom right tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - 20, h - margins.top()/2), QPointF(w - 27, h - 1), QPointF(w - 34, h - margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - tipOverlay.width() 
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("left-top")
class LeftTopTailQCustomQToolTipManager(LeftTailQCustomQToolTipManager):
    """ Left top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(margins.right()/2, margins.top() ), QPointF(0, margins.top() + 7), QPointF(margins.right()/2, margins.top() + 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), 0))

        x = pos.x()
        y = pos.y()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("left-bottom")
class LeftBottomTailQCustomQToolTipManager(LeftTailQCustomQToolTipManager):
    """ Left bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(margins.right()/2, h - margins.top()), QPointF(0, h - margins.top() - 7), QPointF(margins.right()/2, h - margins.top() - 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))

        x = pos.x()
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("right-top")
class RightTopTailQCustomQToolTipManager(RightTailQCustomQToolTipManager):
    """ Right top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - margins.right()/2, margins.bottom()), QPointF(w, margins.top() + 7), QPointF(w - margins.right()/2, margins.bottom() + 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, 0))
        
        x = pos.x() - tipOverlay.width()
        y = pos.y()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("right-bottom")
class RightBottomTailQCustomQToolTipManager(RightTailQCustomQToolTipManager):
    """ Right bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - margins.right()/2, h - margins.bottom()), QPointF(w, h - margins.bottom() - 7), QPointF(w - margins.right()/2, h - margins.bottom() - 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, target.height()))

        x = pos.x() - tipOverlay.width()
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("auto")
class AutoPositionQCustomQToolTipManager(QCustomTipOverlayManager):
    """ Auto-positioning QCustomOverlay manager """

    def draw(self, tipOverlay, painter, path):
        self.manager = self.createManager(tipOverlay)
        self.manager.draw(tipOverlay, painter, path)

    def position(self, tipOverlay: QCustomTipOverlay):
        manager = self.createManager(tipOverlay)
        position = manager.position(tipOverlay)
        return position
    
    def createManager(self, tipOverlay: QCustomTipOverlay):
        tip_position = self.getTipOverlay(tipOverlay)

        manager = QCustomTipOverlayManager.make(tip_position)
        return manager

    
    def getTipOverlay(self, tipOverlay: QCustomTipOverlay):
        # Get the current screen's available geometry
        app = QApplication.instance()

        app_window = app.primaryScreen().availableGeometry()
        target = tipOverlay.target
        target_rect = target.geometry()
        tip_rect = tipOverlay.geometry()

        m = tipOverlay.layout().contentsMargins()

        # Calculate available space around the target widget
        top_space = target_rect.top() - app_window.top() - m.top()
        bottom_space = app_window.bottom() - target_rect.bottom() - m.bottom()
        left_space = target_rect.left() - app_window.left() - m.left()
        right_space = app_window.right() - target_rect.right() - m.right()

        # Check if the mouse pointer is within the selected space
        mouse_pos = QCursor.pos()
        target_pos = target.mapFromGlobal(mouse_pos)


        # Calculate the relative position of the mouse
        rel_x = target_pos.x() / target_rect.width()
        rel_y = target_pos.y() / target_rect.height()

        # Check if the mouse position is within any of the spaces
        top = False
        bottom = False
        left = False
        right = False
        center = False
        if rel_y < 0.5:
            top = True
        if rel_y > 0.5:
            bottom = True
        if rel_x < 0.5:
            left = True
        if rel_x > 0.5:
            right = True
        if rel_x >= 0.3 and rel_y >= 0.2 and rel_x <= 0.8 and rel_y <= 0.8:
            center = True

        # Determine the best position based on available space
        if top_space >= tipOverlay.height() and center:
            return "bottom-center"
        
        if bottom_space >= tipOverlay.height() and center:
            return "top-center"
        
        if top_space >= tipOverlay.height() and bottom and left: 
            return "right-top"
        
        if top_space >= tipOverlay.height() and bottom and right:
            return "left-top"
        
        if bottom_space >= tipOverlay.height() and bottom and right: 
            return "top-right"
        
        if bottom_space >= tipOverlay.height() and bottom and left:
            return "top-left"
        
        if left_space >= tipOverlay.width() and left: 
            return "right-center"
        
        if right_space >= tipOverlay.width() and right:
            return "left-center"
        
        if bottom_space >= tipOverlay.height() and bottom and right:
            return "top-left"
        
        if bottom_space >= tipOverlay.height() and bottom and left:
            return "top-right"
        
        if top_space >= tipOverlay.height() and top and left:
            return "bottom-left"
        
        if top_space >= tipOverlay.height() and top and right:
            return "bottom-right"
        
        return "top-center"
            

class QCustomQToolTipFilter(QObject):
    def __init__(self, duration=1500, icon=None, tailPosition="auto"):
        super().__init__()
        self.duration = duration
        self.icon = icon
        self.tailPosition = tailPosition

    def eventFilter(self, obj, event):
        if event.type() == QEvent.ToolTip:
            tooltip_text = obj.toolTip()
            QTimer.singleShot(0, lambda: self.showCustomToolTip(tooltip_text, obj))
            return True
        try:
            return super().eventFilter(obj, event)
        except:
            return False

    def showCustomToolTip(self, text, target):
        if not text or hasattr(target, "customTooltip") and target.customTooltip is not None:
            return
        target.customTooltip = QCustomTipOverlay(text=text, target=target, duration = self.duration, tailPosition=self.tailPosition)
        target.customTooltip.show()




