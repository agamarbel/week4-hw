import os
import sys
from pathlib import Path

if sys.platform == "darwin":
    qt_platform_plugins = (
        Path(__file__).resolve().parent.parent / "qtplugins" / "platforms"
    )
    if qt_platform_plugins.is_dir():
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = str(qt_platform_plugins)

from PySide6.QtWidgets import QApplication, QDialog, QLabel, QGraphicsDropShadowEffect
from PySide6.QtGui import QPixmap, Qt, QColor


class AboutWindow(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('About Me')
        self.resize(340, 470)

        self.my_name = QLabel('Agam Arbel', self)
        self.my_name.setGeometry(20, 20, 300, 36)
        self.my_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.my_name.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            background-color: #F2DFDE;
            color: #593636;
            border-radius: 12px;
        """)

        self.my_email = QLabel('agamarbel2004@gmail.com', self)
        self.my_email.setGeometry(20, 60, 300, 36)
        self.my_email.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.my_email.setStyleSheet("""font-size: 16px;
                    font-weight: bold;color: #593636;""")


        self.my_linkedin = QLabel('<a href="https://www.linkedin.com/in/a-a-93262144b/">My LinkedIn</a>', self)
        self.my_linkedin.setGeometry(20, 90, 300, 30)
        self.my_linkedin.setStyleSheet("""font-size: 16px;
                            font-weight: bold;""")
        
        self.my_linkedin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.my_linkedin.setOpenExternalLinks(True)

        
        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(20, 130, 300, 300)
        self.my_picture.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.my_picture.setStyleSheet("""
            background-color: #FAF6F0;
            border: 11px ridge #C89D54;
            border-radius: 6px;
        """)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 90))
        self.my_picture.setGraphicsEffect(shadow)

        image_path = Path(__file__).resolve().with_name("littlemy1_fixed.png")
        image = QPixmap(str(image_path))
        if image.isNull():
            raise RuntimeError(f"Could not load About image: {image_path}")

        image = image.scaled(
            500, 500,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        image.setDevicePixelRatio(2)

        self.my_picture.setPixmap(image)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AboutWindow()
    window.show()
    app.exec()