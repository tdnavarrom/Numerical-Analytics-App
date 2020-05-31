import math
from .Function import Function

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





        '''
        self.values.append(
            [0, initial_value, Function.evaluate(initial_value)])
        if self.values[0][1] == 0:
            return f"{self.values[0][0]} es una raiz"
        elif increment == 0:
            return "El valor asignado al incremento es incorrecto"
        elif iterations < 1:
            return "El valor del iterador es incorrecto"
        else:
            cont = 1
            new_value = initial_value+increment
            while (cont < iterations):
                self.values.append(
                    [cont, new_value, Function.evaluate(new_value)])
                valor_evaluado_nuevo = Function.evaluate(new_value)
                new_value += increment
                cont += 1

            if self.values[cont][1]*valor_evaluado_nuevo < 0:
                return f"Los valores [{round(self.values[cont][0],2)},{round(new_value,2)}] definen un intervalo"
            elif self.values[cont][1] == 0:
                return f"{round(self.values[cont][0],2)} es una raiz"
            elif(valor_evaluado_nuevo == 0):
                return f"{round(new_value,2)} es una raiz"
            else:
                return f"Could not find root in {iterations}"
        '''

    def tabla_values(self):
        return self.values
