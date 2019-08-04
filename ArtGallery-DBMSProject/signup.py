# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signupform.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt4 import QtCore, QtGui
from login import Ui_LoginDialog

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

class Ui_accountDialog(object):

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()


    def showLoginForm(self):
        self.loginWindow = QtGui.QDialog()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self.loginWindow)
        self.loginWindow.show()

    def signupCheck(self):
        flag=1
        fullname = self.full_name.text()
        adminid = self.id_text.text()
        email = self.email_text.text()
        username = self.set_username.text()
        password = self.set_password.text()
        if(email=='' or fullname=='' or adminid == '' or username == '' or password == ''):
            self.showMessageBox('Warning','Oops! Sign Up Failed!!\nPlease, check your values. \n Make sure no field is empty.')
        else:
            connection  = sqlite3.connect("AccountInfo.db")
            cur = connection.cursor()
            cur.execute("INSERT INTO Users VALUES(?,?,?,?,?)",(adminid,fullname,username,password,email))
            self.showMessageBox('Success','Account Created! You are now a member of our Art Gallery!')
            connection.commit()
            connection.close()

    def setupUi(self, accountDialog):
        accountDialog.setObjectName(_fromUtf8("accountDialog"))
        accountDialog.resize(539, 475)
        accountDialog.setStyleSheet(_fromUtf8("QDialog{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(176, 0, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
""))
        self.headLabel = QtGui.QLabel(accountDialog)
        self.headLabel.setGeometry(QtCore.QRect(120, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.headLabel.setFont(font)
        self.headLabel.setAutoFillBackground(False)
        self.headLabel.setStyleSheet(_fromUtf8("color:rgb(235, 0, 127)"))
        self.headLabel.setObjectName(_fromUtf8("headLabel"))
        self.userLabel = QtGui.QLabel(accountDialog)
        self.userLabel.setGeometry(QtCore.QRect(120, 241, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.passLabel = QtGui.QLabel(accountDialog)
        self.passLabel.setGeometry(QtCore.QRect(120, 280, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.passLabel.setFont(font)
        self.passLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.passLabel.setObjectName(_fromUtf8("passLabel"))
        self.set_username = QtGui.QLineEdit(accountDialog)
        self.set_username.setGeometry(QtCore.QRect(280, 250, 151, 21))
        self.set_username.setAutoFillBackground(False)
        self.set_username.setStyleSheet(_fromUtf8(""))
        self.set_username.setObjectName(_fromUtf8("set_username"))
        self.signupBtn = QtGui.QPushButton(accountDialog)
        self.signupBtn.setGeometry(QtCore.QRect(360, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.signupBtn.setFont(font)
        self.signupBtn.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 183, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.signupBtn.setObjectName(_fromUtf8("signupBtn"))
        self.signupBtn.clicked.connect(self.signupCheck)
        self.set_password = QtGui.QLineEdit(accountDialog)
        self.set_password.setGeometry(QtCore.QRect(280, 290, 151, 21))
        self.set_password.setEchoMode(QtGui.QLineEdit.Password)
        self.set_password.setObjectName(_fromUtf8("set_password"))
        self.id_text = QtGui.QLineEdit(accountDialog)
        self.id_text.setGeometry(QtCore.QRect(280, 170, 151, 21))
        self.id_text.setObjectName(_fromUtf8("id_text"))
        self.idLabel = QtGui.QLabel(accountDialog)
        self.idLabel.setGeometry(QtCore.QRect(120, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.idLabel.setFont(font)
        self.idLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.email_text = QtGui.QLineEdit(accountDialog)
        self.email_text.setGeometry(QtCore.QRect(280, 210, 151, 21))
        self.email_text.setObjectName(_fromUtf8("email_text"))
        self.email_label = QtGui.QLabel(accountDialog)
        self.email_label.setGeometry(QtCore.QRect(120, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.email_label.setObjectName(_fromUtf8("email_label"))
        self.fullname_label = QtGui.QLabel(accountDialog)
        self.fullname_label.setGeometry(QtCore.QRect(120, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.fullname_label.setFont(font)
        self.fullname_label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.fullname_label.setObjectName(_fromUtf8("fullname_label"))
        self.full_name = QtGui.QLineEdit(accountDialog)
        self.full_name.setGeometry(QtCore.QRect(280, 130, 151, 21))
        self.full_name.setObjectName(_fromUtf8("full_name"))
        self.gotologin_btn = QtGui.QPushButton(accountDialog)
        self.gotologin_btn.setGeometry(QtCore.QRect(40, 350, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.gotologin_btn.setFont(font)
        self.gotologin_btn.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 183, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.gotologin_btn.setObjectName(_fromUtf8("gotologin_btn"))
        self.gotologin_btn.clicked.connect(self.showLoginForm)

        self.retranslateUi(accountDialog)
        QtCore.QMetaObject.connectSlotsByName(accountDialog)

    def retranslateUi(self, accountDialog):
        accountDialog.setWindowTitle(_translate("accountDialog", "Dialog", None))
        self.headLabel.setText(_translate("accountDialog", "Create an Account", None))
        self.userLabel.setText(_translate("accountDialog", "Set Username", None))
        self.passLabel.setText(_translate("accountDialog", "Set Password", None))
        self.signupBtn.setText(_translate("accountDialog", "Sign Up", None))
        self.idLabel.setText(_translate("accountDialog", "Admin ID", None))
        self.email_label.setText(_translate("accountDialog", "Email Id", None))
        self.fullname_label.setText(_translate("accountDialog", "Full Name", None))
        self.gotologin_btn.setText(_translate("accountDialog", "Ready to Log In", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    accountDialog = QtGui.QDialog()
    ui = Ui_accountDialog()
    ui.setupUi(accountDialog)
    accountDialog.show()
    sys.exit(app.exec_())
