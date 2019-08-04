# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchArt.ui'
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

class Ui_SearchArtDialog(object):

    def display(self):
        connection = sqlite3.connect('AllTables.db')
        query = "SELECT Genre, count(*),avg(price) FROM Artworks GROUP BY Genre"
        result = connection.execute(query)
        self.GroupTableWidget.setHorizontalHeaderLabels(('Genre','Count','Average Price'))
        self.GroupTableWidget.setRowCount(0)
        for row_no, row_data in enumerate(result):
            self.GroupTableWidget.insertRow(row_no)
            for column_no, col_data in enumerate(row_data):
                self.GroupTableWidget.setItem(row_no,column_no, QtGui.QTableWidgetItem(str(col_data)))


    def search(self):
        connection = sqlite3.connect('AllTables.db')
        genre = self.comboBox.currentText()
        resultnew = connection.execute("SELECT Artists.FullName, Artworks.Title, Artworks.price from Artists INNER JOIN Artworks ON Artists.MemId = Artworks.MemId WHERE Genre=?",(genre,))
        self.ResultTableWidget.setHorizontalHeaderLabels(('Artist Name','Title','Price'))
        self.ResultTableWidget.setRowCount(0)
        for row_no, row_data in enumerate(resultnew):
            self.ResultTableWidget.insertRow(row_no)
            for column_no, col_data in enumerate(row_data):
                self.ResultTableWidget.setItem(row_no,column_no, QtGui.QTableWidgetItem(str(col_data)))

        connection.close()

    def setupUi(self, SearchArtDialog):
        SearchArtDialog.setObjectName(_fromUtf8("SearchArtDialog"))
        SearchArtDialog.resize(649, 577)
        SearchArtDialog.setStyleSheet(_fromUtf8("background-color:rgb(11, 109, 255)"))
        self.Titlelabel = QtGui.QLabel(SearchArtDialog)
        self.Titlelabel.setGeometry(QtCore.QRect(190, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Edwardian Script ITC"))
        font.setPointSize(26)
        self.Titlelabel.setFont(font)
        self.Titlelabel.setObjectName(_fromUtf8("Titlelabel"))
        self.memid_label = QtGui.QLabel(SearchArtDialog)
        self.memid_label.setGeometry(QtCore.QRect(60, 290, 231, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.memid_label.setFont(font)
        self.memid_label.setObjectName(_fromUtf8("memid_label"))
        self.search_button = QtGui.QPushButton(SearchArtDialog)
        self.search_button.setGeometry(QtCore.QRect(460, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0)"))
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.search_button.clicked.connect(self.search)
        self.GroupTableWidget = QtGui.QTableWidget(SearchArtDialog)
        self.GroupTableWidget.setGeometry(QtCore.QRect(140, 90, 321, 161))
        self.GroupTableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.GroupTableWidget.setRowCount(2)
        self.GroupTableWidget.setColumnCount(3)
        self.GroupTableWidget.setObjectName(_fromUtf8("GroupTableWidget"))
        self.display()
        self.comboBox = QtGui.QComboBox(SearchArtDialog)
        self.comboBox.setGeometry(QtCore.QRect(320, 290, 91, 22))
        self.comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.ResultTableWidget = QtGui.QTableWidget(SearchArtDialog)
        self.ResultTableWidget.setGeometry(QtCore.QRect(140, 360, 321, 161))
        self.ResultTableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.ResultTableWidget.setRowCount(2)
        self.ResultTableWidget.setColumnCount(3)
        self.ResultTableWidget.setObjectName(_fromUtf8("ResultTableWidget"))

        self.retranslateUi(SearchArtDialog)
        QtCore.QMetaObject.connectSlotsByName(SearchArtDialog)

    def retranslateUi(self, SearchArtDialog):
        SearchArtDialog.setWindowTitle(_translate("SearchArtDialog", "Search Art Works", None))
        self.Titlelabel.setText(_translate("SearchArtDialog", "Search for ArtWorks", None))
        self.memid_label.setText(_translate("SearchArtDialog", "Now, choose your desired Genre", None))
        self.search_button.setText(_translate("SearchArtDialog", "Search", None))
        self.comboBox.setItemText(0, _translate("SearchArtDialog", "Oil Painting", None))
        self.comboBox.setItemText(1, _translate("SearchArtDialog", "Dot Art", None))
        self.comboBox.setItemText(2, _translate("SearchArtDialog", "Wax Painting", None))
        self.comboBox.setItemText(3, _translate("SearchArtDialog", "3D Art", None))
        self.comboBox.setItemText(4, _translate("SearchArtDialog", "Abstract Art", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SearchArtDialog = QtGui.QDialog()
    ui = Ui_SearchArtDialog()
    ui.setupUi(SearchArtDialog)
    SearchArtDialog.show()
    sys.exit(app.exec_())
