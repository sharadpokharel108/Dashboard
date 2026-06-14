from PySide6.QtWidgets import QWidget, QHBoxLayout
from ui.widgets.topbar import Topbar
from ui.widgets.footbar import Footbarbar
from ui.widgets.toolbar import Toolbar
from ui.widgets.topbar import Topbar
class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Certificate Manager")
        
        
    def layout(self):
        main_layout=QHBoxLayout(self)
        
    def create_widgets(self):
        pass