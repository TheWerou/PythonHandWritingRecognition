import math
import random


class Neuron:
    def __init__(self):
        self.output = 0
        self.derivative = 0
        self.factor = 0
        self.modifcation_vector = 0.1

        self.self_in_value = 0
        self.in_val_table = []

        self.input_table = []
        self.wanted_value = 0

    def calc_output(self):
        sum_of_values = self.self_in_value
        for i in range(len(self.input_table)):
            sum_of_values += self.input_table[i] * self.in_val_table[i]

        output = self.activation_function_calc(sum_of_values)
        self.output = output

    def add_input(self, list_to_add):
        for i in range(len(list_to_add)):
            self.input_table.append(list_to_add[i])
            self.in_val_table.append(random.random(1, 8))

    def activation_function_calc(self, sum_of_values):
        return 1 / (1 + math.exp(-sum_of_values))

    def derivative_calc(self):
        self.derivative = self.output * (1 - self.output)

    def calc_factor_out(self, ck_output):
        self.factor = (ck_output - self.output) * self.derivative   # ck_output to wartosc oczekiwana

    def calc_factor_beetwen(self, sum_prev_factor_ml_val):
        self.factor = sum_prev_factor_ml_val * self.derivative

    def update_in_val_table(self):
        self.self_in_value += self.modifcation_vector * self.factor * self.output

        for i in range(len(self.in_val_table)):
            self.in_val_table[i] += self.modifcation_vector * self.factor * self.output

    def get_factor_mul_in_val_table(self, nr_of_neuron):
        return self.in_val_table[nr_of_neuron] * self.factor

    def get_output(self):
        return self.output

    def get_derivative(self):
        return self.derivative

    def get_factor(self):
        return self.factor

    def get_modifcation_vector(self):
        return self.modifcation_vector

    def set_self_in_value(self, new_value):
        self.self_in_value = new_value

    def set_modifcation_vector(self, new_value):
        self.modifcation_vector = new_value
