import numpy as np
import matplotlib.pyplot as plt
import math


class BasicLayer:
    def __init__(self):
        pass

    def version_1(self):
        pass

    def propagacja_w_przod(self):
        pass

    def basic_main(self):
        A = np.zeros((4, 4))
        A[0, 0] = 1
        A[0, 1] = 0
        A[0, 2] = 0
        A[0, 3] = 0
        A[1, 0] = 1
        A[1, 1] = 0
        A[1, 2] = 1
        A[1, 3] = 1
        A[2, 0] = 1
        A[2, 1] = 1
        A[2, 2] = 0
        A[2, 3] = 1
        A[3, 0] = 1
        A[3, 1] = 1
        A[3, 2] = 1
        A[3, 3] = 0
        # ---- wykreslenie obszaru klasyfikacji
        Licz = 0
        IleKrokow = 50000
        err = 0
        WRR = np.zeros((2, 5000))

        for x in range(5000):
            WRR[0, x] = x

        # ---- utworzenie odpowiednich tablic na dane
        W = np.zeros(9)  # zbior wszystkich wag
        Wp = np.zeros(9)
        S = np.zeros(3)  # Sumy wazona dla wszystkich neuronow
        U = np.zeros(3)  # Wartosci dla neuronow
        F = np.zeros(3)  # wartosc pochodnej funkcji sig
        d = np.zeros(3)  # Jakies wspolczyniki
        w8 = 0
        w7 = 0
        w6 = 0
        w5 = 0
        w4 = 0
        w3 = 0
        w2 = 0
        w1 = 0
        w0 = 0
        ro = 0.2  # skok
        iteracja = 0  # iteracje

        # ---- losowa inicjalizacja wag poczatkowych
        for i in range(0, 9):
            W[i] = np.random.rand() - 0.5
            Wp[i] = W[i]
        while iteracja < IleKrokow:
            # ---- losowe wybieranie wektora trenujacego
            i = np.random.randint(4)
            # ---- faza propagacji w przod - warstwa posrednia
            S[0] = W[0] * A[i, 0] + W[1] * A[i, 1] + W[2] * A[i, 2]  # oblicznie sumy wazonej
            S[1] = W[3] * A[i, 0] + W[4] * A[i, 1] + W[5] * A[i, 2]

            U[0] = 1 / (1 + math.exp(-S[0]))  # obliczanie wartosci funkcji
            U[1] = 1 / (1 + math.exp(-S[1]))  # dla warstwy ukrytej

            # ---- faza propagacji w przod - warstwa wyjsciowa
            S[2] = W[6] * A[i, 0] + W[7] * U[0] + W[8] * U[1]  # suma wazona dla warsty wyjsciowej
            U[2] = 1 / (1 + math.exp(-S[2]))  # oblicznie wartosci funkcji

            if iteracja == 0:
                WRR[1, 0] = A[i, 3] - U[2]

            if iteracja % 100 == 0:
                WRR[1, int(iteracja / 100)] = A[i, 3] - U[2]
                if WRR[1, int(iteracja / 100)] < 0:
                    WRR[1, int(iteracja / 100)] = -WRR[1, int(iteracja / 100)]

            # ---- faza propagacji wstecz - warstwa wyjsciowa
            F[2] = U[2] * (1 - U[2])  # obliczanie pochodnej dla wyjsciowej
            d[2] = (A[i, 3] - U[2]) * F[2]  # oblicznie wspolczynika
            # ---- faza propagacji wstecz - warstwa posrednia
            F[0] = U[0] * (1 - U[0])  # pochodna funkcji wartsy posredniej
            d[0] = W[7] * d[2] * F[0]  # wspolczynik czegos tam
            F[1] = U[1] * (1 - U[1])  # pochodna funkcji wartsy posredniej
            d[1] = W[8] * d[2] * F[1]  # wspolczynik czegos tam
            # ---- uaktualnienie wag - warstwa wyjsciowa

            Wp[6] = W[6]
            W[6] = W[6] + (0.9 * w6) + (ro * d[2] * A[i, 0])  # uaktualnienie wag
            w6 = W[6] - Wp[6]

            Wp[7] = W[7]
            W[7] = W[7] + (0.9 * w7) + (ro * d[2] * U[0])  # -||-
            w7 = W[7] - Wp[7]

            Wp[8] = W[8]
            W[8] = W[8] + (0.9 * w8) + (ro * d[2] * U[1])  # -||-
            w8 = W[8] - Wp[8]

            # ---- uaktualnienie wag - warstwa posrednia
            Wp[0] = W[0]
            W[0] = W[0] + (0.9 * w0) + (ro * d[0] * A[i, 0])
            w0 = W[0] - Wp[0]

            Wp[1] = W[1]
            W[1] = W[1] + (0.9 * w1) + (ro * d[0] * A[i, 1])
            w1 = W[1] - Wp[1]

            Wp[2] = W[2]
            W[2] = W[2] + (0.9 * w2) + (ro * d[0] * A[i, 2])
            w2 = W[2] - Wp[2]

            Wp[3] = W[3]
            W[3] = W[3] + (0.9 * w3) + (ro * d[1] * A[i, 0])
            w3 = W[3] - Wp[3]

            Wp[4] = W[4]
            W[4] = W[4] + (0.9 * w4) + (ro * d[1] * A[i, 1])
            w4 = W[4] - Wp[4]

            Wp[5] = W[5]
            W[5] = W[5] + (0.9 * w5) + (ro * d[1] * A[i, 2])
            w5 = W[5] - Wp[5]

            iteracja = iteracja + 1

        a = 1
        b = 1
        suma1 = W[0] * 1 + W[1] * a + W[2] * b
        suma2 = W[3] * 1 + W[4] * a + W[5] * b

        u_odp_1 = 1 / (1 + math.exp(-suma1))
        u_odp_2 = 1 / (1 + math.exp(-suma2))

        suma3 = W[6] * 1 + W[7] * u_odp_1 + W[8] * u_odp_2
        u_odp = 1 / (1 + math.exp(-suma3))

        print("U1 i U2 - {:.6f} {:.6f}".format(U[0], U[1]))
        print("poprawnae - {:.6f}".format(u_odp))

        return W
