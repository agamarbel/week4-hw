import os
import sys

if sys.platform == "darwin":
    os.environ.setdefault(
        "QT_QPA_PLATFORM_PLUGIN_PATH",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "qtplugins", "platforms"),
    )

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 180)
window.setGeometry(100, 100, 400, 180)
window.setWindowTitle("Prime Number Checker")

num_label = QLabel("Enter a number to see if it is a prime number: (0-1000)", window)
num_label.setGeometry(20, 15, 360, 20)

user_input = QSpinBox(window)
user_input.setGeometry(20, 40, 100, 30)
user_input.setRange(0, 1000)


check_button = QPushButton("Check", window)
check_button.setGeometry(130, 40, 90, 30)

result_label = QLabel("Result:", window)
result_label.setGeometry(20, 90, 350, 35)
result_label.setStyleSheet("background-color: lightgrey;")

def is_prime():
#מספר ראשוני מוגדר ככזה שמתחלק רק באחד ובעצמו
#, הלולאה עוברת מספר מספר מ2 עד שורש המספר ובודקת חלוקה ללא שארית
#  . מספיק לבדוק עד עד השורש כי מעבר לזה המחלקים חוזרים על עצמם בזוגות
    num = user_input.value()
    if num < 2:
        result_label.setText(f"{num} is not a prime number.")
        return
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            result_label.setText(f"{num} is not a prime number.")
            break
    else:
        result_label.setText(f"{num} is a prime number.")

check_button.clicked.connect(is_prime)

window.show()
app.exec()
