from UI.Interpolation.Functions.NewtonInterpolation import NewtonInterpolation
from UI.Interpolation.Functions.Lagrange import Lagrange
from UI.Interpolation.Functions.LinearSpline import LinearSpline
from UI.Interpolation.Functions.QuadraticSpline import QuadraticSpline
from UI.Interpolation.Functions.CubicSpline import CubicSpline
#from UI.Interpolation.Messages.errors import Errors
#from UI.Interpolation.Messages.help import Help
from UI.matrixTable import TreeView2


class Interpolation_Control:

    def __init__(self, parameters3):
        self.parameters3 = parameters3
        self.errors = Errors()
        self.help = Help()

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
    
    def helpInterpolation_pressed(self, button):
        method = self.parameters3[4].get_active()

        if method == 0:
            self.help.interpolacion_help("Newton")
        elif method == 1:
            self.help.interpolacion_help("Lagrange")
        elif method == 2:
            self.help.interpolacion_help("Neville")
        elif method == 3:
            self.help.interpolacion_help("Spline")
        