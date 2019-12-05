
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

# Designer 파일을 가져오는 부분


class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        # self.setupUi(self)
        # uic.loadUi('UI_Files/dash.ui', self)


        uic.loadUi('UI_Files/learn_activity.ui', self)


# app = QApplication(sys.argv)
# app = QApplication([])
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()



