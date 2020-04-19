from gi.repository import Gtk
import gi
import pandas as pd
import numpy as np

gi.require_version("Gtk", "3.0")


class TreeView(Gtk.Window):
    def __init__(self, table, column, tip):
        Gtk.Window.__init__(self, title="Treeview Filter Demo")
        self.set_border_width(10)
        self.set_default_size(500, 600)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        self.table_tree = Gtk.TreeView()
        scrollTree.add(self.table_tree)

        if(self.table_tree.get_model() != None):
            for i in len(column):
                self.table_tree.remove_column(self.table_tree.get_column(0))

        df = pd.DataFrame(table,
                          columns=column)
        # los foat dicen de cuantas columnas va a ser la tabla
        if tip == "Bisection":
            self.store = Gtk.ListStore(int, float, float, float, str, str)
        elif tip == "Incremental_search":
            self.store = Gtk.ListStore(int, float, float)

        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))

        self.table_tree.set_model(self.store)

        for i, col in enumerate(column):
            renderer = Gtk.CellRendererText()

            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            self.table_tree.append_column(column)

        self.grid.attach(scrollTree, 0, 0, 8, 10)
