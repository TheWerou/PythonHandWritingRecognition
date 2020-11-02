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


#test_get_ck()
#test_get_img_form_letter()
#test_png_to_array()
test_make_letter_list()
