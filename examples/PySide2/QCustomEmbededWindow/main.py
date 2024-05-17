########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
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
from Custom_Widgets.QCustomEmbededWindow import QCustomEmbededWindow
########################################################################
from PySide2.QtWidgets import QStyle
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################

        self.show()

        # Get the current directory (folder) of the Python script
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the style.css file
        css_file_path = os.path.join(current_directory, 'style.css')

        # Read the CSS styles from the file
        with open(css_file_path, 'r') as f:
            self.css_style = f.read()

        # Apply the CSS style to the QCustomEmbededWindow instance
        self.setStyleSheet(self.css_style)

        @self.ui.pushButton.clicked.connect
        def slot():
            label = QLabel("My parent is the top-level widget so I can move anywhere 😎")
            label.setWordWrap(True)
            self.embededWindow = QCustomEmbededWindow(
                self.ui.scrollAreaWidgetContents,
                icon = QIcon(self.style().standardIcon(QStyle.SP_TitleBarMenuButton))
                )
            self.embededWindow.addWidget(label)
            self.embededWindow.show()

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  