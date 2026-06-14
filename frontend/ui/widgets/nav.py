from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtGui import QIcon
from ui.style.theme import Theme
import os

class navbar(QListWidget):
    NORMAL_ICON_ROLE = 1000
    ACTIVE_ICON_ROLE = 1001

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    ICON_DIR = os.path.join(BASE_DIR, "resources", "nav_icons")
    
    ICONS = {
        "Certificates": ("house.png", "house (1).png"),
        "Authorities": ("mail.png", "mail (1).png"),
        "Revocation": ("users.png", "users (1).png"),
        "Compliance": ("wallet.png", "wallet (1).png"),
        "Settings": ("circle-dollar-sign.png", "circle-dollar-sign (1).png"),
    }

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(220)

        self.setStyleSheet(f"""
        QListWidget {{
            background: {Theme.side_bar_background};
            border: none;
            color: {Theme.secondary};
            font-family: {Theme.body_family};
            font-size: 17px;
            font-weight: 500;
        }}

        QListWidget::item {{
            height: 40px;
            padding-left: 10px;
        }}

        QListWidget::item:hover {{
            background: #2b3a4a;
        }}

        QListWidget::item:selected {{
            background: #1f2a3c;
            border-left: 3px solid #4da3ff;
            color: {Theme.primary};
        }}
        """)

        self._create_items()
        self.currentItemChanged.connect(self._on_change)

        if self.count():
            self.setCurrentRow(0)

    def _create_items(self):
        for text, (normal_icon, active_icon) in self.ICONS.items():
            item = QListWidgetItem(text)
            
            normal_path = os.path.join(self.ICON_DIR, normal_icon)
            active_path = os.path.join(self.ICON_DIR, active_icon)

            item.setIcon(QIcon(normal_icon))
            item.setData(self.NORMAL_ICON_ROLE, normal_path)
            item.setData(self.ACTIVE_ICON_ROLE, active_path)

            self.addItem(item)

    def _on_change(self, current, previous):
        for row in range(self.count()):
            item = self.item(row)

            if item == current:
                item.setIcon(QIcon(item.data(self.ACTIVE_ICON_ROLE)))
            else:
                item.setIcon(QIcon(item.data(self.NORMAL_ICON_ROLE)))