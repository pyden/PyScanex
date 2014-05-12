# coding=utf-8

from application import app, MainWindow
import sys

if __name__ == '__main__':
    MainWindow.show()
    sys.exit(app.exec_())