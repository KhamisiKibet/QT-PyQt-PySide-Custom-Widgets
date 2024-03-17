########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################

########################################################################
## MODULE UPDATED TO USE QT.PY
########################################################################
from qtpy.QtWidgets import QPushButton

########################################################################
## GROUP BUTTONS
########################################################################
class QCustomQPushButtonGroup(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.group = None

    ########################################################################
    ## BUTTON GROUP
    ########################################################################
    def getButtonGroup(self):
        return self.group
    def getButtonGroupActiveStyle(self):
        group = self.getButtonGroup()
        if group == None:
            return None
        return getattr(self.groupParent, "group_active_"+str(group))
    def getButtonGroupNotActiveStyle(self):
        group = self.getButtonGroup()
        if group == None:
            return None
        return getattr(self.groupParent, "group_not_active_"+str(group))
    def getButtonGroupButtons(self):
        group = self.getButtonGroup()
        if group == None:
            return None
        return getattr(self.groupParent, "group_btns_"+str(group))

    def setButtonGroupActiveStyle(self, style):
        group = self.getButtonGroup()
        if group == None:
            raise Exception("Unknown button group. The button does not belong to any group")
        setattr(self.groupParent, "group_active_"+str(group), style)
        groupBtns = self.getButtonGroupButtons()
        for x in groupBtns:
            if x.active:
                x.setStyleSheet(style)

    def setButtonGroupNotActiveStyle(self, style):
        group = self.getButtonGroup()
        if group == None:
            raise Exception("Unknown button group. The button does not belong to any group")
        setattr(self.groupParent, "group_not_active_"+str(group), style)