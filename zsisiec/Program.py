import os

from PyQt5 import QtCore, QtGui, QtWidgets
from Gui.MainWinPersonal import MainWinPersonal
from Gui.MainWindowModel import MainWindowModel
from HandWritingRecognition.main import ZSIproject
import sys


if __name__ == "__main__":
    main_file = os.path.dirname(os.path.realpath(__file__))

    program_model = MainWindowModel(main_file)

    ai = ZSIproject(program_model)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = MainWinPersonal(ai, program_model)
    ui.setupUi(MainWindow)

    sys.exit(app.exec_())
