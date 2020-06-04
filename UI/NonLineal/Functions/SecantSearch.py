import math
from UI.NonLineal.Functions.Function import Function

class Secant:
    def __init__(self):
        self.values = []

    def evaluate(self, tol, x0, x1, fun, niter, type_error=1):

        fun = Function(fun)

        fx0 = fun.evaluate(x0)

        if fx0 == 0:
            return f"{x0} es raiz"
        elif niter < 1:
            return "El valor del iterador es incorrecto"
        else:
            fx1 = fun.evaluate(x1)
            cont = 0
            self.values.append([-1, str(x0), str("{:.2e}".format(fx0)), None])
            self.values.append(
                [cont, str(x1), str("{:.2e}".format(fx1)), None])
            error = tol + 1
            den = fx1 - fx0

            while error > tol and fx1 != 0 and den != 0 and cont < niter:
                x2 = x1 - (fx1*(x1 - x0)/den)

                if type_error == 0:
                    error = abs(x2-x1)
                else:
                    error = abs((x2-x1)/x2)

                x0 = x1
                fx0 = fx1
                x1 = x2
                fx1 = fun.evaluate(x2)
                den = fx1 - fx0

                cont = cont + 1
                self.values.append(
                    [cont, str(x2), str("{:.2e}".format(fx1)), str("{:.2e}".format(error))])

            if fx1 == 0:
                return f"{x1} es raíz"
            elif error < tol:
                return f"{x1} es una aprox. a una raíz con una tolerancia = {tol}"
            elif den == 0:
                return f"Hay una posible raíz multiple"
            else:
                return f"Fracasó en {niter} iteraciones"


    def tabla_values(self):
        return self.values
