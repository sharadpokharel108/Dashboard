from PySide6.QtGui import QFont
from ui.style.theme import theme as t

class Typography:

    @staticmethod
    def headline():
        font = QFont(f"{t.headline}", {t.headline_size})
        font.setWeight(QFont.Weight.Bold)
        return font

    @staticmethod
    def body():
        return QFont(f"{t.body_family}", {t.body_size})

    @staticmethod
    def label():
        return QFont(f"{t.label_family}", {t.label_size})