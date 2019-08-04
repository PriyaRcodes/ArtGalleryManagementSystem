# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCustomer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3

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

class Ui_AddCustomerDialog(object):

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()    

    def add(self):
        cid = self.CidlineEdit.text()
        fullname = self.fullname_lineEdit.text()
        pincode = self.pincode_lineEdit.text()
        phno = self.phno_lineEdit.text()

        conn = sqlite3.connect('AllTables.db')
        conn.execute("INSERT INTO Customers VALUES(?,?,?,?)",(cid,fullname,pincode,phno))
        conn.commit()
        conn.close()
        self.showMessageBox('Success','Record Added Successfully')

    def setupUi(self, AddCustomerDialog):
        AddCustomerDialog.setObjectName(_fromUtf8("AddCustomerDialog"))
        AddCustomerDialog.resize(455, 446)
        AddCustomerDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.Titlelabel = QtGui.QLabel(AddCustomerDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(100, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.add_Button = QtGui.QPushButton(AddCustomerDialog)
        self.add_Button.setGeometry(QtCore.QRect(280, 360, 101, 31))
        self.add_Button.clicked.connect(self.add)

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.add_Button.setFont(font)
        self.add_Button.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.add_Button.setObjectName(_fromUtf8("add_Button"))
        self.fullname_lineEdit = QtGui.QLineEdit(AddCustomerDialog)
        self.fullname_lineEdit.setGeometry(QtCore.QRect(260, 180, 121, 20))
        self.fullname_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.fullname_lineEdit.setObjectName(_fromUtf8("fullname_lineEdit"))
        self.idlabel_3 = QtGui.QLabel(AddCustomerDialog)
        self.idlabel_3.setGeometry(QtCore.QRect(80, 230, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel_3.setFont(font)
        self.idlabel_3.setObjectName(_fromUtf8("idlabel_3"))
        self.CidlineEdit = QtGui.QLineEdit(AddCustomerDialog)
        self.CidlineEdit.setGeometry(QtCore.QRect(260, 130, 121, 20))
        self.CidlineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.CidlineEdit.setObjectName(_fromUtf8("CidlineEdit"))
        self.idlabel_4 = QtGui.QLabel(AddCustomerDialog)
        self.idlabel_4.setGeometry(QtCore.QRect(80, 280, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel_4.setFont(font)
        self.idlabel_4.setObjectName(_fromUtf8("idlabel_4"))
        self.phno_lineEdit = QtGui.QLineEdit(AddCustomerDialog)
        self.phno_lineEdit.setGeometry(QtCore.QRect(260, 280, 121, 20))
        self.phno_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.phno_lineEdit.setObjectName(_fromUtf8("phno_lineEdit"))
        self.pincode_lineEdit = QtGui.QLineEdit(AddCustomerDialog)
        self.pincode_lineEdit.setGeometry(QtCore.QRect(260, 230, 121, 20))
        self.pincode_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pincode_lineEdit.setObjectName(_fromUtf8("pincode_lineEdit"))
        self.idlabel = QtGui.QLabel(AddCustomerDialog)
        self.idlabel.setGeometry(QtCore.QRect(80, 130, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel.setFont(font)
        self.idlabel.setObjectName(_fromUtf8("idlabel"))
        self.idlabel_2 = QtGui.QLabel(AddCustomerDialog)
        self.idlabel_2.setGeometry(QtCore.QRect(80, 180, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel_2.setFont(font)
        self.idlabel_2.setObjectName(_fromUtf8("idlabel_2"))

        self.retranslateUi(AddCustomerDialog)
        QtCore.QMetaObject.connectSlotsByName(AddCustomerDialog)

    def retranslateUi(self, AddCustomerDialog):
        AddCustomerDialog.setWindowTitle(_translate("AddCustomerDialog", "Add Customer", None))
        self.Titlelabel.setText(_translate("AddCustomerDialog", "Add Customer Record", None))
        self.add_Button.setText(_translate("AddCustomerDialog", "Add Record", None))
        self.idlabel_3.setText(_translate("AddCustomerDialog", "Pincode", None))
        self.idlabel_4.setText(_translate("AddCustomerDialog", "Contact No.", None))
        self.idlabel.setText(_translate("AddCustomerDialog", "Customer ID", None))
        self.idlabel_2.setText(_translate("AddCustomerDialog", "Full Name", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AddCustomerDialog = QtGui.QDialog()
    ui = Ui_AddCustomerDialog()
    ui.setupUi(AddCustomerDialog)
    AddCustomerDialog.show()
    sys.exit(app.exec_())
