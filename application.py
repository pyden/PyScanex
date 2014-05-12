# coding=utf-8

from PyQt4 import QtGui, QtCore
from pyscanex import Ui_MainWindow
from pyscanex import _fromUtf8
import sys
import os
import datetime
import kbparser


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    signalCompilationDone = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)
ui = MainWindow()


sizes = [0.6, 0.145, 0.25,]
for i in xrange(3):
    ui.tableFiles.setColumnWidth(i, ui.tableFiles.width() * sizes[i])


ui.kbParser = kbparser.KBParser()
ui.parent = MainWindow

ui.tabConsultation.setEnabled(False)

def actionAddTriggered():
    global ui
    fileName = QtGui.QFileDialog.getOpenFileName(ui, 'Open file', '',
                                                 'TXT (*.txt);;BW (*.bw);;KB (*.kb)')

    if len(fileName.split('.')) == 1:
        return

    path = os.path.abspath(fileName)
    rows = ui.tableFiles.rowCount()
    ui.tableFiles.setRowCount(rows + 1)

    ui.tableFiles.setItem(rows, 0, QtGui.QTableWidgetItem(path))
    ui.tableFiles.setItem(rows, 2, QtGui.QTableWidgetItem("%d bytes" % os.path.getsize(path)))
    dateAdded = str(datetime.datetime.now()).split('.')[0]
    ui.tableFiles.setItem(rows, 3, QtGui.QTableWidgetItem(dateAdded))


def actionDeleteTriggered():
    row = ui.tableFiles.currentRow()
    if row == -1:
        return

    ui.tableFiles.removeRow(row)

def actionCompileTriggered():
    global ui
    row = ui.tableFiles.currentRow()
    if row == -1:
        return

    fileName = str(ui.tableFiles.itemAt(row, 0).text())

    class CompileProcess(QtCore.QThread):

        def __init__(self, fileName, parent = None):
            super(CompileProcess, self).__init__(parent)
            self.fileName = fileName

        def run(self):
            global ui
            ui.kb = ui.kbParser.parse(self.fileName)
            self.sleep(2)
            ui.signalCompilationDone.emit()


    ui.progressDialog = QtGui.QProgressDialog('Compiling ...', 'Abort', 0, 1)
    ui.progressDialog.setRange(0, 0)
    ui.progressDialog.setFixedSize(400, 100)
    ui.progressDialog.show()

    ui.compileProcessThread = CompileProcess(fileName)
    ui.compileProcessThread.start()

def compilationDoneTriggered():
    global ui
    ui.progressDialog.cancel()
    ui.compileProcessThread = None

    rows = ui.tableFiles.rowCount()
    ui.tableFiles.setRowCount(rows + 1)


def actionRunTriggered():
    pass


QtCore.QObject.connect(ui.actionAdd, QtCore.SIGNAL(_fromUtf8("triggered()")), actionAddTriggered)
QtCore.QObject.connect(ui.actionDelete, QtCore.SIGNAL(_fromUtf8("triggered()")), actionDeleteTriggered)
QtCore.QObject.connect(ui.actionCompile, QtCore.SIGNAL(_fromUtf8("triggered()")), actionCompileTriggered)
QtCore.QObject.connect(ui.actionRun, QtCore.SIGNAL(_fromUtf8("triggered()")), actionRunTriggered)
QtCore.QObject.connect(ui, QtCore.SIGNAL('signalCompilationDone()'), compilationDoneTriggered)