import math


class FixedPoint:

    def __init__(self):
        self.values = []

    def evaluate(self, xi, tolerancia, iter, fun, gx):

        fx = fun.evaluate2(xi)

        if fx == 0:
            return f"{xi} es raiz"
        if iter < 1:
            return "El valor del iterador es incorrecto"
        if tolerancia < 0:
            return "Error en la tolerancia, debe ser mayor o igual a 0"

        contador = 0
        xn = gx.evaluate2(xi)
        error = tolerancia + 0.1
        self.values.append([contador, xn, fx, error])
        while fx != 0 and error > tolerancia and contador < iter:
            xn = gx.evaluate2(xi)
            fi = fun.evaluate2(xn)
            error = abs((xn-xi)/xn)
            xi = xn
            self.values.append([contador, xn, fi, error])
            contador = contador + 1

        if fx == 0:
            return f"{xi} es raiz"
        elif error < tolerancia:
            return f"{xi} es una aprox. con una tolerancia = {tolerancia}"
        else:
            return f"El método fracasó en {iter} iteraciones"

    def tabla_values(self):
        return self.values
