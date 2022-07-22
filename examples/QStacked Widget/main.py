########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
from PySide2 import QtCore
from PySide2.QtCore import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        ## QSTACKWIDGETS NAVIGATION
        ########################################################################
        self.ui.prev.clicked.connect(lambda: self.ui.myStackedWidget.slideToPreviousWidget())
        self.ui.nxt.clicked.connect(lambda: self.ui.myStackedWidget.slideToNextWidget())

        self.ui.page1.clicked.connect(lambda: self.ui.myStackedWidget.setCurrentWidget(self.ui.page))
        self.ui.page2.clicked.connect(lambda: self.ui.myStackedWidget.setCurrentWidget(self.ui.page_2))
        ########################################################################
        ## 
        ########################################################################

        ########################################################################
        ## QSTACKWIDGETS ANIMATION
        # ########################################################################        
        self.ui.myStackedWidget.setTransitionDirection(QtCore.Qt.Vertical)
        self.ui.myStackedWidget.setTransitionSpeed(500)
        self.ui.myStackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
        # ACTIVATE Animation
        self.ui.myStackedWidget.setSlideTransition(True)

        # # Fade animation
        self.ui.myStackedWidget.setFadeSpeed(500)
        self.ui.myStackedWidget.setFadeCurve(QtCore.QEasingCurve.Linear)
        self.ui.myStackedWidget.setFadeTransition(True)
        ########################################################################
        ## 
        ########################################################################

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