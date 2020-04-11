import math
import numpy as np
import pandas as pd
from matplotlib import pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from .IncrementalSearch import IncrementalSearch as ISearch
from .Function import Function
from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


class incremental_search_ui(Gtk.Grid):

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
        grid.attach(vbox, 0, 0, 1, 2)

        return grid, vbox

    def initial_value_and_entry(self, grid, vbox):
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
        self.x0 = Gtk.Entry()
        self.x0.set_placeholder_text("Initial Value")
        vbox2.pack_start(self.x0, True, True, 0)
        grid.attach_next_to(vbox2, vbox, Gtk.PositionType.RIGHT, 1, 2)

        return grid, vbox2

    def increment_value_entry(self, grid, vbox):
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
        self.increment = Gtk.Entry()
        self.increment.set_placeholder_text("Increment")
        vbox3.pack_start(self.increment, True, True, 0)
        grid.attach_next_to(vbox3, vbox, Gtk.PositionType.BOTTOM, 1, 2)

        return grid, vbox3

    def iteration_value_entry(self, grid, vbox3):
        '''
        Iterations Value Label and Entry at the bottom.

        Parameters:
            grid
            vbox3
        Returns:
            grid
            vbox4
        '''
        vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.iterations = Gtk.Entry()
        self.iterations.set_placeholder_text("Iterations")
        vbox4.pack_start(self.iterations, True, True, 0)
        grid.attach_next_to(vbox4, vbox3, Gtk.PositionType.RIGHT, 1, 2)

        return grid, vbox4

    def button_box(self, grid, vbox2):
        '''
        Box that contains all Buttons.

        Parameters:
            grid
            vbox2
        Returns:
            grid
            vbox5
        '''
        vbox5 = Gtk.Box(spacing=8)
        button = Gtk.Button(label="Evaluate")
        button.connect('clicked', self.evaluate_function)
        vbox5.pack_start(button, True, True, 0)
        button2 = Gtk.Button(label="Graph")
        button2.connect('clicked', self.graph_function)
        vbox5.pack_start(button2, True, True, 0)
        button3 = Gtk.Button(label="Table")
        button3.connect('clicked', self.show_table)
        vbox5.pack_start(button3, True, True, 0)
        grid.attach_next_to(vbox5, vbox2, Gtk.PositionType.BOTTOM, 2, 1)

        return grid, vbox5

    def result_entry(self, grid, vbox5):
        '''
        Result Entry.

        Parameters:
            grid
            vbox5
        Returns:
            grid
            vbox6
        '''
        vbox6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.result = Gtk.Entry()
        self.result.set_placeholder_text("Result")
        vbox6.pack_start(self.result, True, True, 0)
        grid.attach_next_to(vbox6, vbox5, Gtk.PositionType.BOTTOM, 2, 1)

        return grid, vbox6

    def graph(self, grid, vbox6):
        '''
        Graphic of the function.

        Parameters:
            grid
            vbox6
        Returns:
            grid
            vbox7
        '''
        vbox7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        label_graph = Gtk.Label("Function's Graph")
        self.figure = Figure(figsize=(3, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.set_size_request(400, 300)
        vbox7.pack_start(label_graph, True, True, 0)
        vbox7.pack_start(self.canvas, True, True, 0)
        grid.attach_next_to(vbox7, vbox6, Gtk.PositionType.BOTTOM, 2, 5)

        return grid, vbox7

    def table(self, grid, vbox):
        '''
        Table of the function.

        Parameters:
            grid
            vbox
        Return:
            grid
        '''
        vbox8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.table_tree = Gtk.TreeView()
        scrollTree.add(self.table_tree)
        vbox8.pack_start(scrollTree, True, True, 0)
        grid.attach_next_to(vbox8, vbox, Gtk.PositionType.RIGHT, 3, 25)
        grid.set_column_homogeneous(True)
        grid.set_column_spacing(25)
        grid.set_row_spacing(25)

        return grid

    def create_ui(self):
        grid, vbox = self.function_entry()
        grid, vbox2 = self.initial_value_and_entry(grid, vbox)
        grid, vbox3 = self.increment_value_entry(grid, vbox)
        grid, vbox4 = self.iteration_value_entry(grid, vbox3)
        grid, vbox5 = self.button_box(grid, vbox3)
        grid, vbox6 = self.result_entry(grid, vbox5)
        grid, vbox7 = self.graph(grid, vbox6)
        grid = self.table(grid, vbox2)

        return grid

    def evaluate_function(self, widget):
        initial_value = float(self.x0.get_text())
        increment = float(self.increment.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())

        self.incremental_Search = ISearch()
        range_of_root = self.incremental_Search.evaluate(
            initial_value, increment, iterations, func)
        self.result.set_text(str(range_of_root))

    def graph_function(self, widget):
        initial_value = float(self.x0.get_text())
        increment = float(self.increment.get_text())
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

        df = pd.DataFrame(self.incremental_Search.values,
                          columns=['Iter', 'x Value', 'F(x) Value'])
        self.store = Gtk.ListStore(int, float, float)

        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))

        self.table_tree.set_model(self.store)

        for i, col in enumerate(['Iter', 'x Value', 'F(x) value']):
            renderer = Gtk.CellRendererText()

            column = Gtk.TreeViewColumn(col, renderer, text=i)

            self.table_tree.append_column(column)
