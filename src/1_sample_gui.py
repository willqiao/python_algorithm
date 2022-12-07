import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def on_click():
    print("done")


def window():
    app = QApplication(sys.argv)
    w = QMainWindow()
    # window position, and then width + height
    w.setGeometry(500, 200, 500, 500)
    w.setWindowTitle("PyQt5")

    b = QLabel(w)
    b.setText("Hello World!")
    # move label to this x,y
    b.move(50, 20)

    button = QPushButton(w)
    button.setText("This is a Button")
    button.adjustSize()
    button.move(50, 90)
    button.clicked.connect(on_click)

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
