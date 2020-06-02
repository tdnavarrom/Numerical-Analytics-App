from gi.repository import Gtk, Gdk
import gi

gi.require_version('Gtk', '3.0')

class Help():        
    def non_linear_equation_help(self, method):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, method)
        if method == "Incremental":
            text = "El metodo de la busqueda incremental funciona ingresando una funcion, un valor inferior y superior que conformaran un conjunto.\nDentro de este conjunto,utilizando el incremento ingresado se evalua la funcion en un valor hasta encontrar un cambio de signo o que f(x)=0.\n\n En el caso de un cambio de signo, la raiz esta dentro del intervalo, o en el caso de encontrar f(x)=0, la raiz es x. "
        elif method == "Bisection":
            text = "El metodo de Biseccion es un metodo para encontrar raices de una funcion.\n\nFunciona mediante ingresando un intervalo dentro del cual evaluar, con un numero de iteraciones y cierta tolerancia a la precision del resultado."
        elif method == "False Rule":
            text = "Dado un intervalo inicial [xi,xu], se encuentra el punto de interseccion del eje x con la recta secante que une los puntos (xi,f(xi) y (xu,f(xu) y se evalúa en la función f(x).\nLa función f debe estar definida en el intervalo [xi,xu], f debe de ser continua en el intervalo [xi,xu] y  f(xi)∗f(xu)<0."
        elif method == "Fixed Point":
            text = "El método de punto fijo reformula la ecuación f(x)=0 y genera una ecuación de la forma x=g(x) que permite encontrar un valor de x que al reemplazarlo en g su resultado sea el mismo, es decir que x sea invariable para g, y adicionalmente que la f(x) converja a cero.\n\nSe dispone de un intervalo [a,b] para el cual la función g es continua y se cumple que para todo valor de x en el intervalo, g(x) también pertenece al mismo intervalo. Además para garantizar la unicidad de dicho punto se debe cumplir que la derivada g′(x)<1 en el intervalo."
        elif method == "Newton":
            text = "Newton help"
        elif method == "Secant":
            text = "Secant Help"
        elif method == "Multiple Roots":
            text = "Multiple Roots Help"
        dialog.format_secondary_text(text)
        dialog.run()
        dialog.destroy()

    def linear_equations_help(self, method):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, method)
        if method == "Simple Gaussian":
            text = "El metodo de eliminacion Gausseana se aplica para resolver sistemas lineas de la forma Ax = b, Donde A es una matriz con los coeficientes de las ecuaciones organizadas en forma descendiente y b es un vector con las Ys de las ecuaciones.\n"
            text += "Se comienza generando una Matriz Aumentada (Ab) e iterativamente se calculan los coeficientes de tal manera que se haga la parte inferior de la matriz 0.\n" 
            text += "Luego de tener la matriz resuelta se le aplica sustitución regresiva para conocer los valores que satisfacen el sistema de ecuaciones."
        elif method =="Parcial Pivot":
            text = "Las estrategias de pivoteo son normalmente utilizadas conjuntamente con el metodo de eliminacion Gaussiana, sirven para reducir los efectos del error de redondeo.\n\n"  
            text += "- Para el pivoteo parcial, se pretende que el elemento de la diagonal sea el máximo en valor absoluto y se elige con los elementos de la misma columna a partir del akk, luego se realiza el intercambio entre la fila donde esta el mayor elemento y la fila k.\n\n"
        elif method =="Total Pivot":
            text = "Las estrategias de pivoteo son normalmente utilizadas conjuntamente con el metodo de eliminacion Gaussiana, sirven para reducir los efectos del error de redondeo.\n\n"
            text += "- Para el pivoteo total, se pretende buscar en la k-ésima etapa el el elemento mayor en valor absoluto entre todos los elementos, una vez se disponga del elemento mayor, se realizan cambios cambios entre filas y columnas con el objetivo de ubicar el mayor en la diagonal sobre la fila que actualmente se esta pivotando."
        elif method =="Crout":
            text =  "Hace parte de los métodos de LU para la factorización de matrices, donde una matriz A se factoriza en L(Triangular superior) y U(Triangular inferior).\n"
            text += "Dado Ax= b, se tendría LUx = b  y si Ux = z, entonces Lz = b. En este método especifico, La diagonal de L y U son iguales U[i][i] = 1.\n"
            text += "Luego de que se tiene la matriz factorizada, se hace sustitución progresiva con la matriz L y los resultados b para hallar los valores de z, luego se utiliza sustitución regresiva para hallar los valores de x, que serian la solución del sistema.\n"
        elif method =="Doolittle":
            text = "Hace parte de los métodos de LU para la factorización de matrices, donde una matriz A se factoriza en L(Triangular superior) y U(Triangular inferior).\n"
            text += "Dado Ax= b, se tendría LUx = b  y si Ux = z, entonces Lz = b. En este método especifico, La diagonal de L y U son iguales L[i][i] = 1.\n"
            text += "Luego de que se tiene la matriz factorizada, se hace sustitución progresiva con la matriz L y los resultados b para hallar los valores de z, luego se utiliza sustitución regresiva para hallar los valores de x, que serian la solución del sistema."
        elif method =="Cholesky":
            text =  "Hace parte de los métodos de LU para la factorización de matrices, donde una matriz A se factoriza en L(Triangular superior) y U(Triangular inferior).\n"
            text += "Dado Ax= b, se tendría LUx = b  y si Ux = z, entonces Lz = b. En este método especifico, La diagonal de L y U son iguales L[i][i] = U[i][i].\n"
            text += "Luego de que se tiene la matriz factorizada, se hace sustitución progresiva con la matriz L y los resultados b para hallar los valores de z, luego se utiliza sustitución regresiva para hallar los valores de x, que serian la solución del sistema.\n"
        elif method =="Jacobi":
            text =  "Jacobi es un método iterativo para determinar la solución de ecuaciones. Se basa en generar aproximaciones al resultado en base a una aproximación inicial.\n"
            text += "El método primero trata de convertir la matriz dada en una matriz diagonalmente dominante mediante permutaciones de filas y columnas. Posteriormente, se toma cada ecuación y se pone la variable de la diagonal en términos de las otras variables, luego de esto se haya la primera aproximación asignando valores iniciales a las variables usando las ecuaciones generadas anteriormente, los valores asignados se obtienen mediante los cálculos realizados en el mismo ciclo. Se repite este proceso hasta que el valor de la dispersión sea menor que el de la tolerancia, o hasta que se superen el número de iteraciones.\n"
        elif method =="Gauss-Seidel":
            text = "Gauss-Seidel es un método iterativo para determinar la solución de ecuaciones. Se basa en generar aproximaciones al resultado en base a una aproximación inicial.\n"
            text += "El método primero trata de convertir la matriz dada en una matriz diagonalmente dominante mediante permutaciones de filas y columnas. Posteriormente, se toma cada ecuación y se pone la variable de la diagonal en términos de las otras variables, luego de esto se haya la primera aproximación asignando valores iniciales a las variables usando las ecuaciones generadas anteriormente, los valores asignados se obtienen mediante los cálculos realizados en el mismo ciclo. Se repite este proceso hasta que el valor de la dispersión sea menor que el de la tolerancia, o hasta que se superen el número de iteraciones.\n"
            
        dialog.format_secondary_text(text)
        dialog.run()
        dialog.destroy()