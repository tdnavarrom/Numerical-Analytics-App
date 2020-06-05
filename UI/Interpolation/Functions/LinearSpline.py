from decimal import *
import numpy as np
from sympy import *
import math

class LinearSpline:
    def __init__(self):
        self.x = []
        self.y = []
        self.resultado = []
        self.filas = []
        self.total = []

    def algorithm_linearSpline(self, xi, yi):
        denominador = 0.0
        self.x = xi[0]
        self.y = yi[0]
        if len(self.x) <= 0 or self.x is None:
            self.resultado.append("No hay valores de x")
        elif len(self.y) <= 0 or self.y is None:
            self.resultado.append("No hay valores de f(x)")
        else:
            for i in range(1,len(self.x)):
                denominador = (self.x[i] - self.x[i-1])
                if denominador != 0:
                    pendiente = (self.y[i] - self.y[i-1])/denominador
                    rest = (pendiente * - self.x[i]) + self.y[i]
                    self.resultado.append(["p(x" + str(i) + ") = " + str(pendiente) + "x + " + str(rest), str(self.x[i-1]) + "<= X <=  " + str(self.x[i])])
                else:
                    self.resultado.append(["Div by 0","please, check your values"])

    def value_table(self):
        return self.resultado

    def get_resultados(self):
        resultados=""
        aux=1
        for i in self.resultado:
            resultados+=f""+(str)(i[0])+"  "
            aux+=1
        return resultados

    def check_values(self, ar,br):
        if not ar or not br:
            return False
        arr = ar[0]
        arr.sort()
        iter = 1
        for i in arr:
            if i != arr[iter] and i != 0 and iter != (len(arr)-1):
                iter += 1
            elif iter != (len(arr)-1):
                return True
            else:
                return True