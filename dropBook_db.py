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
        bookid = self.bookIdEdit.text().strip()
        dropnum = 0
        if self.addNumEdit.text() == '':
            print(QMessageBox.warning(self,'提示','淘汰图书数量为空，请核对'),QMessageBox.Yes,QMessageBox.Yes)
        dropnum = int(self.addNumEdit.text().strip())
        sql = "SELECT * FROM book where bookId = '{}'".format(bookid)
        row = PymysqlDb().query(sql=sql)
        if (dropnum<0 or dropnum>row[0][5]):
            print(QMessageBox.warning(self,'提示','您要淘汰{}本图书,实际库存数量{}本,请核实！！'.format(dropnum,row[0][5])),QMessageBox.Yes,
                  QMessageBox.Yes)
        if (dropnum == row[0][6]):
            sql = "delete from book where BookId = '{}'".format(bookid)
            PymysqlDb().deleteDb(sql)
            print(QMessageBox.warning(self,'提示','数据删除成功'),QMessageBox.Yes,QMessageBox.Yes)
        else:
            sql = "update book set Numstorage = Numstorage - {},NumCanBorrow = NumCanBorrow - {} " \
                  "where BookId = '{}'".format(dropnum,dropnum,bookid)
            PymysqlDb().updateDb(sql)
            print(QMessageBox.warning(self,'提示','数据已更新'),QMessageBox.Yes,QMessageBox.Yes)
        #文本框中的数据清空
        self.bookNameEdit.clear()
        self.bookIdEdit.clear()
        self.authNameEdit.clear()
        self.publisherEdit.clear()
        self.publishTime.clear()
        self.addNumEdit.clear()



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