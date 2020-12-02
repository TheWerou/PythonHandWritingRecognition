from numba import jit, cuda
import numpy as np


class Basic:
    def __init__(self):
        self.Neurony1 = 2
        self.Neurony2 = 1
        self.Neurony3 = 0
        self.W1 = np.zeros((self.Neurony1, 2 + 1))
        self.W2 = np.zeros((self.Neurony2, 2 + 1))
        self.W3 = np.zeros((self.Neurony3, 0))

        self.Wp1 = np.zeros(self.Neurony1)
        self.Wp2 = np.zeros(self.Neurony2)
        self.Wp3 = np.zeros(self.Neurony3)

        self.DW1 = np.zeros(self.Neurony1)
        self.DW2 = np.zeros(self.Neurony2)
        self.DW3 = np.zeros(self.Neurony3)

        self.S1 = np.zeros(self.Neurony1)
        self.S2 = np.zeros(self.Neurony2)
        self.S3 = np.zeros(self.Neurony3)

        self.U1 = np.zeros(self.Neurony1)
        self.U2 = np.zeros(self.Neurony2)
        self.U3 = np.zeros(self.Neurony3)

        self.F1 = np.zeros(self.Neurony1)
        self.F2 = np.zeros(self.Neurony2)
        self.F3 = np.zeros(self.Neurony3)

    def suma_waz_warstwy(self, S, W, Dane):
        Dane.insert(0, 1)
        for k in range(len(S)):
            for i in range(len(W)):
                S[k] += W[k, i] * Dane[i][0]

        return S

    def prop_tyl(self):
        pass

    def run(self):
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

        dane = [[A[0, 1]], [A[0, 2]]]
        print(len(self.S1))
        print(len(self.W1[0, :]))
        self.S1 = self.suma_waz_warstwy(self.S1, self.W1, dane)
        print(self.S1)



basic = Basic()
basic.run()
