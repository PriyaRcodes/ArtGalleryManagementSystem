# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginform.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt4 import QtCore, QtGui
from mainpage import Ui_MainWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoginDialog(object):

    def showMainPage(self):
        self.MainPage = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainPage)
        self.MainPage.show()

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def loginCheck(self):
        username = self.username_text.text()
        password = self.password_text.text()

        connection = sqlite3.connect("AccountInfo.db")
        result = connection.execute("SELECT * FROM Users WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
        if(len(result.fetchall()) > 0):
            self.showMessageBox('Login Successful','Welcome!')
            self.showMainPage()
        else:
            self.showMessageBox('Warning','Login Failed!!! Invalid Username/Password')
        connection.commit()
        connection.close()

    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(509, 386)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Freestyle Script"))
        font.setPointSize(10)
        LoginDialog.setFont(font)
        LoginDialog.setStyleSheet(_fromUtf8("QDialog{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(176, 0, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
""))
        self.loginLabel = QtGui.QLabel(LoginDialog)
        self.loginLabel.setGeometry(QtCore.QRect(90, 50, 311, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("French Script MT"))
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet(_fromUtf8("color:rgb(235, 0, 127);"))
        self.loginLabel.setObjectName(_fromUtf8("loginLabel"))
        self.userLabel = QtGui.QLabel(LoginDialog)
        self.userLabel.setGeometry(QtCore.QRect(110, 160, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet(_fromUtf8("color:rgb(236,236,226)"))
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.passLabel = QtGui.QLabel(LoginDialog)
        self.passLabel.setGeometry(QtCore.QRect(110, 210, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.passLabel.setFont(font)
        self.passLabel.setStyleSheet(_fromUtf8("color:rgb(236,236,226)"))
        self.passLabel.setObjectName(_fromUtf8("passLabel"))
        self.password_text = QtGui.QLineEdit(LoginDialog)
        self.password_text.setGeometry(QtCore.QRect(240, 210, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_text.setFont(font)
        self.password_text.setEchoMode(QtGui.QLineEdit.Password)
        self.password_text.setObjectName(_fromUtf8("password_text"))
        self.loginform_btn = QtGui.QPushButton(LoginDialog)
        self.loginform_btn.setGeometry(QtCore.QRect(290, 280, 91, 31))
        self.loginform_btn.clicked.connect(self.loginCheck)

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.loginform_btn.setFont(font)
        self.loginform_btn.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 183, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.loginform_btn.setObjectName(_fromUtf8("loginform_btn"))
        self.username_text = QtGui.QLineEdit(LoginDialog)
        self.username_text.setGeometry(QtCore.QRect(240, 160, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_text.setFont(font)
        self.username_text.setObjectName(_fromUtf8("username_text"))

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login Form", None))
        self.loginLabel.setText(_translate("LoginDialog", "Identity Verification", None))
        self.userLabel.setText(_translate("LoginDialog", "Username", None))
        self.passLabel.setText(_translate("LoginDialog", "Password", None))
        self.loginform_btn.setText(_translate("LoginDialog", "Log In", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoginDialog = QtGui.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())
