########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT CUSTOM WIDGETS MODULE
from Custom_Widgets import *
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
        ## LOAD STYLE FROM JSON FILE
        ########################################################################
        loadJsonStyle(self, self.ui, jsonFiles = {
            "JsonStyle/style.json"
        })
        ########################################################################
        ## 
        ########################################################################

        ########################################################################
        # Customize QCustomCheckBox
        ########################################################################
        self.ui.checkBox.customizeQCustomCheckBox(
            bgColor = "#c3c3c3",
            circlecolor = "#fff",
            activecolor = "#17a8e3",
            animationEasingCurve = QEasingCurve.Linear,
            animationDuration = 200
        )

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
