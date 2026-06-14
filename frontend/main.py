from PySide6.QtWidgets import QApplication, QWidget
import sys
from ui.windows.main_window import Mainwindow

app=QApplication(sys.argv)
window=Mainwindow()
window.show()
app.exec()