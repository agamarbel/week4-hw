import os
import sys
from pathlib import Path

if sys.platform == "darwin":
    qt_platform_plugins = (
        Path(__file__).resolve().parent.parent / "qtplugins" / "platforms"
    )
    if qt_platform_plugins.is_dir():
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(qt_platform_plugins)

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
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

        self.about_button= QPushButton( 'About',self)
        self.about_button.setGeometry(20, 50, 100,40 )
        self.about_button.clicked.connect(self.show_about)


        self.load_button= QPushButton('Press to upload grade file')
        self.load_button. setGeometry(20, 30, 50, 60)
        self.load_button.clicked.connect(self.load_met)


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
        for line in line [1:]:
            part= line.strip().split(',')
            self.student_ids.append(part[0].strip())
            grade= int(part[1])
            self.original_grades.append(grade)
            self.corrected_grades.append(grade)
            






    def show_about(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradeCorrectionWindow()
    window.show()
    sys.exit(app.exec())

