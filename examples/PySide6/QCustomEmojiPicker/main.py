from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QPushButton, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
from Custom_Widgets.QCustomEmojiPicker import QCustomEmojiPicker
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Emoji Picker Test")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a container widget for the edit widgets and buttons
        container_widget = QWidget()
        container_layout = QHBoxLayout()
        container_widget.setLayout(container_layout)
        layout.addWidget(container_widget)

        # Create a QLineEdit widget
        line_edit = QLineEdit()
        container_layout.addWidget(line_edit)

        # Create a QPushButton for emoji picker for QLineEdit
        line_edit_btn = QPushButton("😀")
        line_edit_btn.clicked.connect(lambda: self.showEmojiPicker(line_edit))
        container_layout.addWidget(line_edit_btn)

        # Create a QTextEdit widget
        text_edit = QTextEdit()
        container_layout.addWidget(text_edit)

        # Create a QPushButton for emoji picker for QTextEdit
        text_edit_btn = QPushButton("😀")
        text_edit_btn.clicked.connect(lambda: self.showEmojiPicker(text_edit))
        container_layout.addWidget(text_edit_btn)

        self.show()

    def showEmojiPicker(self, target_widget):
        emoji_picker = QCustomEmojiPicker(target=target_widget, parent=self, itemsPerRow=16)
        emoji_picker.show()

        # Add shadow effect
        effect = emoji_picker.graphicsEffect()
        if effect is None:
            effect = QGraphicsDropShadowEffect(emoji_picker)
        effect.setColor(QColor(30, 30, 30, 200))
        effect.setBlurRadius(20)
        effect.setXOffset(0)
        effect.setYOffset(0)
        emoji_picker.setGraphicsEffect(effect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
