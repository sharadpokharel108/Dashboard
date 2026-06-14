from PySide6.QtWidgets import QWidget, QHBoxLayout
class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Certificate Manager")
        
        
    def layout(self):
        main_layout=QHBoxLayout(self)