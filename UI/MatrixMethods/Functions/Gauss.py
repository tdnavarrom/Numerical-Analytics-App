import numpy


class Gauss:
    
    def __init__(self,matrix,m):
        self.matrix = matrix.copy()
        self.m = m
        self.etapas = []
        self.fail = False

    
    def evaluate(self):

        for fila in range(self.m+1):
            for columna in range(self.m):
                if columna > fila:
                    try:
                        multiplicador = (self.matrix.item(columna, fila) / self.matrix.item(fila, fila))
                    except:
                        raise ZeroDivisionError

                    for k in range(self.m+1):
                        self.matrix[columna, k] = self.matrix.item(columna,k) - (multiplicador * self.matrix.item(fila,k)) 

            self.etapas.append(self.matrix.copy())

        self.x = numpy.empty(self.m)

        for i in range(self.m,0,-1):
	        suma = 0
	        for j in range(i,self.m):
		        suma = suma + self.matrix[i-1][j]*self.x[j]
	        #Obtener los valores de las variables
	        self.x[i-1] = ((self.matrix[i-1][self.m]-suma) / self.matrix[i-1][i-1])
        	
        
        return "Executed"
