import os
import string

import numpy as np
import math

from HandWritingRecognition.AInetworkClasses.NeuronLayer import NeuronLayer
from HandWritingRecognition.toolfornetwork.ReadCSV import ReadCSV
from HandWritingRecognition.toolfornetwork.VektorEkiCK import VektorEKiCK


class ZSIproject:
    def __init__(self, datamodel):
        self.layer1 = NeuronLayer()
        self.layer2 = NeuronLayer()
        self.layer3 = NeuronLayer()
        self.layer1.add_neuron(784, 1)
        self.layer2.add_neuron(63, 784)
        self.layer3.add_neuron(5, 63)
        self.csv_reader = ReadCSV("")
        self.vector = VektorEKiCK("")
        self.datamodel = datamodel
        self.blad_sieci = 0
        self.set_paths()

    def set_paths(self, path_to_check=None):
        if path_to_check is not None:
            self.csv_reader = ReadCSV(self.datamodel.get_path_to_save_for_rec())
        else:
            self.csv_reader = ReadCSV(self.datamodel.get_path_to_save())

        self.vector = VektorEKiCK(self.datamodel.get_path_to_vector())
        try:
            self.read_wagas()
        except Exception as e:
            pass

    def get_paths(self):
        return [self.csv_reader.file_path, self.vector.data_storage_folder]

    def creat_empty_wagas(self):
        pass

    def calc_out(self, dane):
        layer_1 = self.layer1
        layer_2 = self.layer2
        layer_3 = self.layer3

        dane = self.vector.change_255_to_0_1(self.vector.png_to_array_full_path(dane)).flatten()

        layer_1.use_neuron_input_one_to_one(dane)  # tu wprowadzic dane wejsciowe
        layer_1.calc_neurons_output()

        layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
        layer_2.calc_neurons_output()

        layer_3.use_neuron_input(layer_2.generate_list_of_outputs())
        layer_3.calc_neurons_output()

        return self.intepret_output(layer_3.get_outputs())

    def teach_01(self, dane, CK):
        layer_1 = self.layer1
        layer_2 = self.layer2
        layer_3 = self.layer3

        # faza prop przod

        layer_1.use_neuron_input_one_to_one(dane)  # tu wprowadzic dane wejsciowe
        layer_1.calc_neurons_output()

        layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
        layer_2.calc_neurons_output()

        layer_3.use_neuron_input(layer_2.generate_list_of_outputs())
        layer_3.calc_neurons_output()

        # faza prop tyl
        layer_3.calc_pochodnas()
        layer_3.calc_wspoczynikas_wyjsciowy(CK)  # tu wprowadzic dane wyjsciowe

        layer_2.calc_pochodnas()
        layer_2.calc_wspoczynikas_posredni(layer_3.generate_list_of_wspolczyniki_x_wagi(layer_2.get_neurons()))

        layer_1.calc_pochodnas()
        layer_1.calc_wspoczynikas_posredni(layer_2.generate_list_of_wspolczyniki_x_wagi(layer_1.get_neurons()))

        layer_3.update_wagas_in_layer()
        layer_2.update_wagas_in_layer()
        layer_1.update_wagas_in_layer()

        self.layer1 = layer_1
        self.layer2 = layer_2
        self.layer3 = layer_3

    def save_wagas(self, ck=55):
        self.csv_reader.write_neuron_to_csv("warstwa_1_wejsciowa", self.layer1.generate_wagas_table())
        self.csv_reader.write_neuron_to_csv("warstwa_2_posrednia", self.layer2.generate_wagas_table())
        self.csv_reader.write_neuron_to_csv("warstwa_3_wyjsciowa", self.layer3.generate_wagas_table())

        self.csv_reader.write_neuron_to_csv("warstwa_1_wejsciowa_pop", self.layer1.generate_popwagas_table())
        self.csv_reader.write_neuron_to_csv("warstwa_2_posrednia_pop", self.layer2.generate_popwagas_table())
        self.csv_reader.write_neuron_to_csv("warstwa_3_wyjsciowa_pop", self.layer3.generate_popwagas_table())

        self.csv_reader.write_neuron_to_csv("warstwa_1_wejsciowa_del", self.layer1.generate_deltwag_table())
        self.csv_reader.write_neuron_to_csv("warstwa_2_posrednia_del", self.layer2.generate_deltwag_table())
        self.csv_reader.write_neuron_to_csv("warstwa_3_wyjsciowa_del", self.layer3.generate_deltwag_table())

        helper = self.layer3.get_outputs()
        helper.append(ck)
        self.csv_reader.write_log_to_csv("log_outputs", helper)
        #print("zapis")

    def intepret_output(self, list_of_output):
        alph = list(string.ascii_uppercase)
        for k in range(len(list_of_output)):
            if list_of_output[k] > 0.5:
                list_of_output[k] = 1
            else:
                list_of_output[k] = 0

        helper_string = ""
        for i in range(len(list_of_output)):
            helper_string += str(list_of_output[i])

        output_index = self.bin_to_dec(helper_string)

        return alph[output_index]

    def bin_to_dec(self, n):
        bin_nr = n
        sum = 0
        for i in range(len(bin_nr)):
            sum += int(n[i]) * 2 ** (len(bin_nr) - i - 1)

        return sum

    def dec_to_bin(self, n):
        binary = ""
        result = ""
        x = 0
        if n != 0:
            while n > 0 and x <= 4:
                s1 = str(int(n % 2))
                binary = binary + s1
                n /= 2
                x = x + 1
                result = binary[::-1]
        else:
            result = "00000"
        return result

    def get_ck(self, letter):
        list_to_save = np.zeros(5)
        letter = self.dec_to_bin(letter)
        list_to_save[0] = float(letter[4])
        list_to_save[1] = float(letter[3])
        list_to_save[2] = float(letter[2])
        list_to_save[3] = float(letter[1])
        list_to_save[4] = float(letter[0])

        return [list_to_save[4], list_to_save[3], list_to_save[2], list_to_save[1], list_to_save[0]]

    def get_img_list(self, path_img):
        return self.vector.change_255_to_0_1(self.vector.png_to_array_full_path(path_img)).flatten()

    def get_ek(self, letter, nr, dane):
        return self.vector.change_255_to_0_1(self.vector.png_to_array(dane[letter][nr])).flatten()

    def read_wagas(self):
        self.layer1.set_neuron_wagi(self.csv_reader.read_neuron_to_csv("warstwa_1_wejsciowa"))
        self.layer2.set_neuron_wagi(self.csv_reader.read_neuron_to_csv("warstwa_2_posrednia"))
        self.layer3.set_neuron_wagi(self.csv_reader.read_neuron_to_csv("warstwa_3_wyjsciowa"))

        self.layer1.set_neuron_popwagi(self.csv_reader.read_neuron_to_csv("warstwa_1_wejsciowa_pop"))
        self.layer2.set_neuron_popwagi(self.csv_reader.read_neuron_to_csv("warstwa_2_posrednia_pop"))
        self.layer3.set_neuron_popwagi(self.csv_reader.read_neuron_to_csv("warstwa_3_wyjsciowa_pop"))

        self.layer1.set_neuron_delta(self.csv_reader.read_neuron_to_csv("warstwa_1_wejsciowa_del"))
        self.layer2.set_neuron_delta(self.csv_reader.read_neuron_to_csv("warstwa_2_posrednia_del"))
        self.layer3.set_neuron_delta(self.csv_reader.read_neuron_to_csv("warstwa_3_wyjsciowa_del"))

    def main(self, amount_of_steps, amout_of_test_data):
        il = amout_of_test_data
        dane = self.vector.make_letter_list_static(il)
        try:
            self.read_wagas()
        except FileNotFoundError:
            pass
        list_of_blad = []
        iter = 0
        ilekrokow = amount_of_steps
        blad = 0
        while iter < ilekrokow:
            #print("------")
            blad = 0
            list_of_blad = []
            rand_letter = np.random.randint(26)
            rand_nr = np.random.randint(il)

            CK_list = self.get_ck(rand_letter)
            wejsciowe = self.get_ek(rand_letter, rand_nr, dane)
            self.teach_01(wejsciowe, CK_list)

            helper = self.layer3.get_outputs()
            for k in range(len(self.layer3.get_outputs())):
                blad += math.fabs(CK_list[k] - helper[k])

            print(blad)
            if iter % 20 == 1:
                list_of_blad.append(blad)
                self.save_wagas(rand_letter)
                self.csv_reader.write_log_to_csv("log_bledu", list_of_blad)
            #print(dane[rand_letter][rand_nr])
            #print(iter)
            iter += 1

        self.save_wagas()
        self.csv_reader.write_log_to_csv("log_bledu", list_of_blad)


