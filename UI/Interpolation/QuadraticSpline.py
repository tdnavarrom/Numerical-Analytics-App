import numpy as np
import string
from sympy import *
import math
class QuadraticSpline:
    def __init__(self):
        self.functions = []
        self.functionsValues = []
        self.constants = []
        self.constantsUseds = []
        self.px = []
        self.rows = []
        self.x = Symbol('x')
        self.f = Function('f')
        self.result = []
        self.results = []
    def algorithm_quadratic_spline(self,xVal,yVal):
        constanNum = 0
        x = xVal[0]
        y = yVal[0]
        points = []
        intervals = []
        alf = list(string.ascii_lowercase) #From a to z
        for i in alf:
            for j in range(1,3):
                s = symbols(str(i)+str(j))
                self.constants.append(s)
        for p in range(len(x)):
            points.append([x[p],y[p]])
        for i in range(1,len(x)):
            intervals.append([points[i-1][0],points[i][0]])
        dicPoints = dict(points)
        for i in intervals:
            self.f = self.constants[constanNum]*self.x**2 + self.constants[constanNum+1]*self.x + self.constants[constanNum+2]
            self.functions.append(self.f)
            self.f = self.constants[constanNum]*self.x**2 + self.constants[constanNum+1]*self.x + self.constants[constanNum+2]  - dicPoints[i[0]]
            self.functionsValues.append(self.f.subs(x,i[0]))
            self.f = self.constants[constanNum]*self.x**2 + self.constants[constanNum+1]*self.x +self.constants[constanNum+2]  - dicPoints[i[1]]
            self.functionsValues.append(self.f.subs(self.x,i[1]))
            self.constantsUseds.append(self.constants[constanNum])
            self.constantsUseds.append(self.constants[constanNum+1])
            self.constantsUseds.append(self.constants[constanNum+2])
            constanNum += 3
        for i in range(0,len(self.functions)-1,1):
            print(diff(self.functions[i],self.x))
            print(diff(self.functions[i+1],self.x))
            self.f = diff(self.functions[i],self.x).subs(self.x,intervals[i][1]) - diff(self.functions[i+1],self.x).subs(self.x,intervals[i+1][0])
            self.functionsValues.append(self.f)
        self.functionsValues.append(diff(self.functions[0],self.x,2).subs(self.x,intervals[0][0]))
        for i in range(0,len(self.functionsValues)):
            self.results.append((str(i + 1)+") " +str(self.functionsValues[i])))
            self.result.append(self.functionsValues[i])
            #print(str(self.functionsValues[i]))
        """
        solucion = solve(self.functionsValues, self.constantsUseds)
        constValues = dict(solucion)
        marc = 0
        funcActual = 0
        valTree = []
        for i in constValues:
            marc += 1
            valTree.append(constValues[i])
            if marc%3 == 0:
                self.functions[funcActual] = self.functions[funcActual].subs(self.constantsUseds[marc-1],valTree[2])
                self.functions[funcActual] = self.functions[funcActual].subs(self.constantsUseds[marc-2],valTree[1])
                self.functions[funcActual] = self.functions[funcActual].subs(self.constantsUseds[marc-3],valTree[0])
                print(str(self.functions[funcActual]) + "             " + str(intervals[funcActual][0]) + " <=  X <= " + str(intervals[funcActual][1]))
                valTree = []
                funcActual += 1
        """
    def value_table(self):
        return self.result

    def get_results(self):
        results=""
        for i in self.results:
            results+=f""+(str)(i)+"\n"
        return results