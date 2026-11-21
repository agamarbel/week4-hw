
import os
import sys

if sys.platform == "darwin":
    os.environ.setdefault(
        "QT_QPA_PLATFORM_PLUGIN_PATH",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "qtplugins", "platforms"),
    )

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel

app = QApplication.instance() or QApplication(sys.argv)
window = QWidget()

window.resize(400, 200)
window.setGeometry(100, 100, 400, 200)

name_input = QLineEdit(window)
name_input.setGeometry(20, 20, 220, 30)
name_input.setPlaceholderText("Enter your name")

res_label = QLabel("", window)
res_label.setGeometry(20, 95, 350, 30)
res_label.setStyleSheet("background-color: lightgrey;")


def len_name():
    name = name_input.text()
    length = len(name)
    res_label.setText(f" your name is : {length}  letters long")


name_input.returnPressed.connect(len_name)
window.show()
app.exec()