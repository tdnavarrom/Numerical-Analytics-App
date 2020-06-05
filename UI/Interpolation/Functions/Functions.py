import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class Functions:
    def __init__(self,entrada):
        self.function=parse_expr(entrada)
        self.derivate(self.function)

    def evaluate(self,valor):
        values=self.function.evalf(subs=dict(x=valor))
        try:
            aux=float(values)
            if(isinstance(aux, float)):
                return values
            else:
                return True
        except:
            return "Final"

    def evaluate_derivate(self,valor):
        values=self.derivate.evalf(subs=dict(x=valor))
        try:
            aux=float(values)
            if(isinstance(aux, float)):
                return values
            else:
                return True
        except:
            return "Final"

    def derivate(self,entrada):
    	x = sp.Symbol('x')
    	self.derivate = sp.diff(entrada,x)
    
    def derivateM(self,entrada, veces, valor):
        x = sp.Symbol('x')
        derivate = sp.diff(self.function,x,int(veces))
        values=derivate.evalf(subs=dict(x=valor))
        return values
