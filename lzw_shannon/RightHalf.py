import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class RightHalf(QWidget):
    def __init__(self):
        super().__init__()
        self.mainVbox = QVBoxLayout()
        self.label = QLabel("Logs")
        self.scroll = QScrollArea()
        self.labelVbox = QVBoxLayout()
        self.scrollWidget = QWidget()
        self.imageLabel = QLabel()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100,100,300,300)
        self.mainVbox.addWidget(self.label)
        self.mainVbox.addWidget(self.imageLabel)
        self.imageLabel.setMaximumWidth(500)
        self.imageLabel.setMaximumHeight(300)
        self.imageLabel.setScaledContents(True)

        self.scrollWidget.setLayout(self.labelVbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.scrollWidget)


        self.mainVbox.addWidget(self.scroll)
        self.setLayout(self.mainVbox)
        self.show()
    def setImage(self,path):
        self.imageLabel.setPixmap(QPixmap(path))
    def addText(self,txt):
        self.labelVbox.addWidget(QLabel(txt))


