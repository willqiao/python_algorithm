import datetime
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle("This is my window")

        self.label = QLabel(self)
        self.label.setText("This is my label")
        self.label.move(50, 20)

        self.button = QPushButton(self)
        self.button.setText("This is a Button")
        self.button.adjustSize()
        self.button.move(50, 90)
        self.button.clicked.connect(self.button_click)

    def button_click(self):
        self.label.setText("new text: " + str(datetime.datetime.now()))
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    w = MyWindow()

    w.show()
    sys.exit(app.exec_())


window()
