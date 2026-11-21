
import os
import sys

if sys.platform == "darwin":
    os.environ.setdefault(
        "QT_QPA_PLATFORM_PLUGIN_PATH",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "qtplugins", "platforms"),
    )

from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QWidget,
)

app = QApplication(sys.argv)
window = QWidget()

window.resize(400, 200)
window.setGeometry(100, 100, 400, 200)

num1 = QDoubleSpinBox(window)
num1.setGeometry(20, 20, 120, 30)
num1.setRange(-100, 100)
num1.setDecimals(2)
num1.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)


num2 = QDoubleSpinBox(window)
num2.setGeometry(20, 60, 120, 30)
num2.setRange(-100, 100)
num2.setDecimals(2)
num2.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

res_num = QDoubleSpinBox(window)
res_num.setGeometry(160, 40, 120, 30)
res_num.setRange(-100000, 100000)
res_num.setReadOnly(True)
res_num.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

def add_func():
    num1_value = num1.value()
    num2_value = num2.value()
    result = num1_value + num2_value
    res_num.setValue(result)
def subtract_func():
    num1_value = num1.value()
    num2_value = num2.value()
    result = num1_value - num2_value
    res_num.setValue(result)
def multiply_func():
    num1_value = num1.value()
    num2_value = num2.value()
    result = num1_value * num2_value
    res_num.setValue(result)
def divide_func():
    divisor = num2.value()
    if divisor == 0:
        QMessageBox.warning(window, "Invalid operation", "Cannot divide by zero.")
        return
    res_num.setValue(num1.value() / divisor)


addbutton = QPushButton("+", window)       
addbutton.setGeometry(20, 100, 50, 30)
addbutton.setStyleSheet("background-color: lightblue;")
addbutton.clicked.connect(add_func)    

subtractbutton = QPushButton("-", window)
subtractbutton.setGeometry(80, 100, 50, 30)
subtractbutton.setStyleSheet("background-color: lightblue;")
subtractbutton.clicked.connect(subtract_func)   

multiplybutton = QPushButton("*", window)
multiplybutton.setGeometry(140, 100, 50, 30)
multiplybutton.setStyleSheet("background-color: lightblue;")
multiplybutton.clicked.connect(multiply_func)       

dividebutton = QPushButton("/", window)
dividebutton.setGeometry(200, 100, 50, 30)
dividebutton.setStyleSheet("background-color: lightblue;")
dividebutton.clicked.connect(divide_func)   


window.show()
app.exec()