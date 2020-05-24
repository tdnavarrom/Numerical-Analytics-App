import numpy



class Gauss:
    
    def __init__(self,matrix,m):
        self.matrix = matrix.copy()
        self.m = m
        self.etapas = []

    
    def evaluate(self):

        for fila in range(self.m+1):
            for columna in range(self.m):
                if columna > fila:
                    multiplicador = (self.matrix.item(columna, fila) / self.matrix.item(fila, fila))
                    #print(f"multiplicador para fila {fila} y columna {columna}: {multiplicador}")
                    for k in range(self.m+1):
                        self.matrix[columna, k] = self.matrix.item(columna,k) - (multiplicador * self.matrix.item(fila,k)) 
            
            #print(f"Etapas:\n{self.matrix}\n\n")
            self.etapas.append(self.matrix.copy())
        
        for i in range(self.m -1):
            print(self.etapas[i])
    
        x = numpy.empty(self.m)
        for i in range(self.m,0,-1):
	        suma=0
	        for j in range(i,self.m):
		        suma=suma+self.matrix[i-1][j]*x[j]
	        #Obtener los valores de las variables
	        x[i-1]=((self.matrix[i-1][self.m]-suma)/self.matrix[i-1][i-1])	
        #Mostrar los valores de las variables
        for i in range(0,self.m):
	        print("x"+str(i)+" = "+str(x[i]))

        return x, self.etapas


    