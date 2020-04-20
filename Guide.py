from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')

class Guide(Gtk.Grid):

    def __init__(self):
        self.grid = Gtk.Grid()
        self.grid = self.create_ui()


    def create_ui(self):
        grid = Gtk.Grid()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        welcome_label = Gtk.Label()
        welcome_label.set_markup("<big>Guide</big>")
        welcome_label.set_line_wrap(True)
        vbox.pack_start(welcome_label, True, True, 0)

        guide_text = Gtk.Label()

        guide_text.set_markup(
            "This is the Guide for the application. Please <b>follow the syntax</b> listed below for the equations.\n"
            'e^n ==> exp(n)\n'
            'x^n ==> x**n\n'
            'ln(x) ==> log(x)\n'
            'cos(x) ==> cos(x)\n'
            'sin(x) ==> sin(x)\n\n'

            "El metodo de la <b>busqueda incremental</b> funciona ingresando una funcion, un valor inferior y superior que conformaran un conjunto.\n"
            "Dentro de este conjunto,utilizando el incremento ingresado se evalua la funcion en un valor hasta encontrar un cambio de signo o que f(x)=0.\n"
            "En el caso de un cambio de signo, la raiz esta dentro del intervalo, o en el caso de encontrar f(x)=0, la raiz es x.\n\n"

            "El metodo de <b>Biseccion</b> es un metodo para encontrar raices de una funcion.\n"
            "Funciona mediante ingresando un intervalo dentro del cual evaluar, con un numero de iteraciones y cierta tolerancia a la precision del resultado.\n\n"

            "El metodo de <b>Regla Falsa</b> funciona mediante un intervalo inicial [xi,xu], se encuentra el punto de interseccion del eje x con la recta secante que une los puntos (xi,f(xi) y (xu,f(xu) y se evalúa en la funcion f(x).\n"
            "La funcion f debe estar definida en el intervalo [xi,xu], f debe de ser continua en el intervalo [xi,xu] y  f(xi)∗f(xu) &lt; 0.\n\n"

            "El metodo de <b>Punto Fijo</b> reformula la ecuación f(x)=0 y genera una ecuacion de la forma x=g(x) que permite encontrar un valor de x que al reemplazarlo en g su resultado sea el mismo, es decir que x sea invariable para g, y adicionalmente que la f(x) converja a cero.\n"
            "Se dispone de un intervalo [a,b] para el cual la función g es continua y se cumple que para todo valor de \'x\' en el intervalo, g(x) también pertenece al mismo intervalo. Además para garantizar la unicidad de dicho punto se debe cumplir que la derivada g\′(x) &lt; 1 en el intervalo.\n\n"
        )


        guide_text.set_line_wrap(True)
        vbox.pack_start(guide_text, True, True, 0)

        grid.attach(vbox, 0, 0, 2, 2)

        return grid
