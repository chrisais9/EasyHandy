import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)

TIME_LIMIT = 100


class External(QThread):

    # count = 0
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 5
            time.sleep(1)
            self.countChanged.emit(count)

            # if count >= TIME_LIMIT:
            #     self.close()


class Actions(QDialog):
    """
    Simple dialog that consists of a Progress Bar and a Button.
    Clicking on the button results in the start of a timer and
    updates the progress bar.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Progress Bar')
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)

        self.button = QPushButton('Start', self)
        self.button.move(0, 30)
        self.show()

        # 뷰 띄운 다음 바로재생
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

        # self.button.clicked.connect(self.onButtonClick)

    # def onButtonClick(self):
    #     self.calc = External()
    #     self.calc.countChanged.connect(self.onCountChanged)
    #     self.calc.start()

    def onCountChanged(self, value):
        self.progress.setValue(value)
        # if value >= TIME_LIMIT:
        #     self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())