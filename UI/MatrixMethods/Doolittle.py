import numpy

class Doolittle:

    def __init__(self,matrix,m,indp):
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
            
            #self.L.[fila,fila] = 1
            self.U[fila, fila] = self.matrix.item(fila, fila) - suma1
            
            #self.etapas.append(self.matrix.copy())

            #for s in range(self.m -1):
            #    print(self.etapas[s])
            
            for i in range(fila+1, self.m):
                suma2 = 0
                for columna in range(fila):
                    suma2 += self.L.item(i, columna)*self.U.item(columna, fila)
                if self.L.item(fila, fila)!=0:
                    self.L[i, fila] = (self.matrix.item(i, fila) - suma2)/self.U.item(fila,fila)
                else:
                    print("Posiblemente no tiene solución")
            
            for j in range(fila+1,self.m):
                suma3 = 0
                for columna in range(fila):
                    suma3 += self.L.item(fila, columna)*self.U.item(columna, j)

                if self.L.item(fila, fila)!=0:  
                    self.U[fila, j] = (self.matrix.item(fila, j) - suma3)
                else:
                    print("Posiblemente el sistema no tiene solución")
        
       

        detU = 1
        detL=1
        for each in self.U.diagonal(0,0):
            detU*= each
        
        prod = detU * detL
        if prod != 0:
            for i in range(self.m):
                suma = 0
                for p in range(i):
                    suma+= (self.L.item(i,p)*self.z.item(p))
                self.z[i] = (self.indp.item(i)-suma)/self.L.item(i,i)

            for i in range(self.m-1,-1,-1):
	            suma=0
	            for p in range(i+1,self.m):
		            suma=suma+(self.U.item(i,p)*self.x.item(p))
	            self.x[i]=((self.z.item(i)-suma)/self.U.item(i,i))
            
        else:
            print("La determinante es igual a 0, por lo tanto tiene infinitas soluciones, o ninguna.")
            return
        

      
        print(f"L:\n {self.L}\n\nU:\n{self.U}\n")
        for each in range(self.m):
            print(f"x{each} = {self.x[each]}")
        return self.L,self.U, self.z, self.x
