import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle  #样式表
from sing import Ui_Form
from db import PymysqlDb

class logui(QWidget,Ui_Form):
    def __init__(self):
        super(logui,self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = logui()
    form.show()
    sys.exit(app.exec())