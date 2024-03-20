import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget, QGraphicsDropShadowEffect
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCustomTipOverlay Tail Position Test")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        # Create buttons to test different tail positions
        self.create_button("Auto", "auto")
        self.create_button("Top-Left", "top-left")
        self.create_button("Top-Center", "top-center")
        self.create_button("Top-Right", "top-right")
        self.create_button("Bottom-Left", "bottom-left")
        self.create_button("Bottom-Center", "bottom-center")
        self.create_button("Bottom-Right", "bottom-right")
        self.create_button("Auto", "auto")
        self.create_button("Left-Top", "left-top")
        self.create_button("Left-Bottom", "left-bottom")
        self.create_button("Right-Top", "right-top")
        self.create_button("Right-Bottom", "right-bottom")
        self.create_button("Left-Center", "left-center")
        self.create_button("Right-Center", "right-center")
        self.create_button("Auto", "auto")

        self.setStyleSheet("""
            QMainWindow, * {
                background-color: #f0f0f0;
            }
            QCustomTipOverlay > QFrame {
                border-radius: 10px;
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

    def create_button(self, text, tail_position):
        button = QPushButton(text)
        button.clicked.connect(lambda: self.show_tip(button, tail_position))
        self.layout.addWidget(button)
        self.addShadow(button)

    def show_tip(self, button, tail_position):
        tip = QCustomTipOverlay(
            target=button,
            title='Test Tip',
            description="This is a test tip",
            isClosable=True,
            tailPosition=tail_position,
            parent=self,
            duration=3000
        )

        self.addShadow(tip)

        tip.show()
    
    def addShadow(self, widget):
        effect = QGraphicsDropShadowEffect(widget)
        effect.setColor(QColor(0, 0, 0, 180))
        effect.setBlurRadius(35)
        effect.setXOffset(0)
        effect.setYOffset(0)
        widget.setGraphicsEffect(effect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 800)
    window.show()
    sys.exit(app.exec())
