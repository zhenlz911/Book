import sys
from db import PymysqlDb
import hashlib
from PyQt5.QtWidgets import *
from singl import Ui_Form
import qdarkstyle

class Singlwin(QWidget,Ui_Form):
    def __init__(self):
        super(Singlwin,self).__init__()
        self.setupUi(self)
        #信号绑定
        self.pushButton.clicked.connect(self.singl)

    def singl(self):
        studentid = self.IDlineEdit.text()
        password = self.passwordlineEdit.text()

        if (studentid == '' or password == ''):
            print(QMessageBox.warning(self,'警告','学号或密码不能为空！',QMessageBox.Yes,QMessageBox.Yes))
            return
        sql = 'select StudentId,PassWord from user where StudentId = {}'.format(studentid)
        row = PymysqlDb().query(sql)
        h1 = hashlib.md5()
        h1.update(password.encode(encoding='utf-8'))
        if not row:
            print(QMessageBox.information(self,'提示','该账户不存在',QMessageBox.Yes,QMessageBox.Yes))
        else:
            if (studentid == row[0][0] and h1.hexdigest() == row[0][1]):
                print(QMessageBox.information(self,'登陆窗体','登陆成功',QMessageBox.Yes,QMessageBox.Yes))
            else:
                print('密码错误')

        return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = Singlwin()
    form.show()
    sys.exit(app.exec())