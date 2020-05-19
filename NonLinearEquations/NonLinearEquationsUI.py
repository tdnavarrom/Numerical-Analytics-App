from gi.repository import Gtk, Gdk
from .functions.IncrementalSearch import IncrementalSearch as ISearch
from .functions.BisectionSearch import Bisection as BSearch
from .functions.FalseRuleSearch import FalseRule as FSearch
from .functions.FixedPointSearch import FixedPoint as FPSearch
from .functions.NewtonSearch import Newton as NSearch
from .functions.SecantSearch import Secant as SSearch
from .functions.MultipleRoots import MultipleRoots as MRoots
from .graph import *
from .table import *
from .matrixTable import *
from .derivate import *
import gi
import math
import numpy as np
import pandas as pd
gi.require_version('Gtk', '3.0')


class Handler:
    def __init__(self, parameters, parameters2):
        self.parameters = parameters
        self.parameters2 = parameters2

    def onDestroy(self, *args):
        Gtk.main_quit()

    def eval_method(self, button):
        method = self.parameters[0].get_active()
        if method == 0:
            self.incremental_search_method()
        elif method == 1:
            self.bisection_method()
        elif method == 2:
            self.false_rule_method()
        elif method == 3:
            self.fixed_point_method()
        elif method == 4:
            self.newton_method()
        elif method == 5:
            self.secant_method()
        elif method == 6:
            self.multiple_roots_method()

    def incremental_search_method(self):
        try:
            initial_value = float(self.parameters[7].get_text())
            increment = float(self.parameters[6].get_text())
            iterations = float(self.parameters[5].get_text())
            func = self.parameters[3].get_text()

            self.incremental_Search = ISearch()
            range_of_root = self.incremental_Search.evaluate(
                initial_value, increment, iterations, func)
            self.parameters[9].set_text(str(range_of_root))

            self.table = self.incremental_Search.values
            self.table_names = ["Iter", "x Value",
                                "F(x) value"]
            self.type = "Incremental_search"
        except:
            self.parameters[9].set_text(
                "Seleccione el metodo acorde a trabajar o ingrese los valores")

    def bisection_method(self):
        try:
            error = self.parameters[1].get_active()

            inferior_value = float(self.parameters[7].get_text())
            superior_value = float(self.parameters[8].get_text())
            tolerance = float(self.parameters[10].get_text())
            iterations = float(self.parameters[5].get_text())
            func = self.parameters[3].get_text()

            self.bisection_Search = BSearch()
            range_of_root = self.bisection_Search.evaluate(
                inferior_value, superior_value, tolerance, iterations, func, error)

            self.parameters[9].set_text(str(range_of_root))
            self.table = self.bisection_Search.values
            self.table_names = ["Iter", "Xi", "Xu", "Xm", "F(Xm)", "Error"]
            self.type = "Bisection"
        except:
            self.parameters[9].set_text(
                "Seleccione el metodo acorde a trabajar o ingrese los valores")

    def false_rule_method(self):
        try:

            error = self.parameters[1].get_active()

            inferior_value = float(self.parameters[7].get_text())
            superior_value = float(self.parameters[8].get_text())
            tolerance = float(self.parameters[10].get_text())
            iterations = float(self.parameters[5].get_text())
            func = self.parameters[3].get_text()

            self.false_rule_Search = FSearch()
            range_of_root = self.false_rule_Search.evaluate(
                inferior_value, superior_value, tolerance, iterations, func, error)
            self.parameters[9].set_text(str(range_of_root))
            self.table = self.false_rule_Search.values
            self.table_names = ["Iter", "Xi", "Xu", "Xm", "F(Xm)", "Error"]
            self.type = "False Rule"
        except:
            self.parameters[9].set_text(
                "Seleccione el metodo acorde a trabajar o ingrese los valores")

    def fixed_point_method(self):
        try:
            error = self.parameters[1].get_active()

            initial_value = float(self.parameters[7].get_text())
            tolerance = float(self.parameters[10].get_text())
            iterations = float(self.parameters[5].get_text())
            func = self.parameters[3].get_text()
            g_func = self.parameters[4].get_text()

            self.fixed_point_Search = FPSearch()
            range_of_root = self.fixed_point_Search.evaluate(
                initial_value, tolerance, iterations, func, g_func, error)
            self.parameters[9].set_text(str(range_of_root))
            self.table = self.fixed_point_Search.values
            self.table_names['iter', 'x Value', 'F(x) Value', 'Error']
            self.type = "Fixed Point"
        except:
            self.parameters[9].set_text(
                "Seleccione el metodo acorde a trabajar o ingrese los valores")

    def newton_method(self):
        try:
            error = self.parameters[1].get_active()

            initial_value = float(self.parameters[7].get_text())
            tolerance = float(self.parameters[10].get_text())
            iterations = float(self.parameters[5].get_text())
            func = self.parameters[3].get_text()
            d_func = derivate_function(self.parameters[3].get_text())

            self.newton_Search = NSearch()
            range_of_root = self.newton_Search.evaluate(
                tolerance, initial_value, iterations, func, d_func, error)
            self.parameters[9].set_text(str(range_of_root))

            self.table = self.newton_Search.values
            self.table_names = ['Iter', 'Xn', 'f(Xn)', 'f\'(Xn)', 'Error']
            self.type = "Newton"
        except:
            self.parameters[9].set_text(
                "Seleccione el metodo acorde a trabajar o ingrese los valores")

    def secant_method(self):
        try:
            error = self.parameters[1].get_active()

            inferior_value = float(self.parameters[7].get_text())
            superior_value = float(self.parameters[8].get_text())
            tolerance = float(self.parameters[10].get_text())
            iterations = float(self.parameters[5].get_text())
            func = self.parameters[3].get_text()

            self.secant_Search = SSearch()
            range_of_root = self.secant_Search.evaluate(tolerance,
                                                        inferior_value, superior_value, func, iterations, error)
            self.parameters[9].set_text(str(range_of_root))
            self.table = self.secant_Search.values
            self.table_names = ['Iter', 'Xn', 'f(Xn)', 'Error']
            self.type = "Secant"
        except:
            self.parameters[9].set_text(
                "Seleccione el metodo acorde a trabajar o ingrese los valores")

    def multiple_roots_method(self):
        try:
            error = self.parameters[1].get_active()

            initial_value = float(self.parameters[7].get_text())
            tolerance = float(self.parameters[10].get_text())
            iterations = float(self.parameters[5].get_text())
            func = self.parameters[3].get_text()
            d_func = derivate_function(self.parameters[3].get_text())
            dd_func = derivate_function(d_func)
            self.multiple_roots = MRoots()
            range_of_root = self.multiple_roots.evaluate(
                tolerance, initial_value, iterations, func, d_func, dd_func, error)
            self.parameters[9].set_text(str(range_of_root))
            self.table = self.multiple_roots.values
            self.table_names = ['Iter', 'Xn',
                                'f(Xn)', 'f\'(Xn)', 'f\'\'(Xn)', 'Error']
            self.type = "Multiple Roots"
        except:
            self.parameters[9].set_text(
                "Seleccione el metodo acorde a trabajar o ingrese los valores")

    def help_pressed(self, button):
        method = self.parameters[0].get_active()
        if method == 0:
            self.on_IncHelp_clicked()
        elif method == 1:
            self.on_BisectHelp_clicked()
        elif method == 2:
            self.on_FruleHelp_clicked()
        elif method == 3:
            self.on_FpointHelp_clicked()
        elif method == 4:
            self.on_Newtonhelp_clicked()
        elif method == 5:
            self.on_Sechelp_clicked()
        elif method == 6:
            self.on_Mroothelp_clicked()

    def on_IncHelp_clicked(self):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Incremental Search Help")
        dialog.format_secondary_text(
            "El metodo de la busqueda incremental funciona ingresando una funcion, un valor inferior y superior que conformaran un conjunto.\nDentro de este conjunto,utilizando el incremento ingresado se evalua la funcion en un valor hasta encontrar un cambio de signo o que f(x)=0.\n\n En el caso de un cambio de signo, la raiz esta dentro del intervalo, o en el caso de encontrar f(x)=0, la raiz es x. ")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_BisectHelp_clicked(self):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Bisection Search Help")
        dialog.format_secondary_text(
            "El metodo de Biseccion es un metodo para encontrar raices de una funcion.\n\nFunciona mediante ingresando un intervalo dentro del cual evaluar, con un numero de iteraciones y cierta tolerancia a la precision del resultado.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_FruleHelp_clicked(self):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "False Rule Help")
        dialog.format_secondary_text(
            "Dado un intervalo inicial [xi,xu], se encuentra el punto de interseccion del eje x con la recta secante que une los puntos (xi,f(xi) y (xu,f(xu) y se evalúa en la función f(x).\nLa función f debe estar definida en el intervalo [xi,xu], f debe de ser continua en el intervalo [xi,xu] y  f(xi)∗f(xu)<0.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_FpointHelp_clicked(self):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Fixed Point Search Help")
        dialog.format_secondary_text(
            "El método de punto fijo reformula la ecuación f(x)=0 y genera una ecuación de la forma x=g(x) que permite encontrar un valor de x que al reemplazarlo en g su resultado sea el mismo, es decir que x sea invariable para g, y adicionalmente que la f(x) converja a cero.\n\nSe dispone de un intervalo [a,b] para el cual la función g es continua y se cumple que para todo valor de x en el intervalo, g(x) también pertenece al mismo intervalo. Además para garantizar la unicidad de dicho punto se debe cumplir que la derivada g′(x)<1 en el intervalo.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_Newtonhelp_clicked(self):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Newton Help")
        dialog.format_secondary_text(
            "Newton Help")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_Sechelp_clicked(self):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Secant Help")
        dialog.format_secondary_text(
            "Secant help")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_Mroothelp_clicked(self):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Multiple Roots Help")
        dialog.format_secondary_text(
            "Multiple Roots help")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def table_pressed(self, button):
        tree = TreeView(self.table, self.table_names, self.type)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()

    def graph_pressed(self, button):
        func = self.parameters[3].get_text()
        initial_value = float(self.parameters[7].get_text()) - 100
        iterations = float(self.parameters[5].get_text())
        graphic(func, initial_value, iterations)
    
    def matrix_generate(self, button):
        rows = int(self.parameters2[0].get_text())
        columns = rows + 1
        tree = TreeView(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        
    
