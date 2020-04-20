import math


class Newton:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, xi, niter, fun, dfun):
        fx = fun.evaluate2(xi)
        dfx = dfun.evaluate2(xi)
        contador = 0
        error = tol + 1
        self.values.append([contador, str(xi), str(
            "{:.2e}".format(fx)), str(dfx), None])

        while error > tol and fx != 0 and dfx != 0 and contador < niter:
            xn = xi - (fx/dfx)
            fx = fun.evaluate2(xn)
            dfx = dfun.evaluate2(xn)
            error = abs((xn - xi)/xn)
            xi = xn

            contador = contador + 1
            self.values.append([contador, str(xn), str(
                "{:.2e}".format(fx)), str(dfx), str("{:.2e}".format(error))])

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
