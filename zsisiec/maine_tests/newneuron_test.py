import numpy as np
import matplotlib.pyplot as plt
import math


from BasicLayer import BasicLayer
from AInetworkClasses.NewNeuron import NewNeuron
from AInetworkClasses.NeuronLayer import NeuronLayer
from toolfornetwork.ReadCSV import ReadCSV
from toolfornetwork.VektorEkiCK import VektorEKiCK


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
            print("------------------Bład-------------------------------")
            print(A[i, 2] - layer_2.get_outputs())
            print("-----------------------------------------------------")
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


def prop_tyl_test_one_to_one():
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
    A[0, 2] = 0

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
        layer_1.use_neuron_input_one_to_one([A[i, 0], A[i, 1]])    # tu wprowadzic dane wejsciowe
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
            print("------------------Bład-------------------------------")
            print(A[i, 2] - layer_2.get_outputs())
            print("-----------------------------------------------------")
        # faza prop tyl
        layer_2.calc_pochodnas()
        layer_2.calc_wspoczynikas_wyjsciowy([A[i, 2]]) # tu wprowadzic dane wejsciowe

        layer_1.calc_pochodnas()
        layer_1.calc_wspoczynikas_posredni(layer_2.generate_list_of_wspolczyniki_x_wagi(layer_1.get_neurons()))

        layer_2.update_wagas_in_layer()
        layer_1.update_wagas_in_layer()
        iter += 1

    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    layer_1.use_neuron_input_one_to_one([1, 0])  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()
    print("input - 1 0")
    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.get_outputs())

    layer_1.use_neuron_input_one_to_one([1, 1])  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()
    print("input - 1 1")
    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.get_outputs())

    layer_1.use_neuron_input_one_to_one([0, 0])  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()
    print("input - 0 0")
    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()
    print(layer_2.get_outputs())

    layer_1.use_neuron_input_one_to_one([0, 1])  # tu wprowadzic dane wejsciowe
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
    layer3.add_neuron(26, 143)

    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    helper = vector.png_to_array(img_letter)
    input = vector.change_255_to_0_1(helper).flatten()
    print(input)
    layer1.use_neuron_input_one_to_one(input)
    layer1.calc_neurons_output()
    print(layer1.get_neurons()[0].get_wejscia())

    layer2.use_neuron_input(layer1.generate_list_of_outputs())
    layer2.calc_neurons_output()

    layer3.use_neuron_input(layer2.generate_list_of_outputs())
    layer3.calc_neurons_output()
    print(layer3.generate_list_of_outputs())


def multy_layer_test():
    A = np.zeros((8, 6))
    A[0, 0] = 1
    A[0, 1] = 1
    A[0, 2] = 1
    A[0, 3] = 1
    A[0, 4] = 1
    A[0, 5] = 1

    A[1, 0] = 0
    A[1, 1] = 0
    A[1, 2] = 1
    A[1, 3] = 1
    A[1, 4] = 0
    A[1, 5] = 1

    A[2, 0] = 1
    A[2, 1] = 1
    A[2, 2] = 0
    A[2, 3] = 0
    A[2, 4] = 1
    A[2, 5] = 0

    A[3, 0] = 0
    A[3, 1] = 0
    A[3, 2] = 0
    A[3, 3] = 0
    A[3, 4] = 0
    A[3, 5] = 0

    A[4, 0] = 1
    A[4, 1] = 0
    A[4, 2] = 0
    A[4, 3] = 1
    A[4, 4] = 0
    A[4, 5] = 0

    A[5, 0] = 0
    A[5, 1] = 1
    A[5, 2] = 1
    A[5, 3] = 0
    A[5, 4] = 0
    A[5, 5] = 0

    A[6, 0] = 0
    A[6, 1] = 1
    A[6, 2] = 0
    A[6, 3] = 0
    A[6, 4] = 0
    A[6, 5] = 0

    A[7, 0] = 0
    A[7, 1] = 0
    A[7, 2] = 1
    A[7, 3] = 0
    A[7, 4] = 0
    A[7, 5] = 0

    layer1 = NeuronLayer()
    layer2 = NeuronLayer()
    layer3 = NeuronLayer()
    layer1.add_neuron(4, 1)
    layer2.add_neuron(3, 4)
    layer3.add_neuron(2, 3)

    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")

    iter = 0
    kroki = 50000

    while iter < kroki:
        i = np.random.randint(8)

        layer1.use_neuron_input_one_to_one([A[i, 0], A[i, 1], A[i, 2], A[i, 3]])
        layer1.calc_neurons_output()

        layer2.use_neuron_input(layer1.generate_list_of_outputs())
        layer2.calc_neurons_output()

        layer3.use_neuron_input(layer2.generate_list_of_outputs())
        layer3.calc_neurons_output()

        layer3.calc_pochodnas()
        layer3.calc_wspoczynikas_wyjsciowy([A[i, 4], A[i, 5]])

        layer2.calc_pochodnas()
        layer2.calc_wspoczynikas_posredni(layer3.generate_list_of_wspolczyniki_x_wagi(layer2.get_neurons()))  # tu wprowadzic dane wejsciowe

        layer1.calc_pochodnas()
        layer1.calc_wspoczynikas_posredni(layer2.generate_list_of_wspolczyniki_x_wagi(layer1.get_neurons()))

        layer3.update_wagas_in_layer()
        layer2.update_wagas_in_layer()
        layer1.update_wagas_in_layer()

        if iter % 5000 == 0:
            list_of_errr = [A[i, 4], A[i, 5]]
            blad = 0
            helper = layer3.get_outputs()
            for k in range(len(layer3.get_outputs())):
                blad += math.fabs(list_of_errr[k] - helper[k])
            print(blad)

            csv_reader.write_neuron_to_csv("warstwa_1_wejsciowa_test", layer1.generate_wagas_table())
            csv_reader.write_neuron_to_csv("warstwa_2_posrednia_test", layer2.generate_wagas_table())
            csv_reader.write_neuron_to_csv("warstwa_3_wyjsciowa_test", layer3.generate_wagas_table())
            csv_reader.write_log_to_csv("log_outputs_test", [blad])
        iter += 1

    for k in range(8):
        layer1.use_neuron_input_one_to_one([A[k, 0], A[k, 1], A[k, 2], A[k, 3]])
        layer1.calc_neurons_output()

        layer2.use_neuron_input(layer1.generate_list_of_outputs())
        layer2.calc_neurons_output()

        layer3.use_neuron_input(layer2.generate_list_of_outputs())
        layer3.calc_neurons_output()
        print(layer3.get_outputs())

    print("powino byc 11 01 10 00 00 00 00 00")


def multy_layer_test_01():
    A = np.zeros((8, 6))
    A[0, 0] = 1
    A[0, 1] = 1
    A[0, 2] = 1
    A[0, 3] = 1
    A[0, 4] = 1
    A[0, 5] = 1

    A[1, 0] = 0
    A[1, 1] = 0
    A[1, 2] = 1
    A[1, 3] = 1
    A[1, 4] = 0
    A[1, 5] = 1

    A[2, 0] = 1
    A[2, 1] = 1
    A[2, 2] = 0
    A[2, 3] = 0
    A[2, 4] = 1
    A[2, 5] = 0

    A[3, 0] = 0
    A[3, 1] = 0
    A[3, 2] = 0
    A[3, 3] = 0
    A[3, 4] = 0
    A[3, 5] = 0

    A[4, 0] = 1
    A[4, 1] = 0
    A[4, 2] = 0
    A[4, 3] = 1
    A[4, 4] = 0
    A[4, 5] = 0

    A[5, 0] = 0
    A[5, 1] = 1
    A[5, 2] = 1
    A[5, 3] = 0
    A[5, 4] = 0
    A[5, 5] = 0

    A[6, 0] = 0
    A[6, 1] = 1
    A[6, 2] = 0
    A[6, 3] = 0
    A[6, 4] = 0
    A[6, 5] = 0

    A[7, 0] = 0
    A[7, 1] = 0
    A[7, 2] = 1
    A[7, 3] = 0
    A[7, 4] = 0
    A[7, 5] = 0

    layer1 = NeuronLayer()
    layer2 = NeuronLayer()
    layer3 = NeuronLayer()
    layer1.add_neuron(4, 1)
    layer2.add_neuron(3, 4)
    layer3.add_neuron(2, 3)
    warstwy = [layer1, layer2, layer3]

    iter = 0
    kroki = 50000

    while iter < kroki:
        i = np.random.randint(8)
        warstwy = teach_01([A[i, 0], A[i, 1], A[i, 2], A[i, 3]], [A[i, 4], A[i, 5]], warstwy)
        if iter % 5000 == 0:
            list_of_errr = [A[i, 4], A[i, 5]]
            blad = 0
            helper = layer3.get_outputs()
            for k in range(len(layer3.get_outputs())):
                blad += math.fabs(list_of_errr[k] - helper[k])
            print(blad)
        iter += 1
    layer1 = warstwy[0]
    layer2 = warstwy[1]
    layer3 = warstwy[2]

    for k in range(8):
        layer1.use_neuron_input_one_to_one([A[k, 0], A[k, 1], A[k, 2], A[k, 3]])
        layer1.calc_neurons_output()

        layer2.use_neuron_input(layer1.generate_list_of_outputs())
        layer2.calc_neurons_output()

        layer3.use_neuron_input(layer2.generate_list_of_outputs())
        layer3.calc_neurons_output()
        print(layer3.get_outputs())

    print("powino byc 11 01 10 00 00 00 00 00")


def use_neuron_input_one_to_one_test():
    A = np.zeros((8, 6))
    A[0, 0] = 1
    A[0, 1] = 1
    A[0, 2] = 1
    A[0, 3] = 1
    A[0, 4] = 1
    A[0, 5] = 1

    A[1, 0] = 0
    A[1, 1] = 0
    A[1, 2] = 1
    A[1, 3] = 1
    A[1, 4] = 0
    A[1, 5] = 1

    A[2, 0] = 1
    A[2, 1] = 1
    A[2, 2] = 0
    A[2, 3] = 0
    A[2, 4] = 1
    A[2, 5] = 0

    A[3, 0] = 0
    A[3, 1] = 0
    A[3, 2] = 0
    A[3, 3] = 0
    A[3, 4] = 0
    A[3, 5] = 0

    A[4, 0] = 1
    A[4, 1] = 0
    A[4, 2] = 0
    A[4, 3] = 1
    A[4, 4] = 0
    A[4, 5] = 0

    A[5, 0] = 0
    A[5, 1] = 1
    A[5, 2] = 1
    A[5, 3] = 0
    A[5, 4] = 0
    A[5, 5] = 0

    A[6, 0] = 0
    A[6, 1] = 1
    A[6, 2] = 0
    A[6, 3] = 0
    A[6, 4] = 0
    A[6, 5] = 0

    A[7, 0] = 0
    A[7, 1] = 0
    A[7, 2] = 1
    A[7, 3] = 0
    A[7, 4] = 0
    A[7, 5] = 0

    layer1 = NeuronLayer()
    layer1.add_neuron(4, 1)
    layer1.use_neuron_input_one_to_one([A[1, 0], A[1, 1], A[1, 2], A[1, 3]])
    print(layer1.get_neurons()[0].get_wejscia())
    print(layer1.get_neurons()[1].get_wejscia())
    print(layer1.get_neurons()[2].get_wejscia())
    print(layer1.get_neurons()[3].get_wejscia())


def small_tests():
    rand_letter = np.random.randint(26)
    CK_list = []
    for i in range(26):
        if i == rand_letter:
            CK_list.append(1)
        else:
            CK_list.append(0)
    print(CK_list[rand_letter])
    print(CK_list)


def teach_01(dane, CK, warstwy):
    layer_1 = warstwy[0]
    layer_2 = warstwy[1]
    layer_3 = warstwy[2]

    # faza prop przod

    layer_1.use_neuron_input_one_to_one(dane)  # tu wprowadzic dane wejsciowe
    layer_1.calc_neurons_output()

    layer_2.use_neuron_input(layer_1.generate_list_of_outputs())
    #print(layer_1.generate_list_of_outputs())
    layer_2.calc_neurons_output()

    layer_3.use_neuron_input(layer_2.generate_list_of_outputs())
    #print(layer_2.generate_list_of_outputs())
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

    return [layer_1, layer_2, layer_3]


def test_ck_and_dane():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    dane = vector.make_letter_list_static(2)
    rand_letter = 1
    CK_list = []
    for i in range(26):
        if i == rand_letter:
            CK_list.append(1)
        else:
            CK_list.append(0)
    print(dane[rand_letter][0])
    print(CK_list)


def dec_to_bin(n):
    binary = ""
    result = ""
    x = 0
    if n != 0:
        while n > 0 and x<=4:
            s1 = str(int(n%2))
            binary = binary + s1
            n /= 2
            x = x + 1
            result = binary[::-1]
    else:
        result = "00000"
    return result


def get_ck(letter):
    list_to_save = np.zeros(5)
    letter = dec_to_bin(letter)
    print(letter)
    list_to_save[0] = float(letter[4])
    list_to_save[1] = float(letter[3])
    list_to_save[2] = float(letter[2])
    list_to_save[3] = float(letter[1])
    list_to_save[4] = float(letter[0])

    return [list_to_save[4], list_to_save[3], list_to_save[2], list_to_save[1], list_to_save[0]]


def test_get_ck(nr):
    print(get_ck(nr))


def get_ek(vector, letter, nr, dane):
    return vector.change_255_to_0_1(vector.png_to_array(dane[letter][nr])).flatten()


def general_input_test():
    layer1 = NeuronLayer()
    layer2 = NeuronLayer()
    layer3 = NeuronLayer()
    layer1.add_neuron(784, 1)
    layer2.add_neuron(63, 784)
    layer3.add_neuron(5, 63)

    warstwy = [layer1, layer2, layer3]

    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")

    dane = vector.make_letter_list_static(1)

    rand_letter = np.random.randint(26)
    rand_nr = np.random.randint(1)
    CK_list = get_ck(rand_letter)
    wejsciowe = get_ek(vector, rand_letter, rand_nr, dane)
    warstwy = teach_01(wejsciowe, CK_list, warstwy)



#prop_przod_test()
#upgraded_prop_przod()
#prop_tyl_test()
prop_tyl_test_one_to_one()
#big_input_test()
#multy_layer_test()
#use_neuron_input_one_to_one_test()
#small_tests()
#multy_layer_test_01()
#test_ck_and_dane()
#general_input_test()
#test_get_ck(0)
