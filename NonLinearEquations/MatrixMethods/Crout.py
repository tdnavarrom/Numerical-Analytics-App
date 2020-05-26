import numpy


class Crout:

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

        for k in range(self.m):
            suma1 = 0
            #self.U[k,k] = 1
            for p in range(k):
                suma1+= (self.L.item(k,p) * self.U.item(p,k))
            
            self.L[k,k] = self.matrix.item(k,k) - suma1

            for i in range(k+1,self.m):
                suma2 = 0
                for p in range(k):
                    suma2 += (self.L.item(i,p) * self.U.item(p,k))
                if self.L.item(k, k)!=0:
                    self.L[i,k] = self.matrix.item(i,k) - suma2 #OJO
                else:
                    print("Posiblemente no tiene solución")

            for j in range(k+1,self.m):
                suma3 = 0
                for p in range(k):
                    suma3+= (self.L.item(k,p) * self.U.item(p,j))
                if self.L.item(k, k)!=0:
                    self.U[k,j] = (self.matrix.item(k,j)-suma3)/float(self.L.item(k,k))
                else:
                    print("Posiblemente no tiene solución")
            print(f"L:\n{str(self.L)}\nU:\n{str(self.U)}")
            self.etapas.append(f"L:\n{str(self.L)}\nU:\n{str(self.U)}")
            

        detU = 1
        detL=1
        
        for each in self.L.diagonal(0,0):
            detL*= each
        
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
		            suma= suma+ self.U.item(i,p)*self.x[p]
	            self.x[i]=((self.z.item(i)-suma)/self.U.item(i,i))
            
        else:
            print("La determinante es igual a 0, por lo tanto tiene infinitas soluciones, o ninguna.")
            return
        

      
        #print(f"L:\n {self.L}\n\nU:\n{self.U}\n")
        x_text = ""
        for each in range(self.m):
            print(f"x{each} = {self.x[each]}")
            x_text+=f"x{each}= {self.x[each]}\n"
            


        return x_text, self.etapas

