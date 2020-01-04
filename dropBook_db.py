import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dropBookDialog import Ui_Dialog

class DropBook(QDialog,Ui_Dialog):
    def __init__(self):
        super(DropBook,self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DropBook()
    form.show()
    sys.exit(app.exec())