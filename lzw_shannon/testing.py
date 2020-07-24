import sys
from PyQt5 import (QtWidgets, QtGui, QtCore)

from lzw_shannon.RightHalf import RightHalf


class TestFileDialog(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show()

        self.init_ui()
    def openFileDialog(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         str("Open Image"),
                                                         "/home/jana",
                                                         str("Images (*.png *.jpg);;Text files (*.txt)"))
        if fileName:
            self.right.setImage(fileName[0])
            print(fileName[0])
    def init_ui(self):
        self.mainHbox = QtWidgets.QHBoxLayout()
        self.leftVbox = QtWidgets.QVBoxLayout()
        self.rightVbox = QtWidgets.QVBoxLayout()

        self.button = QtWidgets.QPushButton("open")
        self.button.clicked.connect(self.openFileDialog)
        self.right = RightHalf()
        self.leftVbox.addWidget(self.button)
        self.rightVbox.addWidget(self.right)

        self.mainHbox.addLayout(self.leftVbox)
        self.mainHbox.addLayout(self.rightVbox)
        self.setLayout(self.mainHbox)


app = QtWidgets.QApplication(sys.argv)
t = TestFileDialog()
sys.exit(app.exec_())
