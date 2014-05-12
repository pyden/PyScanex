# coding=utf-8

from application import app, ui
import sys

if __name__ == '__main__':
    ui.show()
    sys.exit(app.exec_())