import numpy
 
class Pivoteo:
 
    def __init__(self,matrix,m):
        self.matrix = matrix.copy()
        self.m = m
        self.etapas = []
        self.x_pos=[]
    
    def evaluate_total(self):
        for i in range(self.m):
            self.x_pos.append(i)

        for fila in range(self.m):

            mayor = 0
            filaMayor = "False"
            for columna in range(fila,self.m):
                for k in range(self.m):
                    if abs(self.matrix.item(columna, k)) > abs(self.matrix.item(fila, fila)) and (abs(self.matrix.item(columna, k))) > abs(mayor):
                        print(f"{self.matrix.item(columna,k)} es mayor que {self.matrix.item(fila,fila)} y el mayor global: {mayor}")
                        mayor = self.matrix.item(columna,k)
                        filaMayor = columna
                        columnaMayor = k

            if filaMayor != "False":
                #Cambio de Filas
                temp = self.matrix.take(fila,0)
                self.matrix[fila] = self.matrix.take(filaMayor,0)
                self.matrix[filaMayor] = temp
                print(f"Etapas:\n{self.matrix}\n\n")

                #actualizacion posicion de las x
                pos_temp = self.x_pos[fila]
                self.x_pos[fila] = self.x_pos[columnaMayor]
                self.x_pos[columnaMayor] = pos_temp

                #Cambio de columnas
                temp = self.matrix.take(fila,1)
                for k in range(self.m):
                    self.matrix[k,fila] = self.matrix.item(k,columnaMayor)
                for k in range(self.m):
                    self.matrix[k,columnaMayor] = temp[k]
                print(f"Etapas:\n{self.matrix}\n\n")
                self.etapas.append(self.matrix)
                
            for j in range(self.m):
                if j > fila:
                    multiplicador = (self.matrix.item(j, fila) / self.matrix.item(fila, fila))
                    #print(f"multiplicador para fila {fila} y columna {columna}: {multiplicador}")
                    for q in range(self.m+1):
                        self.matrix[j, q] = self.matrix.item(j,q) - (multiplicador * self.matrix.item(fila,q)) 
            print(f"Gauss:\n{self.matrix}\n\n")
        
        x = numpy.empty(self.m)
        x_text = ""
        for i in range(self.m,0,-1):
	        suma=0
	        for j in range(i,self.m):
		        suma=suma+self.matrix[i-1][j]*x[j]
	        #Obtener los valores de las variables
	        x[i-1]=((self.matrix[i-1][self.m]-suma)/self.matrix[i-1][i-1])	
        #Mostrar los valores de las variables
        for i in range(0,self.m):
	        #print(f"x{self.x_pos[i]} = {str(x[i])}")
            x_text+= f"x{self.x_pos[i]} = {str(x[i])}\n"


        return x_text, self.etapas
        
        
        


        # if (abs(self.matrix.item(fila, fila)) == 0 ):
        #     print(f"El sistema no tiene solución única")
        # elif (filaMayor != columna):
        #         pass
        #         #swapRows(a, filaMayor, columna)
    


    def evaluate_parcial(self):
        
        for fila in range(self.m):
            mayor = 0
            filaMayor = "False"
            for columna in range(fila,self.m):
                    if abs(self.matrix.item(columna, fila)) > abs(self.matrix.item(fila, fila)) and (abs(self.matrix.item(columna, fila))) > abs(mayor):
                        mayor = self.matrix.item(columna,fila)
                        filaMayor = columna


            if filaMayor != "False":
                temp = self.matrix.take(fila,0)
                self.matrix[fila] = self.matrix.take(filaMayor,0)
                self.matrix[filaMayor] = temp
                print(f"Etapas:\n{self.matrix}\n\n")

            for j in range(self.m):
                if j > fila:
                    multiplicador = (self.matrix.item(j, fila) / self.matrix.item(fila, fila))
                    #print(f"multiplicador para fila {fila} y columna {columna}: {multiplicador}")
                    for q in range(self.m+1):
                        self.matrix[j, q] = self.matrix.item(j,q) - (multiplicador * self.matrix.item(fila,q)) 
            print(f"Gauss:\n{self.matrix}\n\n")
            self.etapas.append(self.matrix)

        x_text = ""
        x = numpy.empty(self.m)
        for i in range(self.m,0,-1):
	        suma=0
	        for j in range(i,self.m):
		        suma=suma+self.matrix[i-1][j]*x[j]
	        #Obtener los valores de las variables
	        x[i-1]=((self.matrix[i-1][self.m]-suma)/self.matrix[i-1][i-1])	
        #Mostrar los valores de las variables
        for i in range(0,self.m):
	        #print("x"+str(i)+" = "+str(x[i]))
            x_text+= f"x{str(i)} = {str(x[i])}\n"

        return x_text,self.etapas




        # if (abs(self.matrix.item(fila, fila)) == 0 ):
        #     print(f"El sistema no tiene solución única")
        # elif (filaMayor != columna):
        #     pass    #swapRows(a, filaMayor, columna)
 
        # print(f"Etapas:\n{self.matrix}\n\n")