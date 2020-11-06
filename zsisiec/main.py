import numpy as np

from zsisiec.AInetworkClasses.NeuronLayer import NeuronLayer


class ZSIproject:
    def __init__(self):
        self.layer1 = NeuronLayer()
        self.layer2 = NeuronLayer()
        self.layer3 = NeuronLayer()

    def teach_01(self, ilisckrokow):
        kroki = ilisckrokow
        iter = 0
        pom = 0
        layer_1 = self.layer1
        layer_2 = self.layer2
        layer_3 = self.layer3

        layer_1.add_neuron(2, 2)
        layer_2.add_neuron(1, 2)
        layer_3.add_neuron(1, 2)

        # faza prop przod
        while iter < kroki:
            i = np.random.randint(4)
            layer_1.use_neuron_input()  # tu wprowadzic dane wejsciowe
            layer_1.calc_neurons_output()

            layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
            layer_2.calc_neurons_output()

            # faza prop tyl
            layer_2.calc_pochodnas()
            layer_2.calc_wspoczynikas_wyjsciowy()  # tu wprowadzic dane wyjsciowe

            layer_1.calc_pochodnas()
            layer_1.calc_wspoczynikas_posredni(
                layer_2.generate_list_of_wspolczyniki_x_wagi(layer_1.get_amount_of_neurons()))

            layer_2.update_wagas_in_layer()
            layer_1.update_wagas_in_layer()
            iter += 1