import numpy as np
import matplotlib.pyplot as plt
import math
from numba import jit


class NewNeuron:
    def __init__(self):
        self.suma = 0
        self.wyjscie = 0
        self.pochodna = 0
        self.wspolczynik = 0
        self.wagi = np.zeros(1)
        self.popwagi = np.zeros(1)
        self.deltawag = np.zeros(1)
        self.wejscia = np.zeros(1)
        self.ro = 0.01

    #   ---------------------------------------------------- Propagacja w przód
    def add_wejscia(self, amount):
        self.wejscia = np.zeros(amount + 1, dtype=float)
        self.wagi = np.zeros(amount + 1, dtype=float)
        self.popwagi = np.zeros(amount + 1, dtype=float)
        self.deltawag = np.zeros(amount + 1, dtype=float)
        self.wejscia[0] = 1

        for i in range(len(self.wagi)):
            self.wagi[i] = np.random.rand() - 0.5

    def use_wejscia(self, list_of_input):
        a = 0
        while a < len(list_of_input):
            self.wejscia[a + 1] = list_of_input[a]
            a += 1

    def use_wejscie_one(self, list_of_input):   # jest ok
        self.wejscia[1] = list_of_input

    def set_wagi(self, wagi):
        i = 0
        while i < len(wagi):
            self.wagi[i] = wagi[i]
            i += 1

    def set_popwagi(self, popwagi):
        i = 0
        while i < len(popwagi):
            self.popwagi[i] = popwagi[i]
            i += 1

    def set_deltawag(self, deltawag):
        i = 0
        while i < len(deltawag):
            self.deltawag[i] = deltawag[i]
            i += 1

    def calc_output(self):
        self.suma = 0
        for i in range(len(self.wejscia)):
            self.suma += self.wagi[i] * self.wejscia[i]

        self.wyjscie = self.activation_funcion_2(self.suma)
        return self.wyjscie

    def activation_funcion(self, sum_of_values):
        h1 = (1 - math.exp(-sum_of_values))
        h2 = (1 + math.exp(-sum_of_values))
        helper = h1/h2
        return helper

    def activation_funcion_2(self, sum_of_values):
        h1 = 1
        h2 = (1 + math.exp(-sum_of_values))
        return h1/h2

    def get_output(self):
        return self.wyjscie

    #   -------------------------------------------------- Propagacja w tył
    def calc_wspo_x_wag(self, nr):
        return self.wagi[nr] * self.wspolczynik

    def get_single_waga(self, nr):
        return self.wagi[nr]

    def calc_pochodna(self):
        self.pochodna = self.wyjscie * (1 - (self.wyjscie**2))
        return self.pochodna

    def calc_pochodna_2(self):
        self.pochodna = self.wyjscie * (1 - self.wyjscie)
        return self.pochodna

    def calc_wspolczynik_wyjsciowy(self, CK):
        self.wspolczynik = (CK - self.wyjscie) * self.pochodna
        return self.wspolczynik

    def calc_wspolczynik_posredni(self, suma_waga_x_wspolczynik):
        self.wspolczynik = suma_waga_x_wspolczynik * self.pochodna
        return self.wspolczynik

    def get_wspolczynik(self):
        return self.wspolczynik

    def get_wagas(self):
        return self.wagi

    def get_deltawag(self):
        return self.deltawag

    def get_popwagi(self):
        return self.popwagi

    def update_wagas(self):
        for i in range(len(self.wagi)):
            self.popwagi[i] = self.wagi[i]
            self.wagi[i] = self.wagi[i] + (0.9 * self.deltawag[i]) + (self.ro * self.wspolczynik * self.wejscia[i])
            self.deltawag[i] = self.wagi[i] - self.popwagi[i]

    def get_wejscia(self):
        return self.wejscia
