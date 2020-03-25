import math

class FalseRule:
    def __init__(self,xi,xs,tolerancia,iter):
        self.xi = xi
        self.xs =xs
        self.tolerancia = tolerancia
        self.iter = iter
    

    def operacion(self,xi,xs,tolerancia,iter,funcion):
        fxi = funcion.evaluate(xi)
        fxs = funcion.evaluate(xs)
        if fxi == 0:
            print(f"{xi} es una raiz")
        elif fxs == 0:
            print(f"{xs} es una raiz")
        elif fxi *fxs < 0:
            xm =xi-((fxi*(xi-xs))/(fxi-fxs))
            fxm = funcion.evaluate(xm)
            contador = 1
            error = tolerancia + 1

            print("++ XI ++ XS ++ XM ++ FXM ++")
            print("--------------------")
            print(f"++ {xi} ++ {xs} ++ {xm} ++ {fxm} ++")

            while error > tolerancia and fxm != 0 and contador < iter:
                if fxm * fxi < 0:
                    xs = xm
                    fxs = fxm
                else:
                    xi = xm
                    fxi = fxm
                xaux = xm
                xm = xi-((fxi*(xi-xs))/(fxi-fxs))
                fxm = funcion.evaluate(xm)
                error = abs(xm-xaux)
                contador+=1

                print(f"++ {xi} ++ {xs} ++ {xm} ++ {fxm} ++")
            
            if fxm == 0:
                print(f"{xm} es raiz")
            elif (error < tolerancia):
                print(f"{xm} es una aprox. a una raiz con tolerancia = {tolerancia}")
            else:
                print(f"fracaso en {iter} iteraciones")
        else:
            print("el intervalo es inadecuado")