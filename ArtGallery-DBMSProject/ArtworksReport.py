# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArtWorksReport.ui'
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

class Ui_ReportArtworksDialog(object):

    def ArtworksReport(self):
        connection = sqlite3.connect('AllTables.db')
        cur = connection.cursor()
        query = "SELECT * FROM ArtWorks ORDER BY ArtId"
        result = connection.execute(query)
        self.tableWidget.setHorizontalHeaderLabels(('ArtId','Title','Genre','MemId','Price'))
        self.tableWidget.setRowCount(0)
        for row_no, row_data in enumerate(result):
            self.tableWidget.insertRow(row_no)
            for column_no, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_no,column_no, QtGui.QTableWidgetItem(str(col_data)))
        connection.close()

    def setupUi(self, ReportArtworksDialog):
        ReportArtworksDialog.setObjectName(_fromUtf8("ReportArtworksDialog"))
        ReportArtworksDialog.resize(634, 469)
        ReportArtworksDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.tableWidget = QtGui.QTableWidget(ReportArtworksDialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 90, 521, 271))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.pushButton = QtGui.QPushButton(ReportArtworksDialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 390, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.ArtworksReport)
        self.ReportLabel = QtGui.QLabel(ReportArtworksDialog)
        self.ReportLabel.setGeometry(QtCore.QRect(200, 40, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.ReportLabel.setFont(font)
        self.ReportLabel.setObjectName(_fromUtf8("ReportLabel"))

        self.retranslateUi(ReportArtworksDialog)
        QtCore.QMetaObject.connectSlotsByName(ReportArtworksDialog)

    def retranslateUi(self, ReportArtworksDialog):
        ReportArtworksDialog.setWindowTitle(_translate("ReportArtworksDialog", "Art Works Report", None))
        self.pushButton.setText(_translate("ReportArtworksDialog", "Load Records", None))
        self.ReportLabel.setText(_translate("ReportArtworksDialog", "ArtWorks - Report", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ReportArtworksDialog = QtGui.QDialog()
    ui = Ui_ReportArtworksDialog()
    ui.setupUi(ReportArtworksDialog)
    ReportArtworksDialog.show()
    sys.exit(app.exec_())
