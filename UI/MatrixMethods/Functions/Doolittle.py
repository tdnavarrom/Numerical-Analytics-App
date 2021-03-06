import numpy
from ..Messages.errors import ZeroDeterminantException


class Doolittle:

    def __init__(self, matrix, m, indp):
        self.matrix = matrix.copy()
        self.m = m
        self.etapas = []
        self.U = numpy.identity(m)
        self.L = numpy.identity(m)
        self.indp = indp.copy()
        self.z = numpy.empty(m)
        self.x = numpy.empty(m)

    def evaluate(self):

        for fila in range(self.m):
            suma1 = 0
            for columna in range(fila):
                suma1 += self.L.item(fila, columna)*self.U.item(columna, fila)

            # self.L.[fila,fila] = 1
            self.U[fila, fila] = self.matrix.item(fila, fila) - suma1

            for i in range(fila+1, self.m):
                suma2 = 0
                for columna in range(fila):
                    suma2 += self.L.item(i, columna)*self.U.item(columna, fila)
                if self.L.item(fila, fila) != 0:
                    self.L[i, fila] = (self.matrix.item(
                        i, fila) - suma2)/self.U.item(fila, fila)

            for j in range(fila+1, self.m):
                suma3 = 0
                for columna in range(fila):
                    suma3 += self.L.item(fila, columna)*self.U.item(columna, j)

                if self.L.item(fila, fila) != 0:
                    self.U[fila, j] = (self.matrix.item(fila, j) - suma3)

        detU = 1
        detL = 1
        for each in self.U.diagonal(0, 0):
            detU *= each

        prod = detU * detL
        if prod != 0:
            for i in range(self.m):
                suma = 0
                for p in range(i):
                    suma += (self.L.item(i, p)*self.z.item(p))
                try:
                    self.z[i] = (self.indp.item(i)-suma)/self.L.item(i, i)
                except:
                    raise ZeroDivisionError
            for i in range(self.m-1, -1, -1):
                suma = 0
                for p in range(i+1, self.m):
                    suma = suma+(self.U.item(i, p)*self.x.item(p))
                try:
                    self.x[i] = ((self.z.item(i)-suma)/self.U.item(i, i))
                except:
                    raise ZeroDivisionError
        else:
            raise ZeroDeterminantException
        return self.L, self.U, self.z, self.x
