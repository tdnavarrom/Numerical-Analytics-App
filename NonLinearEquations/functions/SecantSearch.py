import math

class Secant:
    def _init_(self):
        self.values = []

    def evaluate(self, tol, x0, x1, fun, niter):

        fx0 = fun.evaluate(x0)

        if fx0 == 0:
            return f"{x0} es raiz"
        else:
            fx1 = fun.evaluate(x1)
            contador = 0
            error = tol + 1
            den = fx1 - fx0
            while error > tol and fx1 != 0 and den != 0 and cont < niter:
                x2 = x1 - (fx1*(x1 - x0)/den)
                error  = abs((xn-x1)/xn)
                x0 = x1
                fx0 = fx1
                x1 = x2
                fx1 = fun.evaluate(xn)
                den = fx1 - fx0
                self.values.append([contador, x2, fx1, error])
                contador = contador + 1
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