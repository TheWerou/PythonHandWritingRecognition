import numpy as np
import matplotlib.pyplot as plt
import math

from zsisiec.BasicLayer import BasicLayer
from zsisiec.AInetworkClasses.NewNeuron import NewNeuron
from zsisiec.AInetworkClasses.NeuronLayer import NeuronLayer


def prop_przod_test():
    basic = BasicLayer()
    neuron_1 = NewNeuron()
    neuron_2 = NewNeuron()
    neuron_3 = NewNeuron()

    neuron_1.add_wejscia(2)
    neuron_2.add_wejscia(2)
    neuron_3.add_wejscia(2)

    helper = basic.basic_main()
    neuron_1.set_wagi([helper[0], helper[1], helper[2]])
    neuron_2.set_wagi([helper[3], helper[4], helper[5]])
    neuron_3.set_wagi([helper[6], helper[7], helper[8]])

    neuron_1.use_wejscia([1, 0])
    neuron_2.use_wejscia([1, 0])

    neuron_1.calc_output()
    neuron_2.calc_output()
    print("U1 i U2 moje - {:.6f} {:.6f}".format(neuron_1.get_output(), neuron_2.get_output()))
    neuron_3.use_wejscia([neuron_1.get_output(), neuron_2.get_output()])
    print("n3 wejscie {}".format(neuron_3.wejscia))
    print('output {:.6f}'.format(neuron_3.calc_output()))


def upgraded_prop_przod():
    basic = BasicLayer()
    helper = basic.basic_main()

    layer_1 = NeuronLayer()
    layer_2 = NeuronLayer()

    layer_1.add_neuron(2, 2)
    layer_2.add_neuron(1, 2)

    layer_1.set_neuron_wagi([[helper[0], helper[1], helper[2]], [helper[3], helper[4], helper[5]]])
    layer_2.set_neuron_wagi([[helper[6], helper[7], helper[8]]])

    layer_1.use_neuron_input([1, 1])
    layer_1.calc_neurons_output()

    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.generate_list_of_outputs())


def prop_tyl_test():
    # faza przygotowania
    kroki = 50000
    iter = 0
    pom = 0
    layer_1 = NeuronLayer()
    layer_2 = NeuronLayer()

    layer_1.add_neuron(2, 2)
    layer_2.add_neuron(1, 2)

    A = np.zeros((4, 4))
    A[0, 0] = 0.1
    A[0, 1] = 0.2
    A[0, 2] = 1

    A[1, 0] = 0.2
    A[1, 1] = 0.95
    A[1, 2] = 0

    A[2, 0] = 0.98
    A[2, 1] = 0.22
    A[2, 2] = 0

    A[3, 0] = 0.97
    A[3, 1] = 0.98
    A[3, 2] = 1
    # faza prop przod

    while iter < kroki:
        i = np.random.randint(4)
        layer_1.use_neuron_input([A[i, 0], A[i, 1]])    # tu wprowadzic dane wejsciowe
        layer_1.calc_neurons_output()

        layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
        layer_2.calc_neurons_output()

        if i == 3:
            pom += 1

        if iter % 5000 == 0:
            print("-----------------------------------------------------")
            print("dane wejsciowe - " + str([A[i, 0], A[i, 1]]))
            print("Ck - " + str([A[i, 2]]))
            print("layer1 outputs - " + str(layer_1.get_outputs()))
            print("layer2 outputs - " + str(layer_2.get_outputs()))

        # faza prop tyl
        layer_2.calc_pochodnas()
        layer_2.calc_wspoczynikas_wyjsciowy([A[i, 2]]) # tu wprowadzic dane wejsciowe

        layer_1.calc_pochodnas()
        layer_1.calc_wspoczynikas_posredni(layer_2.generate_list_of_wspolczyniki_x_wagi(layer_1.get_amount_of_neurons()))

        layer_2.update_wagas_in_layer()
        layer_1.update_wagas_in_layer()
        iter += 1

    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    layer_1.use_neuron_input([1, 0])  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()
    print("input - 1 0")
    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.get_outputs())

    layer_1.use_neuron_input([1, 1])  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()
    print("input - 1 1")
    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.get_outputs())

    layer_1.use_neuron_input([0, 0])  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()
    print("input - 0 0")
    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.get_outputs())

    layer_1.use_neuron_input([0, 1])  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()
    print("input - 0 1")
    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.get_outputs())
    print(pom)


def big_input_test():
    layer1 = NeuronLayer()
    layer2 = NeuronLayer()
    layer3 = NeuronLayer()
    layer1.add_neuron(784, 1)
    layer2.add_neuron(143, 784)
    layer3.add_neuron(24, 143)

    layer1.use_neuron_input([1, 1])
    layer1.calc_neurons_output()

    layer2.use_neuron_input(layer1.generate_list_of_outputs())
    layer2.calc_neurons_output()
    print(layer2.generate_list_of_outputs())

#prop_przod_test()
#upgraded_prop_przod()
prop_tyl_test()
