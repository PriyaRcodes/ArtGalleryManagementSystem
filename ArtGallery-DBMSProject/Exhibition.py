# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exhibition.ui'
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

class Ui_ExhibitionReport(object):
    def LoadTable(self):
        connection = sqlite3.connect('AllTables.db')
        cur = connection.cursor()
        query = "SELECT * FROM Exhibitions ORDER BY ExCount"
        result = connection.execute(query)
        self.tableWidget.setHorizontalHeaderLabels(('ExCount','Theme','Pincode','PhoneNo','FromDate','ToDate'))
        self.tableWidget.setRowCount(0)
        for row_no, row_data in enumerate(result):
            self.tableWidget.insertRow(row_no)
            for column_no, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_no,column_no, QtGui.QTableWidgetItem(str(col_data)))
        connection.close()

    def setupUi(self, ExhibitionReport):
        ExhibitionReport.setObjectName(_fromUtf8("ExhibitionReport"))
        ExhibitionReport.resize(615, 499)
        ExhibitionReport.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.ReportLabel = QtGui.QLabel(ExhibitionReport)
        self.ReportLabel.setGeometry(QtCore.QRect(210, 40, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.ReportLabel.setFont(font)
        self.ReportLabel.setObjectName(_fromUtf8("ReportLabel"))
        self.tableWidget = QtGui.QTableWidget(ExhibitionReport)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 521, 301))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.LoadButton = QtGui.QPushButton(ExhibitionReport)
        self.LoadButton.setGeometry(QtCore.QRect(230, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(11)
        self.LoadButton.setFont(font)
        self.LoadButton.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.LoadButton.setObjectName(_fromUtf8("LoadButton"))
        self.LoadButton.clicked.connect(self.LoadTable)
        self.retranslateUi(ExhibitionReport)
        QtCore.QMetaObject.connectSlotsByName(ExhibitionReport)

    def retranslateUi(self, ExhibitionReport):
        ExhibitionReport.setWindowTitle(_translate("ExhibitionReport", "Exhibition Report", None))
        self.ReportLabel.setText(_translate("ExhibitionReport", "Exhibition Report", None))
        self.LoadButton.setText(_translate("ExhibitionReport", "Load Recent Records", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ExhibitionReport = QtGui.QDialog()
    ui = Ui_ExhibitionReport()
    ui.setupUi(ExhibitionReport)
    ExhibitionReport.show()
    sys.exit(app.exec_())
