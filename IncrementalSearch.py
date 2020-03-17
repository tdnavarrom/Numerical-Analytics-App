import math

class IncrementalSearch:
    def __init__(self):
        self.values=[]

    def Operacion(self, initial_value,increment,item,Function):
        self.values.append([initial_value,Function.evaluate(initial_value)])
        if self.values[0][1]==0:
            print(f"{self.values[0][0]} es una raiz")
        else:
            if increment == 0:
                print("El valor asignado al incremento es incorrecto")
            else:
                if item<=0:
                    print("El valor del iterador es incorrecto")
                else:
                    cont=0
                    new_value=initial_value+increment
                    while (cont<item):
                        self.values.append([new_value,Function.evaluate(new_value)]) 
                        print(initial_value) 
                        valor_evaluado_nuevo=Function.evaluate(new_value)
                        if(self.values[cont][1]*valor_evaluado_nuevo<=0):
                            break
                        
                        new_value+=increment
                        cont+=1
                        
                    if self.values[cont][1]*valor_evaluado_nuevo<0:
                        print(f"Los valores [{round(self.values[cont][0],2)},{round(new_value,2)}] definen un intervalo")
                    else:
                        if self.values[cont][1]==0:
                            print(f"{round(self.values[cont][0],2)} es una raiz")
                        else:
                            if(valor_evaluado_nuevo==0):
                                print(f"{round(new_value,2)} es una raiz")
                            else:
                                print("Se presento un fraso en las num_iterations")
    
    def tabla_values(self):
        for x in self.values:
            print(x)
        return self.values
    

