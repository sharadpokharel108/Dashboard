from PySide6.QtWidgets import QWidget, QHBoxLayout

from ui.widgets.sidebar import Sidebar
from ui.widgets.content import Contentbar
class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Certificate Manager")
        self.layout()
        self.create_widgets()
        self.add_widgets()
        
        
    def layout(self):
        self.main_layout=QHBoxLayout(self)
        
    def create_widgets(self):
        self.sidebar=Sidebar()
        self.content=Contentbar()
        
        
    def add_widgets(self):
        self.main_layout.addWidget(self.sidebar, stretch=15)
        self.main_layout.addWidget(self.content, stretch=85)