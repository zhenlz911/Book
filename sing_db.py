from sing import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from db import PymysqlDb
import hashlib

class singdb(QWidget,Ui_Form):
    def __init__(self):
        super(singdb,self).__init__()
        self.setupUi(self)

        self.signUpbutton.clicked.connect(self.singup)
        self.studentIdLineEdit.returnPressed.connect(self.singup)
        self.studentNameLineEdit.returnPressed.connect(self.singup)
        self.passwordLineEdit.returnPressed.connect(self.singup)
        self.passwordConfirmLineEdit.returnPressed.connect(self.singup)



    def singup(self):
        studentId = self.studentIdLineEdit.text().strip()
        studentName = self.studentNameLineEdit.text().strip()
        password = self.passwordLineEdit.text().strip()
        passwordConfirst = self.passwordConfirmLineEdit.text().strip()
        if studentId == '' or studentName == '' or password == '' or passwordConfirst == '':
            print(QMessageBox.warning(self, '警告', '表单不可为空，请重新输入',QMessageBox.Yes,
                                                    QMessageBox.No))
            return
        else:
            if (password != passwordConfirst):
                print(QMessageBox.warning(self, '警告', '两次输入的密码不一样，请核对！',QMessageBox.Yes,
                                                        QMessageBox.Yes))
            elif (password == passwordConfirst):
                # md5编码
                h1 = hashlib.md5()
                h1.update(password.encode(encoding='utf-8'))
                md5password = h1.hexdigest()
                sql = "select * from user where StudentId = {}".format(studentId)
                row = PymysqlDb().query(sql)
                if row:
                    print(QMessageBox.warning(self, '警告', '已存在这个账户，请重新输入',QMessageBox.Yes,
                                                            QMessageBox.Yes))
                    return
                else:
                    sql = "insert into user(StudentId,Name,PassWord) values ('{0}','{1}','{2}')".format(studentId,
                                                                                                            studentName,
                                                                                                            md5password)
                    PymysqlDb().insert_db(sql)
                    print(QMessageBox.information(self, '警告', '注册成功',QMessageBox.Yes,QMessageBox.Yes))
                return
