from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout,
    QToolButton, QMenu
)
from PySide6.QtGui import QAction
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        header = QWidget()
        layout = QHBoxLayout(header)

        # 🔽 Create dropdown menu
        menu = QMenu(self)

        action1 = QAction("Production", self)
        action2 = QAction("Staging", self)
        action3 = QAction("Sandbox", self)

        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)

        # 🔘 Button that shows menu
        dropdown_btn = QToolButton()
        dropdown_btn.setText("Environment")
        dropdown_btn.setMenu(menu)
        dropdown_btn.setPopupMode(QToolButton.InstantPopup)  # important

        layout.addWidget(dropdown_btn)

        self.setCentralWidget(QWidget())  # dummy
        self.setMenuWidget(header)


app = QApplication([])
w = MainWindow()
w.show()
app.exec()