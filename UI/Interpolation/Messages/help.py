from gi.repository import Gtk, Gdk
import gi

gi.require_version('Gtk', '3.0')

class Help():

    def interpolacion_help(self, method):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, method)
        if method == "Newton":
            text = "El metodo de interpolacion de Newton, toma como parámetros un conjunto de puntos y un valor a evaluar y usando una aproximación de las series de Taylor, calcula el polinomio correspondiente y evalúa el valor.\n\n"
            text += "p(x) = b0 + b1(x-x0) + b2(x-x0)(x-x1) + b3(x-x0)(x-x1)(x-x2)\n\n"
            text += "Donde los bi son la diagonal de la matriz aux y se calculan teniendo en cuenta las filas anteriores. Así\n"
            text += "b0 = f[x0]\nb1 = f[x1, x0]\nb2 = f[x2, x1, x0]\nbn = f[xn,...,x0]"
        elif method == "Lagrange":
            text = "El objetivo del método es encontrar un polinomio interpolante que represente una función o un problema sin definición exacta, que pase por un conjunto de puntos dados."
            text += "El polinomio interpolante de Lagrange se presenta de la siguiente manera:\n\n"
            text += "1. Se consideran n los puntos x dados de la función, con su respectivo valor de y; dados estos puntos existe un único polinomio de grado a lo sumo de n-1 que pase por ellos. \n"
            text += "2. Para poder definir el polinomio se hallan los valores de cada Li(x) con i desde 1 hasta n.\n"
            text += "3. Una vez calculados los valores de L, podemos confirmar el polinomio y posteriormente, algunos cálculos adicionales.\n"
            text += "4. Los valores de L se pueden calcular de la siguiente estructura, adicionalmente se puede observar la estructura del polinomio de Lagrange."
        else:
            text = "En el subcampo matemático del análisis numérico, un spline es una curva diferenciable definida en porciones mediante polinomios.\n"
            text += "En los problemas de interpolación, se utiliza a menudo la interpolación mediante splines porque da lugar a resultados similares\n"
            text += "requiriendo solamente el uso de polinomios de bajo grado, evitando así las oscilaciones, indeseables en la mayoría de las aplicaciones, encontradas al interpolar mediante polinomios de grado elevado.\n"
            text += "Para el ajuste de curvas, los splines se utilizan para aproximar formas complicadas. La simplicidad de la representación y la facilidad\n" 
            text += "de cómputo de los splines los hacen populares para la representación de curvas en informática, particularmente en el terreno de los gráficos por ordenador."



        dialog.format_secondary_text(text)
        dialog.run()
        dialog.destroy()
