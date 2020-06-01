from gi.repository import Gtk, Gdk
from .functions.IncrementalSearch import IncrementalSearch as ISearch
from .functions.BisectionSearch import Bisection as BSearch
from .functions.FalseRuleSearch import FalseRule as FSearch
from .functions.FixedPointSearch import FixedPoint as FPSearch
from .functions.NewtonSearch import Newton as NSearch
from .functions.SecantSearch import Secant as SSearch
from .functions.MultipleRoots import MultipleRoots as MRoots
from .MatrixMethods.Gauss import Gauss
from .MatrixMethods.Pivoteo import Pivoteo
from .MatrixMethods.Pivoteo import Pivoteo
from .MatrixMethods.Crout import Crout
from .MatrixMethods.Doolittle import Doolittle
from .MatrixMethods.Cholesky import Cholesky
from .MatrixMethods.GaussSeidel import GaussSeidel
from .graph import *
from .table import *
from .matrixTable import *
from .derivate import *
from .Messages.help import Help
from .Messages.errors import Errors
import gi
import math
import numpy as np
import pandas as pd
gi.require_version('Gtk', '3.0')


class Handler:
    def __init__(self, parameters, parameters2):
        self.parameters = parameters
        self.parameters2 = parameters2
        self.help = Help()
        self.errors = Errors()

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
        initial_value = self.parameters[7].get_text()
        increment = self.parameters[6].get_text()
        iterations = self.parameters[5].get_text()
        func = self.parameters[3].get_text()
        try:
            initial_value = float(initial_value)
            increment = float(increment)
            iterations = float(iterations)

            self.incremental_Search = ISearch()
            range_of_root = self.incremental_Search.evaluate(
                initial_value, increment, iterations, func)
            self.parameters[9].set_text(str(range_of_root))

            self.table = self.incremental_Search.values
            self.table_names = ["Iter", "x Value",
                                "F(x) value"]
            self.type = "Incremental_search"
        except :
            list_error = [0, 0, 0, 0, 0, 0 , 0]
            if func == '':
                list_error[0] = 1
            if initial_value == '':
                list_error[4] = 1
            if increment == '':
                list_error[3] = 1
            if iterations == '':
                list_error[2] = 1
            
            self.errors.non_lineal_errors(list_error)
                
            
            

    def bisection_method(self):
        inferior_value = self.parameters[7].get_text()
        superior_value = self.parameters[8].get_text()
        tolerance = self.parameters[10].get_text()
        iterations = self.parameters[5].get_text()
        func = self.parameters[3].get_text()
        try:
            error = self.parameters[1].get_active()

            inferior_value = float(inferior_value)
            superior_value = float(superior_value)
            tolerance = float(tolerance)
            iterations = float(iterations)

            func = self.parameters[3].get_text()

            self.bisection_Search = BSearch()
            range_of_root = self.bisection_Search.evaluate(
                inferior_value, superior_value, tolerance, iterations, func, error)

            self.parameters[9].set_text(str(range_of_root))
            self.table = self.bisection_Search.values
            self.table_names = ["Iter", "Xi", "Xu", "Xm", "F(Xm)", "Error"]
            self.type = "Bisection"
        except:
            list_error = [0, 0, 0, 0, 0, 0 , 0]
            if func == '':
                list_error[0] = 1
            if iterations == '':
                list_error[2] = 1
            if inferior_value == '':
                list_error[4] = 1
            if superior_value == '':
                list_error[5] = 1
            if tolerance == '':
                list_error[6] = 1
            
            self.errors.non_lineal_errors(list_error)

    def false_rule_method(self):
        inferior_value = self.parameters[7].get_text()
        superior_value = self.parameters[8].get_text()
        tolerance = self.parameters[10].get_text()
        iterations = self.parameters[5].get_text()
        func = self.parameters[3].get_text()

        try:
            error = self.parameters[1].get_active()

            inferior_value = float(inferior_value)
            superior_value = float(superior_value)
            tolerance = float(tolerance)
            iterations = float(iterations)

            self.false_rule_Search = FSearch()
            range_of_root = self.false_rule_Search.evaluate(
                inferior_value, superior_value, tolerance, iterations, func, error)
            self.parameters[9].set_text(str(range_of_root))
            self.table = self.false_rule_Search.values
            self.table_names = ["Iter", "Xi", "Xu", "Xm", "F(Xm)", "Error"]
            self.type = "False Rule"
        except:
            list_error = [0, 0, 0, 0, 0, 0 , 0]

            if func == '':
                list_error[0] = 1
            if iterations == '':
                list_error[2] = 1
            if inferior_value == '':
                list_error[4] = 1
            if superior_value == '':
                list_error[5] = 1
            if tolerance == '':
                list_error[6] = 1
            
            self.errors.non_lineal_errors(list_error)

    def fixed_point_method(self):
        initial_value = self.parameters[7].get_text()
        tolerance = self.parameters[10].get_text()
        iterations = self.parameters[5].get_text()
        func = self.parameters[3].get_text()
        g_func = self.parameters[4].get_text()

        try:
            error = self.parameters[1].get_active()

            initial_value = float(initial_value)
            tolerance = float(tolerance)
            iterations = float(iterations)

            self.fixed_point_Search = FPSearch()
            range_of_root = self.fixed_point_Search.evaluate(
                initial_value, tolerance, iterations, func, g_func, error)
            self.parameters[9].set_text(str(range_of_root))
            self.table = self.fixed_point_Search.values
            self.table_names['iter', 'x Value', 'F(x) Value', 'Error']
            self.type = "Fixed Point"
        except:
            list_error = [0, 0, 0, 0, 0, 0 , 0]
            
            if func == '':
                list_error[0] = 1
            if g_func == '':
                list_error[1] = 1
            if iterations == '':
                list_error[2] = 1
            if initial_value == '':
                list_error[4] = 1
            if tolerance == '':
                list_error[6] = 1
            
            self.errors.non_lineal_errors(list_error)

    def newton_method(self):
        initial_value = self.parameters[7].get_text()
        tolerance = self.parameters[10].get_text()
        iterations = self.parameters[5].get_text()
        func = self.parameters[3].get_text()

        try:
            error = self.parameters[1].get_active()

            initial_value = float(initial_value)
            tolerance = float(tolerance)
            iterations = float(iterations)

            d_func = derivate_function(self.parameters[3].get_text())

            self.newton_Search = NSearch()
            range_of_root = self.newton_Search.evaluate(
                tolerance, initial_value, iterations, func, d_func, error)
            self.parameters[9].set_text(str(range_of_root))

            self.table = self.newton_Search.values
            self.table_names = ['Iter', 'Xn', 'f(Xn)', 'f\'(Xn)', 'Error']
            self.type = "Newton"
        except:
            list_error = [0, 0, 0, 0, 0, 0 , 0]
            
            if func == '':
                list_error[0] = 1
            if iterations == '':
                list_error[2] = 1
            if initial_value == '':
                list_error[4] = 1
            if tolerance == '':
                list_error[6] = 1
            
            self.errors.non_lineal_errors(list_error)

    def secant_method(self):
        inferior_value = self.parameters[7].get_text()
        superior_value = self.parameters[8].get_text()
        tolerance = self.parameters[10].get_text()
        iterations = self.parameters[5].get_text()
        func = self.parameters[3].get_text()
        try:
            error = self.parameters[1].get_active()

            inferior_value = float(inferior_value)
            superior_value = float(superior_value)
            tolerance = float(tolerance)
            iterations = float(iterations)

            self.secant_Search = SSearch()
            range_of_root = self.secant_Search.evaluate(tolerance,
                                                        inferior_value, superior_value, func, iterations, error)
            self.parameters[9].set_text(str(range_of_root))
            self.table = self.secant_Search.values
            self.table_names = ['Iter', 'Xn', 'f(Xn)', 'Error']
            self.type = "Secant"
        except:
            list_error = [0, 0, 0, 0, 0, 0 , 0]
            
            if func == '':
                list_error[0] = 1
            if iterations == '':
                list_error[2] = 1
            if inferior_value == '':
                list_error[4] = 1
            if superior_value == '':
                list_error[5] = 1
            if tolerance == '':
                list_error[6] = 1
            
            self.errors.non_lineal_errors(list_error)

    def multiple_roots_method(self):
        initial_value = self.parameters[7].get_text()
        tolerance = self.parameters[10].get_text()
        iterations = self.parameters[5].get_text()
        func = self.parameters[3].get_text()

        try:
            error = self.parameters[1].get_active()

            initial_value = float(initial_value)
            tolerance = float(tolerance)
            iterations = float(iterations)
            
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
            list_error = [0, 0, 0, 0, 0, 0 , 0]
            
            if func == '':
                list_error[0] = 1
            if iterations == '':
                list_error[2] = 1
            if initial_value == '':
                list_error[4] = 1
            if tolerance == '':
                list_error[6] = 1
            
            self.errors.non_lineal_errors(list_error)

    def help_pressed(self, button):
        method = self.parameters[0].get_active()
        if method == 0:
            self.help.non_linear_equation_help("Incremental")
        elif method == 1:
            self.help.non_linear_equation_help("Bisection")
        elif method == 2:
            self.help.non_linear_equation_help("False Rule")
        elif method == 3:
            self.help.non_linear_equation_help("Fixed Point")
        elif method == 4:
            self.help.non_linear_equation_help("Newton")
        elif method == 5:
            self.help.non_linear_equation_help("Secant")
        elif method == 6:
            self.help.non_linear_equation_help("Multiple Roots")

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
        tree = TreeView2(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.matrixTable = tree.returnTable()
        print(self.matrixTable.dtypes)
        self.matrixTable = self.matrixTable.to_numpy()
        self.matrixTable = self.matrixTable.astype(np.float)
        print(self.matrixTable)

    def initialValues_generate(self, button):
        columns = int(self.parameters2[2].get_text())
        rows = 1
        tree = TreeView2(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.initialValuesTable = tree.returnTable()
        print(self.initialValuesTable.dtypes)
        self.initialValuesTable = self.initialValuesTable.to_numpy()
        self.initialValuesTable = self.initialValuesTable.astype(np.float)
        print(self.initialValuesTable)

    def evaluateMatrix_pressed(self, button):
        method = self.parameters2[4].get_active()
        if method == 0:
            self.evaluate_gauss()
        elif method == 1:
            self.evaluate_pivot_parcial()
        elif method == 2:
            self.evaluate_pivot_total()
        elif method == 3:
            self.evaluate_crout()
        elif method == 4:
            self.evaluate_doolittle()
        elif method == 5:
            self.evaluate_cholesky()
        elif method == 6:
            self.evaluate_jacobi()
        elif method == 7:
            self.evaluate_gauss_seidel()


    def evaluate_gauss(self):
        self.etapa_index = 0

        print(f"Matriz\n{self.matrixTable}")
        matrixSize = self.matrixTable.shape[0]
        gauss = Gauss(self.matrixTable, matrixSize)
        self.x_result, self.etapas =gauss.evaluate()

        #CODIGO POPUP
        # self.etapas_text = ""
        # for i in range(len(x)-1):
        #     etapas_text+= f"Etapa {i}:\n {str(self.etapas[i])}\n\n"

        # etapas_popover = Gtk.Popover()
        # etapas_label = Gtk.Label(etapas_text)
        # etapas_popover.add(etapas_label)

        # etapas_popover.set_relative_to(self.Gaussbutton)
        # etapas_popover.show_all()
        # etapas_popover.popup()

        print(self.x_result)
        print(self.etapas)

    def evaluate_pivot_parcial(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        pivot = Pivoteo(self.matrixTable,matrixSize)
        self.x_text,self.etapas = pivot.evaluate_parcial()

    def evaluate_pivot_total(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())

        pivot = Pivoteo(self.matrixTable,matrixSize)
        self.x_text,self.etapas = pivot.evaluate_total()

    def evaluate_crout(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        crout = Crout(matrix,matrixSize,indp)
        self.x_text,self.etapas = crout.evaluate()

    def evaluate_doolittle(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        doo = Doolittle(matrix,matrixSize,indp)
        self.L, self.U, self.Z, self.X = doo.evaluate()

    def evaluate_cholesky(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        chol = Cholesky(matrix,matrixSize,indp)
        self.L, self.U, self.Z, self.X = chol.evaluate()

    def evaluate_jacobi(self,widget):
        matrixSize = int(self.parameters2[0].get_text())

        tol = float(self.parameters2[6].get_text())
        iter = int(self.parameters2[7].get_text())
        lamb = float(self.parameters2[8].get_text())

        initialValues = self.initialValuesTable
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,m,indp,initialValues)
        seidel.evaluate(tol,iter,lamb)

    def evaluate_gauss_seidel(self,widget):
        matrixSize = int(self.parameters2[0].get_text())

        tol = float(self.parameters2[6].get_text())
        iter = int(self.parameters2[7].get_text())
        lamb = float(self.parameters2[8].get_text())

        initialValues = self.initialValuesTable
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,m,indp,initialValues)
        seidel.evaluate(tol,iter,lamb)
    
    def helpMatrix_pressed(self, button):
        method = self.parameters2[4].get_active()
      
        if method == 0:
            self.help.linear_equations_help("Simple Gaussian")
        elif method == 1:
            self.help.linear_equations_help("Parcial Pivot")
        elif method == 2:
            self.help.linear_equations_help("Total Pivot")
        elif method == 3:
            self.help.linear_equations_help("Crout")
        elif method == 4:
            self.help.linear_equations_help("Doolittle")
        elif method == 5:
            self.help.linear_equations_help("Cholesky")
        elif method == 6:
            self.help.linear_equations_help("Jacobi")
        elif method == 7:
            self.help.linear_equations_help("Gauss-Seidel")
