

class MainWindowModel:
    def __init__(self, main_file):
        self.main_file = main_file
        self.path_to_save = "Not set"
        self.path_to_save_for_rec = self.main_file + "\\BaseData\\1"
        self.path_to_vector = "Not set"
        self.path_to_uploaded_png = self.main_file + "\\Static\\A-0.png"
        self.amount_of_loops = 500
        self.sum_of_err = 0
        self.avrage_of_error = 0

    def set_path_to_save_for_rec(self, path_to_save_for_rec ):
        self.path_to_save_for_rec = path_to_save_for_rec

    def set_amount_of_loops(self, amount_of_loops):
        self.amount_of_loops = amount_of_loops

    def set_sum_of_error(self, sum_of_error):
        self.sum_of_err = sum_of_error

    def set_avrage_of_errorr(self, avrage_of_error):
        self.avrage_of_error = avrage_of_error

    def set_path_to_save(self, path_to_self):
        self.path_to_save = path_to_self

    def set_path_to_vector(self, path_to_vector):
        self.path_to_vector = path_to_vector

    def set_path_to_uploaded_png(self, path_to_uploaded_png):
        self.path_to_uploaded_png = path_to_uploaded_png

    def get_path_to_uploaded_png(self):
        return self.path_to_uploaded_png

    def get_path_to_save_for_rec(self):
        return self.path_to_save_for_rec

    def get_path_to_save(self):
        return self.path_to_save

    def get_path_to_vector(self):
        return self.path_to_vector

    def get_amount_of_loops(self):
        return self.amount_of_loops

    def get_sum_of_error(self):
        return self.sum_of_err

    def get_avrage_of_errorr(self):
        return self.avrage_of_error

    def __get_main_file(self):
        return self.main_file
