from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from ui.style.theme import Theme as t

from ui.widgets.sidebar.sidebar import Sidebar
from ui.widgets.content import Contentbar
class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Certificate Manager")
        self.create_layout()
        self.create_widgets()
        self.add_widgets()
        
        
    def create_layout(self):
        self.main_layout=QHBoxLayout(self)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
    def create_widgets(self):
        self.sidebar = QWidget()
        self.sidebar.setStyleSheet(f"background-color: {t.side_bar_background};")
        self.sidebar.setAutoFillBackground(True)

        layout = QVBoxLayout(self.sidebar)
        layout.addWidget(Sidebar())
        
        self.content=Contentbar()
        
        
    def add_widgets(self):
        self.main_layout.addWidget(self.sidebar, stretch=15)
        self.main_layout.addWidget(self.content, stretch=85)