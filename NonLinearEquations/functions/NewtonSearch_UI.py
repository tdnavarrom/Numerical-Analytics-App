import math
import numpy as np
import pandas as pd
from matplotlib import pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from .NewtonSearch import Newton as NSearch
from .Function import Function
from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


class newton_search_ui(Gtk.Grid):

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

    def derivate_function_entry(self, grid, vbox):
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
        self.derivate_function = Gtk.Entry()
        self.derivate_function.set_placeholder_text("Derivate Function")
        vbox2.pack_start(self.derivate_function, True, True, 0)
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
        vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.x0 = Gtk.Entry()
        self.x0.set_placeholder_text("Initial Value")
        vbox4.pack_start(self.x0, True, True, 0)
        grid.attach_next_to(vbox4, vbox3, Gtk.PositionType.RIGHT, 1, 2)

        return grid, vbox4

    def iteration_value_entry(self, grid, vbox3):
        '''
        Iterations Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox4
        Returns:
            grid
            vbox5
        '''
        vbox5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.iterations = Gtk.Entry()
        self.iterations.set_placeholder_text("Iterations")
        vbox5.pack_start(self.iterations, True, True, 0)
        grid.attach_next_to(vbox5, vbox3, Gtk.PositionType.BOTTOM, 1, 2)

        return grid, vbox5

    def button_box(self, grid, vbox5):
        '''
        Box that contains all Buttons.

        Parameters:
            grid
            vbox4
        Returns:
            grid
            vbox6
        '''
        vbox6 = Gtk.Box(spacing=8)
        button = Gtk.Button(label="Evaluate")
        button.connect('clicked', self.evaluate_function)
        vbox6.pack_start(button, True, True, 0)
        button2 = Gtk.Button(label="Graph")
        button2.connect('clicked', self.graph_function)
        vbox6.pack_start(button2, True, True, 0)
        button3 = Gtk.Button(label="Table")
        button3.connect('clicked', self.show_table)
        vbox6.pack_start(button3, True, True, 0)
        button4 = Gtk.Button(label="Help")
        button4.connect('clicked', self.on_help_clicked)
        vbox6.pack_start(button4, True, True, 0)
        grid.attach_next_to(vbox6, vbox5, Gtk.PositionType.BOTTOM, 2, 2)

        return grid, vbox6

    def result_entry(self, grid, vbox6):
        '''
        Result Entry.

        Parameters:
            grid
            vbox6
        Returns:
            grid
            vbox7
        '''
        vbox7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.result = Gtk.Entry()
        self.result.set_placeholder_text("Result")
        vbox7.pack_start(self.result, True, True, 0)
        grid.attach_next_to(vbox7, vbox6, Gtk.PositionType.BOTTOM, 2, 2)

        return grid, vbox7

    def graph(self, grid, vbox7):
        '''
        Graphic of the function.

        Parameters:
            grid
            vbox7
        Returns:
            grid
            vbox8
        '''
        vbox8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.figure = Figure(figsize=(3, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.set_size_request(350, 250)
        vbox8.pack_start(self.canvas, True, True, 0)
        grid.attach_next_to(vbox8, vbox7, Gtk.PositionType.BOTTOM, 2, 1)

        return grid, vbox8

    def table(self, grid, vbox):
        '''
        Table of the function.

        Parameters:
            grid
            vbox
        Return:
            grid
        '''
        vbox9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.table_tree = Gtk.TreeView()
        scrollTree.add(self.table_tree)
        vbox9.pack_start(scrollTree, True, True, 0)
        grid.attach_next_to(vbox9, vbox, Gtk.PositionType.RIGHT, 3, 25)
        grid.set_column_homogeneous(True)
        grid.set_column_spacing(25)
        grid.set_row_spacing(25)

        return grid

    def create_ui(self):
        grid, vbox = self.function_entry()
        grid, vbox2 = self.derivate_function_entry(grid, vbox)
        grid, vbox3 = self.tolerancia_value_entry(grid, vbox2)
        grid, vbox4 = self.initial_value_and_entry(grid, vbox3)
        grid, vbox5 = self.iteration_value_entry(grid, vbox3)
        grid, vbox6 = self.button_box(grid, vbox5)
        grid, vbox7 = self.result_entry(grid, vbox6)
        grid, vbox8 = self.graph(grid, vbox7)
        grid = self.table(grid, vbox)

        return grid

    def evaluate_function(self, widget):
        initial_value = float(self.x0.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())
        d_func = Function(self.derivate_function.get_text())

        self.fixed_point_Search = FPSearch()
        range_of_root = self.fixed_point_Search.evaluate(
        tolerance, initial_value, iterations, func, d_func)
        self.result.set_text(str(range_of_root))

    def graph_function(self, widget):
        initial_value = float(self.x0.get_text())
        increment = 0.1
        iterations = float(self.iterations.get_text())
        final_value = math.fabs(initial_value+math.fabs(increment*iterations))
        func = Function(self.function.get_text())

        a = self.figure.add_subplot(111)
        x = np.arange(initial_value, final_value, increment)
        a.plot(x, [func.evaluate(i) for i in x])

        self.canvas.draw()

    def show_table(self, widget):

        if(self.table_tree.get_model() != None):
            self.table_tree.set_model(self.table_tree.get_model().clear())
            self.table_tree.remove_column(self.table_tree.get_column(0))
            self.table_tree.remove_column(self.table_tree.get_column(0))
            self.table_tree.remove_column(self.table_tree.get_column(0))
            self.table_tree.remove_column(self.table_tree.get_column(0))

        df = pd.DataFrame(self.fixed_point_Search.values,
                          columns=['iter', 'x Value', 'F(x) Value', 'Error'])
        # los foat dicen de cuantas columnas va a ser la tabla
        self.store = Gtk.ListStore(int, float, float, float)

        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))

        self.table_tree.set_model(self.store)

        for i, col in enumerate(['Iter', 'g(Xn)', 'f(Xn)', 'Error']):
            renderer = Gtk.CellRendererText()

            column = Gtk.TreeViewColumn(col, renderer, text=i)

            self.table_tree.append_column(column)

    def on_help_clicked(self, widget):
        dialog = Gtk.MessageDialog(
            None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Newton Search Help")
        dialog.format_secondary_text(
            "El método de punto fijo reformula la ecuación f(x)=0 y genera una ecuación de la forma x=g(x) que permite encontrar un valor de x que al reemplazarlo en g su resultado sea el mismo, es decir que x sea invariable para g, y adicionalmente que la f(x) converja a cero.\n\nSe dispone de un intervalo [a,b] para el cual la función g es continua y se cumple que para todo valor de x en el intervalo, g(x) también pertenece al mismo intervalo. Además para garantizar la unicidad de dicho punto se debe cumplir que la derivada g′(x)<1 en el intervalo.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()
