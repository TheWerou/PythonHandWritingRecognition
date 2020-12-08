import math

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic.properties import QtWidgets, QtGui
import numpy as np
import threading

from Gui.MainWindow import Ui_MainWindow


class MainWinPersonal(Ui_MainWindow):
    def __init__(self, handRecon, dataModel):
        super().__init__()
        self.handRec = handRecon
        self.dataModel = dataModel
        self.myThred = None

    def setupUi(self, MainWindow):
        super(MainWinPersonal, self).setupUi(MainWindow)
        self.ChgIMGButton.clicked.connect(self.ChgIMGButton_on_click)
        self.MLcheck.clicked.connect(self.MLcheck_on_click)
        self.MLbasefolder_butt.clicked.connect(self.MLbasefolder_butt_for_rec_on_click)
        self.FolderStatistic.clicked.connect(self.MLbasefolder_butt_on_click)
        self.FolderVector.clicked.connect(self.folder_vector_on_click)
        self.TeachLayer.clicked.connect(self.teach_onclick)

        pixmap = QPixmap(self.dataModel.get_path_to_uploaded_png())
        self.ImgToShow.setPixmap(pixmap)
        MainWindow.setFixedSize(449, 523)
        self.LabelStatistic.setText(self.dataModel.get_path_to_save())
        self.LabelPathVector.setText(self.dataModel.get_path_to_vector())
        MainWindow.show()

    def MLbasefolder_butt_for_rec_on_click(self):
        try:
            dialog = QFileDialog()
            img_path = dialog.getExistingDirectory()
            self.dataModel.set_path_to_save_for_rec(img_path)
            self.LabelOutputCheck.setText("Folder at " + img_path)
            self.LabelStatistic.setText(self.dataModel.get_path_to_save())

        except Exception as e:
            print(e)
            self.LabelOutputCheck.setText("Directory not set sorry :C")

    def MLbasefolder_butt_on_click(self):
        try:
            dialog = QFileDialog()
            img_path = dialog.getExistingDirectory()
            self.dataModel.set_path_to_save(img_path)
            self.LabelOutputCheck.setText("Folder at " + img_path)
            self.LabelStatistic.setText(self.dataModel.get_path_to_save())

        except Exception as e:
            print(e)
            self.LabelOutputCheck.setText("Directory not set sorry :C")

    def ChgIMGButton_on_click(self):
        try:
            dialog = QFileDialog()
            img_path, _ = dialog.getOpenFileName()
            if img_path.endswith(".png"):
                self.handRec.set_paths()
                pixmap = QPixmap(img_path)
                self.ImgToShow.setPixmap(pixmap)
                self.LabelOutputCheck.setText("Nice pic let's find out what it is")
            else:
                self.LabelOutputCheck.setText("Sorry file must be .png")

        except Exception as e:
            print(e)
            self.LabelOutputCheck.setText("Something went wrong")

    def MLcheck_on_click(self):
        try:
            self.handRec.set_paths(1)
            output = self.handRec.calc_out(self.dataModel.get_path_to_uploaded_png())
            self.LabelOutputCheck.setText("I think it's " + output)
        except Exception as e:
            pass

    def folder_vector_on_click(self):
        try:
            dialog = QFileDialog()
            img_path = dialog.getExistingDirectory()
            self.dataModel.set_path_to_vector(img_path)
            self.handRec.set_paths()
            self.LabelPathVector.setText(self.dataModel.get_path_to_vector())

        except Exception as e:
            pass

    def teach_onclick(self):
        self.handRec.set_paths()
        self.progressBar.setValue(0)
        il = int(self.LoopPclick_2.text())
        dane = self.handRec.vector.make_letter_list_static(il)
        ilekrokow = int(self.LoopPclick.text())
        self.myThred = threading.Thread(target=self.teach, args=(dane, ilekrokow, il))

        if not self.myThred.is_alive():
            self.TeachLayer.setDisabled(True)
            self.myThred.start()
        else:
            self.label_4.setText("Pls wait layer learning")

    def teach(self, dane, ilekrokow, il):
        # musisz to dokonczyc chodzi o to ze jak masz kilka watkow to nie mozesz wypisywac ekran i mussiz dzielic czas
        try:
            self.handRec.read_wagas()
        except FileNotFoundError:
            pass

        iter = 0
        list_of_blad = []

        while iter < ilekrokow:
            # print("------")
            blad = 0
            rand_letter = np.random.randint(26)
            rand_nr = np.random.randint(il)

            CK_list = self.handRec.get_ck(rand_letter)
            wejsciowe = self.handRec.get_ek(rand_letter, rand_nr, dane)
            self.handRec.teach_01(wejsciowe, CK_list)

            helper = self.handRec.layer3.get_outputs()

            for k in range(len(self.handRec.layer3.get_outputs())):
                blad += math.fabs(CK_list[k] - helper[k])

            if ((iter/ilekrokow) * 100) % 20 == 0:
                list_of_blad.append(blad)
                self.handRec.save_wagas(rand_letter)
                self.handRec.csv_reader.write_log_to_csv("log_bledu", list_of_blad)
                self.progressBar.setValue(((iter/ilekrokow) * 100))

            iter += 1

        self.handRec.save_wagas()
        self.progressBar.setValue(100)
        self.TeachLayer.setDisabled(False)


