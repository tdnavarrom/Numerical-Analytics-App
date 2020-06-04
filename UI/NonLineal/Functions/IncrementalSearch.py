import math
from UI.NonLineal.Functions.Function import Function

class IncrementalSearch:
    def __init__(self):
        self.values = []

    def evaluate(self, initial_value, increment, iterations, function):

        function = Function(function)
        x = initial_value
        fx = function.evaluate(initial_value)
        self.values.append([0, str(initial_value), str(fx)])
        if fx == 0:
            return str(initial_value) + " es una raiz."
        elif increment == 0:
            return "El valor asignado al incremento es incorrecto"
        elif iterations < 1:
            return "El valor del iterador es incorrecto"
        else:
            x1 = initial_value + increment
            contador = 1
            fx1 = function.evaluate(x1)
            self.values.append([contador, str(x1), str(fx1)])
            while fx * fx1 > 0 and contador < iterations:
                x = x1
                fx = fx1
                x1 = x + increment
                fx1 = function.evaluate(x1)
                contador += 1
                self.values.append([contador, str(x1), str(fx1)])

            if fx1 == 0:
                return str(x1) + " es una Raiz."
            elif fx * fx1 < 0:
                return "Los valores "+ str(x) + " y " + str(x1) +" definen un intervalo"
            else:
                return "No se encontro un intervalo que contenga al menos una raiz."

    def tabla_values(self):
        return self.values
