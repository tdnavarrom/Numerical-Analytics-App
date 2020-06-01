import math
from .Function import Function


class MultipleRoots:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, xi, iter, function, d1, dd2, type_error=1):
        fun = Function(function)
        der1 = Function(d1)
        der2 = Function(dd2)

        fx = fun.evaluate2(xi)
        dfx = der1.evaluate2(xi)
        ddfx = der2.evaluate2(xi)

        contador = 0
        self.values.append([contador, str(xi), str("{:.2e}".format(
            fx)), str("{:.2e}".format(dfx)), str(ddfx), None])
        error = tol + 1

        while error > tol and fx != 0 and ddfx != 0 and contador < iter:
            x = xi
            xi = x - (fx*dfx)/((dfx**2)-fx*ddfx)
            fx = fun.evaluate2(xi)
            dfx = der1.evaluate2(xi)
            ddfx = der2.evaluate2(xi)

            if type_error == 0:
                error = abs(xi-x)
            else:
                error = abs((xi-x)/xi)

            contador += 1
            self.values.append([contador, str(xi), str("{:.2e}".format(
                fx)), str("{:.2e}".format(dfx)), str(ddfx), str("{:.2e}".format(error))])

        if fx == 0:
            return f"{xi} es raiz"
        elif error < tol:
            return f"{xi} es una aprox. a una raiz con una tolerancia = {tol}"
        else:
            return f"El método fracasó en {iter} iteraciones"

    def tabla_values(self):
        return self.values
