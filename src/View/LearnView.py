'''
배우기 화면입니다.
'''
import sys
# import Layout Component
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
                             QApplication, QLabel)

# 리스트뷰 구현 할 때 필요한 것들
from PyQt5.QtWidgets import QMessageBox, QListWidget

# QWebEngineView에 필요한 모듈들
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# 알파벳 임포트
from string import ascii_uppercase

# 리스트위젯 클래스 생성. 클릭 이벤트 처리등 추가기능 구현하기위해 클래스로 구현.
class ListWidget(QListWidget):

    def Clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 800, 400) # 하나의 클래스가 하나의 window라고 생각하는듯1
        self.setWindowTitle("Learn Sign Language") # 하나의 클래스가 하나의 window라고 생각하는듯22

        # 가로,세로 레이아웃 생성
        hlayout_webview = QHBoxLayout()
        hlayout_statusview = QHBoxLayout()
        vlayout = QVBoxLayout()


        # 라벨 생성
        label_recognizedText = QLabel("A")
        label_recognizedText.setStyleSheet("background-color: gray;")
        label_recognizedPercentage = QLabel("0%")

        # 리스트 생성
        alpha_list = list(ascii_uppercase)

        listwidget= ListWidget()
        for i in alpha_list:
            listwidget.addItem(i)
        # 리스트위젯 클릭 이벤트
        listwidget.itemClicked.connect(listwidget.Clicked)



        # 웹엔진뷰 생성 + 가로 레이아웃에 위젯 추가
        web = QWebEngineView()
        web.setUrl(QUrl("https://www.youtube.com"))
        hlayout_webview.addWidget(web)

        # 가로 레이아웃에 위젯들 추가
        hlayout_statusview.addWidget(label_recognizedText)
        hlayout_statusview.addWidget(label_recognizedPercentage)
        hlayout_statusview.addWidget(listwidget)







        # 세로 레이아웃에 가로 레이아웃들 추가
        vlayout.addLayout(hlayout_webview)
        vlayout.addLayout(hlayout_statusview)

        # 레이아웃 설정 + 보이기
        self.setLayout(vlayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
