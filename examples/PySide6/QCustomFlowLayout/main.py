import sys
from PySide6 import QtCore, QtWidgets
from Custom_Widgets.QCustomFlowLayout import QCustomFlowLayout

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCustomFlowLayout Example")
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.flow_layout = QCustomFlowLayout(parent=self.central_widget, margin=10, spacing=5)

        # Create and add buttons to the flow layout
        for i in range(10):
            button = QtWidgets.QPushButton(f"Button {i+1}")
            self.flow_layout.addWidget(button)

        self.central_widget.setLayout(self.flow_layout)

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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())
