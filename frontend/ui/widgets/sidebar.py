from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from ui.style.labels import headline_label1,headline_label2
from ui.style.theme import Theme as t
from ui.widgets.nav import navbar
from ui.widgets.nav_button import make_nav_button
from PySide6.QtGui import QIcon

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
        
        self.alerts_btn = make_nav_button("Alerts", QIcon("icons/warning.png"))
        self.logs_btn = make_nav_button("Logs", QIcon("icons/log.png"))
                        
    
    def add_widgets(self):
        self.main_layout.addWidget(self.heading1, stretch=2)
        self.main_layout.addWidget(self.heading2, stretch=2)
        self.main_layout.addStretch(stretch=20)

        self.main_layout.addWidget(self.nav_bar,stretch=80)
        self.main_layout.addStretch(stretch=50)
        self.main_layout.addWidget(self.new_certificate,stretch=2)
        self.main_layout.addWidget(self.alerts_btn,stretch=2)
        self.main_layout.addWidget(self.logs_btn,stretch=2)
