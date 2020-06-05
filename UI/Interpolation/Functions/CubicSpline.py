import numpy as np
import string
from sympy import *
import math


class CubicSpline:
    def __init__(self):
        self.functions = []
        self.functions_values = []
        self.constantes = []
        self.constantes_usadas = []
        self.px = []
        self.filas = []
        self.x = Symbol('x')
        self.f = Function('f')
        self.resultado = []
        self.resultados = []

    def algorithm_cubic_spline(self, xVal, yVal):
        x = xVal[0]
        y = yVal[0]
        constanNum = 0
        points = []
        intervals = []
        alf = list(string.ascii_lowercase)  # From a to z
        for i in alf:
            for j in range(1, 4):
                s = symbols(str(i)+str(j))
                self.constantes.append(s)
        for p in range(len(x)):
            points.append([x[p], y[p]])
        for i in range(1, len(x)):
            intervals.append([points[i-1][0], points[i][0]])
        dicPoints = dict(points)
        for i in intervals:
            self.f = self.constantes[constanNum]*self.x**3 + self.constantes[constanNum+1] * \
                self.x**2 + self.constantes[constanNum+2] * \
                self.x + self.constantes[constanNum+3]
            self.functions.append(self.f)
            self.f = self.constantes[constanNum]*self.x**3 + self.constantes[constanNum+1]*self.x**2 + \
                self.constantes[constanNum+2]*self.x + \
                self.constantes[constanNum+3] - dicPoints[i[0]]
            self.functions_values.append(self.f.subs(x, i[0]))
            self.f = self.constantes[constanNum]*self.x**3 + self.constantes[constanNum+1]*self.x**2 + \
                self.constantes[constanNum+2]*self.x + \
                self.constantes[constanNum+3] - dicPoints[i[1]]
            self.functions_values.append(self.f.subs(self.x, i[1]))
            self.constantes_usadas.append(self.constantes[constanNum])
            self.constantes_usadas.append(self.constantes[constanNum+1])
            self.constantes_usadas.append(self.constantes[constanNum+2])
            self.constantes_usadas.append(self.constantes[constanNum+3])
            constanNum += 4
        for i in range(0, len(self.functions)-1, 1):
            self.f = diff(self.functions[i], self.x).subs(
                self.x, intervals[i][1]) - diff(self.functions[i+1], self.x).subs(self.x, intervals[i+1][0])
            self.functions_values.append(self.f)
        for i in range(0, len(self.functions)-1, 1):
            self.f = diff(self.functions[i], self.x, 2).subs(
                self.x, intervals[i][1]) - diff(self.functions[i+1], self.x, 2).subs(self.x, intervals[i+1][0])
            self.functions_values.append(self.f)
        self.functions_values.append(
            diff(self.functions[0], self.x, 2).subs(self.x, intervals[0][0]))
        self.functions_values.append(
            diff(self.functions[0], self.x, 2).subs(self.x, intervals[0][0]))
        self.functions_values.append(diff(self.functions[len(
            self.functions)-1], self.x, 2).subs(self.x, intervals[len(intervals)-1][1]))
        for i in range(0, len(self.functions_values)):
            #print(str(i + 1)+") " +str(self.functions_values[i]))
            self.resultados.append(str(i + 1)+") " +
                                str(self.functions_values[i]))
            self.resultado.append(self.functions_values[i])

    def value_table(self):
        return self.resultado

    def get_resultados(self):
        resultados = ""
        for i in self.resultados:
            resultados += f""+(str)(i)+" "
        return resultados
