from PyQt5.QtWidgets import *
import os
from PIL.ImageFilter import *
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image



papka = ""
app = QApplication([])
app.setStyleSheet("""
    QWidget {
        background: grey;
        color: white;
    }

    QPushButton {
        color: black;
        font-family: Monotype Corsiva;
        font-size: 25px;
    }
""")
window = QWidget()
window.resize(800, 600)
window.setWindowTitle("ІЗІ ФОТОШОП")

folderBtn = QPushButton("Папка")
leftBtn = QPushButton("Ліворуч")
rightBtn = QPushButton("праворуч")
mirrorBtn = QPushButton("дзеркало")
blurBtn = QPushButton("Розмиття")

imgLbl = QLabel("фоточка")
fileList = QListWidget()

mainLine = QHBoxLayout()
columnLeft = QVBoxLayout()
columnLeft.addWidget(folderBtn)
columnLeft.addWidget(fileList)
mainLine.addLayout(columnLeft)
columnRight = QVBoxLayout()
columnRight.addWidget(imgLbl)
line1 = QHBoxLayout()
line1.addWidget(leftBtn)
line1.addWidget(rightBtn)

line1.addWidget(blurBtn)
columnRight.addLayout(line1)
mainLine.addLayout(columnRight)





window.setLayout(mainLine)
window.show()
app.exec_()

