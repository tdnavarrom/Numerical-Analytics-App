import math

class FixedPoint:
   def __init__(self):
        self.values = []

def evaluate(self, xi, tolerancia, iter, fun, gx):
        fx = fun.evaluate(xi)
        contador = 0
        error = tolerancia + 1
        while fx != 0 and error > tolerancia and contador < iter:
            xn = gx(xi)
            fx = fun(xn)
            error = abs(xn-xi)/xn
            xi = xn
            self.values.append([xn, fx, error])
            contador = contador + 1

            
        if fx == 0:
            return f"{xi} es raiz"
        else: 
            if error<tolerancia:
                return f"{xi} es una aprox. con una tolerancia = {tolerancia}"
            else:
                return f"El método fracasó en {iter} iteraciones"   

def tabla_values(self):
        return self.values
