import math
import numpy as np
import pandas as pd
from matplotlib import pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from .FalseRuleSearch import FalseRule as FSearch
from .Function import Function
from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


class falseRule_search_ui(Gtk.Grid):

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
        label_function = Gtk.Label("Function")
        vbox.pack_start(label_function, True, True, 0)
        vbox.pack_start(self.function, True, True, 0)
        grid.attach(vbox, 0, 0, 3, 5)

        return grid, vbox


    def tolerancia_value_entry(self, grid, vbox):
        """
        Increment Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox
        Returns:
            grid
            vbox2

        """
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.tolerance = Gtk.Entry()
        label_tolerance = Gtk.Label("Tolerance")
        vbox2.pack_start(label_tolerance, True, True, 0)
        vbox2.pack_start(self.tolerance, True, True, 0)
        grid.attach_next_to(vbox2, vbox, Gtk.PositionType.BOTTOM, 3, 5)

        return grid, vbox2


    def inferior_value_and_entry(self, grid, vbox2):
        """
        Initial Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox2
        Returns:
            grid
            vbox3
        """
        vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.x0 = Gtk.Entry()
        label_x0 = Gtk.Label("Inferior Value")
        vbox3.pack_start(label_x0, True, True, 0)
        vbox3.pack_start(self.x0, True, True, 0)
        grid.attach_next_to(vbox3, vbox2, Gtk.PositionType.BOTTOM, 1, 5)

        return grid, vbox3

    def superior_value_entry(self, grid, vbox3):
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
        self.xs = Gtk.Entry()
        label_xs = Gtk.Label("Superior Value")
        vbox4.pack_start(label_xs, True, True, 0)
        vbox4.pack_start(self.xs, True, True, 0)
        grid.attach_next_to(vbox4, vbox3, Gtk.PositionType.RIGHT, 1, 5)

        return grid, vbox4

    def iteration_value_entry(self, grid, vbox4):
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
        label_iterations = Gtk.Label("Iterations")
        vbox5.pack_start(label_iterations, True, True, 0)
        vbox5.pack_start(self.iterations, True, True, 0)
        grid.attach_next_to(vbox5, vbox4, Gtk.PositionType.RIGHT, 1, 5)

        return grid, vbox5

    def button_box(self, grid, vbox3):
        '''
        Box that contains all Buttons.

        Parameters:
            grid
            vbox3
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
        grid.attach_next_to(vbox6, vbox3, Gtk.PositionType.BOTTOM, 3, 5)

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
        label_result = Gtk.Label("Result")
        self.result = Gtk.Entry()
        vbox7.pack_start(label_result, True, True, 0)
        vbox7.pack_start(self.result, True, True, 0)
        grid.attach_next_to(vbox7, vbox6, Gtk.PositionType.BOTTOM, 3, 5)

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
        label_graph = Gtk.Label("Function's Graph")
        self.figure = Figure(figsize=(3, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.set_size_request(400, 300)
        vbox8.pack_start(label_graph, True, True, 0)
        vbox8.pack_start(self.canvas, True, True, 0)
        grid.attach_next_to(vbox8, vbox7, Gtk.PositionType.BOTTOM, 3, 5)

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
        label_table = Gtk.Label("Function's Table")
        vbox9.pack_start(label_table, True, True, 0)
        vbox10 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.table_tree = Gtk.TreeView()
        scrollTree.add(self.table_tree)
        vbox10.pack_start(scrollTree, True, True, 0)
        grid.attach_next_to(vbox9, vbox, Gtk.PositionType.RIGHT, 1, 5)
        grid.attach_next_to(vbox10, vbox9, Gtk.PositionType.BOTTOM, 1, 25)
        grid.set_column_homogeneous(True)
        grid.set_column_spacing(8)
        grid.set_row_spacing(8)

        return grid

    def create_ui(self):
        grid, vbox = self.function_entry()
        grid, vbox2 = self.tolerancia_value_entry(grid, vbox)
        grid, vbox3 = self.inferior_value_and_entry(grid, vbox2)
        grid, vbox4 = self.superior_value_entry(grid, vbox3)
        grid, vbox5 = self.iteration_value_entry(grid, vbox4)
        grid, vbox6 = self.button_box(grid, vbox3)
        grid, vbox7 = self.result_entry(grid, vbox6)
        grid, vbox8 = self.graph(grid, vbox7)
        grid = self.table(grid, vbox)

        return grid

    def evaluate_function(self, widget):
        inferior_value = float(self.x0.get_text())
        superior_value = float(self.xs.get_text())
        tolerance = float(self.tolerance.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())

        self.false_rule_Search = FSearch()
        range_of_root = self.false_rule_Search.evaluate(
            inferior_value, superior_value, tolerance, iterations, func, type_error = 1)
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

        df = pd.DataFrame(self.false_rule_Search.values,
                          columns=['x Value', 'F(x) Value', 'Error'])
        # los foat dicen de cuantas columnas va a ser la tabla
        self.store = Gtk.ListStore(float, float, float)

        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            print(tuple_of_row)
            self.store.append(list(tuple_of_row))

        self.table_tree.set_model(self.store)

        for i, col in enumerate(['X value', 'F(x) value', 'Error']):
            renderer = Gtk.CellRendererText()

            column = Gtk.TreeViewColumn(col, renderer, text=i)

            self.table_tree.append_column(column)
