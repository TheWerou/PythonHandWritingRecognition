from zsisiec.AInetworkClasses.NeuronLayer import NeuronLayer
from zsisiec.toolfornetwork.ReadCSV import ReadCSV
from zsisiec.toolfornetwork.VektorEkiCK import VektorEKiCK


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
    helper = vector.make_letter_list(10)
    print(helper)


def test_array_255_to_0_1():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    img_array = vector.png_to_array(img_letter)
    print(type(img_array))
    print(vector.change_255_to_0_1(img_array))


def test_2d_to_1d_array():
    vector = VektorEKiCK(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    img_letter = vector.preper_ek_ck("A")
    img_array = vector.png_to_array(img_letter)
    helper = vector.change_255_to_0_1(img_array).flatten()
    print(helper)


def layer_to_csv():
    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    layer1 = NeuronLayer()
    layer1.add_neuron(784, 1)
    csv_reader.write_neuron_to_csv("test_neuron_layer", layer1.generate_wagas_table())


def csv_to_layer():
    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    print(len(csv_reader.read_neuron_to_csv("warstwa_1_wejsciowa")))
    print(csv_reader.read_neuron_to_csv("warstwa_1_wejsciowa"))


def test_append_data_to_csv():
    csv_reader = ReadCSV(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    helper = [1, 2]
    csv_reader.write_log_to_csv("log_bledu", helper)


#dopisac zmiane z sieci 2d na 1d
#test_get_ck()
#test_get_img_form_letter()
#test_png_to_array()
#test_make_letter_list()
#test_array_255_to_0_1()
#test_2d_to_1d_array()
#layer_to_csv()
#csv_to_layer()
test_append_data_to_csv()