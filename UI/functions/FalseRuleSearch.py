import math
from .Function import Function

class FalseRule:

    def __init__(self):
        self.values = []

    def evaluate(self, xi, xs, tolerancia, iter, function, type_error=1):

        funcion = Function(function)

        fxi = funcion.evaluate(xi)
        fxs = funcion.evaluate(xs)

        if iter < 1:
            return "El valor del iterador es incorrecto"
        if tolerancia < 0:
            return "Error en la tolerancia, debe ser mayor o igual a 0"

        if fxi == 0:
            return f"{xi} es una raiz"
        elif fxs == 0:
            return f"{xs} es una raiz"
        elif fxi * fxs < 0:
            xm = xi-((fxi*(xi-xs))/(fxi-fxs))
            fxm = funcion.evaluate(xm)
            contador = 1
            error = tolerancia + 1

            self.values.append([contador, str(xi), str(
                xs), str(xm), str("{:.2e}".format(fxm)), None])

            while error > tolerancia and fxm != 0 and contador < iter:
                if fxm * fxi < 0:
                    xs = xm
                    fxs = fxm
                else:
                    xi = xm
                    fxi = fxm
                xaux = xm
                xm = xi-((fxi*(xi-xs))/(fxi-fxs))
                fxm = funcion.evaluate(xm)

                if type_error == 0:
                    error = abs(xm-xaux)
                else:
                    error = abs((xm-xaux)/xm)

                contador += 1
                self.values.append([contador, str(xi), str(xs), str(
                    xm), str("{:.2e}".format(fxm)), str("{:.2e}".format(error))])

            if fxm == 0:
                return f"{xm} es raiz"
            elif (error < tolerancia):
                return f"{xm} es una aprox. a una raiz con tolerancia = {tolerancia}"
            else:
                return f"fracaso en {iter} iteraciones"
        else:
            return "el intervalo es inadecuado"

    def tabla_values(self):
        return self.values
