# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CustomersReport.ui'
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

class Ui_CustomerReportDialog(object):

    def LoadTable(self):
        connection = sqlite3.connect('AllTables.db')
        cur = connection.cursor()
        query = "SELECT * FROM Customers ORDER BY Cid"
        result = connection.execute(query)
        self.tableWidget.setHorizontalHeaderLabels(('Cid','Full Name','Pincode','PhoneNo'))
        self.tableWidget.setRowCount(0)
        for row_no, row_data in enumerate(result):
            self.tableWidget.insertRow(row_no)
            for column_no, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_no,column_no, QtGui.QTableWidgetItem(str(col_data)))
        connection.close()

    def setupUi(self, CustomerReportDialog):
        CustomerReportDialog.setObjectName(_fromUtf8("CustomerReportDialog"))
        CustomerReportDialog.resize(565, 550)
        CustomerReportDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.LoadButton = QtGui.QPushButton(CustomerReportDialog)
        self.LoadButton.setGeometry(QtCore.QRect(210, 450, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(11)
        self.LoadButton.setFont(font)
        self.LoadButton.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.LoadButton.setObjectName(_fromUtf8("LoadButton"))
        self.LoadButton.clicked.connect(self.LoadTable)
        self.Titlelabel = QtGui.QLabel(CustomerReportDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(180, 50, 221, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.tableWidget = QtGui.QTableWidget(CustomerReportDialog)
        self.tableWidget.setGeometry(QtCore.QRect(70, 120, 421, 301))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

        self.retranslateUi(CustomerReportDialog)
        QtCore.QMetaObject.connectSlotsByName(CustomerReportDialog)

    def retranslateUi(self, CustomerReportDialog):
        CustomerReportDialog.setWindowTitle(_translate("CustomerReportDialog", "Customers Report", None))
        self.LoadButton.setText(_translate("CustomerReportDialog", "Load Records", None))
        self.Titlelabel.setText(_translate("CustomerReportDialog", "Customers - Report", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CustomerReportDialog = QtGui.QDialog()
    ui = Ui_CustomerReportDialog()
    ui.setupUi(CustomerReportDialog)
    CustomerReportDialog.show()
    sys.exit(app.exec_())
