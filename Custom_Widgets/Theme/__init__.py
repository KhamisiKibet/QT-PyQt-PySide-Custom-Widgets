from qtpy.QtGui import *
from qtpy.QtWidgets import *

def setNewIcon(self, url):
    icon = QIcon(url)
    self.setIcon(icon)

    self.iconUrl = url

def setNewPixmap(self, url):
    piximap = QPixmap(url)
    self.setPixmap(piximap)

    self.piximapUrl = url

def setNewTabIcon(self, tabName, url):
    icon = QIcon(url)

    # Find the index of the tab with the name "Tab 2"
    tab_index = -1
    for index in range(self.count()):
        tab_object_name = self.widget(index).objectName()
        if tab_object_name == tabName:
            tab_index = index
            break
    # Change icon of the tab with the name "Tab 2"
    if tab_index != -1:
        self.setTabIcon(tab_index, icon)

    self.iconUrl = url
    
