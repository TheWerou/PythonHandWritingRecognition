import os

from Gui.MainWindowModel import MainWindowModel
from HandWritingRecognition.main import ZSIproject

if __name__ == "__main__":
    main_file = os.path.dirname(os.path.realpath(__file__))

    program_model = MainWindowModel(main_file)
    program_model.set_path_to_vector(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Obrazki_do_uczenia")
    program_model.set_path_to_save(r"C:\Users\wojte\OneDrive\Pulpit\Programowanie\Python\ZSI\Data\Siec_neuronowa")
    ai = ZSIproject(program_model)
    ai.main(10000, 50)
