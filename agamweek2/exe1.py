import os
import sys

if sys.platform == "darwin":
    os.environ.setdefault(
        "QT_QPA_PLATFORM_PLUGIN_PATH",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "qtplugins", "platforms"),
    )

from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget

app = QApplication.instance() or QApplication(sys.argv)
window = QWidget()
window.resize(400, 200)
window.setGeometry(100, 100, 400, 200)

label = QLabel("Hello!", window)
label.setGeometry(30, 30, 200, 30)
label.setStyleSheet("background-color: lightgrey;")

button = QPushButton("Click me", window)
button.setGeometry(30, 80, 120, 40)
button.setStyleSheet("background-color: green; color: white; font-weight: bold; border-radius: 10px;")


sec_label = QLabel("", window)
sec_label.setGeometry(30, 130, 200, 30)
sec_label.setStyleSheet("background-color: lightgrey;")




count = 0 
def on_button_click():
    global count
    count += 1
    label.setText(f"Button clicked {count} times")
    if count % 2 == 0:
        sec_label.setText("Button clicked")
    else:
        sec_label.setText("")




button.clicked.connect(on_button_click)


window.show()
app.exec()