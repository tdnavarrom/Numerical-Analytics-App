import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .functions import *

class NonLinealMenu2(Gtk.Notebook):

    def __init__(self):
        """ Grid that contains basic UI Components for all NonLinear Functions"""
        self.grid = Gtk.Grid()
        self.grid = self.create_ui()

    def function_entry(self):
        """
        Function Label and Entry at the bottom, with Evaluate Button.

        Returns:
            grid
            vbox
        """
        grid = Gtk.Grid()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.function = Gtk.Entry()
        self.function.set_placeholder_text("Function")
        vbox.pack_start(self.function, True, True, 0)
        grid.attach(vbox, 0, 0, 2, 2)

        return grid, vbox

    def g_function_entry(self, grid, vbox):
        """
        Initial Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox
        Returns:
            grid
            vbox2
        """
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.g_function = Gtk.Entry()
        self.g_function.set_placeholder_text("G Function")
        vbox2.pack_start(self.g_function, True, True, 0)
        grid.attach_next_to(vbox2, vbox, Gtk.PositionType.BOTTOM, 2, 2)

        return grid, vbox2

    def tolerancia_value_entry(self, grid, vbox2):
        """
        Increment Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox2
        Returns:
            grid
            vbox3

        """
        vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.tolerance = Gtk.Entry()
        self.tolerance.set_placeholder_text("Tolerance")
        vbox3.pack_start(self.tolerance, True, True, 0)
        grid.attach_next_to(vbox3, vbox2, Gtk.PositionType.BOTTOM, 1, 2)

        return grid, vbox3

    def iteration_value_entry(self, grid, vbox3):
        '''
        Iterations Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox3
        Returns:
            grid
            vbox6
        '''
        vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.iterations = Gtk.Entry()
        self.iterations.set_placeholder_text("Iterations")
        vbox4.pack_start(self.iterations, True, True, 0)
        grid.attach_next_to(vbox4, vbox3, Gtk.PositionType.RIGHT, 1, 2)

        return grid, vbox4

    def initial_value_and_entry(self, grid, vbox3):
        """
        Initial Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox3
        Returns:
            grid
            vbox4
        """
        vbox5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.x0 = Gtk.Entry()
        self.x0.set_placeholder_text("Initial Value")
        vbox5.pack_start(self.x0, True, True, 0)
        grid.attach_next_to(vbox5, vbox3, Gtk.PositionType.BOTTOM, 1, 2)

        return grid, vbox5


    def superior_value_entry(self, grid, vbox5):
        """
        Initial Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox4
        Returns:
            grid
            vbox5
        """
        vbox6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.xs = Gtk.Entry()
        self.xs.set_placeholder_text("Superior Value")
        vbox6.pack_start(self.xs, True, True, 0)
        grid.attach_next_to(vbox6, vbox5, Gtk.PositionType.RIGHT, 1, 2)

        return grid, vbox6


    def button_box(self, grid, vbox5):
        '''
        Box that contains all Buttons.

        Parameters:
            grid
            vbox4
        Returns:
            grid
            vbox7
        '''
        vbox7 = Gtk.Box(spacing=8)
        button = Gtk.Button(label="Incremental Search")
        button.connect('clicked', self.incremental_Search_button)
        vbox7.pack_start(button, True, True, 0)
        button2 = Gtk.Button(label="Bisection Method")
        button2.connect('clicked', self.bisection_button)
        vbox7.pack_start(button2, True, True, 0)
        button3 = Gtk.Button(label="False Rule")
        button3.connect('clicked', self.false_rule_button)
        vbox7.pack_start(button3, True, True, 0)
        button4 = Gtk.Button(label="Fixed Point")
        button4.connect('clicked', self.fixed_point_button)
        vbox7.pack_start(button4, True, True, 0)
        button5 = Gtk.Button(label="Newton")
        button5.connect('clicked', self.newton_button)
        vbox7.pack_start(button5, True, True, 0)
        button6 = Gtk.Button(label="Secant")
        button6.connect('clicked', self.secant_button)
        vbox7.pack_start(button6, True, True, 0)
        button7 = Gtk.Button(label="Multiple Roots")
        button7.connect('clicked', self.false_rule_button)
        vbox7.pack_start(button7, True, True, 0)
        button8 = Gtk.Button(label="Help")
        button8.connect('clicked', self.on_help_clicked)
        vbox7.pack_start(button8, True, True, 0)

        grid.attach_next_to(vbox7, vbox5, Gtk.PositionType.BOTTOM, 2, 2)

        return grid, vbox7

    def result_entry(self, grid, vbox7):
        '''
        Result Entry.

        Parameters:
            grid
            vbox6
        Returns:
            grid
            vbox8
        '''
        vbox8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.result = Gtk.Entry()
        self.result.set_placeholder_text("Result")
        vbox8.pack_start(self.result, True, True, 0)
        grid.attach_next_to(vbox8, vbox7, Gtk.PositionType.BOTTOM, 2, 2)

        return grid, vbox8


    def create_ui(self):
        grid, vbox = self.function_entry()
        grid, vbox2 = self.g_function_entry(grid, vbox)
        grid, vbox3 = self.tolerancia_value_entry(grid, vbox2)
        grid, vbox4 = self.iteration_value_entry(grid, vbox3)
        grid, vbox5 = self.initial_value_and_entry(grid, vbox3)
        grid, vbox6 = self.superior_value_entry(grid, vbox5)
        grid, vbox7 = self.button_box(grid, vbox5)
        grid, vbox8 = self.result_entry(grid, vbox7)

        return grid

    def incremental_Search_button(self, widget):
        initial_value = float(self.x0.get_text())
        increment = float(self.increment.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())

        self.incremental_Search = ISearch()
        range_of_root = self.incremental_Search.evaluate(
            initial_value, increment, iterations, func)
        self.result.set_text(str(range_of_root))

    def bisection_button(self, widget):
        inferior_value = float(self.x0.get_text())
        superior_value = float(self.xs.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())

        self.bisection_Search = BSearch()
        range_of_root = self.bisection_Search.evaluate(
            inferior_value, superior_value, tolerance, iterations, func, type_error=1)
        self.result.set_text(str(range_of_root))


    def false_rule_button(self, widget):
        inferior_value = float(self.x0.get_text())
        superior_value = float(self.xs.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())

        self.false_rule_Search = FSearch()
        range_of_root = self.false_rule_Search.evaluate(
            inferior_value, superior_value, tolerance, iterations, func, type_error=1)
        self.result.set_text(str(range_of_root))


    def fixed_point_button(self, widget):
        initial_value = float(self.x0.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())
        g_func = Function(self.g_function.get_text())

        self.fixed_point_Search = FPSearch()
        range_of_root = self.fixed_point_Search.evaluate(
            initial_value, tolerance, iterations, func, g_func)
        self.result.set_text(str(range_of_root))


    def newton_button(self, widget):
        initial_value = float(self.x0.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())
        d_func = Function(self.derivate_function.get_text())

        self.newton_Search = NSearch()
        range_of_root = self.newton_Search.evaluate(
        tolerance, initial_value, iterations, func, d_func)
        self.result.set_text(str(range_of_root))


    def secant_button(self, widget):
        inferior_value = float(self.x0.get_text())
        superior_value = float(self.xs.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())

        self.secant_Search = SSearch()
        range_of_root = self.secant_Search.evaluate(tolerance,
            inferior_value, superior_value, func, iterations,)
        self.result.set_text(str(range_of_root))



    def on_help_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Fixed Point Search Help")
        dialog.format_secondary_text(
            "El método de punto fijo reformula la ecuación f(x)=0 y genera una ecuación de la forma x=g(x) que permite encontrar un valor de x que al reemplazarlo en g su resultado sea el mismo, es decir que x sea invariable para g, y adicionalmente que la f(x) converja a cero.\n\nSe dispone de un intervalo [a,b] para el cual la función g es continua y se cumple que para todo valor de x en el intervalo, g(x) también pertenece al mismo intervalo. Además para garantizar la unicidad de dicho punto se debe cumplir que la derivada g′(x)<1 en el intervalo.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()
