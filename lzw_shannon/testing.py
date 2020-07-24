import sys
from PyQt5 import (QtWidgets, QtGui, QtCore)

from lzw_shannon.LeftHalf import LeftHalf
from lzw_shannon.Lzw import LZW
from lzw_shannon.RightHalf import RightHalf
from lzw_shannon.shannon_fano import SHANNON


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.fano = SHANNON()
        self.lzw = LZW()
        self.init_ui()
    def openFileDialog(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(self,
                                                         str("Open Image"),
                                                         "/home/jana",
                                                         str("Images (*.png *.jpg);;Text files (*.txt)"))
        if self.fileName:
            self.left.compressButton.setEnabled(True)
            self.right.setImage(self.fileName[0])
            self.right.addText(self.fileName[0] + " loaded successfully")
    def extract(self):
        self.extractedFileName = QtWidgets.QFileDialog.getOpenFileName(self,
                                                              str("Open Image"),
                                                              "/home/jana",
                                                              str("Compressed (*.lzw)"))
        if self.extractedFileName:
            self.newName = self.lzw.decompress(self.extractedFileName[0])
            self.right.addText(self.newName + " Extracted successfully")
            self.right.setImage(self.newName)

    def compress(self):
        self.flag =""
        if self.left.lzwRadio.isChecked():
            out = self.lzw.compress(self.fileName[0])
            self.flag ="lzw"
        else:
            out = self.fano.compress(self.fileName[0])
            self.flag="shannon-fano"

        self.right.addText(self.fileName[0] + " compressed successfully")
        self.right.addText("("+self.flag+")"+"the document size before compressing " + str(out[0]))
        self.right.addText("("+self.flag+")"+"the document size after compressing " + str(out[1]))
        self.left.compressButton.setEnabled(False)

    def init_ui(self):
        self.mainHbox = QtWidgets.QHBoxLayout()
        self.leftVbox = QtWidgets.QVBoxLayout()
        self.rightVbox = QtWidgets.QVBoxLayout()

        self.left = LeftHalf()
        self.right = RightHalf()
        self.leftVbox.addWidget(self.left)
        self.rightVbox.addWidget(self.right)

        self.left.openButton.clicked.connect(self.openFileDialog)
        self.left.compressButton.clicked.connect(self.compress)
        self.left.extractButton.clicked.connect(self.extract)

        self.mainHbox.addLayout(self.leftVbox)
        self.mainHbox.addLayout(self.rightVbox)
        self.setLayout(self.mainHbox)


app = QtWidgets.QApplication(sys.argv)
t = Window()
sys.exit(app.exec_())
