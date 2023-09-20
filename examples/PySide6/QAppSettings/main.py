########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

# App functions
from Functions import AppFunctions

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

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        # CHANGE THE THEME NAME IN SETTINGS
        # Use one of the app themes from your JSON file
        # settings = QSettings()
        # settings.setValue("THEME", "Default-Light")
        # QAppSettings.updateAppSettings(self)


        # COLLAPSE SIDE MENU WIDGET
        self.ui.close_exit_prompt.clicked.connect(lambda: self.ui.exitPrompt.collapseMenu())

        # CHECKBOX EVENT LISTENER
        self.ui.checkBox.stateChanged.connect(lambda: self.changeAppTheme())

        # UPDATE THE CHECKBOX STATUS
        settings = QSettings()
        currentTheme = settings.value("THEME")
        if currentTheme == "Default-Dark":
            # Check the checkbox
            self.ui.checkBox.setChecked(True)
        else:
            # Unheck the checkbox
            self.ui.checkBox.setChecked(False)


        #######################################################################
        # APPLICATION FUNCTIONS AND EVENTS
        #######################################################################
        # Show/hide passwords
        self.ui.showHideLoginPass.clicked.connect(lambda: AppFunctions.showHideLoginPassword(self))
        self.ui.show_hide_signup_password.clicked.connect(lambda: AppFunctions.showHideSignupPassword(self))
        self.ui.show_hide_signup_conf_password.clicked.connect(lambda: AppFunctions.showHideSignupConfPassword(self))
        # Submit login details/form
        self.ui.submitLogin.clicked.connect(lambda: AppFunctions.login(self))
        # Submit register details/form
        self.ui.signup_btn.clicked.connect(lambda: AppFunctions.register(self))
        # Logout user
        self.ui.logoutBtn.clicked.connect(lambda: AppFunctions.logout(self))
        self.ui.logoutUser.clicked.connect(lambda: AppFunctions.logout(self))
        # Try again to login or register on network error
        self.ui.tryAgain.clicked.connect(lambda: AppFunctions.checkAppKey(self))
        # Check app key on app startup
        AppFunctions.checkAppKey(self)

        # Create context menu
        self.menu = QtWidgets.QMenu()
        # Add menu action(Action name, Action function)
        self.menu.addAction("Action One", self.action_one)
        self.menu.addAction("Action Two", self.action_two)

        # Add context menu to button
        self.ui.pushButton.setMenu(self.menu)

        # Create context menu
        self.helpMenu = QtWidgets.QMenu()
        # Add menu action(Action name, Action function)
        self.helpMenu.addAction("Help", self.help)
        self.helpMenu.addAction("About", self.about)

        # Add context menu to button
        self.ui.helpBtn.setMenu(self.helpMenu)


    # Create menu action functions
    def action_one(self):
        print("Action one clicked!")

    def action_two(self):
        print("Action two clicked!")

    def help(self):
        print("Should open help page!")

    def about(self):
        print("Should open about page!")



    # Change App Theme
    def changeAppTheme(self):
        settings = QSettings()
        if self.ui.checkBox.isChecked():
            settings.setValue("THEME", "Default-Dark")
        else:
            settings.setValue("THEME", "Default-Light")

        QAppSettings.updateAppSettings(self)


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
