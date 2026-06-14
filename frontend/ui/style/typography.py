from PySide6.QtGui import QFont
from ui.style.theme import Theme as t

class Typography:

    @staticmethod
    def headline1():
        font = QFont(t.headline_family, t.headline_size)
        font.setWeight(QFont.Weight.Medium)
        return font
    def headline2():
        font = QFont(t.headline_family, t.headline_size-10)
        font.setWeight(QFont.Weight.Light)
        return font
    
    

    @staticmethod
    def body():
        return QFont(t.body_family, t.body_size)

    @staticmethod
    def label():
        return QFont(t.label_family, t.label_size)