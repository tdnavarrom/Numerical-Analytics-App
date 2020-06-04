import sympy as sym

class Lagrange:
    def __init__(self):
        self.xValues = []
        self.yValues = []
        self.LValues = []
        self.polinom = 0
    
    def lagrange_interpol_algorithm(self,xVector,yVector):
        self.xValues = xVector
        self.yValues = yVector

        if(len(self.xValues)!=0 and len(self.xValues)==len(self.yValues)):
            x = sym.Symbol('x')
            phases = len(xVector)
            numerator = 1
            denominator = 1
            try:
                for i in range(phases):
                    for j in range(phases):
                        if(j!=i):
                            if(self.xValues[i]!=self.xValues[j]):
                                numerator = numerator*(x - self.xValues[j])
                                denominator = denominator*(self.xValues[i]-self.xValues[j])
                            else:
                                raise Exception('')
                    
                    self.LValues.append(numerator/denominator)
                    self.polinom += self.LValues[i]*self.yValues[i]
                    numerator = 1
                    denominator = 1
                
                self.polinom = str(sym.expand(self.polinom))
            except ZeroDivisionError as e:
                self.polinom = "Error: Division by zero caused by invalid X values"
            except Exception as e:
                self.polinom = "Error: Invalid input one x value mustn't have two y values"
        else:
            self.polinom = "Error: The size of the X vector don't match that of F(X)"
    
    def getpolinom(self):
        return self.polinom