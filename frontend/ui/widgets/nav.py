from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtGui import QIcon


class Sidebar(QListWidget):
    NORMAL_ICON_ROLE = 1000
    ACTIVE_ICON_ROLE = 1001

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

        self.setStyleSheet("""
        QListWidget {
            background: #1f2937;
            border: none;
            color: white;
        }

        /* normal item */
        QListWidget::item {
            height: 40px;
            padding-left: 10px;
        }

        /* hover background + text color change */
        QListWidget::item:hover {
            background: #2b3a4a;
            color: #4da3ff;
        }

        /* selected item */
        QListWidget::item:selected {
            background: #2b3a4a;
            border-left: 3px solid #4da3ff;
            color: #4da3ff;
        }
        """)

        self._create_items()
        self.currentItemChanged.connect(self._on_change)

        if self.count():
            self.setCurrentRow(0)

    def _create_items(self):
        for text, (normal_icon, active_icon) in self.ICONS.items():
            item = QListWidgetItem(text)

            item.setIcon(QIcon(normal_icon))
            item.setData(self.NORMAL_ICON_ROLE, normal_icon)
            item.setData(self.ACTIVE_ICON_ROLE, active_icon)

            self.addItem(item)

    def _on_change(self, current, previous):
        for row in range(self.count()):
            item = self.item(row)

            if item == current:
                item.setIcon(QIcon(item.data(self.ACTIVE_ICON_ROLE)))
            else:
                item.setIcon(QIcon(item.data(self.NORMAL_ICON_ROLE)))