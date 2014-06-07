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


sizes = [0.62, 0.15, 0.2,]
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
    ui.tableFiles.setItem(rows, 2, QtGui.QTableWidgetItem("%d bajt" % os.path.getsize(path)))
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

    fileName = str(ui.tableFiles.item(row, 0).text())

    class CompileProcess(QtCore.QThread):

        def __init__(self, fileName, parent = None):
            super(CompileProcess, self).__init__(parent)
            self.fileName = fileName

        def run(self):
            global ui
            ui.kb = ui.kbParser.parse(self.fileName)
            self.sleep(1)
            ui.signalCompilationDone.emit()


    ui.progressDialog = QtGui.QProgressDialog('Kompilacja ...', u'Powrót', 0, 1)
    ui.progressDialog.setRange(0, 0)
    ui.progressDialog.setFixedSize(400, 100)
    ui.progressDialog.show()

    ui.compileProcessThread = CompileProcess(fileName)
    ui.compileProcessThread.start()

def compilationDoneTriggered():
    global ui
    ui.progressDialog.cancel()
    ui.compileProcessThread = None
    row = ui.tableFiles.rowCount() - 1
    ui.tableFiles.setItem(row, 1, QtGui.QTableWidgetItem('tak'))

def actionRunTriggered():
    global ui
    row = ui.tableFiles.currentRow()

    if row == -1:
        return

    item = ui.tableFiles.item(row, 1)

    if item is None:
        return

    ui.tabWidget.setCurrentIndex(1)
    ui.tabWidget.setTabEnabled(1, True)

    ui.groupBox.setTitle('Cel konsultacji: ' + ui.kb['goal'])
    ui.resultRules = None

    ui.comboBoxquestion.params = {}
    for p in sorted(ui.kb['parameters'].keys()):
        ui.comboBoxquestion.params[ui.kb['parameters'][p]['question']] = p
        ui.comboBoxquestion.addItem(ui.kb['parameters'][p]['question'])

    question = str(ui.comboBoxquestion.itemText(0))
    parameter = ui.comboBoxquestion.params[question]
    ui.comboBoxAnswers.clear()
    ui.comboBoxAnswers.addItem('<niewiadomo>')
    ui.comboBoxAnswers.addItems(list(ui.kb['parameters'][parameter]['values']))

def resetConsultationWidgets():
    ui.listFacts.setEnabled(True)
    ui.comboBoxquestion.clear()
    ui.plainDecisions.setPlainText('')
    ui.listFacts.clear()
    ui.listDecisions.clear()
    ui.comboBoxAnswers.clear()
    ui.pushButtonNext.setEnabled(True)

def resetConsultation():
    global ui
    resetConsultationWidgets()
    ui.resultRules = None
    ui.comboBoxquestion.params = {}
    for p in sorted(ui.kb['parameters'].keys()):
        ui.comboBoxquestion.params[ui.kb['parameters'][p]['question']] = p
        ui.comboBoxquestion.addItem(ui.kb['parameters'][p]['question'])

    question = str(ui.comboBoxquestion.itemText(0))
    parameter = ui.comboBoxquestion.params[question]
    ui.comboBoxAnswers.clear()
    ui.comboBoxAnswers.addItem('<niewiadomo>')
    ui.comboBoxAnswers.addItems(list(ui.kb['parameters'][parameter]['values']))

def pushButtonNextClicked():
    global ui
    answer = str(ui.comboBoxAnswers.currentText())

    index = ui.comboBoxquestion.currentIndex()

    question = str(ui.comboBoxquestion.itemText(index))
    parameter = ui.comboBoxquestion.params[question]

    fact = parameter  + " jest " + answer
    ui.listFacts.addItem(fact)

    ui.comboBoxquestion.removeItem(index)

    if ui.comboBoxquestion.count() == 0:
        ui.pushButtonNext.setEnabled(False)
        ui.plainDecisions.setPlainText(u'Nie ma decyzji dla potocznego zbioru reguł')
        return

    ui.comboBoxquestion.setCurrentIndex(0)
    question = str(ui.comboBoxquestion.itemText(0))
    parameter = ui.comboBoxquestion.params[question]

    ui.comboBoxAnswers.clear()
    ui.comboBoxAnswers.addItem('<niewiadomo>')
    ui.comboBoxAnswers.addItems(list(ui.kb['parameters'][parameter]['values']))


    if answer != '<niewiadomo>':
        fact = fact.replace(" jest ", ":")
        rules = ui.kb['indexer'][fact]

        if ui.resultRules is None:
            ui.resultRules = rules
        else:
            ui.resultRules = ui.resultRules.intersection(rules)

        ui.listDecisions.clear()
        ui.listDecisions.addItems(list(ui.resultRules))


    if ui.resultRules is None:
        return

    if len(ui.resultRules) == 1:
        ui.pushButtonNext.setEnabled(False)
        ui.listFacts.setEnabled(False)
        decisions = ui.kb['rules'][ui.resultRules.pop()]['decisions']
        line = ''
        for k in decisions.keys():
            line += k + ": " + decisions[k] + '\n'

        ui.plainDecisions.setPlainText(line)
    elif len(ui.resultRules) == 0:
        ui.pushButtonNext.setEnabled(False)
        ui.plainDecisions.setPlainText(u'Nie ma decyzji dla potocznego zbioru reguł')




def pushButtonResetClicked():
    resetConsultation()


def pushButtonStopClicked():
    global ui
    resetConsultationWidgets()
    ui.tabConsultation.setEnabled(False)
    ui.tabWidget.setCurrentIndex(0)
    ui.comboBoxAnswers.clear()
    ui.comboBoxquestion.clear()


def comboBoxQuestionItemChanged(item):
    global ui
    q = str(item)
    parameter = ui.comboBoxquestion.params[q]
    ui.comboBoxAnswers.clear()
    ui.comboBoxAnswers.addItem('<niewiadomo>')
    ui.comboBoxAnswers.addItems(list(ui.kb['parameters'][parameter]['values']))


def listFactsItemDoubleClicked(item):
    global ui
    tokens = str(item.text()).split(" jest ")
    question = ui.kb['parameters'][tokens[0]]['question']
    ui.comboBoxquestion.insertItem(0, question)
    item_ = ui.listFacts.takeItem(ui.listFacts.row(item))
    del item_

    if ui.listFacts.count() == 0:
        ui.listDecisions.clear()
        ui.resultRules = None
        return

    if tokens[1] == '<niewiadomo>':
        return

    ui.resultRules = None

    for i in xrange(ui.listFacts.count()):
        fact = str(ui.listFacts.item(i).text())
        fact = fact.replace(" jest ", ":")
        rules = ui.kb['indexer'][fact]

        if ui.resultRules is None:
            ui.resultRules = rules
        else:
            ui.resultRules = ui.resultRules.intersection(rules)

    ui.listDecisions.clear()
    ui.listDecisions.addItems(list(ui.resultRules))
    if not ui.pushButtonNext.isEnabled():
        ui.pushButtonNext.isEnabled(True)
    ui.plainDecisions.setPlainText('')



QtCore.QObject.connect(ui.actionAdd, QtCore.SIGNAL(_fromUtf8("triggered()")), actionAddTriggered)
QtCore.QObject.connect(ui.actionDelete, QtCore.SIGNAL(_fromUtf8("triggered()")), actionDeleteTriggered)
QtCore.QObject.connect(ui.actionCompile, QtCore.SIGNAL(_fromUtf8("triggered()")), actionCompileTriggered)
QtCore.QObject.connect(ui.actionRun, QtCore.SIGNAL(_fromUtf8("triggered()")), actionRunTriggered)
QtCore.QObject.connect(ui, QtCore.SIGNAL('signalCompilationDone()'), compilationDoneTriggered)
QtCore.QObject.connect(ui.pushButtonNext, QtCore.SIGNAL('clicked()'), pushButtonNextClicked)
QtCore.QObject.connect(ui.pushButtonReset, QtCore.SIGNAL('clicked()'), pushButtonResetClicked)
QtCore.QObject.connect(ui.pushButtonStop, QtCore.SIGNAL('clicked()'), pushButtonStopClicked)
QtCore.QObject.connect(ui.comboBoxquestion, QtCore.SIGNAL('activated(QString)'), comboBoxQuestionItemChanged)
QtCore.QObject.connect(ui.listFacts, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem*)'), listFactsItemDoubleClicked)


def displayKbToConsole():
    global ui

    parameters = sorted(ui.kb['parameters'].keys())
    b = """
    for p in parameters:
        print p
        print 'Values: ' + ', '.join(v for v in ui.kb['parameters'][p]['values'])
        print 'Question: ' + ui.kb['parameters'][p]['question']
        print"""
    rules = sorted(ui.kb['rules'].keys())
    for r in rules:
        print r
        print ui.kb['rules'][r]