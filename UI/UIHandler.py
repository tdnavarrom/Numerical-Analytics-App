from gi.repository import Gtk, Gdk
from .functions.IncrementalSearch import IncrementalSearch as ISearch
from .functions.BisectionSearch import Bisection as BSearch
from .functions.FalseRuleSearch import FalseRule as FSearch
from .functions.FixedPointSearch import FixedPoint as FPSearch
from .functions.NewtonSearch import Newton as NSearch
from .functions.SecantSearch import Secant as SSearch
from .functions.MultipleRoots import MultipleRoots as MRoots
from .MatrixMethods.view.matrix_view import Matrix_View
from .MatrixMethods.view.e1_view import Matrix_View2
from .MatrixMethods.view.table_j_s import Tree_View_J_S
from .MatrixMethods.Gauss import Gauss
from .MatrixMethods.Pivoteo import Pivoteo
from .MatrixMethods.Pivoteo import Pivoteo
from .MatrixMethods.Crout import Crout
from .MatrixMethods.Doolittle import Doolittle
from .MatrixMethods.Cholesky import Cholesky
from .MatrixMethods.GaussSeidel import GaussSeidel
from .Interpolation.NewtonInterpolation import NewtonInterpolation
from .Interpolation.Lagrange import Lagrange
from .Interpolation.LinearSpline import LinearSpline
from .Interpolation.QuadraticSpline import QuadraticSpline
from .Interpolation.CubicSpline import CubicSpline
from .Interpolation.Functions import Functions
from .Interpolation.view.matrix_interpolation import Matrix_View_Interpolation
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
    def __init__(self, parameters, parameters2, parameters3):
        self.parameters = parameters
        self.parameters2 = parameters2
        self.parameters3 = parameters3
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


####### EQUATION SYSTEM

    def evaluateMatrix_pressed(self, button):
        method = self.parameters2[4].get_active()
    
        if method == 0:
            try:
                self.evaluate_gauss()
                matrix_gui = Matrix_View(self.x_result, self.etapas, self.matrixTable)
                Gtk.main()
            except ZeroDivisionError:
                self.errors.div_0()

        elif method == 1:
            try:
                self.evaluate_pivot_parcial()
                matrix_gui = Matrix_View(self.x_result, self.etapas, self.matrixTable)
                Gtk.main()
            except ZeroDivisionError:
                self.errors.div_0()

        elif method == 2:
            try:
                self.evaluate_pivot_total()
                matrix_gui = Matrix_View(self.x_result, self.etapas, self.matrixTable)
                Gtk.main()
            except ZeroDivisionError:
                self.errors.div_0()
        elif method == 3:
            self.evaluate_crout()
            matrix_gui2 = Matrix_View2(self.matrix_l, self.matrix_u, self.vector_z, self.x_result)
            Gtk.main()
        elif method == 4:
            self.evaluate_doolittle()
            matrix_gui2 = Matrix_View2(self.matrix_l, self.matrix_u, self.vector_z, self.x_result)
            Gtk.main()
        elif method == 5:
            self.evaluate_cholesky()
            matrix_gui2 = Matrix_View2(self.matrix_l, self.matrix_u, self.vector_z, self.x_result)
            Gtk.main()
        elif method == 6:
            self.evaluate_jacobi()
            Tree_View_J_S(self.table_values)
        elif method == 7:
            self.evaluate_gauss_seidel()
            Tree_View_J_S(self.table_values)
         

    def evaluate_gauss(self):
        self.etapa_index = 0

        matrixSize = self.matrixTable.shape[0]
        gauss = Gauss(self.matrixTable, matrixSize)
        self.answer = gauss.evaluate()
        self.x_result = gauss.x
        self.etapas = gauss.etapas
        

    def evaluate_pivot_parcial(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        pivot = Pivoteo(self.matrixTable,matrixSize)
        self.x_result,self.etapas = pivot.evaluate_parcial()
        self.etapas = pivot.etapas

    def evaluate_pivot_total(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())

        pivot = Pivoteo(self.matrixTable,matrixSize)
        self.x_result,self.etapas = pivot.evaluate_total()

    def evaluate_crout(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        crout = Crout(matrix,matrixSize,indp)
        self.x_result,self.etapas = crout.evaluate()
        self.matrix_u = crout.U
        self.matrix_l = crout.L
        self.vector_z = crout.z

    def evaluate_doolittle(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        doo = Doolittle(matrix,matrixSize,indp)
        self.matrix_l, self.matrix_u, self.vector_z, self.x_result = doo.evaluate()

    def evaluate_cholesky(self):
        self.etapa_index = 0
        matrixSize = int(self.parameters2[0].get_text())
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        chol = Cholesky(matrix,matrixSize,indp)
        self.matrix_l, self.matrix_u, self.vector_z, self.x_result = chol.evaluate()

    def evaluate_jacobi(self):
        matrixSize = int(self.parameters2[0].get_text())

        tol = float(self.parameters2[5].get_text())
        iter = int(self.parameters2[6].get_text())
        lamb = float(self.parameters2[7].get_text())

        initialValues = self.initialValuesTable
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,matrixSize,indp,initialValues)
        seidel.evaluate(tol,iter,lamb)

        self.table_values = seidel.tabla_values()

    def evaluate_gauss_seidel(self):
        matrixSize = int(self.parameters2[0].get_text())

        tol = float(self.parameters2[5].get_text())
        iter = int(self.parameters2[6].get_text())
        lamb = float(self.parameters2[7].get_text())

        initialValues = self.initialValuesTable
        matrix = self.matrixTable[:,:(matrixSize)]
        indp = self.matrixTable[:,-1]

        print(f"Indp: {indp}")
        seidel = GaussSeidel(matrix,matrixSize,indp,initialValues)
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

    def matrix_generate(self, button):
        rows = self.parameters2[0].get_text()
        try:
            rows = int(rows)
            columns = rows + 1
            tree = TreeView2(rows ,columns)
            tree.connect("destroy", Gtk.main_quit)
            tree.show_all()
            Gtk.main()
            self.matrixTable = tree.returnTable()
            self.matrixTable = self.matrixTable.to_numpy()
            self.matrixTable = self.matrixTable.astype(np.float)
        except:
            list_error = []
            if rows == '':          
                list_error[0] = 1
            self.errors.lineal_errors(list_error)
        
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

    #Interpolation
    def evaluateInterpolation_pressed(self, button):
        method = self.parameters3[0].get_active()
        print(method)

        if method == 0:
            self.evaluate_NewtonInterpolation()
            matrix_gui = Matrix_View_Interpolation(self.values)
            Gtk.main()
        elif method == 1:
            self.evaluate_LagrangeInterpolation()
        elif method == 2:
            self.evaluar_linear_spline
        elif method == 3:
            self.evaluar_quadratic_spline
        elif method == 4:
            self.evaluar_cubic_spline

    
    def initial_values_generate_interpolation(self, button):
        columns = int(self.parameters3[1].get_text())
        rows = 1
        tree = TreeView2(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.initialValuesTable = tree.returnTable()
        self.initialValuesTable = self.initialValuesTable.to_numpy()
        self.initialValuesTable = self.initialValuesTable.astype(np.float)
        print(self.initialValuesTable)

    def x_values_interpolation_pressed(self, button):
        columns = int(self.parameters3[4].get_text())
        rows = 1
        tree = TreeView2(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.x_values_interpolation = tree.returnTable()
        self.x_values_interpolation = self.x_values_interpolation.to_numpy()
        self.x_values_interpolation = self.x_values_interpolation.astype(np.float)
        print(self.x_values_interpolation)

    def fx_values_interpolation_pressed(self, button):
        columns = int(self.parameters3[6].get_text())
        rows = 1
        tree = TreeView2(rows ,columns)
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()
        self.fx_values_interpolation = tree.returnTable()
        self.fx_values_interpolation = self.fx_values_interpolation.to_numpy()
        self.fx_values_interpinitialValuesTableolation = self.fx_values_interpolation.astype(np.float)
        print(self.fx_values_interpolation)

    def evaluate_NewtonInterpolation(self):
        function = self.parameters3[3].get_text()
        func = Functions(function)
        newton_interpolation = NewtonInterpolation()
        newton_interpolation.algorithm_newtonInterpolation(func, self.initialValuesTable)
        self.values = newton_interpolation.value_table()
        text = newton_interpolation.get_sol()
        print(text)
        self.parameters3[8].set_text(text)

    def evaluate_LagrangeInterpolation(self):
        lagrange = Lagrange()
        lagrange.lagrange_interpol_algorithm(self.x_values_interpolation, self.fx_values_interpolation)
        text = lagrange.getPolynomial()
        self.parameters3[8].set_text(text)

    def evaluar_linear_spline(self):
        linearSpline = LinearSpline()
        linearSpline.algorithm_linearSpline(self.x_values_interpolation, self.fx_values_interpolation)
        text = linearSpline.get_results()
        self.parameters3[8].set_text(text)

    def evaluar_quadratic_spline(self):
        quadratic_spline = QuadraticSpline()
        quadratic_spline.algorithm_quadratic_spline(self.x_values_interpolation, self.fx_values_interpolation)
        text = QuadraticSpline.get_results()
        self.parameters3[8].set_text(text)

    def evaluar_cubic_spline(self):
        cubic_spline = CubicSpline()
        cubic_spline.algorithm_cubic_spline(self.x_values_interpolation, self.fx_values_interpolation)
        text = CubicSpline.get_results()
        self.parameters3[8].set_text(text)