########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
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

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        ########################################################################


        #######################################################################
        # CUSTOMIZE PROGRESS BAR
        #######################################################################
        # self.ui.widget.updateFormProgressIndicator(
        #     # Set font color
        #     color = "#000", 
        #     # Set fill color
        #     fillColor = "white", 
        #     # Set fill color for warnings
        #     warningFillColor = "purple",
        #     # Set fill color for errors
        #     errorFillColor = "red",
        #     # Set fill color for success
        #     successFillColor = "pink",
        #     # Set number of progress steps(default is 5)
        #     formProgressCount = 10,
        #     # Set progress animation duration
        #     formProgressAnimationDuration = 2000, #2seconds
        #     # Set progress animation easing curve
        #     formProgressAnimationEasingCurve = "InOutQuint",
        #     # Set progress container height
        #     height = 80,
        #     # Set progress container width
        #     width = 1000,
        #     # Set default progress percentage
        #     startPercentage = 50 #half
        # )

        # Slect progress bar theme (range 1-5)
        self.ui.widget.selectFormProgressIndicatorTheme(3)

        # Animate progress to 60 percent
        self.ui.widget.animateFormProgress(100) #60 percent 

        # UPDATE THE PROGRESS STEP STATUS
        self.ui.widget.setStepStatus(
            # Step 5
            step_5_error = True,
            # Step 2
            step_2_warning = True,
            # Step 3
            step_3_success = True
        )


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
