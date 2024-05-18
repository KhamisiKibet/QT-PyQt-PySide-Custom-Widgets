import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from Custom_Widgets.QCustomQDialog import QCustomQDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCustomQDialog Example")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.button = QPushButton("Show Dialog")
        self.button.clicked.connect(self.show_dialog)
        self.layout.addWidget(self.button)

        self.setStyleSheet("""
            QMainWindow, * {
                background-color: #f0f0f0;
            }
            QCustomQToolTip *{
                color: #000
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)

    def show_dialog(self):
        dialog = QCustomQDialog(
            parent = self,
            title="Dialog Title",
            description="Dialog Description",
            yesButtonText="Confirm",
            cancelButtonText="Cancel",
            # yesButtonIcon="yes_icon.png",
            # cancelButtonIcon="cancel_icon.png",
            showYesButton=True,
            showCancelButton=True,
            setModal=True,
            frameless=True,
            windowMovable=True,
            animationDuration=500
        )
        dialog.show()

        # events
        dialog.accepted.connect(lambda: print("Accepted!")) #yes button clicked
        dialog.rejected.connect(lambda: print("Rejected!")) #cancel button clicked

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
