########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## MODULE UPDATED TO USE QT.PY
########################################################################
from qtpy.QtCore import QEasingCurve, QRect, QSettings, QPropertyAnimation, QSize
from qtpy.QtGui import QColor, QPaintEvent, QPainter
from qtpy.QtWidgets import QWidget, QGraphicsDropShadowEffect, QStyleOption, QStyle

import re

class QCustomSlideMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # SET DEFAULT SIZE
        self.defaultWidth = self.width()
        self.defaultHeight = self.height()

        self.collapsedWidth = 0
        self.collapsedHeight = 0

        self.expandedWidth = self.defaultWidth
        self.expandedHeight = self.defaultHeight

        self.animationDuration = 500
        self.animationEasingCurve = QEasingCurve.Linear

        self.collapsingAnimationDuration = self.animationDuration
        self.collapsingAnimationEasingCurve = self.animationEasingCurve

        self.expandingAnimationDuration = self.animationDuration
        self.expandingAnimationEasingCurve = self.animationEasingCurve

        self.collapsedStyle = ""
        self.expandedStyle = ""

        self.collapsed = False
        self.expanded = True

        self.float = False
        self.floatPosition = ""

        # Set the object name
        # self.setObjectName("QCustomSlideMenu")

        # self.setMaximumSize(QSize(0, 0))


    ########################################################################
    # Customize menu
    ########################################################################
    def customizeQCustomSlideMenu(self, **customValues):
        if "defaultWidth" in customValues:
            self.defaultWidth = customValues["defaultWidth"]
            if isinstance(customValues["defaultWidth"], int):
                self.setMaximumWidth(customValues["defaultWidth"])
                self.setMinimumWidth(customValues["defaultWidth"])
            elif customValues["defaultWidth"] == "auto":
                self.setMinimumWidth(0)
                self.setMaximumWidth(16777215)
            elif customValues["defaultWidth"] == "parent":
                self.setMinimumWidth(self.parent().width())
                self.setMaximumWidth(self.parent().width())


        if "defaultHeight" in customValues:
            self.defaultHeight = customValues["defaultHeight"]
            if isinstance(customValues["defaultHeight"], int):
                self.setMaximumHeight(customValues["defaultHeight"])
                self.setMinimumHeight(customValues["defaultHeight"])
            elif customValues["defaultHeight"] == "auto":
                self.setMinimumHeight(0)
                self.setMaximumHeight(16777215)
            elif customValues["defaultHeight"] == "parent":
                self.setMinimumHeight(self.parent().height())
                self.setMaximumHeight(self.parent().height())

        if self.defaultWidth == 0 or self.defaultHeight == 0:
            self.setMaximumWidth(0)
            self.setMaximumHeight(0)

        if "collapsedWidth" in customValues:
            self.collapsedWidth = customValues["collapsedWidth"]

        if "collapsedHeight" in customValues:
            self.collapsedHeight = customValues["collapsedHeight"]


        if "expandedWidth" in customValues:
            self.expandedWidth = customValues["expandedWidth"]

        if "expandedHeight" in customValues:
            self.expandedHeight = customValues["expandedHeight"]


        if "animationDuration" in customValues and int(customValues["animationDuration"]) > 0:
            self.animationDuration = customValues["animationDuration"]

        if "animationEasingCurve" in customValues and len(str(customValues["animationEasingCurve"])) > 0:
            self.animationEasingCurve = customValues["animationEasingCurve"]

        if "collapsingAnimationDuration" in customValues and int(customValues["collapsingAnimationDuration"]) > 0:
            self.collapsingAnimationDuration = customValues["collapsingAnimationDuration"]

        if "collapsingAnimationEasingCurve" in customValues and len(str(customValues["collapsingAnimationEasingCurve"])) > 0:
            self.collapsingAnimationEasingCurve = customValues["collapsingAnimationEasingCurve"]

        if "expandingAnimationDuration" in customValues and int(customValues["expandingAnimationDuration"]) > 0:
            self.expandingAnimationDuration = customValues["expandingAnimationDuration"]

        if "expandingAnimationEasingCurve" in customValues and len(str(customValues["expandingAnimationEasingCurve"])) > 0:
            self.expandingAnimationEasingCurve = customValues["expandingAnimationEasingCurve"]

        if "collapsedStyle" in customValues and len(str(customValues["collapsedStyle"])) > 0:
            self.collapsedStyle = str(customValues["collapsedStyle"])
            if self.collapsed:
                self.setStyleSheet(str(customValues["collapsedStyle"]))

        if "expandedStyle" in customValues and len(str(customValues["expandedStyle"])) > 0:
            self.expandedStyle = str(customValues["expandedStyle"])
            if self.expanded:
                self.setStyleSheet(str(customValues["expandedStyle"]))

        if "floatMenu" in customValues and customValues["floatMenu"] == True:
            self.float = True
            if "relativeTo" in customValues and len(str(customValues["relativeTo"])) > 0:
                if "position" in customValues and len(str(customValues["position"])) > 0:
                    self.floatPosition = str(customValues["position"])

                effect = QGraphicsDropShadowEffect(self)
                if "shadowColor" in customValues and len(str(customValues["shadowColor"])) > 0:
                    effect.setColor(QColor(str(customValues["shadowColor"])))
                else:
                    effect.setColor(QColor(0,0,0,0))
                if "shadowBlurRadius" in customValues and int(customValues["shadowBlurRadius"]) > 0:
                    effect.setBlurRadius(int(customValues["shadowBlurRadius"]))
                else:
                    effect.setBlurRadius(0)
                if "shadowXOffset" in customValues and int(customValues["shadowXOffset"]) > 0:
                    effect.setXOffset(int(customValues["shadowXOffset"]))
                else:
                    effect.setXOffset(0)
                if "shadowYOffset" in customValues and int(customValues["shadowYOffset"]) > 0:
                    effect.setYOffset(int(customValues["shadowYOffset"]))
                else:
                    effect.setYOffset(0)


                self.setGraphicsEffect(effect)

                if "autoHide" in customValues:
                    self.autoHide = customValues["autoHide"]
                else:
                    self.autoHide = True

        if "update" in customValues and not customValues["update"]:
            # self.refresh()
            pass
            

    ########################################################################
    # Float menu
    ########################################################################
    def floatMenu(self):
        if self.float:
            if len(str(self.floatPosition)) > 0:
                position = str(self.floatPosition)

                if position == "top-left":
                    self.setGeometry(QRect(self.parent().x(), self.parent().y(), self.width(), self.height()))

                if position == "top-right":
                    self.setGeometry(QRect(self.parent().width() - self.width(), self.parent().y(), self.width(), self.height()))

                if position == "top-center":
                    self.setGeometry(QRect((self.parent().width() - self.width()) / 2, self.parent().y(), self.width(), self.height()))

                if position == "bottom-right":
                    self.setGeometry(QRect(self.parent().width() - self.width(), self.parent().height() - self.height(), self.width(), self.height()))


                if position == "bottom-left":
                    self.setGeometry(QRect(self.parent().x(), self.parent().height() - self.height(), self.width(), self.height()))

                if position == "bottom-center":
                    self.setGeometry(QRect((self.parent().width() - self.width()) / 2, self.parent().height() - self.height(), self.width(), self.height()))

                if position == "center-center":
                    self.setGeometry(QRect((self.parent().width() - self.width()) / 2, (self.parent().height() - self.height()) / 2, self.width(), self.height()))

                if position == "center-left":
                    self.setGeometry(QRect(self.parent().x(), (self.parent().height() - self.height()) / 2, self.width(), self.height()))

                if position == "center-right":
                    self.setGeometry(QRect(self.parent().width() - self.width(), (self.parent().height() - self.height()) / 2, self.width(), self.height()))

    ########################################################################
    # Menu Toggle Button
    ########################################################################
    def toggleMenu(self, buttonObject):

        self.slideMenu()

        self.applyButtonStyle()


    def activateMenuButton(self, buttonObject):
        buttonObject.clicked.connect(lambda: self.toggleMenu(buttonObject))

    def toggleButton(self, **values):
        if not hasattr(self, "targetBtn") and not "buttonName" in values:
            raise Exception("No button specified for this widget, please specify the QPushButton object")

        if "buttonName" in values:
            toggleButton = values["buttonName"]
            if not hasattr(self, "targetBtn") or self.targetBtn != self:
                toggleButton.menuCollapsedIcon = ""
                toggleButton.menuExpandedIcon = ""
                toggleButton.menuCollapsedStyle = ""
                toggleButton.menuExpandedStyle = ""

            toggleButton.targetMenu = self

            self.targetBtn = toggleButton

            if "update" in values and not values["update"]:
                self.activateMenuButton(self.targetBtn)


        if "iconWhenMenuIsCollapsed" in values and len(str(values["iconWhenMenuIsCollapsed"])) > 0:
            toggleButton.menuCollapsedIcon = str(values["iconWhenMenuIsCollapsed"])


        if "iconWhenMenuIsExpanded" in values and len(str(values["iconWhenMenuIsExpanded"])) > 0:
            toggleButton.menuExpandedIcon = str(values["iconWhenMenuIsExpanded"])

        if "styleWhenMenuIsCollapsed" in values and len(str(values["iconWhenMenuIsExpanded"])) > 0:
            toggleButton.menuCollapsedStyle = str(values["styleWhenMenuIsCollapsed"])

        if "styleWhenMenuIsExpanded" in values and len(str(values["styleWhenMenuIsExpanded"])) > 0:
            toggleButton.menuExpandedStyle = str(values["styleWhenMenuIsExpanded"])



    ########################################################################
    # Slide menu function
    ########################################################################
    def slideMenu(self):
        if self.collapsed:
            self.expandMenu()
        else:
            self.collapseMenu()

    def expandMenu(self):
        if not self.expanded:
            self.collapsed = True
            self.expanded = False

            self.animateMenu()

            self.collapsed = False
            self.expanded = True

            self.applyButtonStyle()

    def collapseMenu(self):
        if not self.collapsed:
            self.collapsed = False
            self.expanded = True

            self.animateMenu()

            self.collapsed = True
            self.expanded = False

            self.applyButtonStyle()

    def applyWidgetStyle(self):
        if self.expanded and len(str(self.expandedStyle)) > 0:

            self.setStyleSheet(str(self.expandedStyle))

        if self.collapsed and len(str(self.collapsedStyle)) > 0:
                self.setStyleSheet(str(self.collapsedStyle))

    def applyButtonStyle(self):
        if hasattr(self, "targetBtn"):
            settings = QSettings()
            if settings.value("ICONS-COLOR") is not None:
                normal_color = settings.value("ICONS-COLOR")
                icons_folder = normal_color.replace("#", "")

                prefix_to_remove = re.compile(r'^Qss/icons/[^/]+/')
                self.targetBtn.menuCollapsedIcon = re.sub(prefix_to_remove, 'Qss/icons/'+icons_folder+'/', self.targetBtn.menuCollapsedIcon)
                self.targetBtn.menuExpandedIcon = re.sub(prefix_to_remove, 'Qss/icons/'+icons_folder+'/', self.targetBtn.menuExpandedIcon)
            
            if self.collapsed:
                if len(self.targetBtn.menuCollapsedIcon) > 0:
                        # self.targetBtn.setIcon(QtGui.QIcon(self.targetBtn.menuCollapsedIcon))
                        self.targetBtn.setNewIcon(self.targetBtn.menuCollapsedIcon)

                if len(str(self.targetBtn.menuCollapsedStyle)) > 0:
                    self.targetBtn.setStyleSheet(self.targetBtn.menuCollapsedStyle)
            else:
                if len(str(self.targetBtn.menuExpandedIcon)) > 0:
                        # self.targetBtn.setIcon(QtGui.QIcon(self.targetBtn.menuExpandedIcon))
                        self.targetBtn.setNewIcon(self.targetBtn.menuExpandedIcon)

                if len(str(self.targetBtn.menuExpandedStyle)) > 0:
                    self.targetBtn.setStyleSheet(self.targetBtn.menuExpandedStyle)

    def animateMenu(self):
        self.setMinimumSize(QSize(0, 0))

        if self.collapsed:
            if self.expandedWidth != "auto" and self.expandedWidth != 16777215 and self.expandedWidth != "parent":
                startWidth = self.width()
                endWidth = self.expandedWidth
            else:
                startWidth = self.width()
                endWidth = self.parent().width()
            if self.floatMenu:
                self._widthAnimation = QPropertyAnimation(self, b"minimumWidth")
            else:
                self._widthAnimation = QPropertyAnimation(self, b"maximumWidth")

            self._widthAnimation.setDuration(self.expandingAnimationDuration)
            self._widthAnimation.setEasingCurve(self.expandingAnimationEasingCurve)


            if self.expandedHeight != "auto" and self.expandedHeight != 16777215 and self.expandedHeight != "parent":
                startHeight = self.height()
                endHeight = self.expandedHeight
            else:
                startHeight = self.height()
                endHeight = self.parent().height()
            if self.floatMenu:
                self._heightAnimation = QPropertyAnimation(self, b"minimumHeight")
            else:
                self._heightAnimation = QPropertyAnimation(self, b"maximumHeight")
            self._heightAnimation.setDuration(self.expandingAnimationDuration)
            self._heightAnimation.setEasingCurve(self.expandingAnimationEasingCurve)



        if self.expanded:
            if self.collapsedWidth != "auto" and self.collapsedWidth != "parent":
                startWidth = self.width()
                endWidth = self.collapsedWidth
            elif self.collapsedWidth == "parent":
                startWidth = self.width()
                endWidth = self.parent().width()
            else:
                startWidth = self.width()
                endWidth = 0

            self._widthAnimation = QPropertyAnimation(self, b"maximumWidth")
            self._widthAnimation.setDuration(self.collapsingAnimationDuration)
            self._widthAnimation.setEasingCurve(self.collapsingAnimationEasingCurve)



            if self.collapsedHeight != "auto" and self.collapsedHeight != "parent":
                startHeight = self.height()
                endHeight = self.collapsedHeight
            elif self.collapsedHeight == "parent":
                startHeight = self.height()
                endHeight = self.parent().height()
            else:
                startHeight = self.height()
                endHeight = 0

            self._heightAnimation = QPropertyAnimation(self, b"maximumHeight")
            self._heightAnimation.setDuration(self.collapsingAnimationDuration)
            self._heightAnimation.setEasingCurve(self.collapsingAnimationEasingCurve)
        
        self.animateWidth(startWidth, endWidth)
        self.animateHeight(startHeight, endHeight)

        self.setMinimumSize(QSize(0, 0))


    def animateWidth(self, startWidth, endWidth):
        if self.expandedWidth == "auto" or self.expandedWidth == 16777215:
            if self.collapsed:
                self._widthAnimation.finished.connect(lambda: self.setMaximumWidth(16777215))
            if self.expanded:
                self._widthAnimation.finished.connect(lambda: self.setMaximumWidth(0))

        self._widthAnimation.setStartValue(startWidth)
        self._widthAnimation.setEndValue(endWidth)
        self._widthAnimation.start()

        self._widthAnimation.finished.connect(lambda: self.applyWidgetStyle())

    def animateHeight(self, startHeight, endHeight):
        if self.expandedHeight == "auto" or self.expandedHeight == 16777215:
            if self.collapsed:
                self._heightAnimation.finished.connect(lambda: self.setMaximumHeight(16777215))
            if self.expanded:
                self._heightAnimation.finished.connect(lambda: self.setMaximumHeight(0))

        self._heightAnimation.setStartValue(startHeight)
        self._heightAnimation.setEndValue(endHeight)
        self._heightAnimation.start()



    def refresh(self):
        if self.isExpanded():

            self.collapsed = False
            self.expanded = True

        else:

            self.collapsed = True
            self.expanded = False

        self.applyWidgetStyle()
        if hasattr(self, "targetBtn"):
            self.applyButtonStyle()


    def isExpanded(self):
        if self.width() > self.getCollapsedWidth() or self.width() > self.getCollapsedHeight():
            return True

    def isCollapsed(self):
        if self.width() < self.getCollapsedWidth() or self.width() < self.getCollapsedHeight():
            return True

    def getDefaultWidth(self):
        if isinstance(self.defaultWidth, int):
            return self.defaultWidth
        if self.defaultWidth == "auto":
            return 0
        if self.defaultWidth == "parent":
            return self.parent().width()

    def getDefaultHeight(self):
        if isinstance(self.defaultHeight, int):
            return self.defaultHeight
        if self.defaultHeight == "auto":
            return 0
        if self.defaultHeight == "parent":
            return self.parent().width()

    def getCollapsedWidth(self):
        if isinstance(self.collapsedWidth, int):
            return self.collapsedWidth
        if self.collapsedWidth == "auto":
            return 0
        if self.collapsedWidth == "parent":
            return self.parent().width()

    def getCollapsedHeight(self):
        if isinstance(self.collapsedHeight, int):
            return self.collapsedHeight
        if self.collapsedHeight == "auto":
            return 0
        if self.collapsedHeight == "parent":
            return self.parent().width()

    def getExpandedWidth(self):
        if isinstance(self.expandedWidth, int):
            return self.expandedWidth
        if self.expandedWidth == "auto":
            return 16777215
        if self.expandedWidth == "parent":
            return self.parent().width()

    def getExpandedHeight(self):
        if isinstance(self.expandedHeight, int):
            return self.expandedHeight
        if self.expandedHeight == "auto":
            return 16777215
        if self.expandedHeight == "parent":
            return self.parent().width()

    def paintEvent(self, event: QPaintEvent):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        
        try:
            if hasattr(self, "_widthAnimation"):
                if self._widthAnimation.finished:
                    if self.collapsed:
                        if self.collapsedWidth == "parent":
                            # self.setMinimumWidth(self.parent().width())
                            self.setMaximumWidth(self.parent().width())
                    if self.expanded:
                        if self.expandedWidth == "parent":
                            # self.setMinimumWidth(self.parent().width())
                            self.setMaximumWidth(self.parent().width())


            if hasattr(self, "_heightAnimation"):
                if self._heightAnimation.finished:
                    if self.collapsed:
                        if self.collapsedHeight == "parent":
                            # self.setMinimumHeight(self.parent().height())
                            self.setMaximumHeight(self.parent().height())
                    if self.expanded:
                        if self.expandedHeight == "parent":
                            # self.setMinimumHeight(self.parent().height())
                            self.setMaximumHeight(self.parent().height())

            if not hasattr(self, "_widthAnimation") and not hasattr(self, "_heightAnimation"):
                if self.defaultWidth == "parent":
                    # self.setMinimumWidth(self.parent().width())
                    self.setMaximumWidth(self.parent().width())

                if self.defaultHeight == "parent":
                    # self.setMinimumHeight(self.parent().height())
                    self.setMaximumHeight(self.parent().height())

        except Exception as e:
            pass
            # print(e)

        self.floatMenu()


    #######################################################################