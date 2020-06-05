import sympy as sym
import numpy as np


class Lagrange:
    def __init__(self):
        self.x_values = []
        self.y_values = []
        self.l_values = []
        self.polinom = 0

    def lagrange_interpol_algorithm(self, xVector, yVector):
        self.x_values = xVector
        self.y_values = yVector

        if(len(self.x_values) != 0 and len(self.x_values) == len(self.y_values)):
            x = sym.Symbol('x')
            etapas = len(xVector)
            numerador = 1
            denominador = 1
            try:
                for i in range(etapas):
                    for j in range(etapas):
                        if(j != i):
                            if(self.x_values[i] != self.x_values[j]):
                                numerador = numerador*(x - self.x_values[j])
                                denominador = denominador * \
                                    (self.x_values[i]-self.x_values[j])
                            else:
                                raise Exception('')

                    self.l_values.append(numerador/denominador)
                    self.polinom += self.l_values[i]*self.y_values[i]
                    numerador = 1
                    denominador = 1

                self.polinom = str(sym.expand(self.polinom))
            except ZeroDivisionError as e:
                self.polinom = "Error: Division por 0"
        else:
            self.polinom = "Error: el tamaño del vector x no concuerda con el vector f(x)"

    def getPolynomial(self):
        return self.polinom
