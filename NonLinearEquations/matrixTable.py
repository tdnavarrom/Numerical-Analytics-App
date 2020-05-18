from gi.repository import Gtk
import gi
import pandas as pd
import numpy as np

gi.require_version("Gtk", "3.0")


class TreeView(Gtk.Window):
    def __init__(self, number):
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
        for i in range(number):
            column.append(str(i))

            
        for i, col in enumerate(column):
            renderer = Gtk.CellRendererText()

            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.table_tree.append_column(column)

        self.grid.attach(scrollTree, 0, 0, 8, 10)
