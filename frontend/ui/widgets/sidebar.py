from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from ui.style.labels import headline_label1,headline_label2
from ui.style.theme import Theme as t
from ui.widgets.nav import navbar
from ui.widgets.nav_button import make_nav_button

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
        self.nav_bar=navbar()
        self.new_certificate = QPushButton("New Certificate")
        self.new_certificate.setStyleSheet(f"""
                QPushButton {{
                    background-color: #0f172a;   /* dark navy */
                    color: {t.primary};              /* light gray text */
                    border: 2px solid #38bdf8;   /* cyan border */
                    padding: 8px 18px;
                    font-size: 12px;
                    letter-spacing: 2px;
                    text-transform: uppercase;   /* note: Qt ignores this */
                }}

                QPushButton:hover {{
                    background-color: #111c33;
                    border-color: #60a5fa;
                }}

                QPushButton:pressed {{
                    background-color: #0b1220;
                    border-color: #1d4ed8;
                }}
                """)
                        
    
    def add_widgets(self):
        self.main_layout.addWidget(self.heading1)
        self.main_layout.addWidget(self.heading2)
        self.main_layout.addWidget(self.nav_bar)
        self.main_layout.addWidget(self.new_certificate)
        self.main_layout.addStretch()