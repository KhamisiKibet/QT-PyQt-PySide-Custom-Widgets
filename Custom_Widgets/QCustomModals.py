import weakref

from qtpy.QtGui import QPaintEvent, QPainter, QIcon, QPalette, QPixmap
from qtpy.QtCore import Qt, QPoint, QSize, QEvent, QTimer, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve, QObject, Signal
from qtpy.QtWidgets import QStyleOption, QWidget, QStyle, QGraphicsOpacityEffect, QApplication
from Custom_Widgets.components.python.ui_info import Ui_Form

class QCustomModals:
    class BaseModal(QWidget, Ui_Form):
        position = None
        title = None
        description = None
        closeIcon = None
        closeIcon = None
        modalIcon = None
        isClosable = True
        animationDuration = 5000
        
        margin = 24
        spacing = 16
        
        closedSignal = Signal()
        
        commonStyle = ("""
                * {
                    background-color: transparent;
                }
                QPushButton#closeButton{
                    background-color: transparent;
                    font-weight: 1000;
                    min-width: 20px;
                    min-height: 20px;
                    max-width: 20px;
                    max-height: 20px;
                }
                QLabel#iconlabel{
                    min-width: 20px;
                    min-height: 20px;
                    max-width: 20px;
                    max-height: 20px;
                }
            """)
        
        def __init__(self, **kwargs):
            super().__init__()
            self.setupUi(self)
            
            # get default icon:
            self.closeIcon = self.style().standardIcon(QStyle.SP_TitleBarCloseButton).pixmap(QSize(32, 32))
            self.closeButton.setIcon(self.closeIcon)
            
            # Get the info icon from the style
            self.infoIcon = self.style().standardIcon(QStyle.SP_MessageBoxInformation).pixmap(QSize(32, 32))
            # Get the success icon from the style
            self.successIcon = self.style().standardIcon(QStyle.SP_DialogApplyButton).pixmap(QSize(32, 32))
            # Get the warning icon from the style
            self.warningIcon = self.style().standardIcon(QStyle.SP_MessageBoxWarning).pixmap(QSize(32, 32))
            # Get the error icon from the style
            self.errorIcon = self.style().standardIcon(QStyle.SP_MessageBoxCritical).pixmap(QSize(32, 32))

            # Customize modal based on kwargs
            if 'title' in kwargs:
                self.titlelabel.setText(kwargs['title'])
                
            if 'description' in kwargs:
                self.bodyLabel.setText(kwargs['description'])
                
            if 'closeIcon' in kwargs:
                # Set icon
                self.closeIcon = QIcon(kwargs['closeIcon'])
                self.closeButton.setIcon(self.closeIcon)
                
            if 'modalIcon' in kwargs:
                # Set modal icon
                self.modalIcon = QPixmap(kwargs['modalIcon'])
                self.iconlabel.setPixmap(self.modalIcon)
                
            if "isClosable"  in kwargs:
                self.isClosable = kwargs['isClosable']
        
            if 'parent' in kwargs:
                self.setParent(kwargs['parent'])

            if not self.parent() is None:
                palette = self.parent().palette()
            else:
                # Get the existing QApplication instance (if it exists)
                app = QApplication.instance()
                # If no QApplication instance exists, create one
                if app is None:
                    app = QApplication([])
                # Get the palette from the application
                palette = app.palette()
                
            background_color = palette.color(QPalette.Window)

            # Calculate the luminance of the background color
            luminance = 0.2126 * background_color.red() + 0.7152 * background_color.green() + 0.0722 * background_color.blue()

            # Determine if the background color is dark or light
            if luminance < 128:
                # Dark background
                self.isDark = True
            else:
                # Light background
                self.isDark = False
        
            if 'position' in kwargs:
                self.position = kwargs['position']
                # self.calculate_position(kwargs['position'])
                
            if 'animationDuration' in kwargs:
                self.animationDuration = kwargs['animationDuration']
            
            self.closeButton.setFixedSize(20, 20)
            self.closeButton.setIconSize(QSize(self.spacing, self.spacing))
            self.closeButton.setCursor(Qt.PointingHandCursor)
            # Connect close button
            self.closeButton.clicked.connect(self.close)
            self.closeButton.setVisible(self.isClosable)
            
            self.opacityEffect = QGraphicsOpacityEffect(self)
            self.opacityAni = QPropertyAnimation(
                self.opacityEffect, b'opacity', self)
            
            # Set attribute to enable styled background
            # self.setAttribute(Qt.WA_StyledBackground, True)
            
        def paintEvent(self, e: QPaintEvent):
            super().paintEvent(e)
            
            opt = QStyleOption()
            opt.initFrom(self)
            painter = QPainter(self)
            self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)

            painter.setRenderHints(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)

            #
            rect = self.rect().adjusted(1, 1, -1, -1)
            painter.drawRoundedRect(rect, 6, 6)
            
            
        def adjustSizeToContent(self):
            # Calculate the size hint based on the content
            content_size = self.layout().sizeHint()
            # Add some padding if needed
            padding = 0
            self.setFixedSize(content_size.width() + padding, content_size.height() + padding)
            
            if self.position == 'top-right':
                x = self.parent().size().width() - self.width() - self.margin
                # Adjust x-position to have a 20-pixel margin
                self.move(x, self.pos().y())
            
            if self.position == 'top-center':
                x = (self.parent().size().width() - self.width()) / 2
                self.move(x, self.pos().y())

            elif self.position == 'top-left':
                x = self.margin
                self.move(x, self.pos().y())

            elif self.position == 'center-center':
                x = (self.parent().size().width() - self.width()) / 2
                y = (self.parent().size().height() - self.height()) / 2
                self.move(x, y)

            elif self.position == 'center-right':
                x = self.parent().size().width() - self.width() - self.margin
                y = (self.parent().size().height() - self.height()) / 2
                self.move(x, y)

            elif self.position == 'center-left':
                x = self.margin
                y = (self.parent().size().height() - self.height()) / 2
                self.move(x, y)

            elif self.position == 'bottom-right':
                x = self.parent().size().width() - self.width() - self.margin
                y = self.parent().size().height() - self.height() - self.margin
                self.move(x, y)

            elif self.position == 'bottom-left':
                x = self.margin
                y = self.parent().size().height() - self.height() - self.margin
                self.move(x, y)

            
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
                    self.adjustSizeToContent()

            return super().eventFilter(obj, e)

        def closeEvent(self, e):
            self.closedSignal.emit()
            self.deleteLater()

        def showEvent(self, e):
            super().showEvent(e)

            self.adjustSizeToContent()
            
            if self.animationDuration > 0:
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
            if self.modalIcon: self.iconlabel.setPixmap(self.modalIcon) 
            else: self.iconlabel.setPixmap(self.infoIcon)
            
            lightStyle = """
                /* Information Modal */
                InformationModal {
                    background-color: #E6F7FF; /* Light blue or teal */
                }
                InformationModal * {
                    color: #333333;
                    background-color: transparent;
                }
            """
            
            darkStyle = """
                InformationModal {
                    background-color: #2799be; /* Light blue or teal for improved contrast */
                }
                InformationModal * {
                    color: #F5F5F5; /* Whitish color */
                    background-color: transparent;
                }
            """
            
            if self.isDark:  
                self.setStyleSheet(darkStyle + self.commonStyle)
            else:
                self.setStyleSheet(lightStyle + self.commonStyle)

    class SuccessModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Success")
            if self.modalIcon: self.iconlabel.setPixmap(self.modalIcon) 
            else: self.iconlabel.setPixmap(self.successIcon)
            
            lightStyle = """
                /* Success Modal */
                SuccessModal {
                    background-color: #C8E6C9; /* Light green */
                }
                SuccessModal * {
                    color: #333333; /* Dark green or gray */
                    background-color: transparent;
                }
            """
            darkStyle = """
                /* Success Modal */
                SuccessModal {
                    background-color: #29b328; /* Dark green for improved contrast */
                }
                SuccessModal * {
                    color: #F5F5F5; /* Whitish color */
                    background-color: transparent;
                }
            """
            if self.isDark:
                self.setStyleSheet(darkStyle + self.commonStyle)
            else:
                self.setStyleSheet(lightStyle + self.commonStyle)
                

    class WarningModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Warning")
            if self.modalIcon: self.iconlabel.setPixmap(self.modalIcon) 
            else: self.iconlabel.setPixmap(self.warningIcon)
            
            lightStyle = """
                /* Warning Modal */
                WarningModal {
                    background-color: #FFF9E1; /* Light yellow */
                }
                WarningModal * {
                    color: #333333; /* Dark yellow or gray */
                    background-color: transparent;
                }
            """
            darkStyle = """
                /* Warning Modal */
                WarningModal {
                    background-color: #bb8128; /* Light yellow for improved contrast */
                }
                WarningModal * {
                    color: #F5F5F5; /* Whitish color */
                    background-color: transparent;
                }
            """
            if self.isDark:
                self.setStyleSheet(darkStyle + self.commonStyle)
            else:
                self.setStyleSheet(lightStyle + self.commonStyle)


    class ErrorModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Error")
            if self.modalIcon: self.iconlabel.setPixmap(self.modalIcon) 
            else: self.iconlabel.setPixmap(self.errorIcon)
            
            lightStyle = """
                /* Error Modal */
                ErrorModal {
                    background-color: #FFEBEE; /* Light red or pink */
                }
                ErrorModal * {
                    color: #333333; /* Dark red or gray */
                    background-color: transparent;
                }
            """
            darkStyle = """
                /* Error Modal */
                ErrorModal {
                    background-color: #bb221d; /* Light red or pink for improved contrast */
                }
                ErrorModal * {
                    color: #F5F5F5; /* Whitish color */
                    background-color: transparent;
                }
            """
            if self.isDark:
                self.setStyleSheet(darkStyle + self.commonStyle)
            else:
                self.setStyleSheet(lightStyle + self.commonStyle)



    class CustomModal(BaseModal):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.setWindowTitle("Custom")
            if self.modalIcon: self.iconlabel.setPixmap(QPixmap(self.modalIcon))

            style = """
                CustomModal * {
                    background-color: transparent;
                }
            """

            self.setStyleSheet(style)
            

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
        slideAni = self.createSlideAni(QCustomModals)  # Create a slide animation
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
        self.updateDropAni(p)
        self.aniGroups[p].start()  # Start the animation group

    def createSlideAni(self, QCustomModals: QCustomModals):
        """Create a slide animation for the given modal"""
        slideAni = QPropertyAnimation(QCustomModals, b'pos')  # Create a slide animation
        
        # Set easing curve for smooth animation
        easing_curve = QEasingCurve.OutCubic
        slideAni.setEasingCurve(easing_curve)
        
        slideAni.setDuration(500)  # Set the duration of the animation

        # Set initial position and end value for the animation
        start_pos = self.slideStartPos(QCustomModals)
        end_pos = self.modalPosition(QCustomModals)
        
        # Ensure that the initial position is set correctly
        QCustomModals.move(start_pos)
        
        # Set start and end values for the animation
        slideAni.setStartValue(start_pos)
        slideAni.setEndValue(end_pos)

        return slideAni

    def updateDropAni(self, parent):
        """Update drop animation for the remaining info bars"""
        for bar in self.QCustomModalss[parent]:
            ani = bar.property('dropAni')  # Get the drop animation property
            if not ani:
                continue

            ani.setStartValue(bar.pos())   # Set the start value of the animation
            ani.setEndValue(self.modalPosition(bar))  # Set the end value of the animation

    def modalPosition(self, QCustomModals: QCustomModals, parentSize=None) -> QPoint:
        """Return the position of the modal"""
        position = QCustomModals.position
        
        if position == 'top-right':
            x = parentSize.width() - QCustomModals.width() - self.margin
            y = self.margin
        elif position == 'top-center':
            x = (parentSize.width() - QCustomModals.width()) / 2
            y = self.margin
        elif position == 'top-left':
            x = self.margin
            y = self.margin
        elif position == 'center-center':
            x = (parentSize.width() - QCustomModals.width()) / 2
            y = (parentSize.height() - QCustomModals.height()) / 2
        elif position == 'center-right':
            x = parentSize.width() - QCustomModals.width() - self.margin
            y = (parentSize.height() - QCustomModals.height()) / 2
        elif position == 'center-left':
            x = self.margin
            y = (parentSize.height() - QCustomModals.height()) / 2
        elif position == 'bottom-right':
            x = parentSize.width() - QCustomModals.width() - self.margin
            y = parentSize.height() - QCustomModals.height() - self.margin
        elif position == 'bottom-left':
            x = self.margin
            y = parentSize.height() - QCustomModals.height() - self.margin
        else:
            # Default to top-right position if position is not recognized
            x = parentSize.width() - QCustomModals.width() - self.margin
            y = self.margin

        return QPoint(x, y)


    def slideStartPos(self, QCustomModals: QCustomModals) -> QPoint:
        """Return the start position of slide animation"""
        if QCustomModals.position.startswith('top'):
            return QPoint(QCustomModals.pos().x(), -QCustomModals.height())
        elif QCustomModals.position.startswith('center'):
            return QPoint(QCustomModals.pos().x(), QCustomModals.parent().height())
        elif QCustomModals.position.startswith('bottom'):
            return QPoint(QCustomModals.pos().x(), QCustomModals.parent().height() + QCustomModals.height())
        else:
            # Default to top position if position is not recognized
            return QPoint(self.pos().x(), -self.height())

    def eventFilter(self, obj, e: QEvent):
        """Event filter to handle resize and window state change events"""
        if obj not in self.QCustomModalss:
            return False

        if e.type() in [QEvent.Resize, QEvent.WindowStateChange]:
            size = e.size() if e.type() == QEvent.Resize else None
            for bar in self.QCustomModalss[obj]:
                bar.move(self.modalPosition(bar, size))

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

    def modalPosition(self, QCustomModals: QCustomModals, parentSize=None):
        """Calculate the position of the modal for center-center"""
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = (parentSize.width() - QCustomModals.width()) // 2
        y = (parentSize.height() - QCustomModals.height()) // 2

        return QPoint(x, y)

    def slideStartPos(self, QCustomModals: QCustomModals):
        """Calculate the start position of slide animation for center-center"""
        return QPoint(QCustomModals.pos().x(), -QCustomModals.height())

@QCustomModalsManager.register("top-center")
class TopQCustomModalsManager(QCustomModalsManager):
    """ Top position info bar manager """

    def modalPosition(self, QCustomModals: QCustomModals, parentSize=None):
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = (QCustomModals.parent().width() - QCustomModals.width()) // 2
        y = self.margin
        index = self.QCustomModalss[p].index(QCustomModals)
        for bar in self.QCustomModalss[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(x, y)

    def slideStartPos(self, QCustomModals: QCustomModals):
       return QPoint(QCustomModals.pos().x(), -QCustomModals.height())


@QCustomModalsManager.register("top-right")
class TopRightQCustomModalsManager(QCustomModalsManager):
    """ Top right position info bar manager """

    def modalPosition(self, QCustomModals: QCustomModals, parentSize=None):
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = parentSize.width() - QCustomModals.width() - self.margin
        y = self.margin
        index = self.QCustomModalss[p].index(QCustomModals)
        for bar in self.QCustomModalss[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(x, y)

    def slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(QCustomModals.parent().width(), self.modalPosition(QCustomModals).y())


@QCustomModalsManager.register("bottom-right")
class BottomRightQCustomModalsManager(QCustomModalsManager):
    """ Bottom right position info bar manager """

    def modalPosition(self, QCustomModals: QCustomModals, parentSize=None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = parentSize.width() - QCustomModals.width() - self.margin
        y = parentSize.height() - QCustomModals.height() - self.margin

        index = self.QCustomModalss[p].index(QCustomModals)
        for bar in self.QCustomModalss[p][0:index]:
            y -= (bar.height() + self.spacing)

        return QPoint(x, y)

    def slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(QCustomModals.parent().width(), self.modalPosition(QCustomModals).y())


@QCustomModalsManager.register("top-left")
class TopLeftQCustomModalsManager(QCustomModalsManager):
    """ Top left position info bar manager """

    def modalPosition(self, QCustomModals: QCustomModals, parentSize=None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        y = self.margin
        index = self.QCustomModalss[p].index(QCustomModals)

        for bar in self.QCustomModalss[p][0:index]:
            y += (bar.height() + self.spacing)

        return QPoint(self.margin, y)

    def slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(-QCustomModals.width(), self.modalPosition(QCustomModals).y())


@QCustomModalsManager.register("bottom-left")
class BottomLeftQCustomModalsManager(QCustomModalsManager):
    """ Bottom left position info bar manager """

    def modalPosition(self, QCustomModals: QCustomModals, parentSize: QSize = None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        y = parentSize.height() - QCustomModals.height() - self.margin
        index = self.QCustomModalss[p].index(QCustomModals)

        for bar in self.QCustomModalss[p][0:index]:
            y -= (bar.height() + self.spacing)

        return QPoint(self.margin, y)

    def slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(-QCustomModals.width(), self.modalPosition(QCustomModals).y())


@QCustomModalsManager.register("bottom-center")
class BottomQCustomModalsManager(QCustomModalsManager):
    """ Bottom position info bar manager """

    def modalPosition(self, QCustomModals: QCustomModals, parentSize: QSize = None) -> QPoint:
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = (parentSize.width() - QCustomModals.width()) // 2
        y = parentSize.height() - QCustomModals.height() - self.margin
        index = self.QCustomModalss[p].index(QCustomModals)

        for bar in self.QCustomModalss[p][0:index]:
            y -= (bar.height() + self.spacing)

        return QPoint(x, y)

    def slideStartPos(self, QCustomModals: QCustomModals):
        return QPoint(self.modalPosition(QCustomModals).x() + self.spacing, self.modalPosition(QCustomModals).y())

@QCustomModalsManager.register("center-left")
class CenterLeftQCustomModalsManager(QCustomModalsManager):
    """ Center left position info bar manager """

    def modalPosition(self, QCustomModals, parentSize=None):
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = self.margin
        y = (parentSize.height() - QCustomModals.height()) // 2

        return QPoint(x, y)

    def slideStartPos(self, QCustomModals):
        return QPoint(-QCustomModals.width(), QCustomModals.pos().y())

@QCustomModalsManager.register("center-right")
class CenterRightQCustomModalsManager(QCustomModalsManager):
    """ Center right position info bar manager """

    def modalPosition(self, QCustomModals, parentSize=None):
        p = QCustomModals.parent()
        parentSize = parentSize or p.size()

        x = parentSize.width() - QCustomModals.width() - self.margin
        y = (parentSize.height() - QCustomModals.height()) // 2

        return QPoint(x, y)

    def slideStartPos(self, QCustomModals):
        return QPoint(QCustomModals.parent().width(), QCustomModals.pos().y())
    