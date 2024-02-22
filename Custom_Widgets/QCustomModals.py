import weakref

from qtpy.QtGui import QPaintEvent, QPainter, QIcon
from qtpy.QtCore import Qt, QPoint, QSize, QEvent, QTimer, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve, QObject, Signal
from qtpy.QtWidgets import QStyleOption, QWidget, QStyle, QGraphicsOpacityEffect
from Custom_Widgets.components.python.ui_info import Ui_Form

class QCustomModals:
    class BaseModal(QWidget, Ui_Form):
        position = None
        title = None
        description = None
        closeIcon = None
        closeIcon = None
        isClosable = True
        animationDuration = 5000
        closedSignal = Signal()
        
        def __init__(self, **kwargs):
            super().__init__()
            self.setupUi(self)

            # Customize modal based on kwargs
            if 'title' in kwargs:
                self.titlelabel.setText(kwargs['title'])
                
            if 'description' in kwargs:
                self.bodyLabel.setText(kwargs['description'])
                
            if 'closeIcon' in kwargs:
                # Set icon
                self.closeIcon = QIcon(kwargs['closeIcon'])
                self.closeButton.setIcon(self.closeIcon)
                
            if "isClosable"  in kwargs:
                self.isClosable = kwargs['isClosable']
        
            if 'parent' in kwargs:
                self.setParent(kwargs['parent'])
        
            if 'position' in kwargs:
                self.position = kwargs['position']
                self.calculate_position(kwargs['position'])
                
            if 'animationDuration' in kwargs:
                self.animationDuration = kwargs['animationDuration']
            
            self.closeButton.setFixedSize(20, 20)
            self.closeButton.setIconSize(QSize(16, 16))
            self.closeButton.setCursor(Qt.PointingHandCursor)
            # Connect close button
            self.closeButton.clicked.connect(self.close)
            self.closeButton.setVisible(self.isClosable)
            
            self.opacityEffect = QGraphicsOpacityEffect(self)
            self.opacityAni = QPropertyAnimation(
                self.opacityEffect, b'opacity', self)
            
            
        def calculate_position(self, position):
            parent_rect = self.parent().geometry()
            modal_rect = self.geometry()
            margin = 20  # Adjust the margin as needed

            if position == 'top-right':
                target_pos = parent_rect.topRight() - modal_rect.topRight() - QPoint(margin, 0)
            elif position == 'top-center':
                target_pos = parent_rect.center() - modal_rect.center() + QPoint(0, -parent_rect.height() / 4)
            elif position == 'top-left':
                target_pos = parent_rect.topLeft() - modal_rect.topLeft() + QPoint(margin, 0)
            elif position == 'center-center':
                target_pos = parent_rect.center() - modal_rect.center()
            elif position == 'center-right':
                target_pos = parent_rect.center() - modal_rect.center() + QPoint(parent_rect.width() / 4, 0)
            elif position == 'center-left':
                target_pos = parent_rect.center() - modal_rect.center() - QPoint(parent_rect.width() / 4, 0)
            elif position == 'bottom-right':
                target_pos = parent_rect.bottomRight() - modal_rect.bottomRight() - QPoint(margin, margin)
            elif position == 'bottom-left':
                target_pos = parent_rect.bottomLeft() - modal_rect.bottomLeft() + QPoint(margin, -margin)

            self.move(target_pos)
            
        def paintEvent(self, e: QPaintEvent):
            super().paintEvent(e)
            
            opt = QStyleOption()
            opt.initFrom(self)
            painter = QPainter(self)
            self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

            painter.setRenderHints(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)

            rect = self.rect().adjusted(1, 1, -1, -1)
            painter.drawRoundedRect(rect, 6, 6)
            
        def fadeOut(self):
            """ fade out """
            self.opacityAni.setDuration(self.animationDuration - 500)
            self.opacityAni.setStartValue(1)
            self.opacityAni.setEndValue(0)
            self.opacityAni.finished.connect(self.close)
            self.opacityAni.start()

        def eventFilter(self, obj, e: QEvent):
            if obj is self.parent():
                if e.type() in [QEvent.Resize, QEvent.WindowStateChange]:
                    pass

            return super().eventFilter(obj, e)

        def closeEvent(self, e):
            self.closedSignal.emit()
            self.deleteLater()

        def showEvent(self, e):
            super().showEvent(e)

            if self.animationDuration >= 0:
                QTimer.singleShot(self.animationDuration, self.fadeOut)

            if self.position != None:
                manager = QCustomModalsManager.make(self.position)
                manager.add(self)

            if self.parent():
                self.parent().installEventFilter(self)


    class InformationModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Information")
            # Set the window modality to WindowModal
            self.setWindowModality(Qt.WindowModal)

    class SuccessModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Success")

    class WarningModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Warning")

    class ErrorModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Error")

    class CustomModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Custom")

class QCustomModalsManager(QObject):
    _instance = None
    managers = {}

    def __new__(cls, *args, **kwargs):
        # Singleton pattern: ensures only one instance of the class is created
        if cls._instance is None:
            cls._instance = super(QCustomModalsManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False

        return cls._instance

    def __init__(self):
        # Initialize the class attributes and instance variables
        if self.__initialized:
            return

        super().__init__()
        self.spacing = 16
        self.margin = 24
        self.QCustomModalss = weakref.WeakKeyDictionary()  # Dictionary to hold modal instances
        self.aniGroups = weakref.WeakKeyDictionary()       # Dictionary to hold animation groups
        self.slideAnis = []  # List to hold slide animations
        self.dropAnis = []   # List to hold drop animations
        self.__initialized = True

    def add(self, QCustomModals: QCustomModals):
        """Add an info bar"""
        p = QCustomModals.parent()    # Get the parent widget
        if not p:
            return

        # Initialize dictionaries if the parent widget is not already in them
        if p not in self.QCustomModalss:
            p.installEventFilter(self)  # Install event filter on parent widget
            self.QCustomModalss[p] = [] # List to hold modal instances for this parent
            self.aniGroups[p] = QParallelAnimationGroup(self) # Animation group for this parent

        # Check if the modal instance already exists for this parent
        if QCustomModals in self.QCustomModalss[p]:
            return

        # Add drop animation if there are already existing modal instances for this parent
        if self.QCustomModalss[p]:
            dropAni = QPropertyAnimation(QCustomModals, b'pos') # Create a drop animation
            dropAni.setDuration(200)  # Set the duration of the animation

            self.aniGroups[p].addAnimation(dropAni)  # Add the drop animation to the animation group
            self.dropAnis.append(dropAni)           # Add the drop animation to the list

            QCustomModals.setProperty('dropAni', dropAni)  # Set a property to hold the drop animation

        # Add slide animation
        self.QCustomModalss[p].append(QCustomModals)    # Add the modal instance to the list
        slideAni = self._createSlideAni(QCustomModals)  # Create a slide animation
        self.slideAnis.append(slideAni)                 # Add the slide animation to the list

        QCustomModals.setProperty('slideAni', slideAni)  # Set a property to hold the slide animation
        QCustomModals.closedSignal.connect(lambda: self.remove(QCustomModals))  # Connect close signal to remove method

        slideAni.start()  # Start the slide animation

    def remove(self, QCustomModals: QCustomModals):
        """Remove an info bar"""
        p = QCustomModals.parent()  # Get the parent widget
        if p not in self.QCustomModalss:
            return

        if QCustomModals not in self.QCustomModalss[p]:
            return

        # Remove the modal instance from the list
        self.QCustomModalss[p].remove(QCustomModals)

        # Remove drop animation
        dropAni = QCustomModals.property('dropAni')   # Get the drop animation property
        if dropAni:
            self.aniGroups[p].removeAnimation(dropAni)  # Remove the drop animation from the animation group
            self.dropAnis.remove(dropAni)              # Remove the drop animation from the list

        # Remove slide animation
        slideAni = QCustomModals.property('slideAni') # Get the slide animation property
        if slideAni:
            self.slideAnis.remove(slideAni)  # Remove the slide animation from the list

        # Adjust the position of the remaining info bars
        self._updateDropAni(p)
        self.aniGroups[p].start()  # Start the animation group

    def _createSlideAni(self, QCustomModals: QCustomModals):
        """Create a slide animation for the given modal"""
        slideAni = QPropertyAnimation(QCustomModals, b'pos')  # Create a slide animation
        slideAni.setEasingCurve(QEasingCurve.OutQuad)        # Set easing curve for smooth animation
        slideAni.setDuration(200)                             # Set the duration of the animation

        # Set start and end values for the animation
        slideAni.setStartValue(self._slideStartPos(QCustomModals))
        slideAni.setEndValue(self._pos(QCustomModals))

        return slideAni

    def _updateDropAni(self, parent):
        """Update drop animation for the remaining info bars"""
        for bar in self.QCustomModalss[parent]:
            ani = bar.property('dropAni')  # Get the drop animation property
            if not ani:
                continue

            ani.setStartValue(bar.pos())   # Set the start value of the animation
            ani.setEndValue(self._pos(bar))  # Set the end value of the animation

    def _pos(self, QCustomModals: QCustomModals, parentSize=None) -> QPoint:
        """Return the position of the info bar"""
        raise NotImplementedError

    def _slideStartPos(self, QCustomModals: QCustomModals) -> QPoint:
        """Return the start position of slide animation"""
        raise NotImplementedError

    def eventFilter(self, obj, e: QEvent):
        """Event filter to handle resize and window state change events"""
        if obj not in self.QCustomModalss:
            return False

        if e.type() in [QEvent.Resize, QEvent.WindowStateChange]:
            size = e.size() if e.type() == QEvent.Resize else None
            for bar in self.QCustomModalss[obj]:
                bar.move(self._pos(bar, size))

        return super().eventFilter(obj, e)

    @classmethod
    def register(cls, name):
        """Register menu animation manager"""
        def wrapper(Manager):
            if name not in cls.managers:
                cls.managers[name] = Manager

            return Manager

        return wrapper

    @classmethod
    def make(cls, position: str):
        """Create info bar manager according to the display position"""
        if position not in cls.managers:
            raise ValueError(f'`{position}` is an invalid animation type.')

        return cls.managers[position]()

@QCustomModalsManager.register("center-center")
class CenterCenterQCustomModalsManager(QCustomModalsManager):
    """Center position info bar manager"""

    def _pos(self, QCustomModals: QCustomModals, parentSize=None):
        """Calculate the position of the modal for center-center"""
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = (parentSize.width() - QCustomModals.width()) // 2
        y = (parentSize.height() - QCustomModals.height()) // 2

        return QPoint(x, y)

    def _slideStartPos(self, QCustomModals: QCustomModals):
        """Calculate the start position of slide animation for center-center"""
        pos = self._pos(QCustomModals)
        return QPoint(pos.x(), pos.y() - 16)

@QCustomModalsManager.register("top-center")
class TopQCustomModalsManager(QCustomModalsManager):
    """ Top position info bar manager """

    def _pos(self, QCustomModals: QCustomModals, parentSize=None):
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = (QCustomModals.parent().width() - QCustomModals.width()) // 2
        y = self.margin
        index = self.QCustomModalss[p].index(QCustomModals)
        for bar in self.QCustomModalss[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(x, y)

    def _slideStartPos(self, QCustomModals: QCustomModals):
        pos = self._pos(QCustomModals)
        return QPoint(pos.x(), pos.y() - 16)


@QCustomModalsManager.register("top-right")
class TopRightQCustomModalsManager(QCustomModalsManager):
    """ Top right position info bar manager """

    def _pos(self, QCustomModals: QCustomModals, parentSize=None):
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = parentSize.width() - QCustomModals.width() - self.margin
        y = self.margin
        index = self.QCustomModalss[p].index(QCustomModals)
        for bar in self.QCustomModalss[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(x, y)

    def _slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(QCustomModals.parent().width(), self._pos(QCustomModals).y())


@QCustomModalsManager.register("bottom-right")
class BottomRightQCustomModalsManager(QCustomModalsManager):
    """ Bottom right position info bar manager """

    def _pos(self, QCustomModals: QCustomModals, parentSize=None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = parentSize.width() - QCustomModals.width() - self.margin
        y = parentSize.height() - QCustomModals.height() - self.margin

        index = self.QCustomModalss[p].index(QCustomModals)
        for bar in self.QCustomModalss[p][0:index]:
            y -= (bar.height() + self.spacing)

        return QPoint(x, y)

    def _slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(QCustomModals.parent().width(), self._pos(QCustomModals).y())


@QCustomModalsManager.register("top-left")
class TopLeftQCustomModalsManager(QCustomModalsManager):
    """ Top left position info bar manager """

    def _pos(self, QCustomModals: QCustomModals, parentSize=None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        y = self.margin
        index = self.QCustomModalss[p].index(QCustomModals)

        for bar in self.QCustomModalss[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(self.margin, y)

    def _slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(-QCustomModals.width(), self._pos(QCustomModals).y())


@QCustomModalsManager.register("bottom-left")
class BottomLeftQCustomModalsManager(QCustomModalsManager):
    """ Bottom left position info bar manager """

    def _pos(self, QCustomModals: QCustomModals, parentSize: QSize = None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        y = parentSize.height() - QCustomModals.height() - self.margin
        index = self.QCustomModalss[p].index(QCustomModals)

        for bar in self.QCustomModalss[p][0:index]:
            y -= (bar.height() + self.spacing)

        return QPoint(self.margin, y)

    def _slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(-QCustomModals.width(), self._pos(QCustomModals).y())


@QCustomModalsManager.register("bottom-center")
class BottomQCustomModalsManager(QCustomModalsManager):
    """ Bottom position info bar manager """

    def _pos(self, QCustomModals: QCustomModals, parentSize: QSize = None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = (parentSize.width() - QCustomModals.width()) // 2
        y = parentSize.height() - QCustomModals.height() - self.margin
        index = self.QCustomModalss[p].index(QCustomModals)

        for bar in self.QCustomModalss[p][0:index]:
            y -= (bar.height() + self.spacing)

        return QPoint(x, y)

    def _slideStartPos(self, QCustomModals: QCustomModals):
        pos = self._pos(QCustomModals)
        return QPoint(pos.x(), pos.y() + 16)

    