from .functions.IncrementalSearch import IncrementalSearch as ISearch
from .functions.BisectionSearch import Bisection as BSearch
from .functions.FalseRuleSearch import FalseRule as FSearch
from .functions.FixedPointSearch import FixedPoint as FPSearch
from .functions.NewtonSearch import Newton as NSearch
from .functions.SecantSearch import Secant as SSearch
from .functions.MultipleRoots import MultipleRoots as MRoots
from .graph import *
from .table import *
from .derivate import *
from .Messages.help import Help
from .Messages.errors import Errors

class NonLinearHandler:


    def __init__(self, parameters):
        self.paramaters = parameters
        self.help = Help()
        self.errors = Errors()
    
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