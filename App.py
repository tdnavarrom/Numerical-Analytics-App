import tkinter
import tkinter.ttk as tk
import math
import numpy
from pandastable import Table, TableModel
import pandas as pd
from matplotlib import pyplot
from Function import Function
from IncrementalSearch import IncrementalSearch


class App:

    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("Metodos Numericos")
        self.root.config(width=600, height=600)
        self.menu = tkinter.Frame(self.root)
        self.valido=False
    
    def clear(self):
        for widget in self.menu.winfo_children():
            widget.destroy()

    def functionVerify(self,function,initial_value):
        if(function==''):
            return True
        else: 
            try:
                function=Function(function)
                function.evaluate(initial_value)
                return False
            except:
                return True
                
    
    def verify(self,function,initial_value,increment,num_iterations):
        error=""
        if(self.functionVerify(function,initial_value)):
            error+="La function es invalida, \n Los comandos son: Potencia x**2 \n Raiz= sqrt(x) \n Logaritmo natura= log(x) \n pi= pi \n seno,cose,tangente= sen(x),cos(x),tan(x)"
        if(increment==0):
            error+="\nEl increment ingresado es invalido "
        if(num_iterations==0):
            error+="\nLas num_iterations ingresadas son invalidas "
        if error!="":
            self.windowError(error)
        else:
            self.valido=True

    def windowError(self,error):
        self.valido=False
        window = tkinter.Toplevel()
        window.wm_title("Error")
        texto= tk.Label(window, text=error)
        texto.grid(row=0, column=0)
        cerrar = tk.Button(window, text="Okay", command=window.destroy)
        cerrar.grid(row=1, column=0)


    def drawFunction(self,function,posicion_inicial,posicion_final,increment):
        self.verify(function,posicion_inicial,posicion_final,posicion_final)
        if(self.valido):
            function=Function(function)
            
            x = numpy.arange(posicion_inicial, posicion_final,increment)
            pyplot.plot(x, [function.evaluate(i) for i in x])

            pyplot.axhline(0, color="black")
            pyplot.axvline(0, color="black")


            pyplot.show()




    def mainMenu(self):
        self.menu.grid()
        self.clear()
        ecuaciones_no_lineales=tkinter.Button(self.menu,width=80,height=7,text="Ecuaciones no Lineales", command=self.chapter1).pack()

    def chapter1(self):
        self.clear()
        IncrementalSearch_boton=tkinter.Button(self.menu,width=80,height=7,text="Busqueda Incremental", command=self.executeIncrementalSearch).pack()
        biseccion_boton=tkinter.Button(self.menu,width=80,height=7, text="Biseccion", command=self.ejecutar_seccion1_biseccion).pack()
        regla_falsa_boton=tkinter.Button(self.menu,width=80,height=7, text="Regla Falsa", command=self.ejecutar_seccion1_regla_falsa).pack()
        punto_fijo_boton=tkinter.Button(self.menu,width=80,height=7, text="Punto Fijo", command=self.ejecutar_seccion1_punto_fijo).pack()
    
    def executeIncrementalSearch(self):
        self.clear()

        function=tkinter.StringVar()
        initial_value=tkinter.DoubleVar()
        increment=tkinter.DoubleVar()
        num_iterations=tkinter.DoubleVar()

        texto_function=tk.Label(self.menu, text="function f(x)").place(x=40,y=20)
        texto_initial_value=tk.Label(self.menu, text="Initial Value").place(x=40,y=60)
        texto_increment=tk.Label(self.menu, text="Increment").place(x=210,y=60)
        texto_num_iterations=tk.Label(self.menu, text="# of iterations").place(x=365,y=60)

        entrada_function = tk.Entry(self.menu,textvariable=function,justify=tkinter.CENTER,width=70).place(x=120,y=20)
        entrada_initial_value = tk.Entry(self.menu,textvariable =initial_value,justify=tkinter.CENTER,width=10).place(x=120,y=60)
        entrada_increment = tk.Entry(self.menu,textvariable =increment,justify=tkinter.CENTER,width=10).place(x=280,y=60)
        entrada_num_iterations = tk.Entry(self.menu,textvariable =num_iterations,justify=tkinter.CENTER,width=10).place(x=440,y=60)

        
        confirmar = tk.Button(self.menu, text="Confirm",command=lambda: self.verify(function.get(),initial_value.get(),increment.get(),num_iterations.get())).place(x=200,y=100)
        Volver = tk.Button(self.menu, text="Return",command=self.chapter1).place(x=300,y=100)
        
        graficar = tkinter.Button(self.menu,width=70,height=4, text="Graph",command=lambda: self.drawFunction(function.get(),initial_value.get(),math.fabs(initial_value.get())+math.fabs((increment.get()*num_iterations.get())),increment.get())).place(x=40,y=200)
        buscar=tkinter.Button(self.menu,width=70,height=4, text="Execute search",command=lambda: self.ejecutar_IncrementalSearch(function.get(),initial_value.get(),increment.get(),num_iterations.get())).place(x=40,y=300)

    def ejecutar_seccion1_biseccion(self):
        pass

    def ejecutar_seccion1_regla_falsa(self):
        pass

    def ejecutar_seccion1_punto_fijo(self):
        pass

    def ejecutar_IncrementalSearch(self,function,initial_value,increment,num_iterations):
        self.verify(function,initial_value,increment,num_iterations)
        if(self.valido):
            search=IncrementalSearch()
            converted_function=Function(function)
            search.Operacion(initial_value,increment,num_iterations,converted_function)
            self.tabla_values(search.tabla_values())

    def color_negative_red(self):
        color = 'red'
        return 'color: %s' % color
    def tabla_values(self,search):
        window = tkinter.Toplevel()
        window.wm_title("Tabla de values")
        df = pd.DataFrame(search,columns=['Posicion','Valor'])
        table = pt = Table(window, dataframe=df,showtoolbar=True, showstatusbar=True)
        pt.show()

    def ejecutar_seccion2(self):
        pass
    
    def ejecutar_seccion3(self):
        pass

    def ejecutar_seccion4(self):
        pass


 
