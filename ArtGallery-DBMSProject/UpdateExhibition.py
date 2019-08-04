# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateExhibition.ui'
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

class Ui_UpdateDialog(object):

    def showConfirmationMessgae(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def updateExhibitionRecord(self):
        excount = self.ExCountlineEdit.text()
        col_name = self.comboBoxField.currentText()
        newval = self.ValLineEdit.text()

        connection = sqlite3.connect('AllTables.db')
        cur = connection.cursor()
        connection.execute("UPDATE Exhibitions SET {} = ? WHERE ExCount = ?".format(col_name),(newval,excount))
        connection.commit()
        connection.close()
        self.showConfirmationMessgae('Success','Database Updated Successfully!')

    def setupUi(self, UpdateDialog):
        UpdateDialog.setObjectName(_fromUtf8("UpdateDialog"))
        UpdateDialog.resize(526, 417)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        UpdateDialog.setFont(font)
        UpdateDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.comboBoxField = QtGui.QComboBox(UpdateDialog)
        self.comboBoxField.setGeometry(QtCore.QRect(310, 190, 111, 22))
        self.comboBoxField.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.comboBoxField.setEditable(True)
        self.comboBoxField.setDuplicatesEnabled(False)
        self.comboBoxField.setObjectName(_fromUtf8("comboBoxField"))
        self.comboBoxField.addItem(_fromUtf8(""))
        self.comboBoxField.addItem(_fromUtf8(""))
        self.comboBoxField.addItem(_fromUtf8(""))
        self.comboBoxField.addItem(_fromUtf8(""))
        self.comboBoxField.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(UpdateDialog)
        self.label.setGeometry(QtCore.QRect(90, 200, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.idlabel = QtGui.QLabel(UpdateDialog)
        self.idlabel.setGeometry(QtCore.QRect(85, 140, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.idlabel.setFont(font)
        self.idlabel.setObjectName(_fromUtf8("idlabel"))
        self.ExCountlineEdit = QtGui.QLineEdit(UpdateDialog)
        self.ExCountlineEdit.setGeometry(QtCore.QRect(310, 140, 113, 20))
        self.ExCountlineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ExCountlineEdit.setObjectName(_fromUtf8("ExCountlineEdit"))
        self.label_2 = QtGui.QLabel(UpdateDialog)
        self.label_2.setGeometry(QtCore.QRect(90, 260, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ValLineEdit = QtGui.QLineEdit(UpdateDialog)
        self.ValLineEdit.setGeometry(QtCore.QRect(310, 260, 113, 20))
        self.ValLineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ValLineEdit.setObjectName(_fromUtf8("ValLineEdit"))
        self.Titlelabel = QtGui.QLabel(UpdateDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(170, 49, 181, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.pushButton = QtGui.QPushButton(UpdateDialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 330, 75, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.updateExhibitionRecord)

        self.retranslateUi(UpdateDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateDialog)

    def retranslateUi(self, UpdateDialog):
        UpdateDialog.setWindowTitle(_translate("UpdateDialog", "Update Records", None))
        self.comboBoxField.setItemText(0, _translate("UpdateDialog", "Theme", None))
        self.comboBoxField.setItemText(1, _translate("UpdateDialog", "FromDate", None))
        self.comboBoxField.setItemText(2, _translate("UpdateDialog", "ToDate", None))
        self.comboBoxField.setItemText(3, _translate("UpdateDialog", "Pincode", None))
        self.comboBoxField.setItemText(4, _translate("UpdateDialog", "PhNo", None))
        self.label.setText(_translate("UpdateDialog", "Choose Field", None))
        self.idlabel.setText(_translate("UpdateDialog", "Exhibition Count", None))
        self.label_2.setText(_translate("UpdateDialog", "Enter New Value", None))
        self.Titlelabel.setText(_translate("UpdateDialog", "Update Details", None))
        self.pushButton.setText(_translate("UpdateDialog", "Update", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UpdateDialog = QtGui.QDialog()
    ui = Ui_UpdateDialog()
    ui.setupUi(UpdateDialog)
    UpdateDialog.show()
    sys.exit(app.exec_())
