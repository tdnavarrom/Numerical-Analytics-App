import gi
import math
import numpy as np
import pandas as pd
gi.require_version('Gtk', '3.0')
from .table import *
from .functions.IncrementalSearch import IncrementalSearch as ISearch
from .functions.BisectionSearch import Bisection as BSearch
from gi.repository import Gtk

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


    def table_pressed(self, button):
        tree = TreeView(self.table, self.table_names, self.type)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
