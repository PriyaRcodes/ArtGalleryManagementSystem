# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddArtwork.ui'
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

class Ui_AddArtWorkDialog(object):

    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()


    def addArtwork(self):
        artid = self.ArtId_lineEdit.text()
        title = self.Title_lineEdit.text()
        genre = self.Genre_lineEdit.text()
        memid = self.MemId_lineEdit.text()
        price = self.Price_lineEdit.text()

        connection = sqlite3.connect('AllTables.db')
        connection.execute("INSERT INTO Artworks VALUES(?,?,?,?,?)",(artid,title,genre,memid,price))
        connection.commit()
        connection.close()
        self.showMessageBox('Success','Art Work Saved!')

    def setupUi(self, AddArtWorkDialog):
        AddArtWorkDialog.setObjectName(_fromUtf8("AddArtWorkDialog"))
        AddArtWorkDialog.resize(469, 466)
        AddArtWorkDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.Titlelabel = QtGui.QLabel(AddArtWorkDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(130, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.save_Button = QtGui.QPushButton(AddArtWorkDialog)
        self.save_Button.setGeometry(QtCore.QRect(280, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.save_Button.setFont(font)
        self.save_Button.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.save_Button.clicked.connect(self.addArtwork)
        self.ArtId_lineEdit = QtGui.QLineEdit(AddArtWorkDialog)
        self.ArtId_lineEdit.setGeometry(QtCore.QRect(240, 110, 121, 20))
        self.ArtId_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ArtId_lineEdit.setObjectName(_fromUtf8("ArtId_lineEdit"))
        self.memid_label = QtGui.QLabel(AddArtWorkDialog)
        self.memid_label.setGeometry(QtCore.QRect(70, 110, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.memid_label.setFont(font)
        self.memid_label.setObjectName(_fromUtf8("memid_label"))
        self.memid_label_2 = QtGui.QLabel(AddArtWorkDialog)
        self.memid_label_2.setGeometry(QtCore.QRect(70, 160, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.memid_label_2.setFont(font)
        self.memid_label_2.setObjectName(_fromUtf8("memid_label_2"))
        self.memid_label_3 = QtGui.QLabel(AddArtWorkDialog)
        self.memid_label_3.setGeometry(QtCore.QRect(70, 210, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.memid_label_3.setFont(font)
        self.memid_label_3.setObjectName(_fromUtf8("memid_label_3"))
        self.memid_label_4 = QtGui.QLabel(AddArtWorkDialog)
        self.memid_label_4.setGeometry(QtCore.QRect(70, 260, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.memid_label_4.setFont(font)
        self.memid_label_4.setObjectName(_fromUtf8("memid_label_4"))
        self.memid_label_5 = QtGui.QLabel(AddArtWorkDialog)
        self.memid_label_5.setGeometry(QtCore.QRect(70, 310, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.memid_label_5.setFont(font)
        self.memid_label_5.setObjectName(_fromUtf8("memid_label_5"))
        self.Title_lineEdit = QtGui.QLineEdit(AddArtWorkDialog)
        self.Title_lineEdit.setGeometry(QtCore.QRect(240, 160, 121, 20))
        self.Title_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Title_lineEdit.setObjectName(_fromUtf8("Title_lineEdit"))
        self.Genre_lineEdit = QtGui.QLineEdit(AddArtWorkDialog)
        self.Genre_lineEdit.setGeometry(QtCore.QRect(240, 210, 121, 20))
        self.Genre_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Genre_lineEdit.setObjectName(_fromUtf8("Genre_lineEdit"))
        self.MemId_lineEdit = QtGui.QLineEdit(AddArtWorkDialog)
        self.MemId_lineEdit.setGeometry(QtCore.QRect(240, 260, 121, 20))
        self.MemId_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.MemId_lineEdit.setObjectName(_fromUtf8("MemId_lineEdit"))
        self.Price_lineEdit = QtGui.QLineEdit(AddArtWorkDialog)
        self.Price_lineEdit.setGeometry(QtCore.QRect(240, 310, 121, 20))
        self.Price_lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Price_lineEdit.setObjectName(_fromUtf8("Price_lineEdit"))

        self.retranslateUi(AddArtWorkDialog)
        QtCore.QMetaObject.connectSlotsByName(AddArtWorkDialog)

    def retranslateUi(self, AddArtWorkDialog):
        AddArtWorkDialog.setWindowTitle(_translate("AddArtWorkDialog", "Add ArtWork", None))
        self.Titlelabel.setText(_translate("AddArtWorkDialog", "Add Art Work", None))
        self.save_Button.setText(_translate("AddArtWorkDialog", "Save", None))
        self.memid_label.setText(_translate("AddArtWorkDialog", "Art Id", None))
        self.memid_label_2.setText(_translate("AddArtWorkDialog", "<html><head/><body><p>Title</p></body></html>", None))
        self.memid_label_3.setText(_translate("AddArtWorkDialog", "Genre", None))
        self.memid_label_4.setText(_translate("AddArtWorkDialog", "Artist-MemID", None))
        self.memid_label_5.setText(_translate("AddArtWorkDialog", "Price", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AddArtWorkDialog = QtGui.QDialog()
    ui = Ui_AddArtWorkDialog()
    ui.setupUi(AddArtWorkDialog)
    AddArtWorkDialog.show()
    sys.exit(app.exec_())
