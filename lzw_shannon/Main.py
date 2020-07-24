from lzw_shannon.Lzw import *
from lzw_shannon.shannon_fano import SHANNON
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import base64

from lzw_shannon.testing import Window

"""with open("i2.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)

co= LZW()
out1=co.compress("Document.txt")
out2=co.decompress("Document.lzw")

out=co.compress_image(str)
print("out",out)
gh=co.decompress_image(out)
print("out",gh)
import base64
imgdata = base64.b64decode(gh)
filename = 'imgde.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata)



"""
"""
co = LZW()
out1 = co.compress("Document.txt")
out2 = co.decompress("Document.lzw")

coo = SHANNON()
OUT2 = coo.compress("i1.png")
"""


if __name__ == "main":
    sh = SHANNON()
    lzw = LZW()
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
