import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from .Functions import Functions

class NewtonInterpolation:
    def __init__(self):
        self.polinom=""
        self.xn=""     #All the x values 
        self.rows=[]

    def algorithm_newtonInterpolation(self, func, xn):

        self.matrix = []
        self.xn= xn[0]
        length= len(self.xn)
        for i in range (length):
            self.matrix.append([0] * (length + 1))
            self.matrix[i][0] = self.xn[i]
            self.matrix[i][1] = func.evaluar(self.xn[i])

        self.polinom = "p(x) = "+ str(self.matrix[0][1])

        for i in range(2,(length+1)):
            for j in range(i-1,length):
                self.matrix[j][i] = (self.matrix[j][i-1]-self.matrix[j-1][i-1])/(self.matrix[j][0]-self.matrix[j-i+1][0])
                if (j==i-1):
                    self.polinom += " + "+ str(self.matrix[j][i])
                    for j in range (0,j):
                        self.polinom += "(x-" + str(self.matrix[j][0]) + ")"
        self.polinom= self.polinom.replace("+ -", "-").replace(" + -","-") 
        #print("---------------------------")
        self.row_definition()
        #print(self.matrix)

    def get_sol(self):
        return self.polinom

    def value_table(self):
        return self.matrix
    
    def row_definition(self):
        self.rows.append("xn")
        self.rows.append("f(xn)")
        for i in range(1,len((self.matrix[0]))-1):
            self.rows.append(i)
        return self.rows




"""
Ejemplo

exp(x)-ln(x+4)
[1,1.3,1.5,1.8,2.3]

"""