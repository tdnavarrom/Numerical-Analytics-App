import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class Functions:
    def __init__(self,entrada):
        self.function=parse_expr(entrada)
        self.derivar(self.function)

    def evaluar(self,valor):
        valores=self.function.evalf(subs=dict(x=valor))
        try:
            aux=float(valores)
            if(isinstance(aux, float)):
                return valores
            else:
                return True
        except:
            return "Final"

    def evaluar_derivada(self,valor):
        valores=self.derivada.evalf(subs=dict(x=valor))
        try:
            aux=float(valores)
            if(isinstance(aux, float)):
                return valores
            else:
                return True
        except:
            return "Final"

    def derivar(self,entrada):
    	x = sp.Symbol('x')
    	self.derivada = sp.diff(entrada,x)
    
    def derivarM(self,entrada, veces, valor):
        x = sp.Symbol('x')
        derivada = sp.diff(self.function,x,int(veces))
        valores=derivada.evalf(subs=dict(x=valor))
        return valores
