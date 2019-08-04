# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcompage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from login import Ui_LoginDialog
from signup import Ui_accountDialog

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

class Ui_DialogHome(object):
    def showLoginForm(self):
        self.loginWindow = QtGui.QDialog()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self.loginWindow)
        self.loginWindow.show()

    def showSignUpForm(self):
        self.signupWindow = QtGui.QDialog()
        self.ui = Ui_accountDialog()
        self.ui.setupUi(self.signupWindow)
        self.signupWindow.show()
        
    def setupUi(self, DialogHome):
        DialogHome.setObjectName(_fromUtf8("DialogHome"))
        DialogHome.resize(683, 476)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Handwriting"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        DialogHome.setFont(font)
        DialogHome.setAutoFillBackground(False)
        DialogHome.setStyleSheet(_fromUtf8("QDialog{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(176, 0, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
""))
        self.welcomeLabel = QtGui.QLabel(DialogHome)
        self.welcomeLabel.setGeometry(QtCore.QRect(160, 90, 361, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monotype Corsiva"))
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet(_fromUtf8("\n"
"color:rgb(226, 226, 226);\n"
""))
        self.welcomeLabel.setObjectName(_fromUtf8("welcomeLabel"))
        self.home_login_btn = QtGui.QPushButton(DialogHome)
        self.home_login_btn.setGeometry(QtCore.QRect(250, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.home_login_btn.setFont(font)
        self.home_login_btn.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 183, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.home_login_btn.setObjectName(_fromUtf8("home_login_btn"))
        self.home_login_btn.clicked.connect(self.showLoginForm)
        self.vline = QtGui.QFrame(DialogHome)
        self.vline.setGeometry(QtCore.QRect(350, 280, 3, 61))
        self.vline.setFrameShape(QtGui.QFrame.VLine)
        self.vline.setFrameShadow(QtGui.QFrame.Sunken)
        self.vline.setObjectName(_fromUtf8("vline"))
        self.home_signup_btn = QtGui.QPushButton(DialogHome)
        self.home_signup_btn.setGeometry(QtCore.QRect(370, 290, 81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.home_signup_btn.setFont(font)
        self.home_signup_btn.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 183, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.home_signup_btn.setObjectName(_fromUtf8("home_signup_btn"))
        self.home_signup_btn.clicked.connect(self.showSignUpForm)
        self.label = QtGui.QLabel(DialogHome)
        self.label.setGeometry(QtCore.QRect(240, 170, 211, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("French Script MT"))
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:rgb(245, 81, 0)"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(DialogHome)
        QtCore.QMetaObject.connectSlotsByName(DialogHome)

    def retranslateUi(self, DialogHome):
        DialogHome.setWindowTitle(_translate("DialogHome", "Art Gallery Management System", None))
        self.welcomeLabel.setText(_translate("DialogHome", "Welcome to our art gallery,", None))
        self.home_login_btn.setToolTip(_translate("DialogHome", "A member of our gallery already? PRESS this button.", None))
        self.home_login_btn.setText(_translate("DialogHome", "Log In", None))
        self.home_signup_btn.setToolTip(_translate("DialogHome", "If you are a new user, PRESS this button to create an account. ", None))
        self.home_signup_btn.setText(_translate("DialogHome", "Sign Up", None))
        self.label.setText(_translate("DialogHome", "Be Inspired!", None))
'''
import hello_rc
import hi_rc
'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogHome = QtGui.QDialog()
    ui = Ui_DialogHome()
    ui.setupUi(DialogHome)
    DialogHome.show()
    sys.exit(app.exec_())
