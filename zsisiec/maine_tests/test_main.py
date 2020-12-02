from zsisiec.AInetworkClasses.NeuronLayer import NeuronLayer
from zsisiec.toolfornetwork.ReadCSV import ReadCSV
from zsisiec.toolfornetwork.VektorEkiCK import VektorEKiCK
import numpy as np

def test_get_ck():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    print(vector.ck_form_folder_name("A"))


def test_get_img_form_letter():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    print(vector.preper_ek_ck("A"))


def test_png_to_array():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    print(vector.png_to_array(img_letter))


def test_make_letter_list():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    helper = vector.make_letter_list(1)
    print(helper)


def test_make_letter_list_static():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    helper = vector.make_letter_list_static(1)
    print(helper)


def test_array_255_to_0_1():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    img_array = vector.png_to_array(img_letter)
    float_array = vector.change_255_to_0_1(img_array)
    float_array = float_array.flatten()
    print(float_array)
    print(type(float_array[0]))


def test_2d_to_1d_array():
    layer1 = NeuronLayer()
    layer1.add_neuron(784, 1)
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    img_array = vector.png_to_array(img_letter)
    helper = vector.change_255_to_0_1(img_array).flatten()
    print(helper)
    layer1.use_neuron_input_one_to_one(helper)
    print(layer1.generate_list_of_inputs())


def layer_to_csv():
    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    img_array = vector.png_to_array(img_letter)
    helper = vector.change_255_to_0_1(img_array).flatten()
    layer1 = NeuronLayer()
    layer1.add_neuron(784, 1)
    layer1.use_neuron_input_one_to_one(helper)
    csv_reader.write_neuron_to_csv("test_neuron_layer", layer1.generate_list_of_inputs())


def csv_to_layer():
    layer1 = NeuronLayer()
    layer1.add_neuron(784, 1)
    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    print(len(csv_reader.read_neuron_to_csv("test_neuron_layer")))
    print("--------------------------------------------------")
    print(csv_reader.read_neuron_to_csv("test_neuron_layer"))
    layer1.set_neuron_wagi(csv_reader.read_neuron_to_csv("test_neuron_layer"))
    print("--------------------------------------------------")
    print(layer1.generate_wagas_table())


def test_append_data_to_csv():
    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    helper = [1, 2]
    csv_reader.write_log_to_csv("log_bledu", helper)


def layer_to_csv_to():
    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    img_array = vector.png_to_array(img_letter)
    helper = vector.change_255_to_0_1(img_array).flatten()
    csv_reader.write_neuron_to_csv("test_data", [helper])
    layer1 = NeuronLayer()
    layer1.add_neuron(784, 1)
    layer1.use_neuron_input_one_to_one(helper)
    csv_reader.write_neuron_to_csv("test_neuron_layer", layer1.generate_list_of_inputs())


def letter_to_binary():
    list_to_save = np.zeros(5)
    letter = bin(1)

    iterr = 0
    for i in range(len(letter)):
        if i > 1:
            list_to_save[iterr] = int(letter[i])
            iterr += 1
    print([list_to_save[0], list_to_save[1], list_to_save[2], list_to_save[3], list_to_save[4]])

#dopisac zmiane z sieci 2d na 1d
#test_get_ck()
#test_get_img_form_letter()
#test_png_to_array()
#test_make_letter_list()
#test_make_letter_list_static()
#test_array_255_to_0_1()
#test_2d_to_1d_array()
#layer_to_csv()
#csv_to_layer()
#test_append_data_to_csv()
#layer_to_csv_to()
letter_to_binary()
