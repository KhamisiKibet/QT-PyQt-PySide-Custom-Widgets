import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor

from Custom_Widgets.QFlowProgressBar import QFlowProgressBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress Bar Test")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        # Initialize the QFlowProgressBase widget
        steps = ["Start: Step 1", "Step 2", "Step 3", "Final step: Step 4"]

        # Initialize different styles of QFlowProgressBar widgets with additional arguments
        self.flow_progress_bars = []
        styles = [
            QFlowProgressBar.Styles.Circular,
            QFlowProgressBar.Styles.Flat,
            QFlowProgressBar.Styles.Square
        ]

        for style in styles:
            # Customize colors for different progress bars
            if style == QFlowProgressBar.Styles.Circular:
                finished_color = QColor(0, 136, 254)  # Blue
                unfinished_color = QColor(228, 231, 237)  # Light gray
            elif style == QFlowProgressBar.Styles.Flat:
                finished_color = QColor(0, 176, 80)  # Green
                unfinished_color = QColor(255, 192, 0)  # Yellow
            else:
                finished_color = QColor(255, 0, 0)  # Red
                unfinished_color = QColor(128, 128, 128)  # Dark gray

            # Create progress bars with customized colors and labels
            progress_bar = QFlowProgressBar(
                steps,
                style,
                finishedBackgroundColor=finished_color,
                unfinishedBackgroundColor=unfinished_color,
                finishedNumberColor=Qt.white,  # White
                numberFontSize=12,  # Font size
                textFontSize=10,  # Font size
                pointerDirection=QFlowProgressBar.Direction.Down,  # Pointer direction for flat style
                animationDuration=1000,  # Animation duration
                stepsClickable=True  # Steps are clickable
            )

            progress_bar.setMaximumHeight(100)
            progress_bar.setMinimumHeight(70)
            progress_bar.onStepClicked.connect(self.on_step_clicked)
            self.flow_progress_bars.append(progress_bar)

        # Add buttons to control the progress bars
        self.next_button = QPushButton("Next Step")
        self.next_button.clicked.connect(self.next_step)

        self.prev_button = QPushButton("Previous Step")
        self.prev_button.clicked.connect(self.prev_step)

        # Add widgets to layout
        for progress_bar in self.flow_progress_bars:
            main_layout.addWidget(progress_bar)

        main_layout.addWidget(self.next_button)
        main_layout.addWidget(self.prev_button)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def next_step(self):
        # Move to the next step for each progress bar
        for progress_bar in self.flow_progress_bars:
            progress_bar.changeCurrentStep(progress_bar.getCurrentStep() + 1)

    def prev_step(self):
        # Move to the previous step for each progress bar
        for progress_bar in self.flow_progress_bars:
            progress_bar.changeCurrentStep(progress_bar.getCurrentStep() - 1)

    def on_step_clicked(self, step: int):
        # Handle step clicked event
        print(f"Step {step + 1} clicked")

        # Set the clicked step for each progress bar
        for progress_bar in self.flow_progress_bars:
            progress_bar.changeCurrentStep(step + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
