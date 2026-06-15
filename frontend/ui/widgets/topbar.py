from PySide6.QtWidgets import QWidget,QHBoxLayout
from ui.style.labels import headline_label1
from ui.widgets.search_bar import search_widget
class Topbar(QWidget):
    def __init__(self):
        super().__init__()
        self.create_layout()
        self.create_widgets()
        self.add_widgets()
        
    def create_layout(self):
        self.main_layout=QHBoxLayout(self)
        
    def create_widgets(self):
        self.heading_dummy=headline_label1("Dummy data")
        self.search_bar=search_widget(self)
        
    
    def add_widgets(self):
        self.main_layout.addWidget(self.heading_dummy)
        self.main_layout.addWidget(self.search_bar)
        
