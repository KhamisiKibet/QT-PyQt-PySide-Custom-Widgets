import sys
import os
from functools import partial
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QVBoxLayout, QWidget, QLabel
from Custom_Widgets.QCustomCodeEditor import QCustomCodeEditor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main container widget
        self.container = QWidget()
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # First editor
        self.editor1_label = QLabel("Primary Code Editor")
        self.editor1 = QCustomCodeEditor()
        self.editor1.setTheme("default")  # Set default theme
        self.editor1.setLang("python")

        # Second editor
        self.editor2_label = QLabel("Embedded Code Editor")
        self.editor2 = QCustomCodeEditor()
        self.editor2.setTheme("default")  # Set default theme
        self.editor2.loadFile(os.path.join( os.path.dirname(__file__), "hello.cpp"))

        # Add widgets to layout
        self.layout.addWidget(self.editor1_label)
        self.layout.addWidget(self.editor1)
        self.layout.addWidget(self.editor2_label)
        self.layout.addWidget(self.editor2)

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = QToolBar("Themes", self)
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        themes = ["Default", "One Light", "One Dark", "Monokai", "Oceanic", "Zenburn"]
        for theme in themes:
            button = QPushButton(theme, self)
            button.clicked.connect(partial(self.set_theme, theme.lower().replace(" ", "-")))
            toolbar.addWidget(button)

    def set_theme(self, theme):
        self.editor1.setTheme(theme)
        self.editor2.setTheme(theme)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
