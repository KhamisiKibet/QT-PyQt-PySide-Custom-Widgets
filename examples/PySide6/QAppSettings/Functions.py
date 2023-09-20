from PySide2.QtWidgets import QLineEdit, QMessageBox
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize

import requests
from requests.structures import CaseInsensitiveDict
import json

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################


########################################################################
# APP FUNCTIONS
# REGISTER/LOGIN USERS
# GENERATE UNIQUE APP ID/KEY
# SAVE APP SESSION(KEY/ID)
########################################################################

# Define the request URL and headers
url = 'https://projects.spinncode.com/python/qtsettings/appsettings/'
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

class AppFunctions():
    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg

    #######################################################################
    # LOGIN FUNCTION
    #######################################################################
    def login(self):
        # Validate form field
        if len(self.ui.loginUsername.text()) > 3:
            if len(self.ui.loginPassword.text()) < 2:
                self.ui.loginResponse.setText("Please enter a valid password")
                self.ui.loginResponse.setStyleSheet("color: red;")
            else:
                self.ui.loginResponse.setText("Please wait...")
                self.ui.loginResponse.setStyleSheet("color: '';")

                # Submit login data
                AppFunctions.loginUser(self)
        
        else:
            self.ui.loginResponse.setText("Please enter a valid username")
            self.ui.loginResponse.setStyleSheet("color: red;")

    #######################################################################
    # SUBMIT LOGIN DETAILS
    #######################################################################
    def loginUser(self):
        username = self.ui.loginUsername.text()
        password = self.ui.loginPassword.text()
        # CATCH NETWORK ERROR USING TRY CATCH METHOD
        try:
            # Get current app id and key from settings(if available)
            id, key = AppFunctions.getAppIdKey(self)
            print("app id:", id, "app key:", key)

            if id is None or key is None:
                id = " "
                key = " "

            data = {"login": True, "username":username,"password":password, "app_id": id, "app_key": key}
            # Convert the data to JSON
            json_data = json.dumps(data)
            # print(json_data)

            # Send the POST request
            responseData = requests.post(url, headers=headers, data=data)
            
            # Check if the request was successful (status code 200)
            if responseData.status_code == 200:
                # Parse the JSON response content
                responseData = responseData.json()
                # print(responseData)

                self.ui.loginResponse.setText(responseData['response_message'])
                # If logged in continue to final page
                if responseData['logged_in']:
                    # Save the returned app key and id
                    AppFunctions.createNewAppKey(self, responseData['app_id'], responseData['app_key'])
                    # then validate the saved app key and id
                    AppFunctions.checkAppKey(self)

                else:
                    self.ui.loginResponse.setStyleSheet("color: red;")

            else:
                print(f'Error: {responseData.status_code}')
                AppFunctions.showPopUpError(self, 
                    "An errror occured: ",
                    responseData.status_code) 

        # Catch exceptions
        except Exception as e:
            self.ui.mainPages.setCurrentWidget(self.ui.networkErrorPage) 
            AppFunctions.showPopUpError(self, 
                "You need internet connection to login. Please check your connection then try again.",
                e) 
            print(e)

    #######################################################################
    # SHOW HIDE LOGIN PASSWORD
    #######################################################################
    def showHideLoginPassword(self):
        if self.ui.loginPassword.echoMode() == QLineEdit.EchoMode.Password:
            # Change Icon
            eyeIcon = QIcon()
            eyeIcon.addFile(u":/icons/Icons/eye.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.showHideLoginPass.setIcon(eyeIcon)
            # Change echo mode
            self.ui.loginPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            # change icon
            eyeIcon = QIcon()
            eyeIcon.addFile(u":/icons/Icons/eye-off.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.showHideLoginPass.setIcon(eyeIcon)
            # Change echo mode
            self.ui.loginPassword.setEchoMode(QLineEdit.EchoMode.Password)

    #######################################################################
    # VALIDATE REGISTRATION FORM
    #######################################################################
    def register(self):
        if len(self.ui.signup_username.text()) > 3:
            if len(self.ui.signup_password.text()) < 4:
                self.ui.registerResponse.setText("Please enter a valid password. Minimum password length is 4")
                self.ui.registerResponse.setStyleSheet("color: red;")
            else:
                if self.ui.signup_password.text() == self.ui.signup_conf_password.text():
                    self.ui.registerResponse.setText("Please wait...")
                    self.ui.registerResponse.setStyleSheet("color: '';")

                    # Submit register data
                    AppFunctions.registeruser(self)
                else:
                    self.ui.registerResponse.setText("Passwords not matching, please check your password.")
                    self.ui.registerResponse.setStyleSheet("color: red;")
        
        else:
            self.ui.registerResponse.setText("Please enter a valid username")
            self.ui.registerResponse.setStyleSheet("color: red;")

    #######################################################################
    # SUBMIT REGISTRATION FORM
    #######################################################################
    def registeruser(self):
        username = self.ui.signup_username.text()
        password = self.ui.signup_password.text()
        c_password = self.ui.signup_conf_password.text()
        # CATCH NETWORK ERROR USING TRY CATCH METHOD
        try:
            data = {"register": True, "username":username,"password":password,"confirm_password":c_password}
            
            # Send the POST request
            responseData = requests.post(url, headers=headers, data=data)
            
            # Check if the request was successful (status code 200)
            if responseData.status_code == 200:
                # Parse the JSON response content
                responseData = responseData.json()
                # print(responseData)
                self.ui.registerResponse.setText(responseData['response_message'])
                # If registered continue to final page
                if responseData['registered']:
                    AppFunctions.createNewAppKey(self, responseData['app_id'], responseData['app_key'])
                    AppFunctions.checkAppKey(self)

                else:
                    self.ui.registerResponse.setStyleSheet("color: red;")

            else:
                print(f'Error: {responseData.status_code}')
                AppFunctions.showPopUpError(self, 
                    "An errror occured: ",
                    responseData.status_code) 

        except Exception as e:
            self.ui.mainPages.setCurrentWidget(self.ui.networkErrorPage) 
            AppFunctions.showPopUpError(self, 
                "You need internet connection to register. Please check your connection then try again.",
                e) 
            print(e)

    #######################################################################
    # SHOW HIDE REGISTER PASSWORDS
    #######################################################################
    def showHideSignupPassword(self):
        if self.ui.signup_password.echoMode() == QLineEdit.EchoMode.Password:
            # Change Icon
            eyeIcon = QIcon()
            eyeIcon.addFile(u":/icons/Icons/eye.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.show_hide_signup_password.setIcon(eyeIcon)
            # Change echo mode
            self.ui.signup_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            # change icon
            eyeIcon = QIcon()
            eyeIcon.addFile(u":/icons/Icons/eye-off.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.show_hide_signup_password.setIcon(eyeIcon)
            # Change echo mode
            self.ui.signup_password.setEchoMode(QLineEdit.EchoMode.Password)

    def showHideSignupConfPassword(self):
        if self.ui.signup_conf_password.echoMode() == QLineEdit.EchoMode.Password:
            # Change Icon
            eyeIcon = QIcon()
            eyeIcon.addFile(u":/icons/Icons/eye.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.show_hide_signup_conf_password.setIcon(eyeIcon)
            # Change echo mode
            self.ui.signup_conf_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            # change icon
            eyeIcon = QIcon()
            eyeIcon.addFile(u":/icons/Icons/eye-off.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.show_hide_signup_conf_password.setIcon(eyeIcon)
            # Change echo mode
            self.ui.signup_conf_password.setEchoMode(QLineEdit.EchoMode.Password)

    #######################################################################
    # SAVE APP DETAILS
    #######################################################################
    def createNewAppKey(self, id, key):
        settings = QSettings()
        settings.setValue("APPID", id)
        settings.setValue("APPKEY", key)

    #######################################################################
    # GET APP KEY AND ID
    #######################################################################
    def getAppIdKey(self):
        settings = QSettings()
        id = settings.value("APPID")
        key = settings.value("APPKEY")

        return id, key

    #######################################################################
    # VALIDATE THE SAVED APP KEY AND ID
    #######################################################################
    def checkAppKey(self):
        # CATCH NETWORK ERROR USING TRY CATCH METHOD
        try:
            id, key = AppFunctions.getAppIdKey(self)
            print("app id:", id, "app key:", key)

            if id is None or key is None:
                AppFunctions.showPopUpError(self, 
                    "Please register your app", "App not registered") 
                
                self.ui.mainPages.setCurrentWidget(self.ui.loginPage) 

                return
            
            data = {"checkapp": True, "app_id": id, "app_key": key}
            # Send the POST request
            responseData = requests.post(url, headers=headers, data=data)
            
            # Check if the request was successful (status code 200)
            if responseData.status_code == 200:
                # Parse the JSON response content
                responseData = responseData.json()
                # print(responseData)
                self.ui.loginResponse.setText(responseData['response_message'])
                # If logged in continue to final page
                if responseData['valid_app']:
                    self.ui.mainPages.setCurrentWidget(self.ui.homePage)
                    self.ui.appDetails.setText("""
                        <html><head/><body>
                        <p align="center">
                        <span style=" font-weight:600;">Username:</span> % s</p>
                        <p align="center"><span style=" font-weight:600;">App ID:</span> % s</p>
                        <p align="center"><span style=" font-weight:600;">APP Key:</span> % s</p>
                        <p align="center"><span style=" font-weight:600;">Expiry Date:</span> % s</p>
                        </body></html>
                        """ %(responseData['username'], responseData['app_id'], 
                            responseData['app_key'], responseData['expiry_date'])
                        )

                    self.ui.userAccountPages.setCurrentWidget(self.ui.loggedAccountDetails)
                    self.ui.username.setText(responseData['username'])
                    self.ui.app_id.setText(responseData['app_id'])
                    self.ui.app_key.setText(responseData['app_key'])
                    self.ui.key_date.setText(responseData['expiry_date'])

                else:
                    self.ui.mainPages.setCurrentWidget(self.ui.loginPage)

            else:
                print(f'Error: {responseData.status_code}')
                AppFunctions.showPopUpError(self, 
                    "An errror occured: ",
                    responseData.status_code) 

        except Exception as e:
            self.ui.mainPages.setCurrentWidget(self.ui.networkErrorPage)   
            AppFunctions.showPopUpError(self, 
                "You need internet connection to login or register. Please check your connection then try again.",
                e)        
            print(e)


    #######################################################################
    # LOGOUT
    #######################################################################
    def logout(self):
        settings = QSettings()
        # settings.setValue("APPID", id)
        settings.setValue("APPKEY", "")
        self.ui.loginResponse.setText("Account logged out. Please login.")
        self.ui.mainPages.setCurrentWidget(self.ui.loginPage)
        self.ui.userAccountPages.setCurrentWidget(self.ui.loginAccount)

    #######################################################################
    # SHOW POPUP MESSAGE
    #######################################################################
    def showPopUpError(self, message, more):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setInformativeText(str(more))
        msg.setWindowTitle("Error")
        msg.exec_()
        