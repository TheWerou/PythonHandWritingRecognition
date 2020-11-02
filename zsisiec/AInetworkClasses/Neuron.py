import math
import random


class Neuron:
    def __init__(self):
        self.output = 0
        self.derivative = 0
        self.factor = 0
        self.modifcation_vector = 0.2

        self.self_in_value = random.randint(-1, 1)
        self.in_val_table = []

        self.input_table = []

    def calc_output(self):
        sum_of_values = self.self_in_value

        for i in range(len(self.input_table)):
            sum_of_values += self.input_table[i] * self.in_val_table[i]

        output = self.activation_function_calc(sum_of_values)
        self.output = output

    def size_of_input(self):
        return len(self.in_val_table)

    def use_input(self, list_of_input):
        for i in range(len(list_of_input)):
            self.input_table[i] = list_of_input[i]

    def add_input(self, amount_of_input):
        for i in range(amount_of_input):
            self.input_table.append(0)
            self.in_val_table.append(random.randint(-1, 1))

    def activation_function_calc(self, sum_of_values):
        h1 = (1 - math.exp(-sum_of_values))
        h2 = (1 + math.exp(-sum_of_values))
        return h1 / h2

    def calc_derivative(self):
        self.derivative = self.output * (1 - (self.output**2))

    def calc_factor_out(self, ck_output):
        self.factor = (ck_output - self.output) * self.derivative   # ck_output to wartosc oczekiwana

    def calc_factor_beetwen(self, prev_factor):
        self.factor = self.get_factor_mul_in_val_table(prev_factor) * self.derivative

    def update_in_val_table(self, ck_list):
        self.self_in_value += (self.modifcation_vector * self.factor)

        for i in range(len(self.in_val_table)):
            self.in_val_table[i] += (self.modifcation_vector * self.factor * ck_list[i])

    def get_factor_mul_in_val_table(self, prev_factor):
        helper = self.get_self_in_value() * prev_factor[0]
        for i in range(len(self.in_val_table)):
            helper += self.in_val_table[i] * prev_factor[i]

        return helper

    def get_output(self):
        return self.output

    def get_self_in_value(self):
        return self.self_in_value

    def get_derivative(self):
        return self.derivative

    def get_factor(self):
        return self.factor

    def get_modifcation_vector(self):
        return self.modifcation_vector

    def get_in_val_table(self):
        return self.in_val_table

    def set_self_in_value(self, new_value):
        self.self_in_value = new_value

    def set_modifcation_vector(self, new_value):
        self.modifcation_vector = new_value

    def get_input_table(self):
        return self.input_table