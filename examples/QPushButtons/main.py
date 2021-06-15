########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from PySide2.QtCore import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT CUSTOM BUTTONS FILE
# Because ill be frequently updating this package,
# run "pip install --upgrade QT-PyQt-PySide-Custom-Widgets"
# to install any updates
from Custom_Widgets.Widgets import *
########################################################################

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ######################################################################
        ## APPLY STYLE FROM JSON FILE
        ########################################################################
        loadJsonStyle(self, self.ui)

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        ######################################################################
        ## UNCOMMENT/COMMENT THE COMMENTED STATEMENTS TO SEE THEIR EFFECTS
        ########################################################################

        # for w in self.ui.widget.findChildren(QPushButton):            

            ########################################################################
            # check if the stylesheet was found 
            ########################################################################
            # if no style was found, apply the default style from the animation theme
            ########################################################################

            # if not w.wasThemed:
            	########################################################################
                # w is the button
                # 9 is the theme
                ########################################################################
                # applyAnimationThemeStyle(w, 2)

                ########################################################################
                # OR
                ########################################################################
                # Appply your own custom theme
                ########################################################################
                # applyCustomAnimationThemeStyle(w, "red", "yellow")
                # print(w)

        ########################################################################
        # Create new button
        ########################################################################
        # button = QPushButton("name")
        # button.setText("Login")
        # button.setObjectTheme(2)
        # self.ui.gridLayout.addWidget(button, 2, 1, 1, 1)

        ########################################################################
        # UNCOMMENT THE STATEMENTS BELOW TO SEE THEIR EFFECTS
        ########################################################################
        # self.ui.pushButton.setObjectTheme(1)
        # self.ui.pushButton_2.setObjectTheme(2)
        # self.ui.pushButton_3.setObjectTheme(3)
        # self.ui.pushButton_4.setObjectTheme(4)
        # self.ui.pushButton_5.setObjectTheme(5)
        # self.ui.pushButton_6.setObjectTheme(6)
        # self.ui.pushButton_7.setObjectTheme(11)
        # self.ui.pushButton_5.setObjectTheme(10)
        # self.ui.pushButton.setObjectCustomTheme("#fff", "#000")
        # self.ui.pushButton.setObjectAnimateOn("hover")
        # self.ui.pushButton_7.setObjectAnimateOn("click")
        # self.ui.pushButton._animation.setEasingCurve(QtCore.QEasingCurve.InOutElastic)

        ########################################################################
        # STYLE APPLIED AFTER THE ANIMATION IS COMPLETE
        ########################################################################
        # self.ui.pushButton.setObjectFallBackStyle("""
        # border-style: solid;
        # border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #FF4200, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);
        # border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #FF4200, stop:0.5 #FF4200, stop:0.6 #C0DB50, stop:1 #C0DB50);
        # border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #FF4200, stop:0.3 #FF4200, stop:0.7 #100E19, stop:1 #100E19);
        # border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);
        # border-width: 5px;
        # border-radius: 1px;
        # color: #d3dae3;
        # padding: 2px;
        # background-color: #100E19;
        # """)  

        ########################################################################
        # STYLE APPLIED ALONGSIDE ANIMATION THEME STYLE AND FALLBACK STYLE
        ########################################################################
        # self.ui.pushButton.setObjectDefaultStyle(
        #     """
        #         border-radius:5px;
        #         border-width: 10px;
        #         color: #d3dae3;
        #         padding: 5px;
        #     """)   

        ########################################################################
        # Apply button icon
        ########################################################################
        # iconify(
            # self.ui.pushButton, 
            # icon = "font-awesome:solid:cloud-download-alt", 
            # color = "orange", 
            # size = 64, 
            # animation = "spin", 
            # animateOn = "click"
            # )

        ########################################################################
        # Apply button shadow
        ########################################################################
        # applyButtonShadow(
        #     self.ui.pushButton_4, 
        #     color= "#fff", 
        #     applyShadowOn= "hover", 
        #     animateShadow = True, 
        #     blurRadius = 100, 
        #     animateShadowDuration = 500,
        #     xOffset = 0,
        #     yOffset = 0
        #     )



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