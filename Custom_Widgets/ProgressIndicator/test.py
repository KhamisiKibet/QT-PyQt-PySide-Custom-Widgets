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
import random
########################################################################
# IMPORT GUI FILE
from Custom_Widgets.ProgressIndicator.ui_interface import *
########################################################################

########################################################################
# IMPORT CUSTOM BUTTONS, FORM PROGRESS INDICATOR AND QSTACKEDWIDGET FILE
# We will only use form progress indicator
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


        # CUSTOMIZE FORM PROGRESS INDICATOR
        self.ui.widget.updateFormProgressIndicator(
            # Set font color
            # color = "#000", 
            # Set fill color
            # fillColor = "white", 
            # Set fill color for warnings
            # warningFillColor = "purple",
            # Set fill color for errors
            # errorFillColor = "red",
            # Set fill color for success
            # successFillColor = "pink",
            # Set number of progress steps(default is 5)
            # formProgressCount = 5,
            # Set progress animation duration
            # formProgressAnimationDuration = 200,
            # Set progress animation easing curve
            formProgressAnimationEasingCurve = "InOutQuint",
            # Set progress container height
            height = 80,
            # Set progress container width
            width = 500,
            # Set default progress percentage
            # startPercentage = 50 #half
            )

        # WIDGET 2
        self.ui.widget_2.updateFormProgressIndicator(
            # Set font color
            # color = "#000", 
            # Set fill color
            # fillColor = "white", 
            # Set fill color for warnings
            # warningFillColor = "purple",
            # Set fill color for errors
            # errorFillColor = "red",
            # Set fill color for success
            # successFillColor = "pink",
            # Set number of progress steps(default is 5)
            formProgressCount = 10,
            # Set progress animation duration
            formProgressAnimationDuration = 2000, #2seconds
            # Set progress animation easing curve
            # formProgressAnimationEasingCurve = "InOutQuint",
            # Set progress container height
            height = 80,
            # Set progress container width
            # width = 1000,
            # Set default progress percentage
            # startPercentage = 50 #half
            )

        self.ui.widget.selectFormProgressIndicatorTheme(4)
        self.ui.widget_2.selectFormProgressIndicatorTheme(2)
        self.ui.widget_2.animateFormProgress(60) #60 percent 

        # WIDGET 3
        self.ui.widget_3.updateFormProgressIndicator(
            # Set font color
            # color = "#000", 
            # Set fill color
            # fillColor = "white", 
            # Set fill color for warnings
            # warningFillColor = "purple",
            # Set fill color for errors
            # errorFillColor = "red",
            # Set fill color for success
            # successFillColor = "pink",
            # Set number of progress steps(default is 5)
            formProgressCount = 10,
            # Set progress animation duration
            formProgressAnimationDuration = 2000, #2seconds
            # Set progress animation easing curve
            # formProgressAnimationEasingCurve = "InOutQuint",
            # Set progress container height
            height = 80,
            # Set progress container width
            width = 500,
            # Set default progress percentage
            # startPercentage = 50 #half
            )

        self.ui.widget_3.selectFormProgressIndicatorTheme(3)
        self.ui.widget_3.animateFormProgress(60)

        # NAVIGATE THROUGH FORM STEPS
        # 20 percent
        self.ui.step_6.clicked.connect(lambda: self.ui.widget_2.animateFormProgress(20))
        # 40 percent
        self.ui.step_7.clicked.connect(lambda: self.ui.widget_2.animateFormProgress(40))
        # 60 percent
        self.ui.step_8.clicked.connect(lambda: self.ui.widget_2.animateFormProgress(60))
        # 80 percent
        self.ui.step_9.clicked.connect(lambda: self.ui.widget_2.animateFormProgress(80))
        # 100 percent
        self.ui.step_10.clicked.connect(lambda: self.ui.widget_2.animateFormProgress(100))

        # UPDATE THE PROGRESS STEP STATUS
        self.ui.widget_2.setStepStatus(
            # Step 5
            step_5_error = True,
            # Step 2
            step_3_warning = True,
            # Step 3
            step_8_success = True
            )

        # UPDATE THE PROGRESS STEP STATUS
        self.ui.widget.setStepStatus(
            # Step 5
            step_5_error = True,
            # Step 2
            step_2_warning = True,
            # Step 3
            step_3_success = True
            )

        # NAVIGATE THROUGH FORM STEPS
        # 20 percent
        self.ui.step_1.clicked.connect(lambda: self.ui.widget.animateFormProgress(20))
        # 40 percent
        self.ui.step_2.clicked.connect(lambda: self.ui.widget.animateFormProgress(40))
        # 60 percent
        self.ui.step_3.clicked.connect(lambda: self.ui.widget.animateFormProgress(60))
        # 80 percent
        self.ui.step_4.clicked.connect(lambda: self.ui.widget.animateFormProgress(80))
        # 100 percent
        self.ui.step_5.clicked.connect(lambda: self.ui.widget.animateFormProgress(100))

        # ANIMATE THE PROGRESS
        # LETS ADD TIMER TO CHANGE PROGRESSES
        self.download = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.downloadProgress) #progress function
        self.timer.start(100)

        # Change all progresses to zero on start
        # QtCore.QTimer.singleShot(0, lambda: self.ui.progressBar.rpb_setValue(0))

    # Simulate download process
    def downloadProgress(self):

        statuses = ["warning", "error", "success"]
        if self.download < 101:
            self.download += 1
            
        else:
            self.download = 0
            # Reset step statuses
            for x in range(1, 11):

                for y in statuses:
                    self.ui.widget_3.setStepStatus(
                        step = int(x),
                        # Step 5
                        status = y,
                        # Step 2
                        value = False,
                    )

            # Apply new style
            formProgressCount = random.choice ([10, 5, 3, 7, 15])
            height = random.choice ([20, 40, 50, 60])
            theme = random.choice ([1, 2, 3, 4, 5])
            # WIDGET 3
            self.ui.widget_3.updateFormProgressIndicator(
                # Set number of progress steps(default is 5)
                formProgressCount = formProgressCount,
                # Set progress animation duration
                height = height
            )
            # Apply theme
            self.ui.widget_3.selectFormProgressIndicatorTheme(theme)

            # Update UI labels
            self.ui.theme.setText(str(theme))
            self.ui.height.setText(str(height))
            self.ui.steps.setText(str(formProgressCount))


        # Animate progress
        self.ui.widget_3.animateFormProgress(self.download)

        # Apply random progress step status
        randStatus = random.choice (statuses)
        if self.download % self.ui.widget_3.formProgressCount == 0:            
            self.ui.widget_3.setStepStatus(
                step = int(self.download / self.ui.widget_3.formProgressCount),
                # Step 5
                status = randStatus,
                # Step 2
                value = True,
                )
        # print(self.ui.widget_3.step_3_error)


########################################################################
## EXECUTE APP
########################################################################
def main():
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
