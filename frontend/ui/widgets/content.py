from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.widgets.topbar import Topbar
class Contentbar(QWidget):
    def __init__(self):
        super().__init__()
        self.create_layout()
        self.create_widgets()
        self.add_widgets()
        
    def create_layout(self):
        self.main_layout=QVBoxLayout(self)
        
    def create_widgets(self):
        #----------------------------------------
        self.top_bar=QWidget()
        self.top_bar.setStyleSheet("""background-color:#081425;""")
        self.top_bar_layout=QVBoxLayout(self.top_bar)
        self.top_bar_layout.addWidget(Topbar())
        #-----------------------------------------
        
    
    def add_widgets(self):
        self.main_layout.addWidget(self.top_bar)