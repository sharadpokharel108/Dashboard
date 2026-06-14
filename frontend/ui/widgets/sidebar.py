from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from ui.style.labels import headline_label1,headline_label2
from ui.style.theme import Theme as t
class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet(f"background-color: {t.side_bar_background};")
        # self.setAutoFillBackground(True)
        self.create_layout()
        self.create_widgets()
        self.add_widgets()
        

    
    def create_layout(self):
        self.main_layout=QVBoxLayout(self)
        
    def create_widgets(self):
        self.heading1= headline_label1("RADIant")
        self.heading2=headline_label2("Infotech Nepal")
    
    def add_widgets(self):
        self.main_layout.addWidget(self.heading1)
        self.main_layout.addWidget(self.heading2)
        self.main_layout.addStretch()