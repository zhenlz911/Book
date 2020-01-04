import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import time
import sip
from db import PymysqlDb

class UserManage(QDialog):
    def __init__(self):
        super(UserManage,self).__init__()
        #self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.resize(600,400)
        self.setWindowTitle('管理用户')
        self.setWindowIcon(QIcon('./images/MainWindow_1.png'))
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        #用户数
        self.userCount = 0
        self.oldDeleteId = ''
        self.oldDeleteName = ''
        self.deleteId = ''
        self.deleteName = ''
        self.setupUi()

    def setupUi(self):
        #获取数据
        self.getRestlt()

        self.table = QTableWidget()
        self.table.setRowCount(self.userCount)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['学号','姓名'])
        self.setRow()
        #设置不可编辑状态
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #标题可拉伸
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #选中整行
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.layout.addWidget(self.table)
        self.deltetUserButton = QPushButton('删除用户')
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.deltetUserButton,Qt.AlignCenter)

        self.widget = QWidget()
        self.widget.setLayout(hlayout)
        self.widget.setFixedHeight(60)
        self.deltetUserButton.setFixedHeight(45)
        self.deltetUserButton.setFixedWidth(180)
        self.layout.addWidget(self.widget,Qt.AlignCenter)

        #设置信号
        self.table.itemClicked.connect(self.getStudentInfo)
        self.deltetUserButton.clicked.connect(self.deleteUser)


    #获取数据表中有多少条数据
    def getRestlt(self):
        sql = 'select StudentId,Name from user where IsAdmin = 0'
        DB = PymysqlDb()
        rows = DB.query(sql)
        self.userCount = len(rows)

    #将数据表中的数据添加到表格中
    def setRow(self):
        font = QFont()
        font.setPixelSize(20)
        sql = 'select StudentId,Name from user where IsAdmin = 0'
        rows = PymysqlDb().query(sql)
        if rows:
            for i in range(self.userCount):
                Studentiditem = QTableWidgetItem(rows[i][0])
                StudentNameItem = QTableWidgetItem(rows[i][1])
                Studentiditem.setFont(font)
                StudentNameItem.setFont(font)
                self.table.setItem(i,0,Studentiditem)
                self.table.setItem(i,1,StudentNameItem)

    #获取表格数据，为删除做准备
    def getStudentInfo(self,item):
        #获取行索引
        row = self.table.currentIndex().row()
        self.table.verticalScrollBar().setSliderPosition(row)
        sql = 'select StudentId,Name from user where IsAdmin = 0'
        db = PymysqlDb().query(sql)
        self.oldDeleteId = self.deleteId
        self.oldDeleteName = self.deleteName
        self.deleteId = db[row][0]
        self.deleteName = db[row][1]
        #print(self.deleteId,self.deleteName)

    def deleteUser(self):
        if self.deleteId == '' and self.deleteName == '':
            print(QMessageBox.warning(self,'警告','请选中要删除的用户',QMessageBox.Yes,QMessageBox.Yes))
        elif self.deleteId == self.oldDeleteId and self.oldDeleteName == self.deleteName:
            print(QMessageBox.warning(self,'警告','请选中要删除的用户',QMessageBox.Yes,QMessageBox.Yes))
        if (QMessageBox.information(self,'提醒','删除用户：{}+{}。\n一经删除将无法恢复，是否继续？'.format(self.deleteId,self.deleteName)
                                   ,QMessageBox.Yes|QMessageBox.No,QMessageBox.No) == QMessageBox.No):
            return

        #删除user表中的用户数据
        sql = 'delete from user where StudentId = {}'.format(self.deleteId)
        db = PymysqlDb().deleteDb(sql)

        #删除所有书籍

        #数据更新
        self.updateUi()


    def updateUi(self):
        self.getRestlt()
        self.layout.removeWidget(self.widget)
        self.layout.removeWidget(self.table)
        sip.delete(self.table)
        sip.delete(self.widget)
        self.table = QTableWidget()
        self.table.setRowCount(self.userCount)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['学号','姓名'])
        self.setRow()
        #不可编辑
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #拉伸
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #选中整行
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.layout.addWidget(self.table)
        self.deltetUserButton = QPushButton('删除用户')
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.deltetUserButton, Qt.AlignCenter)

        self.widget = QWidget()
        self.widget.setLayout(hlayout)
        self.widget.setFixedHeight(60)
        self.deltetUserButton.setFixedHeight(45)
        self.deltetUserButton.setFixedWidth(180)
        self.layout.addWidget(self.widget, Qt.AlignCenter)

        # 设置信号
        self.table.itemClicked.connect(self.getStudentInfo)
        self.deltetUserButton.clicked.connect(self.deleteUser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = UserManage()
    form.show()
    sys.exit(app.exec())
