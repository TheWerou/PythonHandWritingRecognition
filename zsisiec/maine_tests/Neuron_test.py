from math import fabs
from random import random

from zsisiec.AInetworkClasses.Neuron import Neuron


class Pokaz:
    def __init__(self):
        self.n1 = Neuron()
        self.n2 = Neuron()
        self.n3 = Neuron()
        self.in_vect = [[0, 1], [1, 1], [0, 0], [0, 0],
                        [1, 1], [1, 1], [0, 1], [1, 0]]
        self.ck_vect = [0, 1, 0, 0, 1, 1, 0, 0]

    def prep_neurons(self):
        self.n1.add_input(1)
        self.n2.add_input(1)
        self.n3.add_input(2)

    def uczenie_testowe(self):
        self.prep_neurons()
        iter = 0
        bld = 1
        while iter < 10000:
            for i in range(len(self.in_vect)):
                test_vector = self.in_vect[i]
                test_out = self.ck_vect[i]
                self.prop_przod(test_vector, test_out)
                self.prop_tyl(test_out, test_vector)
                bld = fabs(test_out - self.n3.get_output())

                if iter % 1000 == 0:
                    print("-----------------------------------------------")
                    print(iter)
                    print(test_vector)
                    print("ck - " + str(test_out))
                    print("out - " + str(self.n3.get_output()))
                    print("Bład - " + str(bld))
            iter += 1

    def prop_przod(self, input, ck):    # propgacja w przód
        input_here = input

        self.n1.use_input([input_here[0]])
        self.n1.calc_output()

        self.n2.use_input([input_here[1]])
        self.n2.calc_output()

        self.n3.use_input([self.n1.get_output(), self.n2.get_output()])

        self.n3.calc_output()

    def prop_tyl(self, ck, ek):
        self.n3.calc_derivative()
        self.n3.calc_factor_out(ck)

        self.n2.calc_derivative()
        self.n2.calc_factor_beetwen([self.n3.get_factor()])

        self.n1.calc_derivative()
        self.n1.calc_factor_beetwen([self.n3.get_factor()])

        self.n3.update_in_val_table([self.n1.get_output(), self.n2.get_output()])
        self.n2.update_in_val_table([ek[0]])
        self.n1.update_in_val_table([ek[1]])


cos = Pokaz()
cos.uczenie_testowe()
