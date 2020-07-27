import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class LeftHalf(QWidget):
    def __init__(self):
        super().__init__()
        self.mainVbox = QVBoxLayout()
        self.openButton = QPushButton("Open File")
        self.openDirButton = QPushButton("Open Directory")
        self.compressButton = QPushButton("Compress")
        self.extractButton = QPushButton("Extract")
        self.lzwRadio = QRadioButton("LZW")
        self.fanoRadio = QRadioButton("Shannon-Fano")
        self.init_ui()
    def init_ui(self):
        self.mainVbox.addWidget(self.openButton)
        self.mainVbox.addWidget(self.openDirButton)
        self.mainVbox.addWidget(self.compressButton)
        self.mainVbox.addWidget(self.extractButton)
        self.mainVbox.addWidget(self.lzwRadio)
        self.mainVbox.addWidget(self.fanoRadio)
        self.lzwRadio.setChecked(True)
        self.compressButton.setEnabled(False)
        self.mainVbox.addStretch(0)
        self.setLayout(self.mainVbox)
