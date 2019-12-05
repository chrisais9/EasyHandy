from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import *
import sys


# Designer 파일을 가져오는 부분


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        # uic.loadUi('UI_Files/dash.ui', self)

        uic.loadUi('UI_Files/learn_activity.ui', self)

        self._layout = self.layout()
        self.label_3 = QtWidgets.QLabel()
        # self.label_3.setText("aaa")
        movie = QtGui.QMovie("icons/dashAnimation.gif")
        self.label_3.setMovie(movie)
        self.label_3.setGeometry(0, 0, 780, 441)
        movie.start()
        self._layout.addWidget(self.label_3)


# app = QApplication(sys.argv)
# app = QApplication([])
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
