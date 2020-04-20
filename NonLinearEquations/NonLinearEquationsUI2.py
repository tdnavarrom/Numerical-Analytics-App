import gi
import math
import numpy as np
import pandas as pd
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .functions.IncrementalSearch import IncrementalSearch as ISearch
from .functions.BisectionSearch import Bisection as BSearch
from .functions.FalseRuleSearch import FalseRule as FSearch
from .functions.FixedPointSearch import FixedPoint as FPSearch
from .functions.NewtonSearch import Newton as NSearch
from .functions.SecantSearch import Secant as SSearch
from .functions.MultipleRoots import MultipleRoots as MRoots
from .table import *
from .derivate import *


class NonLinealMenu2(Gtk.Notebook):

    def __init__(self):
        """ Grid that contains basic UI Components for all NonLinear Functions"""
        self.grid = Gtk.Grid()
        self.grid = self.create_ui()
        self.type_error = 1

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
        grid.attach(vbox, 0, 0, 6, 2)

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
        grid.attach_next_to(vbox2, vbox, Gtk.PositionType.BOTTOM, 6, 2)

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
        vbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        self.tolerance = Gtk.Entry()
        self.tolerance.set_placeholder_text("Tolerance")
        vbox3.pack_start(self.tolerance, True, True, 0)

        self.relative_button = Gtk.ToggleButton("Relative Error")
        self.relative_button.connect("toggled", self.on_button_toggled, "relative_error")
        vbox3.pack_start(self.relative_button, True, True, 0)

        self.absolute_button = Gtk.ToggleButton("Absolute Error", use_underline=True)
        self.absolute_button.connect("toggled", self.on_button_toggled, "absolute_error")
        vbox3.pack_start(self.absolute_button, True, True, 0)

        grid.attach_next_to(vbox3, vbox2, Gtk.PositionType.BOTTOM, 3, 2)

        return grid, vbox3


    def on_button_toggled(self, button, name):

        if button.get_active():
            if name == "relative_error":
                if self.absolute_button.get_active(): self.absolute_button.set_active(False)
                self.type_error = 1

            elif name == "absolute_error":
                if self.relative_button.get_active(): self.relative_button.set_active(False)
                self.type_error = 0


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
        grid.attach_next_to(vbox4, vbox3, Gtk.PositionType.RIGHT, 3, 2)

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
        grid.attach_next_to(vbox5, vbox3, Gtk.PositionType.BOTTOM, 2, 2)

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
        grid.attach_next_to(vbox6, vbox5, Gtk.PositionType.RIGHT, 2, 2)

        return grid, vbox6

    def increment_value_entry(self, grid, vbox6):
        """
        Initial Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox4
        Returns:
            grid
            vbox5
        """
        vbox7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.increment = Gtk.Entry()
        self.increment.set_placeholder_text("Increment Value")
        vbox7.pack_start(self.increment, True, True, 0)
        grid.attach_next_to(vbox7, vbox6, Gtk.PositionType.RIGHT, 2, 2)

        return grid, vbox7

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
        vbox8 = Gtk.Box(spacing=8)
        button = Gtk.Button(label="Incremental Search")
        button.connect('clicked', self.incremental_Search_button)
        vbox8.pack_start(button, True, True, 0)
        button2 = Gtk.Button(label="Bisection")
        button2.connect('clicked', self.bisection_button)
        vbox8.pack_start(button2, True, True, 0)
        button3 = Gtk.Button(label="False Rule")
        button3.connect('clicked', self.false_rule_button)
        vbox8.pack_start(button3, True, True, 0)
        button4 = Gtk.Button(label="Fixed Point")
        button4.connect('clicked', self.fixed_point_button)
        vbox8.pack_start(button4, True, True, 0)
        button5 = Gtk.Button(label="Newton")
        button5.connect('clicked', self.newton_button)
        vbox8.pack_start(button5, True, True, 0)
        button6 = Gtk.Button(label="Secant")
        button6.connect('clicked', self.secant_button)
        vbox8.pack_start(button6, True, True, 0)
        button7 = Gtk.Button(label="Multiple Roots")
        button7.connect('clicked', self.multiple_roots)
        vbox8.pack_start(button7, True, True, 0)
        button8 = Gtk.Button(label="Help")
        button8.connect('clicked', self.on_help_clicked)
        vbox8.pack_start(button8, True, True, 0)

        grid.attach_next_to(vbox8, vbox5, Gtk.PositionType.BOTTOM, 6, 2)

        return grid, vbox8

    def result_entry(self, grid, vbox8):
        '''
        Result Entry.

        Parameters:
            grid
            vbox6
        Returns:
            grid
            vbox8
        '''
        vbox9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.result = Gtk.Entry()
        self.result.set_placeholder_text("Result")
        vbox9.pack_start(self.result, True, True, 0)

        grid.attach_next_to(vbox9, vbox8, Gtk.PositionType.BOTTOM, 6, 2)

        return grid, vbox9

    def graphic_f_button(self, grid, vbox):
        vbox10 = Gtk.Box(spacing=8)
        button = Gtk.Button(label="Graphic")
        button.connect('clicked', self.graphic_f)
        vbox10.pack_start(button, True, True, 0)

        grid.attach_next_to(vbox10, vbox, Gtk.PositionType.RIGHT, 2, 2)

        return grid

    def graphic_g_button(self, grid, vbox2):
        vbox11 = Gtk.Box(spacing=8)
        button = Gtk.Button(label="Graphic")
        button.connect('clicked', self.graphic_g)
        vbox11.pack_start(button, True, True, 0)

        grid.attach_next_to(vbox11, vbox2, Gtk.PositionType.RIGHT, 2, 2)

        return grid

    def create_ui(self):
        grid, vbox = self.function_entry()
        grid, vbox2 = self.g_function_entry(grid, vbox)
        grid, vbox3 = self.tolerancia_value_entry(grid, vbox2)
        grid, vbox4 = self.iteration_value_entry(grid, vbox3)
        grid, vbox5 = self.initial_value_and_entry(grid, vbox3)
        grid, vbox6 = self.superior_value_entry(grid, vbox5)
        grid, vbox7 = self.increment_value_entry(grid, vbox6)
        grid, vbox8 = self.button_box(grid, vbox5)
        grid, vbox9 = self.result_entry(grid, vbox8)
        grid = self.graphic_f_button(grid, vbox)
        grid = self.graphic_g_button(grid, vbox2)

        return grid

    def incremental_Search_button(self, widget):
        initial_value = float(self.x0.get_text())
        increment = float(self.increment.get_text())
        iterations = float(self.iterations.get_text())
        func = self.function.get_text()

        self.incremental_Search = ISearch()
        range_of_root = self.incremental_Search.evaluate(
            initial_value, increment, iterations, func)
        self.result.set_text(str(range_of_root))

        table = self.incremental_Search.values
        tree = TreeView(table, ['Iter', 'x Value',
                                'F(x) value'], 'Incremental_search')
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()

    def bisection_button(self, widget):
        inferior_value = float(self.x0.get_text())
        superior_value = float(self.xs.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())

        func = self.function.get_text()
        self.bisection_Search = BSearch()
        range_of_root = self.bisection_Search.evaluate(
            inferior_value, superior_value, tolerance, iterations, func, self.type_error)
        self.result.set_text(str(range_of_root))

        table = self.bisection_Search.values
        tree = TreeView(table, ['Iter', 'Xi', 'Xu',
                                'Xm', 'F(Xm)', 'Error'], 'Bisection')
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()

    def false_rule_button(self, widget):
        inferior_value = float(self.x0.get_text())
        superior_value = float(self.xs.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = self.function.get_text()

        self.false_rule_Search = FSearch()
        range_of_root = self.false_rule_Search.evaluate(
            inferior_value, superior_value, tolerance, iterations, func, self.type_error)
        self.result.set_text(str(range_of_root))
        table = self.false_rule_Search.values
        tree = TreeView(table, ['Iter', 'Xi', 'Xu', 'Xm',
                                'F(Xm)', 'Error'], 'False_rule')
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()

    def fixed_point_button(self, widget):
        initial_value = float(self.x0.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = self.function.get_text()
        g_func = self.g_function.get_text()

        self.fixed_point_Search = FPSearch()
        range_of_root = self.fixed_point_Search.evaluate(
            initial_value, tolerance, iterations, func, g_func, self.type_error)
        self.result.set_text(str(range_of_root))
        table = self.fixed_point_Search.values
        tree = TreeView(table, ['iter', 'x Value',
                                'F(x) Value', 'Error'], 'Fixed_point')
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()

    def newton_button(self, widget):
        initial_value = float(self.x0.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())

        func = self.function.get_text()
        d_func = derivate_function(self.function.get_text())

        self.newton_Search = NSearch()
        range_of_root = self.newton_Search.evaluate(
            tolerance, initial_value, iterations, func, d_func, self.type_error)
        self.result.set_text(str(range_of_root))

        table = self.newton_Search.values
        tree = TreeView(table, ['Iter', 'Xn', 'f(Xn)',
                                'f\'(Xn)', 'Error'], 'Newton')
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()

    def secant_button(self, widget):
        inferior_value = float(self.x0.get_text())
        superior_value = float(self.xs.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = self.function.get_text()

        self.secant_Search = SSearch()
        range_of_root = self.secant_Search.evaluate(tolerance,
            inferior_value, superior_value, func, iterations, self.type_error)
        self.result.set_text(str(range_of_root))
        table = self.secant_Search.values
        tree = TreeView(table, ['Iter', 'Xn', 'f(Xn)', 'Error'], 'Secant')
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()

    def multiple_roots(self, widget):
        initial_value = float(self.x0.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())

        func = self.function.get_text()
        d_func = derivate_function(self.function.get_text())
        dd_func = derivate_function(d_func)
        self.multiple_roots = MRoots()
        range_of_root = self.multiple_roots.evaluate(
            tolerance, initial_value, iterations, func, d_func, dd_func, self.type_error)
        table = self.multiple_roots.values
        tree = TreeView(table, ['Iter', 'Xn', 'f(Xn)','f\'(Xn)','f\'\'(Xn)', 'Error'], 'MRoots')
        tree.connect("destroy", Gtk.main_quit)
        tree.show_all()
        Gtk.main()


    def on_help_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Fixed Point Search Help")
        dialog.format_secondary_text(
            "El método de punto fijo reformula la ecuación f(x)=0 y genera una ecuación de la forma x=g(x) que permite encontrar un valor de x que al reemplazarlo en g su resultado sea el mismo, es decir que x sea invariable para g, y adicionalmente que la f(x) converja a cero.\n\nSe dispone de un intervalo [a,b] para el cual la función g es continua y se cumple que para todo valor de x en el intervalo, g(x) también pertenece al mismo intervalo. Además para garantizar la unicidad de dicho punto se debe cumplir que la derivada g′(x)<1 en el intervalo.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def graphic_f(self, widget):
        func = self.function.get_text()
        graphic(func, 1, 1)

    def graphic_g(self, widget):
        func = self.g_function.get_text()
        graphic(func, 1, 1)


def graphic(funcion, initial_value, iterations):
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    from .functions.Function import Function

    from matplotlib.figure import Figure
    from matplotlib.backends.backend_gtk3agg import FigureCanvas
    from matplotlib.backends.backend_gtk3 import (
        NavigationToolbar2GTK3 as NavigationToolbar)

    function = Function(funcion)

    win = Gtk.Window()
    win.connect("destroy", lambda x: Gtk.main_quit())
    win.set_default_size(640, 480)
    win.set_title("Embedding in GTK")

    vbox = Gtk.VBox()
    win.add(vbox)

    #increment = 0.1
    #final_value = math.fabs(initial_value+math.fabs(increment*iterations))

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    x = np.arange(-100, 100, 1)
    ax.plot(x, [function.evaluate(i) for i in x])

    canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
    vbox.pack_start(canvas, True, True, 0)
    toolbar = NavigationToolbar(canvas, win)
    vbox.pack_start(toolbar, False, False, 0)

    win.show_all()
    Gtk.main()
