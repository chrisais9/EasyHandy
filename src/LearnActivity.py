from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
import sys
import PyQt5

from string import ascii_uppercase

class MyListWidget(QListWidget):

    def __init__(self):
        super(MyListWidget, self).__init__()
        self.myListWidget = QListWidget()

        # self.setLayout()
        self.myListWidget.setGeometry(170, 330, 260, 190)
        alpha_list = list(ascii_uppercase)
        for i in alpha_list:
            self.myListWidget.addItem(i)

        self.myListWidget.show()


    def Clicked(self, item):
        print(self, "ListWidget", "You clicked: " + item.text())


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

        # self.listWidget_alpha_selecter.addItem('A')
        # label.show()

        # myListWidget = MyListWidget()
        # myListWidget.setGeometry(170,330,260,190)
        # alpha_list = list(ascii_uppercase)
        # for i in alpha_list:
        #     myListWidget.addItem(i)
        #

        wg = MyListWidget()
        # wg.itemClicked.connect(wg.Clicked)



        # self.setCentralWidget(wg) # 반드시 필요함.

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
