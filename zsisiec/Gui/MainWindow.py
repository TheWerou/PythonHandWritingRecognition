# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(449, 523)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QtCore.QSize(614, 684))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Static/A-0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 411, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ImgToShow = QtWidgets.QLabel(self.tab)
        self.ImgToShow.setGeometry(QtCore.QRect(10, 20, 381, 181))
        self.ImgToShow.setFrameShape(QtWidgets.QFrame.Box)
        self.ImgToShow.setText("")
        self.ImgToShow.setPixmap(QtGui.QPixmap("../../Data/Obrazki_do_uczenia/B/B-0.png"))
        self.ImgToShow.setScaledContents(True)
        self.ImgToShow.setObjectName("ImgToShow")
        self.LabelOutputCheck = QtWidgets.QLabel(self.tab)
        self.LabelOutputCheck.setGeometry(QtCore.QRect(10, 220, 381, 61))
        self.LabelOutputCheck.setStatusTip("")
        self.LabelOutputCheck.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LabelOutputCheck.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LabelOutputCheck.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelOutputCheck.setWordWrap(True)
        self.LabelOutputCheck.setObjectName("LabelOutputCheck")
        self.MLcheck = QtWidgets.QPushButton(self.tab)
        self.MLcheck.setGeometry(QtCore.QRect(10, 390, 381, 41))
        self.MLcheck.setObjectName("MLcheck")
        self.ChgIMGButton = QtWidgets.QPushButton(self.tab)
        self.ChgIMGButton.setGeometry(QtCore.QRect(10, 290, 381, 41))
        self.ChgIMGButton.setObjectName("ChgIMGButton")
        self.MLbasefolder_butt = QtWidgets.QPushButton(self.tab)
        self.MLbasefolder_butt.setGeometry(QtCore.QRect(10, 340, 381, 41))
        self.MLbasefolder_butt.setObjectName("MLbasefolder_butt")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.TeachLayer = QtWidgets.QPushButton(self.tab_2)
        self.TeachLayer.setGeometry(QtCore.QRect(10, 400, 391, 31))
        self.TeachLayer.setObjectName("TeachLayer")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 391, 31))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.LabelStatistic = QtWidgets.QLabel(self.tab_2)
        self.LabelStatistic.setGeometry(QtCore.QRect(10, 160, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.LabelStatistic.setFont(font)
        self.LabelStatistic.setFrameShape(QtWidgets.QFrame.Panel)
        self.LabelStatistic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelStatistic.setWordWrap(True)
        self.LabelStatistic.setObjectName("LabelStatistic")
        self.FolderVector = QtWidgets.QPushButton(self.tab_2)
        self.FolderVector.setGeometry(QtCore.QRect(10, 110, 391, 41))
        self.FolderVector.setObjectName("FolderVector")
        self.FolderStatistic = QtWidgets.QPushButton(self.tab_2)
        self.FolderStatistic.setGeometry(QtCore.QRect(10, 210, 391, 41))
        self.FolderStatistic.setObjectName("FolderStatistic")
        self.LabelPathVector = QtWidgets.QLabel(self.tab_2)
        self.LabelPathVector.setGeometry(QtCore.QRect(10, 50, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.LabelPathVector.setFont(font)
        self.LabelPathVector.setFrameShape(QtWidgets.QFrame.Panel)
        self.LabelPathVector.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelPathVector.setWordWrap(True)
        self.LabelPathVector.setObjectName("LabelPathVector")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 350, 211, 41))
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.LoopPclick = QtWidgets.QLineEdit(self.tab_2)
        self.LoopPclick.setGeometry(QtCore.QRect(230, 350, 171, 41))
        self.LoopPclick.setInputMask("")
        self.LoopPclick.setMaxLength(32767)
        self.LoopPclick.setAlignment(QtCore.Qt.AlignCenter)
        self.LoopPclick.setObjectName("LoopPclick")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 260, 391, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 211, 41))
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.LoopPclick_2 = QtWidgets.QLineEdit(self.tab_2)
        self.LoopPclick_2.setGeometry(QtCore.QRect(230, 300, 171, 41))
        self.LoopPclick_2.setInputMask("")
        self.LoopPclick_2.setMaxLength(32767)
        self.LoopPclick_2.setAlignment(QtCore.Qt.AlignCenter)
        self.LoopPclick_2.setObjectName("LoopPclick_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTest_AI = QtWidgets.QAction(MainWindow)
        self.actionTest_AI.setObjectName("actionTest_AI")
        self.actionTeach_AI = QtWidgets.QAction(MainWindow)
        self.actionTeach_AI.setObjectName("actionTeach_AI")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Handwriting recognition"))
        self.LabelOutputCheck.setText(_translate("MainWindow", "I didn\'t check what it is sorry"))
        self.MLcheck.setText(_translate("MainWindow", "Check what is on the image"))
        self.ChgIMGButton.setText(_translate("MainWindow", "Change your image"))
        self.MLbasefolder_butt.setText(_translate("MainWindow", "Change neuron layer dir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Recognize"))
        self.TeachLayer.setText(_translate("MainWindow", "Teach "))
        self.label_4.setText(_translate("MainWindow", "Your paths"))
        self.LabelStatistic.setText(_translate("MainWindow", "No place were to save data"))
        self.FolderVector.setText(_translate("MainWindow", "Chose traning folder"))
        self.FolderStatistic.setText(_translate("MainWindow", "Chose folder to save data"))
        self.LabelPathVector.setText(_translate("MainWindow", "No path to traning vector"))
        self.label_5.setText(_translate("MainWindow", "Amount of loops per click:"))
        self.LoopPclick.setText(_translate("MainWindow", "500"))
        self.label_6.setText(_translate("MainWindow", "Amount data from vector:"))
        self.LoopPclick_2.setText(_translate("MainWindow", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Teach neuron layers"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTest_AI.setText(_translate("MainWindow", "Test AI"))
        self.actionTeach_AI.setText(_translate("MainWindow", "Teach AI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())