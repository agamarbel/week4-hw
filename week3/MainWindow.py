import os
import sys
from pathlib import Path

if sys.platform == "darwin":
    qt_platform_plugins = (
        Path(__file__).resolve().parent.parent / "qtplugins" / "platforms"
    )
    if qt_platform_plugins.is_dir():
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(qt_platform_plugins)

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QLabel, QComboBox

from Account import Account
from About import AboutWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.accounts = {}
        self.about_window = AboutWindow()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Bank Accounts")
        self.setGeometry(100, 100, 400, 300)

        self.about_button = QPushButton("About me", self)
        self.about_button.setGeometry(20, 20, 100, 30)
        self.about_button.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            background-color: #F2DFDE;
            color: #593636;
            border-radius: 12px;""")

        self.about_button.clicked.connect(self.show_about_window)

        self.user_id= QLineEdit(self)
        self.user_id.setGeometry(20,60,220,30)
        self.user_id.setPlaceholderText("Enter id")
        
        self.open_new_button = QPushButton("Open new account", self)
        self.open_new_button.setGeometry(250, 60, 120, 30)
        self.open_new_button.clicked.connect(self.open_account)
        
        self.accounts_combo = QComboBox(self)
        self.accounts_combo.setGeometry(20, 105, 220, 30)
        self.accounts_combo.currentTextChanged.connect(self.update_display)

        self.balance_label = QLabel("Balance: ", self)
        self.balance_label.setGeometry(250, 105, 130, 30)

        self.history_label = QLabel("History: ", self)
        self.history_label.setGeometry(20, 145, 350, 30)
        
        self.amount_input = QLineEdit(self)
        self.amount_input.setGeometry(20, 190, 140, 30)
        self.amount_input.setPlaceholderText("Enter amount")

        self.deposit_button = QPushButton("Deposit", self)
        self.deposit_button.setGeometry(170, 190, 95, 30)
        self.deposit_button.clicked.connect(self.deposit_clicked)

        self.withdraw_button = QPushButton("Withdraw", self)
        self.withdraw_button.setGeometry(275, 190, 95, 30)
        self.withdraw_button.clicked.connect(self.withdraw_clicked)

        self.message_label = QLabel("", self)
        self.message_label.setGeometry(20, 240, 350, 30)

    def show_about_window(self):
        self.about_window.show()
    def open_account(self):
        user_id = self.user_id.text()
        if user_id in self.accounts:
            self.message_label.setText("The account already exists")
        else:
            self.accounts[user_id] = Account(user_id)
            self.accounts_combo.addItem(user_id)
            self.message_label.setText("Opened successfully")

        self.user_id.setText('')

    def deposit_clicked(self):
        selected_id = self.accounts_combo.currentText()
        acc = self.accounts[selected_id]
        amount = int(self.amount_input.text())
        acc.deposit(amount)
        self.update_display()

    def withdraw_clicked(self):
        selected_id = self.accounts_combo.currentText()
        acc = self.accounts[selected_id]
        amount = int(self.amount_input.text())
        if acc.withdraw(amount) == 0:
            self.message_label.setText("Not enough balance")
        else:
            self.message_label.setText("")
            self.update_display()
  

    def update_display(self):
        selected_id = self.accounts_combo.currentText()
        if selected_id in self.accounts:
            acc = self.accounts[selected_id]
            self.balance_label.setText(f"Balance: {acc.balance}")
            self.history_label.setText(f"History: {acc.history}")

       
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()