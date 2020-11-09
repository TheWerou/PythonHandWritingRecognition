import string

import numpy as np
from numba import jit
import math

from zsisiec.AInetworkClasses.NeuronLayer import NeuronLayer
from zsisiec.toolfornetwork.ReadCSV import ReadCSV
from zsisiec.toolfornetwork.VektorEkiCK import VektorEKiCK


class ZSIproject:
    def __init__(self):
        self.layer1 = NeuronLayer()
        self.layer2 = NeuronLayer()
        self.layer3 = NeuronLayer()
        self.layer1.add_neuron(784, 1)
        self.layer2.add_neuron(143, 784)
        self.layer3.add_neuron(24, 143)
        self.csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
        self.vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")

        self.blad_sieci = 0

    def teach_01(self, dane, CK, list_of_layers):
        layer_1 = list_of_layers[0]
        layer_2 = list_of_layers[1]
        layer_3 = list_of_layers[2]

        # faza prop przod

        i = np.random.randint(4)
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
        layer_2.calc_wspoczynikas_posredni(layer_3.generate_list_of_wspolczyniki_x_wagi(layer_2.get_amount_of_neurons()))

        layer_1.calc_pochodnas()
        layer_1.calc_wspoczynikas_posredni(layer_2.generate_list_of_wspolczyniki_x_wagi(layer_1.get_amount_of_neurons()))

        layer_3.update_wagas_in_layer()
        layer_2.update_wagas_in_layer()
        layer_1.update_wagas_in_layer()

        return [self.layer1, self.layer2, self.layer3]

    def save_wagas(self):
        self.csv_reader.write_neuron_to_csv("warstwa_1_wejsciowa", self.layer1.generate_wagas_table())
        self.csv_reader.write_neuron_to_csv("warstwa_2_posrednia", self.layer2.generate_wagas_table())
        self.csv_reader.write_neuron_to_csv("warstwa_3_wyjsciowa", self.layer3.generate_wagas_table())

    def read_wagas(self):
        self.layer1.set_neuron_wagi(self.csv_reader.read_neuron_to_csv("warstwa_1_wejsciowa"))
        self.layer2.set_neuron_wagi(self.csv_reader.read_neuron_to_csv("warstwa_2_posrednia"))
        self.layer3.set_neuron_wagi(self.csv_reader.read_neuron_to_csv("warstwa_3_wyjsciowa"))

    def main(self):
        dane = self.vector.make_letter_list(10)
        self.read_wagas()
        list_of_blad = []
        iter = 0
        ilekrokow = 500
        blad = 0
        while iter < ilekrokow:
            rand_letter = np.random.randint(24)
            rand_nr = np.random.randint(10)
            CK_list = []
            for i in range(24):
                if i == rand_letter:
                    CK_list.append(1)
                else:
                    CK_list.append(0)
            wejsciowe = self.vector.change_255_to_0_1(self.vector.png_to_array(dane[rand_letter][rand_nr])).flatten()
            helper = self.teach_01(wejsciowe, CK_list, [self.layer1, self.layer2, self.layer3])
            self.layer1 = helper[0]
            self.layer2 = helper[1]
            self.layer3 = helper[2]
            helper = self.layer3.get_outputs()
            if iter % 5 == 0:
                for k in range(len(self.layer3.get_outputs())):
                    blad += CK_list[k] - helper[k]
                list_of_blad.append(math.fabs(blad))
                print(math.fabs(blad))
                self.save_wagas()
                self.csv_reader.write_log_to_csv("log_bledu", list_of_blad)
            print(iter)
            iter += 1

        self.save_wagas()
        self.csv_reader.write_log_to_csv("log_bledu", list_of_blad)


program = ZSIproject()
program.main()
