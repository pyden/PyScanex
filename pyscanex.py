# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\Python\PyScanex\pyscanex.ui'
#
# Created: Fri May 09 23:36:17 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import kbparser

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
    def setupUi(self, MainWindow):
        self.parent = MainWindow
        self.kbParser = kbparser.KBParser()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabFile = QtGui.QWidget()
        self.tabFile.setObjectName(_fromUtf8("tabFile"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabFile)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableFiles = QtGui.QTableWidget(self.tabFile)
        self.tableFiles.setAlternatingRowColors(True)
        self.tableFiles.setColumnCount(3)
        self.tableFiles.setObjectName(_fromUtf8("tableFiles"))
        self.tableFiles.setRowCount(0)
        self.tableFiles.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.tableFiles.setSelectionBehavior(QtGui.QTableWidget.SelectRows)

        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tableFiles.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tableFiles.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tableFiles.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableFiles)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/file_manager.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabFile, icon1, _fromUtf8(""))
        self.tabCompiled = QtGui.QWidget()
        self.tabCompiled.setObjectName(_fromUtf8("tabCompiled"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabCompiled)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableCompiled = QtGui.QTableWidget(self.tabCompiled)
        self.tableCompiled.setObjectName(_fromUtf8("tableCompiled"))
        self.tableCompiled.setColumnCount(3)
        self.tableCompiled.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tableCompiled.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tableCompiled.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tableCompiled.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.tableCompiled)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/database_green.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabCompiled, icon2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd = QtGui.QAction(MainWindow)
        self.actionAdd.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/database_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon3)
        self.actionAdd.setObjectName(_fromUtf8("actionAddKnowledgeBase"))
        self.actionExit = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/door_in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionCompile = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icons/database_lightning.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompile.setIcon(icon5)
        self.actionCompile.setObjectName(_fromUtf8("actionCompile"))
        self.actionRun = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icons/database_go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon6)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCompile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionRun.setEnabled(False)

        sizes = [0.50, 0.145, 0.25]
        for i in xrange(3):
            self.tableFiles.setColumnWidth(i, self.tableFiles.width() * sizes[i])
            self.tableCompiled.setColumnWidth(i, self.tableFiles.width() * sizes[i])


        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Scannex", None))
        self.tableFiles.setSortingEnabled(True)
        item = self.tableFiles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Path", None))
        item = self.tableFiles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size", None))
        item = self.tableFiles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Added", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFile), _translate("MainWindow", "Knowledge Base Files", None))
        item = self.tableCompiled.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Path", None))
        item = self.tableCompiled.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size", None))
        item = self.tableCompiled.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Compiled", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCompiled), _translate("MainWindow", "Compiled Knowledge Base Files", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAdd.setText(_translate("MainWindow", "Add", None))
        self.actionAdd.setToolTip(_translate("MainWindow", "Add new knowledge base to the system", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit from application", None))
        self.actionCompile.setText(_translate("MainWindow", "Compile", None))
        self.actionCompile.setToolTip(_translate("MainWindow", "Compile selected knowledge base", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionRun.setToolTip(_translate("MainWindow", "Run selected knowledge base", None))




