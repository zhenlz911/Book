import sys
from distributed import publish
from addBookDialog import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from db import PymysqlDb
import time

class addBook(QDialog,Ui_Dialog):
    def __init__(self):
        super(addBook,self).__init__()
        self.setupUi(self)
        self.combox()
        self.addBookButton.clicked.connect(self.addBook)

    #图书分类设置
    def combox(self):
        combox = ['科学', '政治', '经济', '哲学', '人文', '历史', '地理', '军事', '摄影', '财经']
        self.categoryComboBox.addItems(combox)

    def addBook(self):
        bookname = self.bookNameEdit.text().strip()
        bookid = self.bookIdEdit.text().strip()
        authname = self.authNameEdit.text().strip()
        publish = self.publisherEdit.text()
        publishtime = self.dateTimeEdit.text()
        addnum = self.addNumEdit.text().strip()
        category = self.categoryComboBox.currentText()
        if (bookname == '' or bookid == '' or authname == '' or publish == ''
        or publishtime == '' or addnum == ''):
            print(QMessageBox.warning(self,'提示','有部分字段信息没填写，请核对',QMessageBox.Yes,
                          QMessageBox.Yes))
        else:
            addnum = int(addnum)
            #检查book表中是否有此书籍的信息
            sql = "select * from book where BookId = '{}'".format(bookid)
            row = PymysqlDb().query(sql)
            #判断是否重复的书号，如果存在则更新book的图书库存量，剩余可借量。
            if row:
                print('书号重复,库存量已更新')
                sql1 = "update book set Numstorage = Numstorage + {},NumCanBorrow = NumCanBorrow + {} where " \
                       "BookId = '{}'".format(addnum,addnum,bookid)
                PymysqlDb().updateDb(sql1)
            else:
                #否则插入往book中插入新的数据，同时插入buyordrop表
                sql2 = "insert into book (BookName,BookId,Auth,Category) values('{}','{}','{}','{}')".format(bookname,bookid,authname,category)
                PymysqlDb().insert_db(sql2)
                #往buyordrop表插入数据
                timenow = time.strftime('%Y-%m-%d',time.localtime())
                sql3 = "insert into buyordrop(BookId,Time,Number) values('{}','{}',{})".format(bookid,timenow,addnum)
                PymysqlDb().insert_db(sql3)
                print(QMessageBox.information(self,'提示','添加成功',QMessageBox.Yes,QMessageBox.Yes))
            return
        self.clearEdit()

    #清除字段内容
    def clearEdit(self):
        self.bookIdEdit.clear()
        self.bookNameEdit.clear()
        self.authNameEdit.clear()
        self.publisherEdit.clear()
        self.addNumEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = addBook()
    form.show()
    sys.exit(app.exec())

