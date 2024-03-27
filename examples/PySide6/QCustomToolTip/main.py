import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QGraphicsDropShadowEffect
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCustomQToolTip Tail Position Test")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

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

        button = QPushButton("HOVER: Auto-positioned Tool-Tip")
        self.layout.addWidget(button)
        self.addShadow(button)
        button.setToolTip("Testing Auto-positioned Tool-Tip.  Try resizing the window then hover again!")

        widget = QWidget()
        widgetLayout = QHBoxLayout()

        button = QPushButton("HOVER: Auto-positioned Tool-Tip")
        self.layout.addWidget(button)
        self.addShadow(button)
        button.setToolTip("Testing Auto-positioned Tool-Tip.  Try resizing the window then hover again!")

        widgetLayout.addWidget(button)

        button = QPushButton("HOVER: Auto-positioned Tool-Tip")
        self.layout.addWidget(button)
        self.addShadow(button)
        button.setToolTip("Testing Auto-positioned Tool-Tip.  Try resizing the window then hover again!")
        
        widgetLayout.addWidget(button)

        widget.setLayout(widgetLayout)
        self.layout.addWidget(widget)
        
        button = QPushButton("HOVER: Auto-positioned Tool-Tip")
        self.layout.addWidget(button)
        self.addShadow(button)
        button.setToolTip("Testing Auto-positioned Tool-Tip.  Try resizing the window then hover again!")


    def addShadow(self, widget):
        effect = QGraphicsDropShadowEffect(widget)
        effect.setColor(QColor(30, 30, 30, 200))
        effect.setBlurRadius(20)
        effect.setXOffset(0)
        effect.setYOffset(0)
        widget.setGraphicsEffect(effect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Install the QCustomQToolTipFilter event to your app in order to use the custom tooltip
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="auto")
    app.installEventFilter(app_tooltip_filter)
    window = MainWindow()
    window.resize(500, 300)
    window.show()
    sys.exit(app.exec())
