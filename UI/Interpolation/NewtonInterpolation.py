import math
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from .Functions import *
class NewtonInterpolation:
    def __init__(self):
        self.polinomial=""
        self.xn=""     #All the x values 
        self.rows=[]

    def algorithm_newtonInterpolation(self, entry, xn):
        self.matrix = []
        self.xn= xn[0]
        length= len(self.xn)
        for i in range (length):
            self.matrix.append([0] * (length + 1))
            self.matrix[i][0] = self.xn[i]
            self.matrix[i][1] = entry.evaluar(self.xn[i])

        self.polinomial = "P(X) = "+ str(self.matrix[0][1])

        for i in range(2,(length+1)): #  col and rows
            for j in range(i-1,length):
                self.matrix[j][i] = (self.matrix[j][i-1]-self.matrix[j-1][i-1])/(self.matrix[j][0]-self.matrix[j-i+1][0])
                if (j==i-1):
                    self.polinomial += " + "+ str(self.matrix[j][i])
                    for j in range (0,j): #j??
                        self.polinomial += "(x-" + str(self.matrix[j][0]) + ")"
        self.polinomial= self.polinomial.replace("+ -", "-").replace(" + -","-") 
        print("---------------------------")
        self.row_definition()
        print(self.matrix)


    def value_table(self):
        return self.matrix
    
    def row_definition(self):
        self.rows.append("Xn")
        self.rows.append("F(Xn)")
        for i in range(1,len((self.matrix[0]))-1): #-1?
            self.rows.append(i)
        return self.rows
    def get_sol(self):
        return self.polinomial
"""
n= NewtonInterpolation()

exp(x)-ln(x+4)
[1,1.3,1.5,1.8,2.3]
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[1,1.3,1.5,1.8,2.3])
n.algorithm_newtonInterpolation("exp(x)-ln(x+4)",[2,3.1,4,5])

"""