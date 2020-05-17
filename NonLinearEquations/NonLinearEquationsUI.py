import gi
import math
import numpy as np
import pandas as pd
gi.require_version('Gtk', '3.0')
from .derivate import *
from .table import *
from .functions.MultipleRoots import MultipleRoots as MRoots
from .functions.SecantSearch import Secant as SSearch
from .functions.NewtonSearch import Newton as NSearch
from .functions.FixedPointSearch import FixedPoint as FPSearch
from .functions.FalseRuleSearch import FalseRule as FSearch
from .functions.BisectionSearch import Bisection as BSearch
from .functions.IncrementalSearch import IncrementalSearch as ISearch
from gi.repository import Gtk, Gdk

class Handler:
    def __init__(self, parameters):
        self.parameters = parameters

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
            self.table_names= ["Iter", "x Value",
                            "F(x) value"]
            self.type = "Incremental_search"
        except:
            self.parameters[9].set_text("Seleccione el metodo acorde a trabajar o ingrese los valores")

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
            self.table_names =["Iter", "Xi", "Xu","Xm", "F(Xm)", "Error"]
            self.type = "Bisection"
        except:
            self.parameters[9].set_text("Seleccione el metodo acorde a trabajar o ingrese los valores")


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
            self.table_names =["Iter", "Xi", "Xu","Xm", "F(Xm)", "Error"]
            self.type = "False Rule"
        except:
            self.parameters[9].set_text("Seleccione el metodo acorde a trabajar o ingrese los valores")

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
            self.table_names['iter', 'x Value','F(x) Value', 'Error']
            self.type = "Fixed Point"
        except:
            self.parameters[9].set_text("Seleccione el metodo acorde a trabajar o ingrese los valores")

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
            self.parameters[9].set_text("Seleccione el metodo acorde a trabajar o ingrese los valores")

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
            self.parameters[9].set_text("Seleccione el metodo acorde a trabajar o ingrese los valores")

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
            self.table_names = ['Iter', 'Xn', 'f(Xn)','f\'(Xn)', 'f\'\'(Xn)', 'Error']
            self.type = "Multiple Roots"
        except:
            self.parameters[9].set_text("Seleccione el metodo acorde a trabajar o ingrese los valores")

    def table_pressed(self, button):
        tree = TreeView(self.table, self.table_names, self.type)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
