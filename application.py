# coding=utf-8

from PyQt4 import QtGui, QtCore
from pyscanex import Ui_MainWindow
from pyscanex import _fromUtf8
import sys
import os
import datetime


app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

def actionAddTriggered():
    global ui
    fileName = QtGui.QFileDialog.getOpenFileName(ui.parent, 'Open file', '', 'TXT (*.txt);;BW (*.bw);;KB (*.kb)')
    path = os.path.abspath(fileName)
    rows = ui.tableFiles.rowCount()
    ui.tableFiles.setRowCount(rows + 1)

    ui.tableFiles.setItem(rows, 0, QtGui.QTableWidgetItem(path))
    ui.tableFiles.setItem(rows, 1, QtGui.QTableWidgetItem("%d bytes" % os.path.getsize(path)))
    dateAdded = str(datetime.datetime.now()).split('.')[0]
    ui.tableFiles.setItem(rows, 2, QtGui.QTableWidgetItem(dateAdded))

def currentTabChanged(tabIndex):
    global ui
    if tabIndex == -1:
        return

    if tabIndex == 0:
        ui.actionCompile.setEnabled(True)
        ui.actionRun.setEnabled(False)
    elif tabIndex == 1:
        ui.actionCompile.setEnabled(False)
        ui.actionRun.setEnabled(True)

def actionCompileTriggered():
    row = ui.tableFiles.currentRow()
    fileName = str(ui.tableFiles.itemAt(row, 0).text())
    kb = ui.kbParser.parse(fileName)
    QtGui.QProgressDialog('Compiling ...', 'Cancel', 0, 0, ui.parent).open()
    print kb


QtCore.QObject.connect(ui.actionAdd, QtCore.SIGNAL(_fromUtf8("triggered()")), actionAddTriggered)
QtCore.QObject.connect(ui.actionCompile, QtCore.SIGNAL(_fromUtf8("triggered()")), actionCompileTriggered)
QtCore.QObject.connect(ui.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), currentTabChanged)