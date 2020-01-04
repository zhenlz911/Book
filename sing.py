# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 574)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/MainWindow_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.signUpLabel = QtWidgets.QLabel(Form)
        self.signUpLabel.setGeometry(QtCore.QRect(350, 10, 191, 81))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(28)
        self.signUpLabel.setFont(font)
        self.signUpLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signUpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signUpLabel.setObjectName("signUpLabel")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 110, 671, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.studentNameLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.studentNameLabel.setFont(font)
        self.studentNameLabel.setObjectName("studentNameLabel")
        self.horizontalLayout_2.addWidget(self.studentNameLabel)
        self.studentNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.studentNameLineEdit.setMaxLength(10)
        self.studentNameLineEdit.setFixedHeight(40)
        self.studentNameLineEdit.setObjectName("studentNameLineEdit")
        self.horizontalLayout_2.addWidget(self.studentNameLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.passwordLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_3.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordLineEdit.setMaxLength(16)
        #设置密码文字为隐形
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setFixedHeight(40)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_3.addWidget(self.passwordLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.passwordConfirmLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.passwordConfirmLabel.setFont(font)
        self.passwordConfirmLabel.setObjectName("passwordConfirmLabel")
        self.horizontalLayout_4.addWidget(self.passwordConfirmLabel)
        self.passwordConfirmLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordConfirmLineEdit.setMaxLength(16)
        #
        self.passwordConfirmLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        #
        self.passwordConfirmLineEdit.setFixedHeight(40)
        self.passwordConfirmLineEdit.setObjectName("passwordConfirmLineEdit")
        self.horizontalLayout_4.addWidget(self.passwordConfirmLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.studentIdLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.studentIdLabel.setFont(font)
        self.studentIdLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.studentIdLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.studentIdLabel.setLineWidth(1)
        self.studentIdLabel.setObjectName("studentIdLabel")
        self.horizontalLayout.addWidget(self.studentIdLabel)
        self.studentIdLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.studentIdLineEdit.setMaxLength(10)
        self.studentIdLineEdit.setFixedHeight(40)
        self.studentIdLineEdit.setObjectName("studentIdLineEdit")
        self.horizontalLayout.addWidget(self.studentIdLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.signUpbutton = QtWidgets.QPushButton(Form)
        self.signUpbutton.setGeometry(QtCore.QRect(340, 450, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.signUpbutton.setFont(font)
        self.signUpbutton.setObjectName("signUpbutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎登陆图书馆管理系统"))
        self.signUpLabel.setText(_translate("Form", "注  册"))
        self.studentNameLabel.setText(_translate("Form", "姓            名"))
        self.passwordLabel.setText(_translate("Form", "密            码"))
        self.passwordConfirmLabel.setText(_translate("Form", "确认密码"))
        self.studentIdLabel.setText(_translate("Form", "学            号"))
        self.signUpbutton.setText(_translate("Form", "注册"))


















