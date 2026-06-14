# ui/components/labels.py

from PySide6.QtWidgets import QLabel
from ui.style.theme import Theme
from ui.style.typography import Typography


def headline_label1(text: str, color=Theme.primary):
    label = QLabel(text)
    label.setFont(Typography.headline1())
    label.setStyleSheet(f"color: {color};")
    return label
def headline_label2(text: str, color=Theme.secondary):
    label = QLabel(text)
    label.setFont(Typography.headline2())
    label.setStyleSheet(f"color: {color};")
    return label


def body_label(text: str, color=Theme.secondary):
    label = QLabel(text)
    label.setFont(Typography.body())
    label.setStyleSheet(f"color: {color};")
    return label