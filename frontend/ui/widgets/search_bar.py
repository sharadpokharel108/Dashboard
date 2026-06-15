from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import  QIcon, QFont, QAction


def search_widget(self):
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search...")
        self.search_box.setFixedWidth(250)
        self.search_box.setFont(QFont("Segoe UI", 10))

        # Add search icon that doesn't disappear
        search_action = QAction(self)
        search_icon = QIcon("D:\login\dashboard\..\images\search.png") 
        search_action.setIcon(search_icon)
        self.search_box.addAction(search_action, QLineEdit.LeadingPosition)

        # Stylish QLineEdit
        self.search_box.setStyleSheet("""
            QLineEdit {
                background: #f0f0f0; 
                padding: 8px 12px 8px 32px; /* left padding for icon */
                border-radius: 15px; 
                border: 1px solid #ccc;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #6c63ff;
                background: #ffffff;
            }
        """)
        return self.search_box