from gi.repository import Gtk, Gdk
from UI.NonLineal.non_linear_control import Non_Linear_Control
from UI.MatrixMethods.linear_control import Linear_Control
#from UI.Interpolation.linear_control import Interpolation_Control
#from UI.Interpolation.Views.matrix_interpolation import Matrix_View_Interpolation

import gi
import math
import numpy as np
import pandas as pd
gi.require_version('Gtk', '3.0')


class Handler:
    def __init__(self, parameters, parameters2, parameters3):
        self.parameters = parameters
        self.parameters2 = parameters2
        self.parameters3 = parameters3
        self.non_lineal = Non_Linear_Control(parameters)
        self.lineal = Linear_Control(parameters2)
        #self.interpolation = Interpolation_Control(parameters3)

    def onDestroy(self, *args):
        Gtk.main_quit()

    def eval_method(self, button):
        method = self.parameters[0].get_active()
        if method == 0:
            self.non_lineal.incremental_method()
        elif method == 1:
            self.non_lineal.bisection_method()
        elif method == 2:
            self.non_lineal.false_rule_method()
        elif method == 3:
            self.non_lineal.fixed_point_method()
        elif method == 4:
            self.non_lineal.newton_method()
        elif method == 5:
            self.non_lineal.secant_method()
        elif method == 6:
            self.non_lineal.multiple_roots_method()

    def help_pressed(self, button):
        self.non_lineal.help_view()

    def table_pressed(self, button):
        self.non_lineal.table_view()

    def graph_pressed(self, button):
        self.non_lineal.graph_view()

####### EQUATION SYSTEM
    def evaluateMatrix_pressed(self, button):
        method = self.parameters2[4].get_active()
        if method == 0:
            self.lineal.evaluate_gauss()
        elif method == 1:
            self.lineal.evaluate_pivot_parcial()
        elif method == 2:
            self.lineal.evaluate_pivot_total()
        elif method == 3:
            self.lineal.evaluate_crout()
        elif method == 4:
            self.lineal.evaluate_doolittle()
        elif method == 5:
            self.lineal.evaluate_cholesky()
        elif method == 6:
            self.lineal.evaluate_jacobi()
        elif method == 7:
            self.lineal.evaluate_gauss_seidel()

    def helpMatrix_pressed(self, button):
        self.lineal.helpMatrix_view()

    def matrix_generate(self, button):
        self.lineal.matrix_generate_view()

    def initialValues_generate(self, button):
        self.lineal.initial_values_view()
'''
    #Interpolation
    def evaluateInterpolation_pressed(self, button):
        method = self.parameters3[0].get_active()
        print(method)

        if method == 0:
            self.interpolation.evaluate_NewtonInterpolation()
            matrix_gui = Matrix_View_Interpolation(self.values)
            Gtk.main()
        elif method == 1:
            self.interpolation.evaluate_LagrangeInterpolation()
        elif method == 2:
            self.interpolation.evaluar_linear_spline
        elif method == 3:
            self.interpolation.evaluar_quadratic_spline
        elif method == 4:
            self.interpolation.evaluar_cubic_spline
'''
