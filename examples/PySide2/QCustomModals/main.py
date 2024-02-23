import sys
from functools import partial
from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QScrollArea, QGraphicsDropShadowEffect, QStyle
from PySide2.QtGui import QColor, QPalette
from Custom_Widgets.QCustomModals import QCustomModals

class TestModalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Test Modal Window")
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignTop)
        
        self.scroll_area = QScrollArea(self.central_widget)
        self.scroll_area.setWidgetResizable(True)
        self.central_widget.setLayout(QVBoxLayout())
        self.central_widget.layout().addWidget(self.scroll_area)
        
        self.scroll_area_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)
        
        self.scroll_layout = QVBoxLayout(self.scroll_area_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        
        self.create_buttons()
        
    def create_buttons(self):
        modal_types = ["Information", "Success", "Warning", "Error", "Custom"]
        positions = ["top-left", "top-center", "top-right", "center-left", "center-center", 
                     "center-right", "bottom-left", "bottom-center", "bottom-right"]
        
        for modal_type in modal_types:
            for position in positions:
                button = QPushButton(f"{modal_type} Modal ({position})")
                button.setObjectName(f"{modal_type.lower()}_{position.replace('-', '_')}_button")
                button.setStyleSheet(f"background-color: {self.get_button_color(modal_type)}")
                button.clicked.connect(partial(self.show_modal, modal_type, position))
                self.scroll_layout.addWidget(button)
        
    def get_button_color(self, modal_type):
        if self.isDark():
            color_map = {
                "Information": "#2799be",  # dark blue or teal
                "Success": "#29b328",       # dark green
                "Warning": "#bb8128",       # dark yellow
                "Error": "#bb221d",         # dark red or pink
                "Custom": "#0E1115"         # 
            }
            
        else:
            color_map = {
                "Information": "#E6F7FF",  # light blue or teal
                "Success": "#C8E6C9",       # light green
                "Warning": "#FFF9E1",       # light yellow
                "Error": "#FFEBEE",         # light red or pink
                "Custom": "#FFFFFF"         # 
            }
        return color_map.get(modal_type, "#FFFFFF")  # Default to white
    
    def show_modal(self, modal_type, position):
        kwargs = {
            "title": f"{modal_type} Title",
            "description": f"This is a {modal_type.lower()} modal in position: {position}",
            "position": position,
            "parent": self,
            "animationDuration": 3000 # set to zero if you want you modal to not auto-close
        }
        
        if modal_type == "Information":
            modal = QCustomModals.InformationModal(**kwargs)
        elif modal_type == "Success":
            modal = QCustomModals.SuccessModal(**kwargs)
        elif modal_type == "Warning":
            modal = QCustomModals.WarningModal(**kwargs)
        elif modal_type == "Error":
            modal = QCustomModals.ErrorModal(**kwargs)
        elif modal_type == "Custom":
            kwargs["modalIcon"] = self.style().standardIcon(QStyle.SP_MessageBoxQuestion).pixmap(QSize(32, 32))  # Change QSystemIcon.Warning to any desired system icon
            kwargs["description"] += "\n\nCustom modals need additional styling since they are transparent by default."
            modal = QCustomModals.CustomModal(**kwargs)
            
            
        # Apply CSS styling to the main window or modal parent to avoid painting over default modal style
        # set dynamic bg & icons color for custom modal to match app theme
        if self.isDark(): 
            bg_color = "#0E1115"
            icons_color = "#F5F5F5" #white
        else: 
            bg_color = "#F0F0F0" 
            icons_color = "#000" #black
        self.setStyleSheet("""
            InformationModal, SuccessModal, ErrorModal, WarningModal, CustomModal{
                border-radius: 10px;
            }
            CustomModal{
                background-color: """ + bg_color + """; /* Light gray background color */
                color: """ + icons_color + """
            }
            CustomModal *{
                background-color: transparent;
            }
        """)
            
            
        # Apply QGraphicsDropShadowEffect to create a shadow effect
        shadow_effect = QGraphicsDropShadowEffect(modal)
        shadow_effect.setBlurRadius(10)
        shadow_effect.setColor(QColor(0, 0, 0, 150))
        shadow_effect.setOffset(0, 0)
        modal.setGraphicsEffect(shadow_effect)
        
        modal.show()
        
    def isDark(self):
        palette = self.palette()
        background_color = palette.color(QPalette.Window)
        # Calculate the luminance of the background color
        luminance = 0.2126 * background_color.red() + 0.7152 * background_color.green() + 0.0722 * background_color.blue()

        # Determine if the background color is dark or light
        if luminance < 128:
            # Dark background
            return True
        else:
            # Light background
            return False
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = TestModalWindow()
    window.resize(800, 600)
    window.show()
    
    sys.exit(app.exec())
