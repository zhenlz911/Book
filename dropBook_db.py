import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dropBookDialog import Ui_Dialog
from db import PymysqlDb
import datetime

class DropBook(QDialog,Ui_Dialog):
    drop_book_signal = pyqtSignal()
    def __init__(self,parent = None):
        super(DropBook,self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.WindowModal)
        self.comobox()
        self.dropBookButton.clicked.connect(self.dropButt)
        self.bookIdEdit.editingFinished.connect(self.bookidchang)

    def comobox(self):
        combox = ['科学', '政治', '经济', '哲学', '人文', '历史', '地理', '军事', '摄影', '财经','']
        self.categoryComboBox.addItems(combox)

    #删除按钮
    def dropButt(self):
        pass


    #输入书号后查询数据
    def bookidchang(self):
        bookid = self.bookIdEdit.text().strip()
        if bookid != "":
            sql = "select * from book where BookId = '%s'" % (bookid)
            row = PymysqlDb().query(sql)
            print(row)
            if row:
                self.bookNameEdit.setText(row[0][0])
                self.authNameEdit.setText(row[0][2])
                self.categoryComboBox.setCurrentText(row[0][3])
                self.publisherEdit.setText(row[0][4])
                if row[0][5]:
                #将时间类型转换成字符串型
                    self.publishTime.setText(datetime.datetime.strftime(row[0][5],'%Y-%m-%d'))
                else:
                    self.publishTime.setText('')
            else:
                print(QMessageBox.warning(self,'提示','没有查到此书信息,请核对',QMessageBox.Yes,QMessageBox.Yes))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DropBook()
    form.show()
    sys.exit(app.exec())