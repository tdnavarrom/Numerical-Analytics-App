import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .Function import Function
from .IncrementalSearch import IncrementalSearch as ISearch

from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib import pyplot
import pandas as pd
import numpy as np
import math

class incremental_search_ui(Gtk.Grid):

    def __init__(self):

        """ Grid that contains basic UI Components for all NonLinear Functions"""
        self.grid = Gtk.Grid()
        self.grid = self.create_ui()



    def create_ui(self):
        #Function Label and Entry at the bottom, with Evaluate Button
        grid = Gtk.Grid()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        self.function = Gtk.Entry()
        label_function = Gtk.Label("Function")
        vbox.pack_start(label_function, True, True, 0)
        vbox.pack_start(self.function, True, True, 0)

        grid.attach(vbox, 0, 0, 3, 5)

        #Initial Value Label and Entry at the bottom
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        self.x0 = Gtk.Entry()
        label_x0 = Gtk.Label("Initial Value")
        vbox2.pack_start(label_x0, True, True, 0)
        vbox2.pack_start(self.x0, True, True, 0)

        grid.attach_next_to(vbox2, vbox, Gtk.PositionType.BOTTOM, 1, 5)

        #Increment Value Label and Entry at the bottom
        vbox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.increment = Gtk.Entry()
        label_increment = Gtk.Label("Increment")
        vbox3.pack_start(label_increment, True, True, 0)
        vbox3.pack_start(self.increment, True, True, 0)

        grid.attach_next_to(vbox3, vbox2, Gtk.PositionType.RIGHT, 1, 5)

        #Iterations Value Label and Entry at the bottom
        vbox4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.iterations = Gtk.Entry()
        label_iterations = Gtk.Label("Iterations")
        vbox4.pack_start(label_iterations, True, True, 0)
        vbox4.pack_start(self.iterations, True, True, 0)

        grid.attach_next_to(vbox4, vbox3, Gtk.PositionType.RIGHT, 1, 5)

        #Box that contains all Buttons
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

        grid.attach_next_to(vbox5, vbox2, Gtk.PositionType.BOTTOM, 3, 5)

        #Result Entry
        vbox6 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        label_result = Gtk.Label("Result")
        self.result = Gtk.Entry()
        vbox6.pack_start(label_result, True, True, 0)
        vbox6.pack_start(self.result, True, True, 0)

        grid.attach_next_to(vbox6, vbox5, Gtk.PositionType.BOTTOM, 3, 5)

        #Graph
        vbox7 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        label_graph = Gtk.Label("Function's Graph")
        self.figure = Figure(figsize=(3,4), dpi = 100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.set_size_request(400,300)
        vbox7.pack_start(label_graph, True, True, 0)
        vbox7.pack_start(self.canvas, True, True, 0)

        grid.attach_next_to(vbox7, vbox6, Gtk.PositionType.BOTTOM, 3, 5)

        #Table
        vbox8 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        label_table = Gtk.Label("Function's Table")
        vbox8.pack_start(label_table, True, True, 0)

        vbox9 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.table_tree = Gtk.TreeView()
        scrollTree.add(self.table_tree)
        vbox9.pack_start(scrollTree, True, True, 0)

        grid.attach_next_to(vbox8, vbox, Gtk.PositionType.RIGHT, 1, 5)
        grid.attach_next_to(vbox9, vbox8, Gtk.PositionType.BOTTOM, 1, 25)

        grid.set_column_homogeneous(True)
        grid.set_column_spacing(8)
        grid.set_row_spacing(8)

        return grid



    def evaluate_function(self, widget):
        initial_value = float(self.x0.get_text())
        increment = float(self.increment.get_text())
        iterations = float(self.iterations.get_text())
        func = Function(self.function.get_text())

        self.incremental_Search = ISearch()
        range_of_root = self.incremental_Search.evaluate(initial_value, increment, iterations, func)
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

        df = pd.DataFrame(self.incremental_Search.values, columns=['x value', 'y value'])
        self.store = Gtk.ListStore(float, float)

        for i,j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))

        self.table_tree.set_model(self.store)

        for i, col in enumerate(['x value', 'y value']):
            renderer = Gtk.CellRendererText()

            column = Gtk.TreeViewColumn(col, renderer, text=i)

            self.table_tree.append_column(column)
