# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from Exhibition import Ui_ExhibitionReport
from UpdateExhibition import Ui_UpdateDialog
from AddArtist import Ui_ArtistDialog
from DeleteArtist import Ui_DeleteDialog
from ArtistsReport import Ui_Dialog
from AddArtwork import Ui_AddArtWorkDialog
from ArtworksReport import Ui_ReportArtworksDialog
from searchArt import Ui_SearchArtDialog
from AddCustomer import Ui_AddCustomerDialog
from CustomerView import Ui_CustomerViewDialog
from CustomersReport import Ui_CustomerReportDialog
from Transactions import Ui_TransactionsDialog

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

class Ui_MainWindow(object):

    def addArtWork(self):
        self.addArtwork = QtGui.QDialog()
        self.ui = Ui_AddArtWorkDialog()
        self.ui.setupUi(self.addArtwork)
        self.addArtwork.show()

    def viewArtWorks(self):
        self.viewArtwork = QtGui.QDialog()
        self.ui = Ui_ReportArtworksDialog()
        self.ui.setupUi(self.viewArtwork)
        self.viewArtwork.show()

    def search(self):
        self.searchArtwork = QtGui.QDialog()
        self.ui = Ui_SearchArtDialog()
        self.ui.setupUi(self.searchArtwork)
        self.searchArtwork.show()

    def addartist(self):
        self.addArtist = QtGui.QDialog()
        self.ui = Ui_ArtistDialog()
        self.ui.setupUi(self.addArtist)
        self.addArtist.show()

    def deleterecord(self):
        self.delArtist = QtGui.QDialog()
        self.ui = Ui_DeleteDialog()
        self.ui.setupUi(self.delArtist)
        self.delArtist.show()

    def viewallArtists(self):
        self.viewArtist = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.viewArtist)
        self.viewArtist.show()

    def showExhibitionReport(self):
        self.ExhibitionReportStruc = QtGui.QDialog()
        self.ui = Ui_ExhibitionReport()
        self.ui.setupUi(self.ExhibitionReportStruc)
        self.ExhibitionReportStruc.show()

    def UpdateExhibition(self):
       self.Update = QtGui.QDialog()
       self.ui = Ui_UpdateDialog()
       self.ui.setupUi(self.Update)
       self.Update.show()

    def addCustomer(self):
       self.AddCustomer = QtGui.QDialog()
       self.ui = Ui_AddCustomerDialog()
       self.ui.setupUi(self.AddCustomer)
       self.AddCustomer.show()

    def customerView(self):
       self.view = QtGui.QDialog()
       self.ui = Ui_CustomerViewDialog()
       self.ui.setupUi(self.view)
       self.view.show()

    def CustomerReport(self):
       self.report = QtGui.QDialog()
       self.ui = Ui_CustomerReportDialog()
       self.ui.setupUi(self.report)
       self.report.show()

    def Transactions(self):
        self.bill = QtGui.QDialog()
        self.ui = Ui_TransactionsDialog()
        self.ui.setupUi(self.bill)
        self.bill.show()

    def Quit(self):
        sys.exit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(804, 577)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(176, 0, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        #self.label = QtGui.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(320, 130, 81, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Serif"))
        font.setPointSize(24)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArt = QtGui.QMenu(self.menubar)
        self.menuArt.setObjectName(_fromUtf8("menuArt"))
        self.menuArt_2 = QtGui.QMenu(self.menubar)
        self.menuArt_2.setObjectName(_fromUtf8("menuArt_2"))
        self.menuExhibitions = QtGui.QMenu(self.menubar)
        self.menuExhibitions.setObjectName(_fromUtf8("menuExhibitions"))
        self.menuCustomers = QtGui.QMenu(self.menubar)
        self.menuCustomers.setObjectName(_fromUtf8("menuCustomers"))
        self.menuTransactions = QtGui.QMenu(self.menubar)
        self.menuTransactions.setObjectName(_fromUtf8("menuTransactions"))
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setObjectName(_fromUtf8("menuQuit"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionAdd_Record = QtGui.QAction(MainWindow)
        self.actionAdd_Record.setObjectName(_fromUtf8("actionAdd_Record"))
        self.actionAdd_Record.triggered.connect(self.addartist)

        self.actionRemove_Artist = QtGui.QAction(MainWindow)
        self.actionRemove_Artist.setObjectName(_fromUtf8("actionRemove_Artist"))
        self.actionRemove_Artist.triggered.connect(self.deleterecord)


        self.actionView_All = QtGui.QAction(MainWindow)
        self.actionView_All.setObjectName(_fromUtf8("actionView_All"))
        self.actionView_All.triggered.connect(self.viewallArtists)

        self.actionAdd_Art_Work = QtGui.QAction(MainWindow)
        self.actionAdd_Art_Work.setObjectName(_fromUtf8("actionAdd_Art_Work"))
        self.actionAdd_Art_Work.triggered.connect(self.addArtWork)

        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionSearch.triggered.connect(self.search)

        self.actionView_All_2 = QtGui.QAction(MainWindow)
        self.actionView_All_2.setObjectName(_fromUtf8("actionView_All_2"))
        self.actionView_All_2.triggered.connect(self.viewArtWorks)

        self.actionUpdate_details = QtGui.QAction(MainWindow)
        self.actionUpdate_details.setObjectName(_fromUtf8("actionUpdate_details"))
        self.actionUpdate_details.triggered.connect(self.UpdateExhibition)

        self.actionView_All_3 = QtGui.QAction(MainWindow)
        self.actionView_All_3.setObjectName(_fromUtf8("actionView_All_3"))
        self.actionView_All_3.triggered.connect(self.showExhibitionReport)

        self.actionAdd_Customer = QtGui.QAction(MainWindow)
        self.actionAdd_Customer.setObjectName(_fromUtf8("actionAdd_Customer"))
        self.actionAdd_Customer.triggered.connect(self.addCustomer)

        self.actionCustomerView = QtGui.QAction(MainWindow)
        self.actionCustomerView.setObjectName(_fromUtf8("actionCustomerView"))
        self.actionCustomerView.triggered.connect(self.customerView)

        self.actionView_All_4 = QtGui.QAction(MainWindow)
        self.actionView_All_4.setObjectName(_fromUtf8("actionView_All_4"))
        self.actionView_All_4.triggered.connect(self.CustomerReport)

        self.actionView = QtGui.QAction(MainWindow)
        self.actionView.setObjectName(_fromUtf8("actionView"))


        self.actionView_Past_Transactions = QtGui.QAction(MainWindow)
        self.actionView_Past_Transactions.setObjectName(_fromUtf8("actionView_Past_Transactions"))
        self.actionView_Past_Transactions.triggered.connect(self.Transactions)

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.Quit)


        self.menuArt.addAction(self.actionAdd_Record)
        self.menuArt.addAction(self.actionRemove_Artist)
        self.menuArt.addSeparator()
        self.menuArt.addAction(self.actionView_All)
        self.menuArt_2.addAction(self.actionAdd_Art_Work)
        self.menuArt_2.addAction(self.actionSearch)
        self.menuArt_2.addSeparator()
        self.menuArt_2.addAction(self.actionView_All_2)
        self.menuExhibitions.addAction(self.actionUpdate_details)
        self.menuExhibitions.addSeparator()
        self.menuExhibitions.addAction(self.actionView_All_3)
        self.menuCustomers.addAction(self.actionAdd_Customer)
        self.menuCustomers.addAction(self.actionCustomerView)
        self.menuCustomers.addSeparator()
        self.menuCustomers.addAction(self.actionView_All_4)
        self.menuTransactions.addAction(self.actionView_Past_Transactions)
        self.menuQuit.addAction(self.actionExit)

        self.menubar.addAction(self.menuArt.menuAction())
        self.menubar.addAction(self.menuArt_2.menuAction())
        self.menubar.addAction(self.menuExhibitions.menuAction())
        self.menubar.addAction(self.menuCustomers.menuAction())
        self.menubar.addAction(self.menuTransactions.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Art Gallery Management System", None))
        #self.label.setText(_translate("MainWindow", "Hello!", None))
        self.menuArt.setTitle(_translate("MainWindow", "Artists", None))
        self.menuArt_2.setTitle(_translate("MainWindow", "Art Works", None))
        self.menuExhibitions.setTitle(_translate("MainWindow", "Exhibitions", None))
        self.menuCustomers.setTitle(_translate("MainWindow", "Customers", None))
        self.menuTransactions.setTitle(_translate("MainWindow", "Transactions", None))
        self.menuQuit.setTitle(_translate("MainWindow", "Quit", None))
        self.actionAdd_Record.setText(_translate("MainWindow", "Add Artist", None))
        self.actionRemove_Artist.setText(_translate("MainWindow", "Remove Artist", None))
        self.actionView_All.setText(_translate("MainWindow", "View All", None))
        self.actionAdd_Art_Work.setText(_translate("MainWindow", "Add Art Work", None))
        self.actionSearch.setText(_translate("MainWindow", "Search", None))
        self.actionView_All_2.setText(_translate("MainWindow", "View All", None))
        self.actionUpdate_details.setText(_translate("MainWindow", "Update details", None))
        self.actionView_All_3.setText(_translate("MainWindow", "View All", None))
        self.actionAdd_Customer.setText(_translate("MainWindow", "Add Customer ", None))
        self.actionCustomerView.setText(_translate("MainWindow", "View Art Gallery as Customer", None))
        self.actionView_All_4.setText(_translate("MainWindow", "View All", None))
        self.actionView.setText(_translate("MainWindow", "View", None))
        self.actionView_Past_Transactions.setText(_translate("MainWindow", "View Past Transactions", None))
        self.actionExit.setText(_translate("MainWindow","Exit",None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
