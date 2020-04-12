import math


class IncrementalSearch:
    def __init__(self):
        self.values = []

    def evaluate(self, initial_value, increment, iterations, Function):
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

    def tabla_values(self):
        return self.values
