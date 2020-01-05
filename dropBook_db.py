import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dropBookDialog import Ui_Dialog
from db import Pymysql

class DropBook(QDialog,Ui_Dialog):
    def __init__(self):
        super(DropBook,self).__init__()
        self.setupUi(self)
        self.comobox()
        self.dropBookButton.clicked.connect(self.dropButt)
        self.bookIdEdit.textChanged.connect(self.bookIdEditChanged)

    def comobox(self):
        combox = ['科学', '政治', '经济', '哲学', '人文', '历史', '地理', '军事', '摄影', '财经']
        self.categoryComboBox.addItems(combox)

    #删除按钮
    def dropButt(self):
        print('hello')

    #书号改变后
    def bookIdEditChanged(self):
        bookid = self.bookIdEdit.text()
        sql = "select * from book where BookId = '{}'".format(bookid)
        row = Pymysql.query(sql)
        if row:
            self.bookNameEdit.setText(row[0])
        return






if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DropBook()
    form.show()
    sys.exit(app.exec())