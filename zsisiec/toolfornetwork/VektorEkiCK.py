
from PIL import Image
from numpy import asarray
import ntpath
import random
import os
import string
# pobierz folder z zdj
# wybierz ilosc branych zdj
# wybierz przedzial (ilosc zdj jaka jest w puli, np od 0 dp 100 zdj)
# otrzymaj EK i CK


class VektorEKiCK:
    def __init__(self, data_storage_folder, amount_of_data_in_vector=1, data_interval=100):
        self.data_storage_folder = data_storage_folder
        self.amount_of_data_in_vector = amount_of_data_in_vector
        self.data_interval = data_interval        # counted from 0

    def make_letter_list(self, amount_of_img_in_list):
        output_list = []

        for i in string.ascii_uppercase:
            helper = []
            for j in range(amount_of_img_in_list):
                helper.append(self.preper_ek_ck(i))
            output_list.append(helper)
        return output_list

    def preper_ek_ck(self, letter):
        numberr = random.randrange(0, self.data_interval, 1)
        string_to_img = letter.upper() + "-" + str(numberr)
        path_to_file = letter.upper() + '\\' + string_to_img
        return path_to_file

    def png_to_array(self, img_to_open):
        path = self.data_storage_folder + "\\" + img_to_open + ".png"
        image = Image.open(os.path.abspath(path)) # tu sypie bład
        data = asarray(image)
        return data

    def ck_form_folder_name(self, folder_with_img):
        helper = self.data_storage_folder + "\\" + folder_with_img
        return ntpath.basename(helper)

    def set_data_storage_folder(self, data_storage_folder):
        self.data_storage_folder = data_storage_folder

    def set_amount_of_data_in_vector(self, amount_of_data_in_vector):
        self.amount_of_data_in_vector = amount_of_data_in_vector

    def get_amount_of_data_in_vector(self):
        return self.amount_of_data_in_vector

    def get_data_storage_folder(self):
        return self.data_storage_folder
