import os
import sys
from pathlib import Path

if sys.platform == "darwin":
    qt_platform_plugins = (
        Path(__file__).resolve().parent.parent / "qtplugins" / "platforms"
    )
    if qt_platform_plugins.is_dir():
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(qt_platform_plugins)

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTableWidget,  QTableWidgetItem, QSpinBox, QLabel
from About import AboutWindow


class GradeCorrectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grade correction ")
        self.resize(720, 520)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""

        self.about_window = AboutWindow()

        self.about_button= QPushButton( 'About',self)
        self.about_button.setGeometry(20, 50, 100,40 )
        self.about_button.clicked.connect(self.show_about)

        self.load_button= QPushButton('Press to upload grade file')
        self.load_button. setGeometry(20, 30, 50, 60)
        self.load_button.clicked.connect(self.load_met)

        self.table = QTableWidget(50,3,self)
        set.table = self.setGeometry(20, 85, 550,45)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.setColumnWidth(0,160)
        self.table.setColumnWidth(1,200)
        self.table.setColumnWidth(2,200)

        self.bouns_label= QLabel(' choose bonus', self)
        self.bouns_label.setGeometry(350, 50, 50, 40)

        self.bonus_spin= QSpinBox(self)
        self.bonus_spin.setGeometry(400,50, 80, 40)
        self.bonus_spin.setRange(0,100)
        self.bonus_spin.valueChanged.clicked.connect(self.uptade_file)

        self.update_file_button= QPushButton('update file', self)
        self.update_file_button.setGeometry(500, 50, 140, 45)
        self.update_file_button.clicked.connect(self.update_file)
        

    def load_met(self):
        result = QFileDialog.getOpenFileName(self, "Press to see student file", "", "CSV files(*.csv)")
        filename = result[0]
        if not filename:
            return
        
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = filename

        with open(self.selected_file) as f:
            lines = f.readlines()
        for line in lines[1:]:
            part= line.strip().split(',')
            self.student_ids.append(part[0].strip())
            grade= int(part[1])
            self.original_grades.append(grade)
            self.corrected_grades.append(grade)


    def update_table(self):
        self.table.clearContents()
        for row_idx in range(len(self.student_ids)):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(self.student_ids[row_idx])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(self.original_grades[row_idx])))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(self.corrected_grades[row_idx])))






    def show_about(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradeCorrectionWindow()
    window.show()
    sys.exit(app.exec())

