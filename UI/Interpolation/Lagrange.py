import sympy as sym

class Lagrange:
    def __init__(self):
        self.xValues = []
        self.yValues = []
        self.LValues = []
        self.polynomial = 0
    
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
                    self.polynomial += self.LValues[i]*self.yValues[i]
                    numerator = 1
                    denominator = 1
                
                self.polynomial = str(sym.expand(self.polynomial))
            except ZeroDivisionError as e:
                self.polynomial = "Error: Division by zero caused by invalid X values"
            except Exception as e:
                self.polynomial = "Error: Invalid input one x value mustn't have two y values"
        else:
            self.polynomial = "Error: The size of the X vector don't match that of F(X)"
    
    def getPolynomial(self):
        return self.polynomial

if __name__ == "__main__":
    X = [-4,-2,-1]
    Y = [-2.5962588,-0.6969583,0.9081217]

    lagi = Lagrange()
    lagi.lagrange_interpol_algorithm(X,Y)
    print(sym.expand(lagi.polynomial))
    #To evaluate
    #x = sym.Symbol('x')
    #print(lagi.polynomial.evalf(subs=dict(x=-1)))
    print(type(lagi.polynomial))
    pass
