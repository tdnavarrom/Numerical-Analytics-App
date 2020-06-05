import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from .Functions import Functions


class NewtonInterpolation:
    def __init__(self):
        self.polinomios = ""
        self.xn = ""  # All the x values
        self.filas = []

    def algorithm_newtonInterpolation(self, func, xn):

        self.matrix = []
        self.xn = xn[0]
        length = len(self.xn)
        for i in range(length):
            self.matrix.append([0] * (length + 1))
            self.matrix[i][0] = self.xn[i]
            self.matrix[i][1] = func.evaluate(self.xn[i])

        self.polinomios = "p(x) = " + str(self.matrix[0][1])

        for i in range(2, (length+1)):
            for j in range(i-1, length):
                self.matrix[j][i] = (
                    self.matrix[j][i-1]-self.matrix[j-1][i-1])/(self.matrix[j][0]-self.matrix[j-i+1][0])
                if (j == i-1):
                    self.polinomios += " + " + str(self.matrix[j][i])
                    for j in range(0, j):
                        self.polinomios += "(x-" + str(self.matrix[j][0]) + ")"
        self.polinomios = self.polinomios.replace("+ -", "-").replace(" + -", "-")
        self.definir_filas()

    def get_sol(self):
        return self.polinomios

    def value_table(self):
        return self.matrix

    def definir_filas(self):
        self.filas.append("xn")
        self.filas.append("f(xn)")
        for i in range(1, len((self.matrix[0]))-1):
            self.filas.append(i)
        return self.filas