# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteArtist.ui'
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

class Ui_DeleteDialog(object):
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def deleterecord(self):
        memberid = self.MemId_lineEdit.text()
        connection = sqlite3.connect('AllTables.db')
        connection.execute("DELETE FROM Artists WHERE MemId = ?",(memberid,))   #comma is used to make the parameters a tuple
        connection.commit()
        connection.close()
        self.showMessageBox('Success','Record Deleted.')

    def setupUi(self, DeleteDialog):
        DeleteDialog.setObjectName(_fromUtf8("DeleteDialog"))
        DeleteDialog.resize(463, 300)
        DeleteDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.Titlelabel = QtGui.QLabel(DeleteDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(100, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.memid_label = QtGui.QLabel(DeleteDialog)
        self.memid_label.setGeometry(QtCore.QRect(80, 120, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.memid_label.setFont(font)
        self.memid_label.setObjectName(_fromUtf8("memid_label"))
        self.MemId_lineEdit = QtGui.QLineEdit(DeleteDialog)
        self.MemId_lineEdit.setGeometry(QtCore.QRect(260, 120, 121, 20))
        self.MemId_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.MemId_lineEdit.setObjectName(_fromUtf8("MemId_lineEdit"))
        self.delete_Button = QtGui.QPushButton(DeleteDialog)
        self.delete_Button.setGeometry(QtCore.QRect(180, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.delete_Button.setFont(font)
        self.delete_Button.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.delete_Button.setObjectName(_fromUtf8("delete_Button"))
        self.delete_Button.clicked.connect(self.deleterecord)
        self.retranslateUi(DeleteDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteDialog)

    def retranslateUi(self, DeleteDialog):
        DeleteDialog.setWindowTitle(_translate("DeleteDialog", "Delete Record", None))
        self.Titlelabel.setText(_translate("DeleteDialog", "Delete Artist Record", None))
        self.memid_label.setText(_translate("DeleteDialog", "Membership ID", None))
        self.delete_Button.setText(_translate("DeleteDialog", "Delete Record", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DeleteDialog = QtGui.QDialog()
    ui = Ui_DeleteDialog()
    ui.setupUi(DeleteDialog)
    DeleteDialog.show()
    sys.exit(app.exec_())
