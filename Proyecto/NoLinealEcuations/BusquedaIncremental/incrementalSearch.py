import math


class IncrementalSearch:
    def __init__(self):
        self.values = []

    def Operacion(self, initial_value, increment, item, Function):
        self.values.append([initial_value, Function.evaluate(initial_value)])
        if self.values[0][1] == 0:
            return f"{self.values[0][0]} es una raiz"
        else:
            if increment == 0:
                return 0, "El valor asignado al incremento es incorrecto"
            else:
                if item <= 0:
                    return 0, "El valor del iterador es incorrecto"
                else:
                    cont = 0
                    new_value = initial_value+increment
                    while (cont < item):
                        self.values.append(
                            [new_value, Function.evaluate(new_value)])
                        valor_evaluado_nuevo = Function.evaluate(new_value)
                        if(self.values[cont][1]*valor_evaluado_nuevo <= 0):
                            break

                        new_value += increment
                        cont += 1

                    if self.values[cont][1]*valor_evaluado_nuevo < 0:
                        return 1, f"Los valores [{self.values[cont][0]},{new_value}] definen un intervalo"
                    else:
                        if self.values[cont][1] == 0:
                            return 2, f"{round(self.values[cont][0],2)} es una raiz"
                        else:
                            if(valor_evaluado_nuevo == 0):
                                return 2, f"{round(new_value,2)} es una raiz"
                            else:
                                return 0, "Se presento un fracaso en las iteraciones"

    def tabla_values(self):
        return self.values
