# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CustomerView.ui'
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

class Ui_CustomerViewDialog(object):

    def view(self):
        connection = sqlite3.connect('AllTables.db')

        #connection.execute("CREATE VIEW customers_view AS\
        #SELECT Artists.FullName,Artworks.Title,Artworks.Genre,Artworks.price\
        #FROM Artists INNER JOIN Artworks ON Artists.MemId = Artworks.MemId")
        #Since creation is done only once, the above lines are commented out.

        result = connection.execute("SELECT * FROM customers_view")
        connection.commit()
        self.tableWidget.setHorizontalHeaderLabels(('Artist Name','Title','Genre','Price'))
        self.tableWidget.setRowCount(0)
        for row_no, row_data in enumerate(result):
            self.tableWidget.insertRow(row_no)
            for column_no, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_no,column_no, QtGui.QTableWidgetItem(str(col_data)))
        connection.close()

    def setupUi(self, CustomerViewDialog):
        CustomerViewDialog.setObjectName(_fromUtf8("CustomerViewDialog"))
        CustomerViewDialog.resize(592, 526)
        CustomerViewDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.Titlelabel = QtGui.QLabel(CustomerViewDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(130, 30, 371, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.tableWidget = QtGui.QTableWidget(CustomerViewDialog)
        self.tableWidget.setGeometry(QtCore.QRect(90, 100, 421, 301))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.LoadButton = QtGui.QPushButton(CustomerViewDialog)
        self.LoadButton.setGeometry(QtCore.QRect(240, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(11)
        self.LoadButton.setFont(font)
        self.LoadButton.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.LoadButton.setObjectName(_fromUtf8("LoadButton"))
        self.LoadButton.clicked.connect(self.view)

        self.retranslateUi(CustomerViewDialog)
        QtCore.QMetaObject.connectSlotsByName(CustomerViewDialog)

    def retranslateUi(self, CustomerViewDialog):
        CustomerViewDialog.setWindowTitle(_translate("CustomerViewDialog", "Customer View", None))
        self.Titlelabel.setText(_translate("CustomerViewDialog", "Art Gallery Report for Customer", None))
        self.LoadButton.setText(_translate("CustomerViewDialog", "Load Art Items", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CustomerViewDialog = QtGui.QDialog()
    ui = Ui_CustomerViewDialog()
    ui.setupUi(CustomerViewDialog)
    CustomerViewDialog.show()
    sys.exit(app.exec_())
