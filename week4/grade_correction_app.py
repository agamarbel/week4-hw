import os
import sys
from pathlib import Path

if sys.platform == "darwin":
    qt_platform_plugins = (
        Path(__file__).resolve().parent.parent / "qtplugins" / "platforms"
    )
    if qt_platform_plugins.is_dir():
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(qt_platform_plugins)

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
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
        

    def show_about(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradeCorrectionWindow()
    window.show()
    sys.exit(app.exec())

