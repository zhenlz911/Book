import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from  BookStorageViewer import Ui_BookStorageViewer
import qdarkstyle
from db import PymysqlDb


class BookStorage(QWidget,Ui_BookStorageViewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #绑定列表框
        combox = ['按书名查询', '按书号查询', '按作者查询', '按分类查询', '按出版社查询']
        self.condisionComboBox.addItems(combox)
        #获取记录行数
        i = self.db_count()
        #创建数据模型，模型为任意数据结构
        self.model = QStandardItemModel(i,8)
        #设置水平表头
        self.model.setHorizontalHeaderLabels(['书名','书号','作者','分类','出版社','出版时间','库存',
                                              '剩余可借'])

        rows = self.db_date()
        for ii in range(len(rows)):
                self.model.setItem(ii,0,QStandardItem(rows[ii][0]))
                self.model.setItem(ii,1, QStandardItem(rows[ii][1]))
                self.model.setItem(ii,2, QStandardItem(rows[ii][2]))
                self.model.setItem(ii,3, QStandardItem(rows[ii][3]))
                self.model.setItem(ii,4, QStandardItem(rows[ii][4]))
                self.model.setItem(ii,6, QStandardItem(str(rows[ii][6])))
                self.model.setItem(ii,7, QStandardItem(str(rows[ii][7])))
                self.model.setItem(ii,5, QStandardItem(str(rows[ii][8])))














        #将数据模型添加到tableview中
        self.tableView.setModel(self.model)
        #最后一列决定充满剩下的界面
        self.tableView.horizontalHeader().setStretchLastSection(True)
        #所有列自动拉伸，充满界面
        #self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #选中整行
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

    #查询数据记录行数，用于tableview模型
    def db_count(self):
        SQL = "SELECT * FROM book"
        ROW = PymysqlDb().query(SQL)
        i = len(ROW)
        return i

    def db_date(self):
        SQL = "SELECT * FROM book"
        ROWS = PymysqlDb().query(SQL)
        return ROWS




















if __name__=="__main__":
    app = QApplication(sys.argv)
    form = BookStorage()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form.show()
    sys.exit(app.exec())
