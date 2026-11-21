import os
import sys

if sys.platform == "darwin":
    os.environ.setdefault(
        "QT_QPA_PLATFORM_PLUGIN_PATH",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "qtplugins", "platforms"),
    )

from PySide6.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QPushButton, QAbstractSpinBox,QLineEdit, QLabel

app = QApplication.instance() or QApplication(sys.argv)
window = QWidget()
window.resize(400, 200)
window.setGeometry(100, 100, 400, 200)
window.setWindowTitle("advanced calculator")


display = QLineEdit(window)
display.setGeometry(20, 20, 360, 30)
display.setText("0")  

defult_num= 0.00
operation=" "


def click_plis():
    global defult_num, operation
    defult_num = float(display.text())
    operation = "+"
    display.clear()

def click_minus():
    global defult_num, operation
    defult_num = float(display.text())
    operation = "-" 
    display.clear()     
def click_multiply():
    global defult_num, operation
    defult_num = float(display.text())
    operation = "*" 
    display.clear() 
def click_divide():
    global defult_num, operation
    defult_num = float(display.text())
    operation = "/" 
    display.clear()

def click_equal():
    global defult_num, operation
    second_num = float(display.text())
    if operation == "+":
        result = defult_num + second_num
    elif operation == "-":
        result = defult_num - second_num
    elif operation == "*":
        result = defult_num * second_num
    elif operation == "/":
        if second_num != 0:
            result = defult_num / second_num
        else:
            display.setText("Error: Division by zero")
            return
    else:
        display.setText("Error: Invalid operation")
        return

    display.setText(str(result))

def click_clear():
    display.setText("0")  
    global defult_num, operation
    defult_num = 0.00
    operation = " "
    display.clear("0")


button_plus = QPushButton("+", window)      
button_plus.setGeometry(20, 60, 80, 30)
button_plus.clicked.connect(click_plis)

button_minus = QPushButton("-", window)
button_minus.setGeometry(110, 60, 80, 30)
button_minus.clicked.connect(click_minus)

button_multiply = QPushButton("*", window)
button_multiply.setGeometry(200, 60, 80, 30)
button_multiply.clicked.connect(click_multiply)

button_divide = QPushButton("/", window)
button_divide.setGeometry(290, 60, 80, 30)
button_divide.clicked.connect(click_divide)

button_equal = QPushButton("=", window)
button_equal.setGeometry(110, 100, 80, 30)
button_equal.clicked.connect(click_equal)

button_clear = QPushButton("C", window)
button_clear.setGeometry(200, 100, 80, 30)
button_clear.clicked.connect(click_clear)   


window.show()   
app.exec()
