from gi.repository import Gtk
import gi
import pandas as pd
import numpy as np

gi.require_version("Gtk", "3.0")


class Tree_View_J_S(Gtk.Window):
    def __init__(self, table):
        Gtk.Window.__init__(self)
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

        if(self.table_tree.get_model() != None and self.table_tree.get_column(0) != None):
            for i in range(len(self.table_tree[1].get_columns())):
                self.table_tree[1].remove_column(
                    self.table_tree[1].get_column(0))

        df = pd.DataFrame(table)
        print(df)
        columns = len(df.columns)
        column = []
        for i in range(columns):
            column.append(str(i))
        # los foat dicen de cuantas columnas va a ser la tabla
        self.store = Gtk.ListStore(*([float]*columns))

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
            column.set_expand(True)
            self.table_tree.append_column(column)

        self.grid.attach(scrollTree, 0, 0, 8, 10)
