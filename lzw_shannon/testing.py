import sys
from PyQt5 import (QtWidgets, QtGui, QtCore)

from lzw_shannon.LeftHalf import LeftHalf
from lzw_shannon.Lzw import LZW
from lzw_shannon.RightHalf import RightHalf
from lzw_shannon.shannon_fano import SHANNON
import os

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show()
        self.fano = SHANNON()
        self.lzw = LZW()
        self.init_ui()
    def openDirDialog(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if dlg.exec_() == QtWidgets.QDialog.Accepted:
            self.dirName = dlg.selectedFiles()[0]
            self.recursiveSearch(self.dirName)


    def recursiveSearch(self,direct):
        for filename in os.listdir(direct):
            name = direct+"/"+filename
            if os.path.isdir(name):
                self.recursiveSearch(name)
                self.right.addText(name + " compressed")
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                    ".png") or filename.endswith(".txt"):
                self.lzw.compress(direct+"/"+filename)
                self.right.addText(direct+"/"+filename + " compressed from folder")

    def openFileDialog(self):
        self.fileName = QtWidgets.QFileDialog.getOpenFileName(self,
                                                str("Open Image"),
                                                "newFile",
                                                str("Images (*.png *.jpg *.jpeg);;Text files (*.txt)"))
        if self.fileName[0] != "":
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
            self.left.compressButton.setEnabled(False)

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
        self.left.openDirButton.clicked.connect(self.openDirDialog)

        self.mainHbox.addLayout(self.leftVbox)
        self.mainHbox.addLayout(self.rightVbox)
        self.setLayout(self.mainHbox)


app = QtWidgets.QApplication(sys.argv)
t = Window()
sys.exit(app.exec_())
