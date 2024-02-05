########################################################################
## IMPORTS
########################################################################
import sys
########################################################################

########################################################################
## MODULE UPDATED TO USE QTPY
########################################################################
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
########################################################################

# IMPORT QTSASS
import qtsass
########################################################################
# IMPORT OS
import os
import shutil

from Custom_Widgets.Qss.colorsystem import CreateColorVariable
########################################################################
## IMPORT WORKER
########################################################################
from Custom_Widgets.WidgetsWorker import Worker, WorkerResponse

from Custom_Widgets.Log import *

########################################################################
## COMPILE STYLESHEET CLASS
########################################################################
class CompileStyleSheet():
    def __init__(self, parent=None):
        super(CompileStyleSheet, self).__init__(parent)      

    ########################################################################
    ## APPLY COMPILED STYLESHEET
    ########################################################################
    def applyCompiledSass(self):
        settings = QSettings()
        
        qcss_folder = os.path.abspath(os.path.join(os.getcwd(), 'Qss/scss'))
        if not os.path.exists(qcss_folder):
            os.makedirs(qcss_folder)
        
        css_folder = os.path.abspath(os.path.join(os.getcwd(), 'generated-files/css/'))
        if not os.path.exists(css_folder):
            os.makedirs(css_folder)

        main_sass_path = os.path.abspath(os.path.join(os.getcwd(), 'Qss/scss/main.scss'))
        styles_sass_path = os.path.abspath(os.path.join(os.getcwd(), 'Qss/scss/_styles.scss'))
        css_path = os.path.abspath(os.path.join(os.getcwd(), 'generated-files/css/main.css'))

        variablesFile = CreateColorVariable.CreateVariables(self)

        if not os.path.exists(main_sass_path):   
            shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scss/main.scss')), qcss_folder)  

        if not os.path.exists(styles_sass_path):   
            shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'scss/_styles.scss')), qcss_folder)  

        default_scss_path = os.path.abspath(os.path.join(os.getcwd(), 'Qss/scss/defaultStyle.scss'))
        if not os.path.exists(default_scss_path):   
            f = open(default_scss_path, 'w')
            print(f"""
            //===================================================//
            // FILE AUTO-GENERATED. PUT YOUR DEFAULT STYLES HERE. 
            // THESE STYLES WILL OVERIDE THE THEME STYLES
            //====================================================//
            
            //===================================================//
            // END //
            //====================================================//
            """, file=f)

            f.close()

        qtsass.compile_filename(main_sass_path, css_path)
        
        with open(css_path,"r") as css:
            stylesheet = css.read()
            self.setStyleSheet(stylesheet)
            # newly created menus may need re-styling
            for obj in QApplication.instance().allWidgets():
                if isinstance(obj, QMenu):
                    obj.setStyleSheet(stylesheet)
        
        # QPalette
        palette = QPalette()

        # Set the background color
        try:
            # pyside2
            palette.setColor(QPalette.Background, QColor(self.theme.COLOR_BACKGROUND_1))
        except AttributeError as e:
            pass
        try:
            # pyside6
            palette.setColor(QPalette.Window, QColor(self.theme.COLOR_BACKGROUND_1))
        except AttributeError as e:
            pass
        

        # Set the text color
        palette.setColor(QPalette.Text, QColor(self.theme.COLOR_TEXT_1))

        # Set the button color
        palette.setColor(QPalette.Button, QColor(self.theme.COLOR_BACKGROUND_3))

        # Set the button text color
        palette.setColor(QPalette.ButtonText, QColor(self.theme.COLOR_TEXT_1))

        # Set the highlight color
        palette.setColor(QPalette.Highlight, QColor(self.theme.COLOR_BACKGROUND_6))

        # Set the highlight text color
        palette.setColor(QPalette.HighlightedText, QColor(self.theme.COLOR_ACCENT_1))

        # Apply the palette to the main window
        self.setPalette(palette)

        self.update()
        
        ########################################################################
        ## GENERATE NEW ICONS
        # START WORKER
        # CURRENT THEME ICONS
        color = CreateColorVariable.getCurrentThemeInfo(self)
        normal_color = str(color["icons-color"])
        icons_folder = normal_color.replace("#", "")
        self.applyIcons(icons_folder)

        self.iconsWorker = Worker(self.compileSassTheme)
        self.iconsWorker.signals.result.connect(WorkerResponse.print_output)
        self.iconsWorker.signals.finished.connect(lambda: self.applyIcons(icons_folder))
        self.iconsWorker.signals.progress.connect(self.sassCompilationProgress)

        # ALL THEME ICONS
        self.allIconsWorker = Worker(self.makeAllIcons)
        self.allIconsWorker.signals.result.connect(WorkerResponse.print_output)
        self.allIconsWorker.signals.finished.connect(lambda: logInfo(self, "all icons have been checked and missing icons generated!"))
        self.allIconsWorker.signals.progress.connect(self.sassCompilationProgress)

        
        if not settings.value("ICONS-COLOR") == normal_color and color["icons-color"] is not None:     
            # Execute
            self.customWidgetsThreadpool.start(self.iconsWorker)
        else:
            self.customWidgetsThreadpool.start(self.allIconsWorker)
        

########################################################################
## ==>END
########################################################################

