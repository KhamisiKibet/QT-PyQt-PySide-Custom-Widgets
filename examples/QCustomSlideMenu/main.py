########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

from Custom_Widgets.Widgets import *


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################


        # ########################################################################
        # # CUSTOMIZE YOUR "MENU" / CONTAINER WIDGET
        # ########################################################################
        # self.ui.widget.customizeQCustomSlideMenu(
        #     ########################################################################
        #     # THESE VALUES ARE OPTIONAL
        #     # ONLY PASS THE VALUES YOU WANT TO CHANGE
        #     ########################################################################
        #     # CHANGE THE DEFAULT WIDGET SIZE ON APP STARTUP
        #     defaultWidth = 500,
        #     defaultHeight = 500,
        #     # CHANGE THE WIDGET SIZE WHEN CALLAPSED/MINIMIZED
        #     collapsedWidth = 0,
        #     collapsedHeight = 0,
        #     # CHANGE THE WIDGET SIZE WHEN EXPANDED/MAXIMIZED
        #     expandedWidth = 500,
        #     expandedHeight = 500,
        #     # CHANGE THE DEFAULT ANIMATION DURATION AND EASING CURVE
        #     # BY DEFAULT IT WILL BE APPLIED THE WIDGET IS EXPANDED OR COLLAPSED
        #     animationDuration = 500,
        #     animationEasingCurve = QtCore.QEasingCurve.Linear,
        #     # CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS COLLAPSING
        #     collapsingAnimationDuration = 500,
        #     collapsingAnimationEasingCurve = QtCore.QEasingCurve.Linear,
        #     # CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS EXPANDING
        #     expandingAnimationDuration = 500,
        #     expandingAnimationEasingCurve = QtCore.QEasingCurve.Linear,
        #     # PASS THE STYLESHEET THAT WILL BE APPLIED TO THE WIDGET WHEN EXPANDED OR COLLAPSED
        #     collapsedStyle = "",
        #     expandedStyle = ""
        # )


        # ########################################################################
        # # CHANGE SINGLE VALUES OF YOUR "MENU" / CONTAINER WIDGET
        # ########################################################################
        # # CHANGE THE WIDGET SIZE WHEN CALLAPSED/MINIMIZED
        # self.ui.widget.defaultWidth = 500
        # self.ui.widget.defaultHeight = 500

        # # CHANGE THE WIDGET SIZE WHEN CALLAPSED/MINIMIZED
        # self.ui.widget.collapsedWidth = 0
        # self.ui.widget.collapsedHeight = 0

        # # CHANGE THE WIDGET SIZE WHEN EXPANDED/MAXIMIZED
        # self.ui.widget.expandedWidth = 500
        # self.ui.widget.expandedHeight = 500

        # # CHANGE THE DEFAULT ANIMATION DURATION AND EASING CURVE
        # # BY DEFAULT IT WILL BE APPLIED THE WIDGET IS EXPANDED OR COLLAPSED
        # self.ui.widget.animationDuration = 500
        # self.ui.widget.animationEasingCurve = QtCore.QEasingCurve.Linear

        # # CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS COLLAPSING
        # self.ui.widget.collapsingAnimationDuration = 1000
        # self.ui.widget.collapsingAnimationEasingCurve = QtCore.QEasingCurve.OutBack

        # # CHANGE ANIMATION DURATION AND EASING CURVE WHEN THE WIDGET IS EXPANDING
        # self.ui.widget.expandingAnimationDuration = 2000
        # self.ui.widget.expandingAnimationEasingCurve = QtCore.QEasingCurve.OutQuad

        # # PASS THE STYLESHEET THAT WILL BE APPLIED TO THE WIDGET WHEN EXPANDED OR COLLAPSED
        # self.ui.widget.collapsedStyle = ""
        # self.ui.widget.expandedStyle = ""

        # # REFRESH WIDGET STYLESHEET
        # self.ui.widget.refresh()

        # ########################################################################
        # # ANIMATE YOUR "MENU" / CONTAINER WIDGET
        # ########################################################################
        # # TOGGLE WIDGET SIZE
        # # EXPAND THE WIDGET IF IT IS CURRENTLY COLLAPSED 
        # # OR
        # # COLLAPSE THE WIDGET IF IT IS CURRENTLY EXPANDED
        # # self.ui.widget.slideMenu()

        # # COLLAPSE WIDGET SIZE
        # # self.ui.widget.collapseMenu()

        # # EXPAND WIDGET SIZE
        # # self.ui.widget.expandMenu()

        # # ADD TOGGLE BUTTON
        # self.ui.widget.toggleButton(
        #     # Toggle button name
        #     buttonName = self.ui.my_toggle_button,
        #     # OPTIONAL VALUES
        #     # Ions
        #     iconWhenMenuIsCollapsed = ":/icons/icons/arrow-up.svg",
        #     iconWhenMenuIsExpanded = ":/icons/icons/arrow-down.svg",
        #     # Style
        #     styleWhenMenuIsCollapsed = "background-color: rgb(255, 255, 255);",
        #     styleWhenMenuIsExpanded = "background-color: rgb(85, 255, 255);"
        # )

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        ########################################################################




########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
