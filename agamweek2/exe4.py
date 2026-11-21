import os
import sys

if sys.platform == "darwin":
    os.environ.setdefault(
        "QT_QPA_PLATFORM_PLUGIN_PATH",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "qtplugins", "platforms"),
    )

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QDoubleSpinBox,
    QLabel,
    QPushButton,
    QWidget,
)

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 200)
window.setGeometry(100, 100, 360, 240)
window.setWindowTitle("tiping Calculator")

QLabel("Bill Amount ($):", window).setGeometry(20, 10, 130, 15)
input_bill= QDoubleSpinBox(window)
input_bill .setGeometry(20, 30, 120, 30)
input_bill.setRange(0, 10000)
input_bill.setDecimals(2)
input_bill.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

QLabel("Tip Percent (10-20%):", window).setGeometry(170, 10, 150, 15)
input_tip_percent= QDoubleSpinBox(window)
input_tip_percent.setGeometry(170, 30, 120, 30)
input_tip_percent.setRange(10, 20)
input_tip_percent.setDecimals(1)
input_tip_percent.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

calc_button = QPushButton("Calculate Tip", window)
calc_button.setGeometry(20, 75, 140, 35)

QLabel("Tip Amount ($):", window).setGeometry(20, 125, 130, 15)
output_tip_amount= QDoubleSpinBox(window)
output_tip_amount.setGeometry(20, 145, 120, 30)
output_tip_amount.setRange(0, 100000)
output_tip_amount.setDecimals(2)        
output_tip_amount.setReadOnly(True)
output_tip_amount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)


QLabel("Total Amount ($):", window).setGeometry(170, 125, 130, 15)
output_total_amount = QDoubleSpinBox(window)
output_total_amount.setGeometry(170, 145, 120, 30)
output_total_amount.setRange(0, 100000)
output_total_amount.setDecimals(2)
output_total_amount.setReadOnly(True)
output_total_amount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

def calculate_tip():
    bill_amount = input_bill.value()
    tip_percent = input_tip_percent.value()
    tip_amount = bill_amount * (tip_percent / 100)
    output_tip_amount.setValue(tip_amount)
    output_total_amount.setValue(bill_amount + tip_amount)

calc_button.clicked.connect(calculate_tip)

window.show()
app.exec()