import string

import numpy as np

from zsisiec.AInetworkClasses.NeuronLayer import NeuronLayer
from zsisiec.toolfornetwork.VektorEkiCK import VektorEKiCK


class ZSIproject:
    def __init__(self):
        self.layer1 = NeuronLayer()
        self.layer2 = NeuronLayer()
        self.layer3 = NeuronLayer()
        self.layer1.add_neuron(784, 1)
        self.layer2.add_neuron(143, 784)
        self.layer3.add_neuron(24, 143)

        self.vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")

        self.blad_sieci = 0

    def teach_01(self, dane, CK):

        layer_1 = self.layer1
        layer_2 = self.layer2
        layer_3 = self.layer3

        # faza prop przod

        i = np.random.randint(4)
        layer_1.use_neuron_input(dane)  # tu wprowadzic dane wejsciowe
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

        self.layer1 = layer_1
        self.layer2 = layer_2
        self.layer3 = layer_3

    def main(self):
        dane = self.vector.make_letter_list(10)

        iter = 0
        ilekrokow = 50000
        print("dziala ?")
        while iter < ilekrokow:
            rand_letter = np.random.randint(24)
            rand_nr = np.random.randint(10)
            CK_list = []
            for i in range(24):
                if i == rand_letter:
                    CK_list.append(1)
                else:
                    CK_list.append(0)
            wejsciowe = self.vector.change_255_to_0_1(self.vector.png_to_array(dane[rand_letter][rand_nr]))
            self.teach_01(wejsciowe, CK_list)
            if iter % 5000 == 0:
                helper = self.layer3.get_outputs()
                for k in range(len(self.layer3.get_outputs())):
                    self.blad_sieci += CK_list[k] - helper[k]
                print(self.blad_sieci)
            iter += 1


program = ZSIproject()
program.main()
