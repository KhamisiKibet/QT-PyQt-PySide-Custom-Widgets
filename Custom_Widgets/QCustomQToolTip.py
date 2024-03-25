# coding:utf-8
from qtpy.QtCore import Qt, QPoint, QObject, QPointF, QTimer, QPropertyAnimation, QEvent, QSize, Signal
from qtpy.QtGui import QPainter, QColor, QPainterPath, QIcon, QPolygonF, QPixmap, QPaintEvent, QPalette
from qtpy.QtWidgets import QWidget, QGraphicsDropShadowEffect, QStyle, QStyleOption, QApplication

from Custom_Widgets.components.python.ui_tooltip import Ui_Form

class QCustomQToolTip(QWidget, Ui_Form):
    """ QCustomOvelay """
    onClosed = Signal()

    def __init__(self, text: str, parent=None, target=None, duration=1500, icon=None, tailPosition="auto"):
        super().__init__()
        self.setupUi(self)

        self.target = target
        self.duration = duration
        self.text = text
        self.icon = icon
        self.tailPosition = tailPosition

        self.layout().setContentsMargins(20, 20, 20, 20)
        self.manager = QCustomQToolTipManager.make(self.tailPosition)
        
        self.setText(self.text)
        
        self.opacityAni = QPropertyAnimation(self, b'windowOpacity', self)
        
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.ToolTipBase)
        self.setForegroundRole(QPalette.ToolTipText)

        self.setWindowFlags(self.windowFlags() | Qt.Popup | Qt.Tool | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 

        self.setShadowEffect()

    def handleThemeChanged(self):
        pass

    def setShadowEffect(self):
        self.effect = QGraphicsDropShadowEffect(self)
        self.effect.setColor(QColor(0, 0, 0, 200))
        self.effect.setBlurRadius(10)
        self.effect.setXOffset(0)
        self.effect.setYOffset(0)
        self.setGraphicsEffect(self.effect)
    
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
        super().closeEvent(e)
        self.target.customTooltip = None
        self.onClosed.emit()

    def eventFilter(self, obj, e: QEvent):
        # if self.parent() and obj is self.parent().window():
        if e.type() in [QEvent.Resize, QEvent.WindowStateChange, QEvent.Move, QEvent.Paint]:
            self.adjustSizeToContent()

        return super().eventFilter(obj, e)
    
    def paintEvent(self, e: QPaintEvent):
        super().paintEvent(e)

        self.painter = QPainter(self)
        self.painter.setRenderHints(QPainter.Antialiasing)
        self.painter.setPen(Qt.NoPen)
        
        # Set the brush color to the parent's background color if a parent is set
        if self.parent():
            self.painter.setBrush(self.parent().palette().window())
        else:
            self.painter.setBrush(self.palette().window())

        w, h = self.width(), self.height()
        margins = self.layout().contentsMargins()

        self.path = QPainterPath()
        self.path.addRoundedRect(margins.left()/2, margins.top()/2, w - margins.right(), h - margins.bottom(), 0, 0)
        
        self.manager.draw(self, self.painter, self.path)

        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, self.painter, self)

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
    
    def setText(self, text):
        self.text = text
        if not self.text:
            self.titlelabel.hide()
            return
        self.titlelabel.setText(text)
        self.adjustSizeToContent()
    
    def adjustSizeToContent(self):
        # Adjust the size to fit the content
        self.adjustSize()

        self.move(self.manager.position(self))

        self.update()

class QCustomQToolTipManager(QObject):
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

@QCustomQToolTipManager.register("top-center")
class TopTailQCustomQToolTipManager(QCustomQToolTipManager):
    """ Top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w/2 - margins.right()/2, margins.top()/2), QPointF(w/2, 1), QPointF(w/2 + margins.right()/2, margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width()/2, target.height()))

        self.margins = tipOverlay.layout().contentsMargins()

        x = pos.x() - tipOverlay.sizeHint().width() + self.margins.right() * 2
        y = pos.y()
        return QPoint(x, y)

@QCustomQToolTipManager.register("bottom-center")
class BottomTailQCustomQToolTipManager(QCustomQToolTipManager):
    """ Bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w/2 - margins.right()/2, h - margins.top()/2), QPointF(w/2, h - 1), QPointF(w/2 + margins.right()/2, h - margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width()/2, 0))

        self.margins = tipOverlay.layout().contentsMargins()

        x = pos.x() - tipOverlay.sizeHint().width() + self.margins.right() * 2
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomQToolTipManager.register("left-center")
class LeftTailQCustomQToolTipManager(QCustomQToolTipManager):
    """ Left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(margins.right()/2, h/2 - margins.top()/2), QPointF(1, h/2), QPointF(margins.right()/2, h/2 + margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x()
        y = pos.y() - tipOverlay.sizeHint().height()/2
        return QPoint(x, y)

@QCustomQToolTipManager.register("right-center")
class RightTailQCustomQToolTipManager(QCustomQToolTipManager):
    """ Left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - margins.right()/2, h/2 - margins.top()/2), QPointF(w - 1, h/2), QPointF(w - margins.right()/2, h/2 + margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, 0))

        x = pos.x() - tipOverlay.width()
        y = pos.y() - tipOverlay.sizeHint().height()/2 
        return QPoint(x, y)

@QCustomQToolTipManager.register("top-left")
class TopLeftTailQCustomQToolTipManager(TopTailQCustomQToolTipManager):
    """ Top left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
                
        path.addPolygon(
            QPolygonF([QPointF(20, margins.top()/2), QPointF(27, 1), QPointF(34, margins.top()/2)]))
        

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, target.height()))

        x = pos.x() 
        y = pos.y()
        return QPoint(x, y)

@QCustomQToolTipManager.register("top-right")
class TopRightTailQCustomQToolTipManager(TopTailQCustomQToolTipManager):
    """ Top right tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - 20, margins.top()/2), QPointF(w - 27, 1), QPointF(w - 34, margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))

        x = pos.x() - tipOverlay.width()
        y = pos.y()
        return QPoint(x, y)

@QCustomQToolTipManager.register("bottom-left")
class BottomLeftTailQCustomQToolTipManager(BottomTailQCustomQToolTipManager):
    """ Bottom left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(20, h - margins.top()/2), QPointF(27, h - 1), QPointF(34, h - margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, 0))
        x = pos.x()
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomQToolTipManager.register("bottom-right")
class BottomRightTailQCustomQToolTipManager(BottomTailQCustomQToolTipManager):
    """ Bottom right tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - 20, h - margins.top()/2), QPointF(w - 27, h - 1), QPointF(w - 34, h - margins.top()/2)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), 0))
        x = pos.x() - tipOverlay.width() 
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomQToolTipManager.register("left-top")
class LeftTopTailQCustomQToolTipManager(LeftTailQCustomQToolTipManager):
    """ Left top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(margins.right()/2, margins.top() ), QPointF(0, margins.top() + 7), QPointF(margins.right()/2, margins.top() + 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), 0))

        x = pos.x()
        y = pos.y()
        return QPoint(x, y)

@QCustomQToolTipManager.register("left-bottom")
class LeftBottomTailQCustomQToolTipManager(LeftTailQCustomQToolTipManager):
    """ Left bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(margins.right()/2, h - margins.top()), QPointF(0, h - margins.top() - 7), QPointF(margins.right()/2, h - margins.top() - 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(target.width(), target.height()))

        x = pos.x()
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomQToolTipManager.register("right-top")
class RightTopTailQCustomQToolTipManager(RightTailQCustomQToolTipManager):
    """ Right top tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - margins.right()/2, margins.bottom()), QPointF(w, margins.top() + 7), QPointF(w - margins.right()/2, margins.bottom() + 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, 0))
        
        x = pos.x() - tipOverlay.width()
        y = pos.y()
        return QPoint(x, y)

@QCustomQToolTipManager.register("right-bottom")
class RightBottomTailQCustomQToolTipManager(RightTailQCustomQToolTipManager):
    """ Right bottom tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins =tipOverlay.layout().contentsMargins()
        
        path.addPolygon(
            QPolygonF([QPointF(w - margins.right()/2, h - margins.bottom()), QPointF(w, h - margins.bottom() - 7), QPointF(w - margins.right()/2, h - margins.bottom() - 14)]))

        painter.drawPath(path.simplified())

    def position(self, tipOverlay: QCustomQToolTip):
        target = tipOverlay.target
        pos = target.mapToGlobal(QPoint(0, target.height()))

        x = pos.x() - tipOverlay.width()
        y = pos.y() - tipOverlay.height()
        return QPoint(x, y)

@QCustomQToolTipManager.register("auto")
class AutoPositionQCustomQToolTipManager(QCustomQToolTipManager):
    """ Auto-positioning QCustomOverlay manager """

    def draw(self, tipOverlay, painter, path):
        self.manager = self.createManager(tipOverlay)
        self.manager.draw(tipOverlay, painter, path)

    def position(self, tipOverlay: QCustomQToolTip):
        manager = self.createManager(tipOverlay)
        position = manager.position(tipOverlay)
        return position
    
    def createManager(self, tipOverlay: QCustomQToolTip):
        tip_position = self.getTipOverlay(tipOverlay)

        manager = QCustomQToolTipManager.make(tip_position)
        return manager

    
    def getTipOverlay(self, tipOverlay: QCustomQToolTip):
        # Get the current screen's available geometry
        app = QApplication.instance()

        app_window = app.primaryScreen().availableGeometry()
        target = tipOverlay.target
        target_rect = target.geometry()

        m = tipOverlay.layout().contentsMargins()

        # Calculate available space around the target widget
        top_space = target_rect.top()  - m.top()
        bottom_space = target_rect.bottom() - m.bottom()
        left_space = target_rect.right() - m.left()
        right_space = app_window.width() - target_rect.right()  - m.right()
        # Determine the best position based on available space
        if left_space >= tipOverlay.sizeHint().width() and right_space >= tipOverlay.sizeHint().width():
            if top_space >= tipOverlay.sizeHint().height() + m.top() + 10:
                return "bottom-center"
            else:
                return "top-center"
        if top_space >= tipOverlay.sizeHint().height() + m.top() + 10 and bottom_space >= tipOverlay.sizeHint().height() + m.bottom() + 10:
            if left_space >= tipOverlay.sizeHint().width():
                return "right-center"
            elif right_space >= tipOverlay.sizeHint().width():
                return "left-center"
        if top_space >= tipOverlay.sizeHint().height() + m.top() + 10:
            if left_space >= tipOverlay.sizeHint().width():
                return "bottom-right"
            elif right_space >= tipOverlay.sizeHint().width():
                return "bottom-left"
        elif bottom_space >= tipOverlay.sizeHint().height() + m.bottom() + 10:
            if left_space >= tipOverlay.sizeHint().width():
                return "top-right"
            elif right_space >= tipOverlay.sizeHint().width():
                return "top-left"
            
        elif left_space >= tipOverlay.sizeHint().width():
            if top_space >= tipOverlay.sizeHint().height() + m.top() + 10:
                return "right-bottom"
            else:
                return "right-top"
        elif right_space >= tipOverlay.sizeHint().width():
            if top_space >= tipOverlay.sizeHint().height() + m.top() + 10:
                return "left-bottom"
            else:
                return "left-top"

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
        return super().eventFilter(obj, event)

    def showCustomToolTip(self, text, target):
        if not text or hasattr(target, "customTooltip") and target.customTooltip is not None:
            return
        target.customTooltip = QCustomQToolTip(text=text, target=target, duration = self.duration, tailPosition=self.tailPosition)
        target.customTooltip.show()




