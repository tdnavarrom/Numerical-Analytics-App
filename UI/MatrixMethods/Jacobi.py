import numpy
from ..Messages.errors import InvalidIterException
from ..Messages.errors import InvalidLambdaException
from ..Messages.errors import InvalidToleranceException
from ..Messages.errors import InvalidMatrix

class Jacobi:

    def __init__(self,matrix,m,indp,x0):
        self.matrix = matrix.copy()
        self.m = m
        self.etapas = []
        self.values = []
        self.x = numpy.empty(m)
        self.indp = indp.copy()
        self.x0 = x0.copy()
        self.x1 = numpy.empty(m)
        self.res = numpy.empty(m)
        self.aux = []
        self.dispersion = 0

    def evaluate(self, tol, niter, relajacion):

        #CONTROLES ITERACION, TOLERANCIA Y LAMBDA    
        if niter <1 and float(niter).is_integer():
            print("invalid iter")
            raise InvalidIterException
        if tol <0 and tol>1 and  not(float(tol).is_integer()):
            print("invalid tol")
            raise InvalidToleranceException
        if relajacion <0:
            print("Invalid lambda")
            raise InvalidLambdaException
        
        #CONTROL MATRIZ DIAGONAL DOMINANTE
        for i in range(self.m):
            suma  = 0
            for j in range(self.m):
                if j!= i:
                    suma+= abs(self.matrix.item(i,j))
                    print(f"sume {self.matrix.item(i,j)}")
        
            if suma > abs(self.matrix.item(i,i)):
                raise InvalidMatrix


        #METODO JACOBI
        cont  = 0
        self.dispersion = float(tol + 1)

        self.values.append([cont, str(self.x0), self.dispersion])
        
                
        while (self.dispersion > tol) and (cont < niter):
            #print("entro while")
            #print([cont, str(self.x0), self.dispersion])

            for i in range(self.m):
                suma = 0
                for j in range(self.m):
                    if j != i:
                        suma += (self.matrix.item(i, j)*self.x0.item(j))
                    try:
                        self.x1[i] = (self.indp.item(i) - suma)/self.matrix.item(i, i)
                    except:
                        raise ZeroDivisionError

                
            self.aux = self.x0 - self.x1
            try:
                self.dispersion = numpy.linalg.norm(self.aux)/numpy.linalg.norm(self.x1)
            except:
                raise ZeroDivisionError
     
            if relajacion != 0:
                for i in range(self.m):
                    self.x1[i] = (relajacion*self.x1.item(i))+((1-relajacion)*self.x0.item(i))
                
            self.x0 = self.x1.copy()
            cont += 1

            print([cont, str(self.x0), self.dispersion])
            self.values.append([cont, str(self.x0), self.dispersion])
        
        if self.dispersion < tol:
            print(f"{self.x1} es aproximación con una tolerancia = {tol}")
        else:
            print(f"Fracasó en {niter} iteraciones")
    
    def tabla_values(self):
        return self.values
