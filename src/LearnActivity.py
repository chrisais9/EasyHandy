import os
import threading
import time

import cv2
import numpy as np
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, pyqtSlot
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt
import time
import sys
import PyQt5

from tensorflow.keras.models import load_model

classifier = load_model('ASLModel.h5')  # loading the model
currentMode = 'A'
recognizedResult = 'Z'
count = 0

def fileSearch():
    fileEntry = []
    for file in os.listdir("SampleGestures"):
        if file.endswith(".png"):
            fileEntry.append(file)
    return fileEntry


'''
predicator using Keras
PyQt 의존성을 가져서는 안됨.
'''


def predictor():
    import numpy as np
    from tensorflow.keras.preprocessing import image
    test_image = image.load_img('1.png', target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    gesname = ''
    fileEntry = fileSearch()
    for i in range(len(fileEntry)):
        image_to_compare = cv2.imread("./SampleGestures/" + fileEntry[i])
        original = cv2.imread("1.png")
        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(original, None)
        kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(desc_1, desc_2, k=2)

        good_points = []
        ratio = 0.6
        for m, n in matches:
            if m.distance < ratio * n.distance:
                good_points.append(m)
        if (abs(len(good_points) + len(
                matches)) > 20):
            gesname = fileEntry[i]
            gesname = gesname.replace('.png', '')
            if (gesname == 'sp'):
                gesname = ' '
            return gesname

    if result[0][0] == 1:
        return 'A'
    elif result[0][1] == 1:
        return 'B'
    elif result[0][2] == 1:
        return 'C'
    elif result[0][3] == 1:
        return 'D'
    elif result[0][4] == 1:
        return 'E'
    elif result[0][5] == 1:
        return 'F'
    elif result[0][6] == 1:
        return 'G'
    elif result[0][7] == 1:
        return 'H'
    elif result[0][8] == 1:
        return 'I'
    elif result[0][9] == 1:
        return 'J'
    elif result[0][10] == 1:
        return 'K'
    elif result[0][11] == 1:
        return 'L'
    elif result[0][12] == 1:
        return 'M'
    elif result[0][13] == 1:
        return 'N'
    elif result[0][14] == 1:
        return 'O'
    elif result[0][15] == 1:
        return 'P'
    elif result[0][16] == 1:
        return 'Q'
    elif result[0][17] == 1:
        return 'R'
    elif result[0][18] == 1:
        return 'S'
    elif result[0][19] == 1:
        return 'T'
    elif result[0][20] == 1:
        return 'U'
    elif result[0][21] == 1:
        return 'V'
    elif result[0][22] == 1:
        return 'W'
    elif result[0][23] == 1:
        return 'X'
    elif result[0][24] == 1:
        return 'Y'
    elif result[0][25] == 1:
        return 'Z'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi('pyqt_UI/learn_activity.ui', self)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

        self.setWindowTitle('EasyHandy')
        self.setWindowIcon(QIcon('icons/windowlogo.png'))
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        """ 현재 모드를 나타냄 ( 모든 로직은 이 변수를 이용해서 처리 ex. mode = A -> 튜토리얼 사진 show 'A' """
        """ OnFirstRun """
        self.notifyModeChanged(currentMode)
        self.setTutorialButton()

        self.heightOfCamView = self.label_camView.height()
        self.widthOfCamView = self.label_camView.width()

        self.roiLeftTop = (500, 100)
        self.roiRightBottom = (750, 300)

        self.video_thread(MainWindow)

        self.playProgress()


    def playProgress(self):
        # 뷰 띄운 다음 바로재생
        self.progressBarThread = ProgressThread()
        # 이벤트 설정
        self.progressBarThread.countChanged.connect(self.onCountChanged)
        self.progressBarThread.start()

    # count 값이 변경 될때 마다 호출.
    def onCountChanged(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            self.showCheckMark()


    def showCheckMark(self):
        height = self.label_checkmark.height()
        width = self.label_checkmark.width()
        pixmap = QPixmap("./resource/UI/checkmark.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label_checkmark.setPixmap(pixmap)

    def hideCheckMark(self):
        height = self.label_checkmark.height()
        width = self.label_checkmark.width()
        pixmap = QPixmap("./resource/UI/hideImage.png")
        pixmap = pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
        self.label_checkmark.setPixmap(pixmap)


    # TODO: 버튼 나열된거 꼴뵈기 싫으니까 최적화 할 필요 있음 (상속해서 한 클래스로 만들기??)
    @pyqtSlot()
    def setTutorialButton(self):
        self.button_A.setIcon(QtGui.QIcon("./resource/alphabet/button/A.png"))
        self.button_A.setIconSize(QSize(30, 30))
        self.button_A.clicked.connect(self.alphabetButtonClicked)

        self.button_B.setIcon(QtGui.QIcon("./resource/alphabet/button/B.png"))
        self.button_B.setIconSize(QSize(30, 30))
        self.button_B.clicked.connect(self.alphabetButtonClicked)

        self.button_C.setIcon(QtGui.QIcon("./resource/alphabet/button/C.png"))
        self.button_C.setIconSize(QSize(30, 30))
        self.button_C.clicked.connect(self.alphabetButtonClicked)

        self.button_D.setIcon(QtGui.QIcon("./resource/alphabet/button/D.png"))
        self.button_D.setIconSize(QSize(30, 30))
        self.button_D.clicked.connect(self.alphabetButtonClicked)

        self.button_E.setIcon(QtGui.QIcon("./resource/alphabet/button/E.png"))
        self.button_E.setIconSize(QSize(30, 30))
        self.button_E.clicked.connect(self.alphabetButtonClicked)

        self.button_F.setIcon(QtGui.QIcon("./resource/alphabet/button/F.png"))
        self.button_F.setIconSize(QSize(30, 30))
        self.button_F.clicked.connect(self.alphabetButtonClicked)

        self.button_G.setIcon(QtGui.QIcon("./resource/alphabet/button/G.png"))
        self.button_G.setIconSize(QSize(30, 30))
        self.button_G.clicked.connect(self.alphabetButtonClicked)

        self.button_H.setIcon(QtGui.QIcon("./resource/alphabet/button/H.png"))
        self.button_H.setIconSize(QSize(30, 30))
        self.button_H.clicked.connect(self.alphabetButtonClicked)

        self.button_I.setIcon(QtGui.QIcon("./resource/alphabet/button/I.png"))
        self.button_I.setIconSize(QSize(30, 30))
        self.button_I.clicked.connect(self.alphabetButtonClicked)

        self.button_J.setIcon(QtGui.QIcon("./resource/alphabet/button/J.png"))
        self.button_J.setIconSize(QSize(30, 30))
        self.button_J.clicked.connect(self.alphabetButtonClicked)

        self.button_K.setIcon(QtGui.QIcon("./resource/alphabet/button/K.png"))
        self.button_K.setIconSize(QSize(30, 30))
        self.button_K.clicked.connect(self.alphabetButtonClicked)

        self.button_L.setIcon(QtGui.QIcon("./resource/alphabet/button/L.png"))
        self.button_L.setIconSize(QSize(30, 30))
        self.button_L.clicked.connect(self.alphabetButtonClicked)

        self.button_M.setIcon(QtGui.QIcon("./resource/alphabet/button/M.png"))
        self.button_M.setIconSize(QSize(30, 30))
        self.button_M.clicked.connect(self.alphabetButtonClicked)

        self.button_N.setIcon(QtGui.QIcon("./resource/alphabet/button/N.png"))
        self.button_N.setIconSize(QSize(30, 30))
        self.button_N.clicked.connect(self.alphabetButtonClicked)

        self.button_O.setIcon(QtGui.QIcon("./resource/alphabet/button/O.png"))
        self.button_O.setIconSize(QSize(30, 30))
        self.button_O.clicked.connect(self.alphabetButtonClicked)

        self.button_P.setIcon(QtGui.QIcon("./resource/alphabet/button/P.png"))
        self.button_P.setIconSize(QSize(30, 30))
        self.button_P.clicked.connect(self.alphabetButtonClicked)

        self.button_Q.setIcon(QtGui.QIcon("./resource/alphabet/button/Q.png"))
        self.button_Q.setIconSize(QSize(30, 30))
        self.button_Q.clicked.connect(self.alphabetButtonClicked)

        self.button_R.setIcon(QtGui.QIcon("./resource/alphabet/button/R.png"))
        self.button_R.setIconSize(QSize(30, 30))
        self.button_R.clicked.connect(self.alphabetButtonClicked)

        self.button_S.setIcon(QtGui.QIcon("./resource/alphabet/button/S.png"))
        self.button_S.setIconSize(QSize(30, 30))
        self.button_S.clicked.connect(self.alphabetButtonClicked)

        self.button_T.setIcon(QtGui.QIcon("./resource/alphabet/button/T.png"))
        self.button_T.setIconSize(QSize(30, 30))
        self.button_T.clicked.connect(self.alphabetButtonClicked)

        self.button_U.setIcon(QtGui.QIcon("./resource/alphabet/button/U.png"))
        self.button_U.setIconSize(QSize(30, 30))
        self.button_U.clicked.connect(self.alphabetButtonClicked)

        self.button_V.setIcon(QtGui.QIcon("./resource/alphabet/button/V.png"))
        self.button_V.setIconSize(QSize(30, 30))
        self.button_V.clicked.connect(self.alphabetButtonClicked)

        self.button_W.setIcon(QtGui.QIcon("./resource/alphabet/button/W.png"))
        self.button_W.setIconSize(QSize(30, 30))
        self.button_W.clicked.connect(self.alphabetButtonClicked)

        self.button_X.setIcon(QtGui.QIcon("./resource/alphabet/button/X.png"))
        self.button_X.setIconSize(QSize(30, 30))
        self.button_X.clicked.connect(self.alphabetButtonClicked)

        self.button_Y.setIcon(QtGui.QIcon("./resource/alphabet/button/Y.png"))
        self.button_Y.setIconSize(QSize(30, 30))
        self.button_Y.clicked.connect(self.alphabetButtonClicked)

        self.button_Z.setIcon(QtGui.QIcon("./resource/alphabet/button/Z.png"))
        self.button_Z.setIconSize(QSize(30, 30))
        self.button_Z.clicked.connect(self.alphabetButtonClicked)

    def alphabetButtonClicked(self):
        button = self.sender()
        self.hideCheckMark()
        self.playProgress()

        objName = button.objectName()
        # I know it's a hack. get object name 'button_A' and slice to 'A'
        self.notifyModeChanged(objName[-1])

    """ 뷰 내의 모든 위젯은 이 함수를 호출해 Refresh 함 """

    def notifyModeChanged(self, modeName):
        global currentMode
        global count
        count = 0

        currentMode = modeName
        self.loadTutorialImageFromMode()
        self.statusBar().showMessage('현재 배우고 있는 문자는 {}입니다.'.format(modeName))

    """ label_tutorialView 에 현재 모드에 맞는 튜토리얼 이미지 삽입 """

    def loadTutorialImageFromMode(self):
        self.image = QPixmap("./resource/alphabet/learn/{}.png".format(currentMode))
        self.image = self.image.scaled(300, 190)
        self.label_tutorialView.setPixmap(self.image)

    def videoToFrame(self, MainWindow):
        global recognizedResult
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            resizedImage = cv2.resize(frame, (self.widthOfCamView, self.heightOfCamView))

            # 딥러닝 모델에 들어갈 프레임
            self.saveToPredictor(resizedImage)

            # UI 에 보여질 프레임 처리
            rgbImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2RGB)
            # img1 = cv2.rectangle(rgbImage, (150, 50), (300, 200), (0, 255, 0), thickness=2, lineType=8, shift=0)
            img1 = cv2.rectangle(rgbImage, self.roiLeftTop, self.roiRightBottom, (0, 255, 0), thickness=2, lineType=8,
                                 shift=0)

            h, w, c = img1.shape
            qImg = QImage(img1.data, w, h, c * w, QImage.Format_RGB888)

            self.label_camView.setPixmap(QPixmap.fromImage(qImg))
            self.label_camView.update()

            # 인식된 텍스트 업데이트
            self.updatePredictedResult()

        cap.release()
        cv2.destroyAllWindows()

    def saveToPredictor(self, frame):

        # 손의 색상 HSV 값을 기반으로 inRange 로 이진화
        lower_blue = np.array([0, 58, 50])
        upper_blue = np.array([30, 255, 255])

        imcrop = frame[self.roiLeftTop[1]:self.roiRightBottom[1], self.roiLeftTop[0]:self.roiRightBottom[0]]
        hsv = cv2.cvtColor(imcrop, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        save_img = cv2.resize(mask, (64, 64))
        cv2.imwrite('1.png', save_img)

    def updatePredictedResult(self):
        global recognizedResult
        recognizedResult = predictor()
        self.label_recognizedText.setText(recognizedResult)


    # video_to_frame을 쓰레드로 사용
    def video_thread(self, MainWindow):
        thread = threading.Thread(target=self.videoToFrame, args=(self,))
        thread.daemon = True  # 프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()


class ProgressThread(QThread):
    """
    Runs a counter thread.
    """
    # 이벤트 전달하기위해서
    countChanged = pyqtSignal(int)

    def run(self):
        TIME_LIMIT = 100
        global count
        # count = 0
        while count < TIME_LIMIT:


            time.sleep(0.1)
            print(currentMode, recognizedResult)
            if currentMode == recognizedResult:
                count += 2
            self.countChanged.emit(count)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec_()
