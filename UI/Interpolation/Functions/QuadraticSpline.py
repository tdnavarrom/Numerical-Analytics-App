import numpy as np
import string
from sympy import *
import math
class QuadraticSpline:
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
    def algorithm_quadratic_spline(self,xVal,yVal):
        constanNum = 0
        x = xVal[0]
        y = yVal[0]
        puntos = []
        intervalos = []
        alf = list(string.ascii_lowercase) #From a to z
        for i in alf:
            for j in range(1,3):
                s = symbols(str(i)+str(j))
                self.constantes.append(s)
        for p in range(len(x)):
            puntos.append([x[p],y[p]])
        for i in range(1,len(x)):
            intervalos.append([puntos[i-1][0],puntos[i][0]])
        dicpuntos = dict(puntos)
        for i in intervalos:
            self.f = self.constantes[constanNum]*self.x**2 + self.constantes[constanNum+1]*self.x + self.constantes[constanNum+2]
            self.functions.append(self.f)
            self.f = self.constantes[constanNum]*self.x**2 + self.constantes[constanNum+1]*self.x + self.constantes[constanNum+2]  - dicpuntos[i[0]]
            self.functions_values.append(self.f.subs(x,i[0]))
            self.f = self.constantes[constanNum]*self.x**2 + self.constantes[constanNum+1]*self.x +self.constantes[constanNum+2]  - dicpuntos[i[1]]
            self.functions_values.append(self.f.subs(self.x,i[1]))
            self.constantes_usadas.append(self.constantes[constanNum])
            self.constantes_usadas.append(self.constantes[constanNum+1])
            self.constantes_usadas.append(self.constantes[constanNum+2])
            constanNum += 3
        for i in range(0,len(self.functions)-1,1):
            print(diff(self.functions[i],self.x))
            print(diff(self.functions[i+1],self.x))
            self.f = diff(self.functions[i],self.x).subs(self.x,intervalos[i][1]) - diff(self.functions[i+1],self.x).subs(self.x,intervalos[i+1][0])
            self.functions_values.append(self.f)
        self.functions_values.append(diff(self.functions[0],self.x,2).subs(self.x,intervalos[0][0]))
        for i in range(0,len(self.functions_values)):
            self.resultados.append((str(i + 1)+") " +str(self.functions_values[i])))
            self.resultado.append(self.functions_values[i])
            #print(str(self.functions_values[i]))
       
    def value_table(self):
        return self.resultado

    def get_resultados(self):
        resultados=""
        for i in self.resultados:
            resultados+=f""+(str)(i)+"  "
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