import sys
import time
from PySide6.QtGui import QColor
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QColor
from Custom_Widgets.QCustomLoadingIndicators import QCustomPerlinLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create a loader widget with the main window as parent
        self.loader = QCustomPerlinLoader()

        # self.loader = QCustomPerlinLoader(
        #     parent=self,
        #     size=QSize(400, 400),
        #     message="LOADING...",
        #     color=QColor("white"),
        #     fontFamily="Ebrima",
        #     fontSize=30,
        #     rayon=200,
        #     duration=60 * 1000,
        #     noiseOctaves=0.8,
        #     noiseSeed=int(time.time()),
        #     backgroundColor=QColor("transparent"),
        #     circleColor1=QColor("#ff2e63"),
        #     circleColor2=QColor("#082e63"),
        #     circleColor3=QColor(57, 115, 171, 100)
        # )

        self.centralwidget = QWidget(self)
        self.layout = QVBoxLayout(self.centralwidget)

        self.layout.addWidget(self.loader)
        self.layout.setAlignment(self.loader, Qt.AlignCenter)  # Align loader widget to the center of the layout

        self.setCentralWidget(self.centralwidget)
        self.resize(800, 450)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create an instance of MainWindow
    main_window = MainWindow()
    main_window.show()
    
    sys.exit(app.exec())

