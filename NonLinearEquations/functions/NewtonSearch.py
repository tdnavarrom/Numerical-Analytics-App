import math

class Newton:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, xi, niter, fun, dfun):

        fx = fun.evaluate(xi)
        dfx = dfun.evaluate(xi)
        contador = 0
        error = tol + 1
        self.values.append([contador, xi, fx, dfx, error])
        while error > tol and fx != 0 and dfx != 0 and contador < niter:
            xn = xi - (fx/dfx)
            fi = fun.evaluate(xn)
            dfi = dfun.evaluate(xn)
            error = abs((xn - xi)/xn)
            xi = xn
            self.values.append([contador, xn, fi, dfi, error])
            contador = contador + 1
        if fx == 0:
            return f"{xi} es raiz"
        elif error < tol:
            return f"{xn} es una aprox. a una raiz con una tolerancia = {tol}"
        elif dfx == 0:
            return f"{xn} es una posible raiz multiple"
        else:
            return f"El método fracasó en {niter} iteraciones"

    def tabla_values(self):
        return self.values
