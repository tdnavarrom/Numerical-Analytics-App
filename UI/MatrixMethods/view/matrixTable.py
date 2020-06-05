from gi.repository import Gtk
import gi
import pandas as pd
import numpy as np

gi.require_version("Gtk", "3.0")


class TreeView2(Gtk.Window):
    def __init__(self,rows ,columns):
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

        column = []
        for i in range(columns):
            column.append(str(i))

        self.store = Gtk.ListStore(*([str]*columns))
        self.table_tree.set_model(self.store)

        self.numpy = np.zeros(shape=(rows, columns))
        self.df = pd.DataFrame(data = self.numpy).astype(str)
        for i, j in self.df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))
        self.table_tree.set_model(self.store)

        renderer = Gtk.CellRendererText()
        renderer.set_property("editable", True)
        for i, col in enumerate(column):
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.table_tree.append_column(column)

        renderer.connect("edited", self.text_edited)
        print(self.store)

        self.grid.attach(scrollTree, 0, 0, 8, 10)


    def text_edited(self, widget, path, text):
        col = int(self.table_tree.get_cursor()[1].get_title())
        self.store[path][col] = text
        self.df.iloc[int(path),int(col)]=float(text)

    def returnTable(self):
        return self.df
