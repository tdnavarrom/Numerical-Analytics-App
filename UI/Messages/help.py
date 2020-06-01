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
            text = "Simple Gaussian Help"
        elif method =="Parcial Pivot":
            text = "Parcial Pivot Help"
        elif method =="Total Pivot":
            text = "Total Pivot Help"
        elif method =="Crout":
            text = "Crout Help"
        elif method =="Doolittle":
            text = "Doolittle Help"
        elif method =="Cholesky":
            text = "Cholesky Help"
        elif method =="Jacobi":
            text = "Jacobi Help"
        elif method =="Gauss-Seidel":
            text = "Gauss-Seidel Help"
        dialog.format_secondary_text(text)
        dialog.run()
        dialog.destroy()