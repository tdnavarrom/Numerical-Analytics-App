import numpy as np
import string
from sympy import *
import math
class CubicSpline:
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

    def algorithm_cubic_spline(self,xVal,yVal):
        x = xVal[0]
        y = yVal[0]
        constanNum = 0
        points = []
        intervals = []
        alf = list(string.ascii_lowercase) #From a to z
        for i in alf:
            for j in range(1,4):
                s = symbols(str(i)+str(j))
                self.constants.append(s)
        for p in range(len(x)):
            points.append([x[p],y[p]])
        for i in range(1,len(x)):
            intervals.append([points[i-1][0],points[i][0]])
        dicPoints = dict(points)
        for i in intervals:
            self.f = self.constants[constanNum]*self.x**3 +self.constants[constanNum+1]*self.x**2 +self.constants[constanNum+2]*self.x + self.constants[constanNum+3] 
            self.functions.append(self.f)
            self.f = self.constants[constanNum]*self.x**3 +self.constants[constanNum+1]*self.x**2 +self.constants[constanNum+2]*self.x + self.constants[constanNum+3]   - dicPoints[i[0]]
            self.functionsValues.append(self.f.subs(x,i[0]))
            self.f = self.constants[constanNum]*self.x**3 +self.constants[constanNum+1]*self.x**2 +self.constants[constanNum+2]*self.x + self.constants[constanNum+3]   - dicPoints[i[1]]
            self.functionsValues.append(self.f.subs(self.x,i[1])) 
            self.constantsUseds.append(self.constants[constanNum])
            self.constantsUseds.append(self.constants[constanNum+1])
            self.constantsUseds.append(self.constants[constanNum+2])
            self.constantsUseds.append(self.constants[constanNum+3])
            constanNum += 4  
        for i in range(0,len(self.functions)-1,1):
            self.f = diff(self.functions[i],self.x).subs(self.x,intervals[i][1]) - diff(self.functions[i+1],self.x).subs(self.x,intervals[i+1][0])
            self.functionsValues.append(self.f)
        for i in range(0,len(self.functions)-1,1):
            self.f = diff(self.functions[i],self.x,2).subs(self.x,intervals[i][1]) - diff(self.functions[i+1],self.x,2).subs(self.x,intervals[i+1][0])
            self.functionsValues.append(self.f)
        self.functionsValues.append(diff(self.functions[0],self.x,2).subs(self.x,intervals[0][0]))
        self.functionsValues.append(diff(self.functions[0],self.x,2).subs(self.x,intervals[0][0]))
        self.functionsValues.append(diff(self.functions[len(self.functions)-1],self.x,2).subs(self.x,intervals[len(intervals)-1][1]))
        for i in range(0,len(self.functionsValues)):
            #print(str(i + 1)+") " +str(self.functionsValues[i]))
            self.results.append(str(i + 1)+") " +str(self.functionsValues[i]))
            self.result.append(self.functionsValues[i])
    def value_table(self):
        return self.result

    def get_results(self):
        results=""
        for i in self.results:
            results+=f""+(str)(i)+"\n"
        return results