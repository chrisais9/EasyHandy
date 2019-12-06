from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
import sys
import PyQt5

class Button(QPushButton):
    def __init__(self, text,callback):
        self.text = text

class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi('UI_Files/learn_activity.ui', self)

        movie = QtGui.QMovie("icons/dashAnimation.gif")

        # label의 값을 조정하기위해서는 데이터 타입을 PyQt5.QtCore.QSize로 넘겨줘야 됨.
        # movie.setScaledSize(s) # PyQt5.QtCore.QSize(360, 270)로 넘겨줘도 됨.
        # self.label_3.setGeometry(0, 0, 780, 441) 아니면 이거 사용해도될듯.. 늦게 서야 봄..
        # movie.setScaledSize(PyQt5.QtCore.QSize(360,270))

        # self.label_imageView.setMovie(movie)
        # movie.start()
        file = self.loadImageFromFile("resource/alphabet/learn/A.png")
        pixmap = QPixmap(file)
        pixmap = pixmap.scaled(330, 215)
        self.label_imageView.setPixmap(pixmap)

        self.label_a.mousePressEvent = self.changeModeTo('a')


        # self.button_A = PicButton(QPixmap("./resource/alphabet/learn/A.png"))
        self.button_A.setIcon(QtGui.QIcon("./resource/alphabet/button/A.png"))
        self.button_A.setIconSize(QSize(30 ,30))
        self.button_A.clicked.connect(Button.Clicked,'A')

        self.button_B.setIcon(QtGui.QIcon("./resource/alphabet/button/B.png"))
        self.button_B.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'B')

        self.button_C.setIcon(QtGui.QIcon("./resource/alphabet/button/C.png"))
        self.button_C.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'C')

        self.button_D.setIcon(QtGui.QIcon("./resource/alphabet/button/D.png"))
        self.button_D.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'D')

        self.button_E.setIcon(QtGui.QIcon("./resource/alphabet/button/E.png"))
        self.button_E.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'E')

        self.button_F.setIcon(QtGui.QIcon("./resource/alphabet/button/F.png"))
        self.button_F.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'F')

        self.button_G.setIcon(QtGui.QIcon("./resource/alphabet/button/G.png"))
        self.button_G.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'G')

        self.button_H.setIcon(QtGui.QIcon("./resource/alphabet/button/H.png"))
        self.button_H.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'H')

        self.button_I.setIcon(QtGui.QIcon("./resource/alphabet/button/I.png"))
        self.button_I.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'I')

        self.button_J.setIcon(QtGui.QIcon("./resource/alphabet/button/J.png"))
        self.button_J.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'J')

        self.button_K.setIcon(QtGui.QIcon("./resource/alphabet/button/K.png"))
        self.button_K.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'K')

        self.button_L.setIcon(QtGui.QIcon("./resource/alphabet/button/L.png"))
        self.button_L.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'L')

        self.button_M.setIcon(QtGui.QIcon("./resource/alphabet/button/M.png"))
        self.button_M.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'M')

        self.button_N.setIcon(QtGui.QIcon("./resource/alphabet/button/N.png"))
        self.button_N.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'N')

        self.button_O.setIcon(QtGui.QIcon("./resource/alphabet/button/O.png"))
        self.button_O.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'O')

        self.button_P.setIcon(QtGui.QIcon("./resource/alphabet/button/P.png"))
        self.button_P.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(Button.Clicked, 'P')

        self.button_Q.setIcon(QtGui.QIcon("./resource/alphabet/button/Q.png"))
        self.button_Q.setIconSize(QSize(30, 30))
        self.button_Q.clicked.connect(Button.Clicked, 'Q')

        self.button_R.setIcon(QtGui.QIcon("./resource/alphabet/button/R.png"))
        self.button_R.setIconSize(QSize(30, 30))
        self.button_R.clicked.connect(Button.Clicked, 'R')

        self.button_S.setIcon(QtGui.QIcon("./resource/alphabet/button/S.png"))
        self.button_S.setIconSize(QSize(30, 30))
        self.button_S.clicked.connect(Button.Clicked, 'S')

        self.button_T.setIcon(QtGui.QIcon("./resource/alphabet/button/T.png"))
        self.button_T.setIconSize(QSize(30, 30))
        self.button_T.clicked.connect(Button.Clicked, 'T')

        self.button_U.setIcon(QtGui.QIcon("./resource/alphabet/button/U.png"))
        self.button_U.setIconSize(QSize(30, 30))
        self.button_U.clicked.connect(Button.Clicked, 'U')

        self.button_V.setIcon(QtGui.QIcon("./resource/alphabet/button/V.png"))
        self.button_V.setIconSize(QSize(30, 30))
        self.button_V.clicked.connect(Button.Clicked, 'V')

        self.button_W.setIcon(QtGui.QIcon("./resource/alphabet/button/W.png"))
        self.button_W.setIconSize(QSize(30, 30))
        self.button_W.clicked.connect(Button.Clicked, 'W')

        self.button_X.setIcon(QtGui.QIcon("./resource/alphabet/button/X.png"))
        self.button_X.setIconSize(QSize(30, 30))
        self.button_X.clicked.connect(Button.Clicked, 'X')

        self.button_Y.setIcon(QtGui.QIcon("./resource/alphabet/button/Y.png"))
        self.button_Y.setIconSize(QSize(30, 30))
        self.button_Y.clicked.connect(Button.Clicked, 'Y')

        self.button_Z.setIcon(QtGui.QIcon("./resource/alphabet/button/Z.png"))
        self.button_Z.setIconSize(QSize(30, 30))
        self.button_Z.clicked.connect(Button.Clicked, 'Z')

        # self.pushButton.setGeometry(0,0,300,300)
        # self.widget.setIcon("./resource/alphabet/learn/A.png")

        # QtGui.QIcon
        print(self.widget)
        print(type(self.widget))

    def Clicked(self):
        button = self.sender()

        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == '<-':
            result = self.display.text()[0:-1]
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)

    def changeModeTo(self, mode):
        print('a')
        return 'a'

    def loadImageFromFile(self, path):
        self.pixmap = QPixmap(path)
        return self.pixmap








    def test(self):
        print('test')





# app = QApplication(sys.argv)
# app = QApplication([])
app = QApplication([])
window = MainWindow()
window.show()

app.exec_()
