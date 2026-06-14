from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem
from PySide6.QtGui import QIcon

app = QApplication([])

sidebar = QListWidget()
sidebar.setStyleSheet("""
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
sidebar.setFixedWidth(220)

items = [
    ("Certificates", "shield.png"),
    ("Authorities", "nodes.png"),
    ("Revocation", "block.png"),
    ("Compliance", "check.png"),
    ("Settings", "gear.png")
]

for text, icon_path in items:
    item = QListWidgetItem(text)
    item.setIcon(QIcon(icon_path))
    sidebar.addItem(item)

sidebar.setCurrentRow(0)

sidebar.show()
app.exec()