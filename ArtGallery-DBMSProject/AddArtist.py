
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddArtist.ui'
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

class Ui_ArtistDialog(object):

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()


    def addRecord(self):
        memid = self.MemIdlineEdit.text()
        fullname = self.fullname_lineEdit.text()
        pincode = self.pincode_lineEdit.text()
        phno = self.phno_lineEdit.text()

        conn = sqlite3.connect('AllTables.db')
        conn.execute("INSERT INTO Artists VALUES(?,?,?,?)",(memid,fullname,pincode,phno))
        conn.commit()
        conn.close()
        self.showMessageBox('Success','Record Added Successfully')


    def setupUi(self, ArtistDialog):
        ArtistDialog.setObjectName(_fromUtf8("ArtistDialog"))
        ArtistDialog.resize(518, 476)
        ArtistDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.Titlelabel = QtGui.QLabel(ArtistDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(150, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.add_Button = QtGui.QPushButton(ArtistDialog)
        self.add_Button.setGeometry(QtCore.QRect(310, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.add_Button.setFont(font)
        self.add_Button.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.add_Button.setObjectName(_fromUtf8("add_Button"))
        self.add_Button.clicked.connect(self.addRecord)
        self.idlabel = QtGui.QLabel(ArtistDialog)
        self.idlabel.setGeometry(QtCore.QRect(110, 120, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel.setFont(font)
        self.idlabel.setObjectName(_fromUtf8("idlabel"))
        self.MemIdlineEdit = QtGui.QLineEdit(ArtistDialog)
        self.MemIdlineEdit.setGeometry(QtCore.QRect(290, 120, 121, 20))
        self.MemIdlineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.MemIdlineEdit.setObjectName(_fromUtf8("MemIdlineEdit"))
        self.idlabel_2 = QtGui.QLabel(ArtistDialog)
        self.idlabel_2.setGeometry(QtCore.QRect(110, 170, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel_2.setFont(font)
        self.idlabel_2.setObjectName(_fromUtf8("idlabel_2"))
        self.idlabel_3 = QtGui.QLabel(ArtistDialog)
        self.idlabel_3.setGeometry(QtCore.QRect(110, 220, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel_3.setFont(font)
        self.idlabel_3.setObjectName(_fromUtf8("idlabel_3"))
        self.idlabel_4 = QtGui.QLabel(ArtistDialog)
        self.idlabel_4.setGeometry(QtCore.QRect(110, 270, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.idlabel_4.setFont(font)
        self.idlabel_4.setObjectName(_fromUtf8("idlabel_4"))
        self.fullname_lineEdit = QtGui.QLineEdit(ArtistDialog)
        self.fullname_lineEdit.setGeometry(QtCore.QRect(290, 170, 121, 20))
        self.fullname_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.fullname_lineEdit.setObjectName(_fromUtf8("fullname_lineEdit"))
        self.pincode_lineEdit = QtGui.QLineEdit(ArtistDialog)
        self.pincode_lineEdit.setGeometry(QtCore.QRect(290, 220, 121, 20))
        self.pincode_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pincode_lineEdit.setObjectName(_fromUtf8("pincode_lineEdit"))
        self.phno_lineEdit = QtGui.QLineEdit(ArtistDialog)
        self.phno_lineEdit.setGeometry(QtCore.QRect(290, 270, 121, 20))
        self.phno_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.phno_lineEdit.setObjectName(_fromUtf8("phno_lineEdit"))

        self.retranslateUi(ArtistDialog)
        QtCore.QMetaObject.connectSlotsByName(ArtistDialog)

    def retranslateUi(self, ArtistDialog):
        ArtistDialog.setWindowTitle(_translate("ArtistDialog", "Add Record", None))
        self.Titlelabel.setText(_translate("ArtistDialog", "Add Artist Record", None))
        self.add_Button.setText(_translate("ArtistDialog", "Add Record", None))
        self.idlabel.setText(_translate("ArtistDialog", "Membership ID", None))
        self.idlabel_2.setText(_translate("ArtistDialog", "Full Name", None))
        self.idlabel_3.setText(_translate("ArtistDialog", "Pincode", None))
        self.idlabel_4.setText(_translate("ArtistDialog", "Contact No.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ArtistDialog = QtGui.QDialog()
    ui = Ui_ArtistDialog()
    ui.setupUi(ArtistDialog)
    ArtistDialog.show()
    sys.exit(app.exec_())
