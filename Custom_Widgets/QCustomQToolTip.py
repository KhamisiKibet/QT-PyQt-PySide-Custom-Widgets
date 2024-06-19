# coding:utf-8
from qtpy.QtCore import Qt, QPoint, QObject, QPointF, QTimer, QPropertyAnimation, QEvent, QSize, Signal, QRect
from qtpy.QtGui import QPainter, QColor, QPainterPath, QIcon, QPolygonF, QPixmap, QPaintEvent, QPalette, QCursor
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

        self.titlelabel.setStyleSheet("background-color: transparent")

        self.layout().setContentsMargins(10, 10, 10, 10)
        self.manager = QCustomQToolTipManager.make(self.tailPosition)
        
        self.setText(self.text)
        self.setIcon(self.icon)
        
        self.opacityAni = QPropertyAnimation(self, b'windowOpacity', self)
        
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.ToolTipBase)
        self.setForegroundRole(QPalette.ToolTipText)

        self.setShadowEffect()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Popup | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground) 

    def handleThemeChanged(self):
        pass

    def setShadowEffect(self):
        self.setGraphicsEffect(None)
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

    def enterEvent(self, event):
        # self._fadeOut()
        self.adjustSizeToContent()

    def showEvent(self, e):
        super().showEvent(e)
        self.adjustSizeToContent()
        self.raise_()
        
        if self.duration >= 0:
            QTimer.singleShot(self.duration, self._fadeOut)
        
        self.opacityAni.setDuration(500)
        self.opacityAni.setStartValue(0)
        self.opacityAni.setEndValue(1)
        self.opacityAni.start()

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

        x = pos.x() - tipOverlay.width() / 2 + self.margins.right()
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

        x = pos.x() - tipOverlay.width() / 2 + self.margins.right()
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
        margins = tipOverlay.layout().contentsMargins()

        pos = target.mapToGlobal(QPoint(target.width(), target.height()/2))
        x = pos.x()
        y = pos.y() - tipOverlay.height()/2
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
        pos = target.mapToGlobal(QPoint(0, target.height()/2))

        x = pos.x() - tipOverlay.width()
        y = pos.y() - tipOverlay.height()/2 
        return QPoint(x, y)

@QCustomQToolTipManager.register("top-left")
class TopLeftTailQCustomQToolTipManager(TopTailQCustomQToolTipManager):
    """ Top left tail QCustomOvelay manager """

    def draw(self, tipOverlay, painter, path):
        w, h = tipOverlay.width(), tipOverlay.height()
        margins = tipOverlay.layout().contentsMargins()
                
        path.addPolygon(
            QPolygonF([QPointF(20, margins.top()/2), QPointF(27, 0), QPointF(34, margins.top()/2)]))
        

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
        try:
            rel_x = target_pos.x() / target_rect.width()
            rel_y = target_pos.y() / target_rect.height()
        except:
            # division by 0
            return "top-center" 

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
        target.customTooltip = QCustomQToolTip(text=text, target=target, duration = self.duration, tailPosition=self.tailPosition)
        target.customTooltip.show()




