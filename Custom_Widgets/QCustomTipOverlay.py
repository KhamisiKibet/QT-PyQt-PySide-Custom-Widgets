# coding:utf-8
from enum import Enum
from typing import Union

from qtpy.QtCore import Qt, QPoint, QObject, QPointF, QTimer, QPropertyAnimation, QEvent, QSize, Signal
from qtpy.QtGui import QPainter, QColor, QPainterPath, QIcon, QPolygonF, QPixmap, QImage, QPaintEvent
from qtpy.QtWidgets import QWidget, QGraphicsDropShadowEffect, QStyle, QStyleOption

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
    def __init__(self, title: str, description: str, icon: Union[QIcon, str] = None,
               image: Union[str, QPixmap, QImage] = None, isClosable=False, target: Union[QWidget, QPoint] = None,
               parent=None, aniType="pull-up", isDeleteOnClose=True, duration=1000, tailPosition="bottom-center", showForm = None, addWidget=None):

        super().__init__()
        self.setupUi(self)
        if parent:
            self.setParent(parent)
        self.target = target
        self.duration = duration
        self.isDeleteOnClose = isDeleteOnClose
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
        self.isClosable = isClosable

        self.showForm = showForm
        self.widget = addWidget

        self.manager = QCustomTipOverlayManager.make(self.tailPosition)

        # get default icon:
        self.closeIcon = self.style().standardIcon(QStyle.SP_TitleBarCloseButton).pixmap(QSize(32, 32))
        self.closeButton.setIcon(self.closeIcon)
        self.closeButton.setStyleSheet("background-color: transparent")
        self.closeButton.clicked.connect(self._fadeOut)

        
        self.setIcon(self.icon)
        self.setTitle(self.title)
        self.setDescription(self.description)
        self.loadForm(self.showForm)
        self.addWidget(self.widget)

        self.opacityAni = QPropertyAnimation(self, b'windowOpacity', self)

        # self.setShadowEffect()

        self.setWindowFlags(Qt.Popup | Qt.Tool | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 

        if parent and parent.window():
            parent.window().installEventFilter(self)

        self.setStyleSheet("background-color: transparent")
        self.layout().setContentsMargins(10, 10, 10, 10)

    def _fadeOut(self):
        """ fade out """
        self.opacityAni.setDuration(500)
        self.opacityAni.setStartValue(1)
        self.opacityAni.setEndValue(0)
        self.opacityAni.finished.connect(self.close)
        self.opacityAni.start()

    def showEvent(self, e):
        if self.duration >= 0:
            QTimer.singleShot(self.duration, self._fadeOut)

        self.move(self.manager.position(self))
        self.adjustSizeToContent()
        self.opacityAni.setDuration(500)
        self.opacityAni.setStartValue(0)
        self.opacityAni.setEndValue(1)
        self.opacityAni.start()
        super().showEvent(e)

    def closeEvent(self, e):
        if self.isDeleteOnClose:
            self.deleteLater()

        super().closeEvent(e)
        self.closed.emit()

    def eventFilter(self, obj, e: QEvent):
        if self.parent() and obj is self.parent().window():
            if e.type() in [QEvent.Resize, QEvent.WindowStateChange, QEvent.Move]:
                self.adjustSizeToContent()

        return super().eventFilter(obj, e)
    
    def paintEvent(self, e: QPaintEvent):
        super().paintEvent(e)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        # Set the brush color to the parent's background color if a parent is set
        if self.parent():
            painter.setBrush(self.parent().palette().window())
        else:
            painter.setBrush(self.palette().window())

        self.manager.draw(self, painter)

        painter.end()

    def setIcon(self, icon):
        self.icon = icon
        if isinstance(icon, QIcon):
            pixmap = icon.pixmap(QSize(32, 32))
            self.iconlabel.setPixmap(pixmap)
        elif isinstance(icon, str):
            # Assuming icon is a path to an image file
            pixmap = QPixmap(icon).scaled(QSize(32, 32))
            self.iconlabel.setPixmap(pixmap)
        else:
            self.iconlabel.hide()

    def setDescription(self, description):
        self.description = description
        if not self.description:
            self.description.hide()
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
            self.verticalLayout_2.addWidget(self.form) 
        
    def addWidget(self, widget):
        self.widget = widget
        if self.widget:
            self.verticalLayout_2.addWidget(self.widget) 
    
    def adjustSizeToContent(self):
        # Move the widget to the position determined by the animation manager
        self.move(self.manager.position(self))
        
        # Adjust the size to fit the content
        self.adjustSize()
        
        # Calculate the size hint based on the description
        content_size = self.layout().sizeHint()
        
        # Set the size with some padding if needed
        # self.setFixedSize(content_size.width(), content_size.height())


    def setGraphicsEffect(self, shadow: QGraphicsDropShadowEffect):
        super().setGraphicsEffect(None)
        shadow.setParent(self.frame)
        self.frame.setGraphicsEffect(shadow)
        

class QCustomTipOverlayManager(QObject):
    """ QCustomOvelay manager """
    managers = {}
    def __init__(self):
        super().__init__()

    def position(self, tipOverlay: QCustomTipOverlay) -> QPoint:
        pos = self._pos(tipOverlay)
        x, y = pos.x(), pos.y()

        rect = QCustomTheme.getCurrentScreenGeometry()
        x = max(rect.left(), min(pos.x(), rect.right() - tipOverlay.width() - 4))
        y = max(rect.top(), min(pos.y(), rect.bottom() - tipOverlay.height() - 4))

        return QPoint(x, y)

    def _pos(self, tipOverlay: QCustomTipOverlay):
        """ return the poisition of tipOverlay """
        return tipOverlay.pos()

    
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
class TopTailQCustomTipOverlayManager(QCustomTipOverlayManager):
    """ Top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pt = tipOverlay.layout().contentsMargins().top()

        path = QPainterPath()
        path.addRoundedRect(1, pt, w - 2, h - pt - 1, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(w/2 - 7, pt), QPointF(w/2, 1), QPointF(w/2 + 7, pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() + target.width()//2 - tipOverlay.width()
        y = pos.y() - tipOverlay.layout().contentsMargins().top()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("bottom-center")
class BottomTailQCustomTipOverlayManager(QCustomTipOverlayManager):
    """ Bottom tail QCustomOvelay manager """

    def doLayout(self, tipOverlay):
        tipOverlay.layout().setContentsMargins(0, 0, 0, 8)

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pt = tipOverlay.layout().contentsMargins().bottom()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - 2, h - pt - 1, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(w/2 - 7, h - pt), QPointF(w/2, h - 1), QPointF(w/2 + 7, h - pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint())
        x = pos.x() + target.width()//2 - tipOverlay.width()
        y = pos.y() - tipOverlay.sizeHint().height() + tipOverlay.layout().contentsMargins().bottom() - target.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("center-left")
class LeftTailQCustomTipOverlayManager(QCustomTipOverlayManager):
    """ Left tail QCustomOvelay manager """

    def doLayout(self, tipOverlay):
        tipOverlay.layout().setContentsMargins(8, 0, 0, 0)

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pl = tipOverlay.layout().contentsMargins().left()

        path = QPainterPath()
        path.addRoundedRect(pl, 1, w - pl - 2, h - 2, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(pl, h/2 - 7), QPointF(1, h/2), QPointF(pl, h/2 + 7)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        m = tipOverlay.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - m.left()
        y = pos.y() - tipOverlay.sizeHint().height()//2 + target.height()//2 - m.top()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("center-right")
class RightTailQCustomTipOverlayManager(QCustomTipOverlayManager):
    """ Left tail QCustomOvelay manager """

    def doLayout(self, tipOverlay):
        tipOverlay.layout().setContentsMargins(0, 0, 8, 0)

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pr = tipOverlay.layout().contentsMargins().right()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - pr - 1, h - 2, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(w - pr, h/2 - 7), QPointF(w - 1, h/2), QPointF(w - pr, h/2 + 7)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        m = tipOverlay.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, 0))
        x = pos.x() - tipOverlay.width() - target.width() + m.right()
        y = pos.y() - tipOverlay.sizeHint().height()//2 + target.height()//2 - m.top()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("top-left")
class TopLeftTailQCustomTipOverlayManager(TopTailQCustomTipOverlayManager):
    """ Top left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pt = tipOverlay.layout().contentsMargins().top()

        path = QPainterPath()
        path.addRoundedRect(1, pt, w - 2, h - pt - 1, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(20, pt), QPointF(27, 1), QPointF(34, pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() - tipOverlay.layout().contentsMargins().left()
        y = pos.y() - tipOverlay.layout().contentsMargins().top()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("top-right")
class TopRightTailQCustomTipOverlayManager(TopTailQCustomTipOverlayManager):
    """ Top right tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pt = tipOverlay.layout().contentsMargins().top()

        path = QPainterPath()
        path.addRoundedRect(1, pt, w - 2, h - pt - 1, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(w - 20, pt), QPointF(w - 27, 1), QPointF(w - 34, pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))
        x = pos.x() - tipOverlay.sizeHint().width()  - target.width() + tipOverlay.layout().contentsMargins().left()
        y = pos.y() - tipOverlay.layout().contentsMargins().top()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("bottom-left")
class BottomLeftTailQCustomTipOverlayManager(BottomTailQCustomTipOverlayManager):
    """ Bottom left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pt = tipOverlay.layout().contentsMargins().bottom()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - 2, h - pt - 1, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(20, h - pt), QPointF(27, h - 1), QPointF(34, h - pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint())
        x = pos.x() - tipOverlay.layout().contentsMargins().left()
        y = pos.y() - tipOverlay.sizeHint().height() + tipOverlay.layout().contentsMargins().bottom() - target.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("bottom-right")
class BottomRightTailQCustomTipOverlayManager(BottomTailQCustomTipOverlayManager):
    """ Bottom right tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pt = tipOverlay.layout().contentsMargins().bottom()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - 2, h - pt - 1, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(w - 20, h - pt), QPointF(w - 27, h - 1), QPointF(w - 34, h - pt)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - tipOverlay.sizeHint().width()  - target.width() + tipOverlay.layout().contentsMargins().left()
        y = pos.y() - tipOverlay.sizeHint().height() + tipOverlay.layout().contentsMargins().bottom() - target.height()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("left-top")
class LeftTopTailQCustomTipOverlayManager(LeftTailQCustomTipOverlayManager):
    """ Left top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pl =  tipOverlay.layout().contentsMargins().left()

        path = QPainterPath()
        path.addRoundedRect(pl, 1, w - pl - 2, h - 2, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(pl, 10), QPointF(1, 17), QPointF(pl, 24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        m = tipOverlay.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - m.left()
        y = pos.y() - m.top()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("left-bottom")
class LeftBottomTailQCustomTipOverlayManager(LeftTailQCustomTipOverlayManager):
    """ Left bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pl =  tipOverlay.layout().contentsMargins().left()

        path = QPainterPath()
        path.addRoundedRect(pl, 1, w - pl - 2, h - 2, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(pl, h - 10), QPointF(1, h - 17), QPointF(pl, h - 24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        m = tipOverlay.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))
        x = pos.x() - m.left()
        y = pos.y() - tipOverlay.sizeHint().height() - target.height() + m.bottom()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("right-top")
class RightTopTailQCustomTipOverlayManager(RightTailQCustomTipOverlayManager):
    """ Right top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pr =  tipOverlay.layout().contentsMargins().right()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - pr - 1, h - 2, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(w - pr, 10), QPointF(w - 1, 17), QPointF(w - pr, 24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        m = tipOverlay.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, 0))
        x = pos.x() - tipOverlay.sizeHint().width()  - target.width() + m.right()
        y = pos.y() - m.top()
        return QPoint(x, y)

@QCustomTipOverlayManager.register("right-bottom")
class RightBottomTailQCustomTipOverlayManager(RightTailQCustomTipOverlayManager):
    """ Right bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter):
        w, h = tipOverlay.width(), tipOverlay.height()
        pr =  tipOverlay.layout().contentsMargins().right()

        path = QPainterPath()
        path.addRoundedRect(1, 1, w - pr - 1, h - 2, 8, 8)
        path.addPolygon(
            QPolygonF([QPointF(w - pr, h-10), QPointF(w - 1, h-17), QPointF(w - pr, h-24)]))

        painter.drawPath(path.simplified())

    def _pos(self, tipOverlay: QCustomTipOverlay):
        target = tipOverlay.target
        m = tipOverlay.layout().contentsMargins()
        pos = target.mapToGlobal(QPoint(0, target.height()))
        x = pos.x() - tipOverlay.sizeHint().width()  - target.width() + m.right()
        y = pos.y() - tipOverlay.sizeHint().height() - target.height() + m.bottom()
        return QPoint(x, y)
