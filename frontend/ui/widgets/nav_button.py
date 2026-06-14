from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize, Qt

def make_nav_button(text, icon=None):
    btn = QPushButton(text)

    if icon:
        btn.setIcon(icon)
        btn.setIconSize(QSize(16, 16))

    btn.setCursor(Qt.PointingHandCursor)
    btn.setCheckable(True)  # important for active state (selected menu item)

    btn.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: #cbd5e1;
        border: none;
        padding: 8px 12px;
        text-align: left;
        font-size: 13px;
    }

    QPushButton:hover {
        background-color: #111c2e;
        color: white;
    }

    QPushButton:checked {
        background-color: #0f1f35;
        color: #ffffff;
        border-left: 3px solid #38bdf8;
        padding-left: 9px;
    }
    """)

    return btn


