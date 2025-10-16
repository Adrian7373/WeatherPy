from PySide6.QtWidgets import QLabel, QApplication, QLineEdit
from mainwindow import MainWindow, Weather
import sys
app = QApplication(sys.argv)

window = MainWindow(app)
window.show()
window.centerOnScreen()
app.exec()
