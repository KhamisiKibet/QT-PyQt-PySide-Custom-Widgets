########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os

########################################################################
## MODULE UPDATED TO USE QT.PY
########################################################################
from qtpy.QtCore import QCoreApplication, QSettings

from Custom_Widgets.Qss.SassCompiler import CompileStyleSheet

########################################################################
## QT APP SETTINGS
########################################################################
class QAppSettings():
    def __init__(self, parent=None):
        super(QAppSettings, self).__init__(parent)
        ########################################################################
        ## CREATE APP SETTINGS
        ########################################################################

    def updateAppSettings(self):

        if len(str(self.orginazationName)) > 0:
            QCoreApplication.setOrganizationName(str(self.orginazationName))
        if len(str(self.applicationName)) > 0:
            QCoreApplication.setApplicationName(str(self.applicationName))
        if len(str(self.orginazationDomain)) > 0:
            QCoreApplication.setOrganizationDomain(str(self.orginazationDomain))

        settings = QSettings()

        if settings.value("THEME") is None:
            for theme in self.ui.themes:
                if theme.defaultTheme:
                    # update app theme
                    settings.setValue("THEME", theme.name)


        #######################################################################
        # APPLY COMPILED STYLESHEET
        #######################################################################
        self.reloadJsonStyles(update = True)
        CompileStyleSheet.applyCompiledSass(self)


########################################################################
## END
########################################################################