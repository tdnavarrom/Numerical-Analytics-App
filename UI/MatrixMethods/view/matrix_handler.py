from gi.repository import Gtk
import gi
import pandas as pd
import numpy as np

gi.require_version("Gtk", "3.0")


# Falta parsear el float de resultados a strings, para que no coma decimales.
class Matrix_Handler:
    def __init__(self, parameters):
        self.parameters = parameters
        self.contador_etapas = 0
        self.columns = 0
    
    def result_pressed(self, button):
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        #self.add(self.grid)
        
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scrollTree.add(self.parameters[1])
        #self.parameters[1].set_model(None)
        print("AAAAA ",self.parameters[1].get_column(0))


        df = pd.DataFrame(self.parameters[4])
        columns = len(df.columns)


        column = []
        for i in range(columns):
            column.append(str(i))
            
        if(self.parameters[1].get_model() != None):
            for i in range(len(self.parameters[1].get_columns())):
                self.parameters[1].remove_column(self.parameters[1].get_column(0))
        
        self.store = Gtk.ListStore(*([float]*columns))
        self.parameters[1].set_model(self.store)

        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            
            tuple_of_row = j
            print(tuple_of_row)
            self.store.append(list(tuple_of_row))
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)

            print('i ', i)
            print('col', col)

            self.parameters[1].append_column(column)

    def step_pressed(self, button):

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        #self.add(self.grid)
        
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scrollTree.add(self.parameters[1])

        self.contador_etapas += 1
        df = pd.DataFrame(self.parameters[5][self.contador_etapas])
        self.columns = len(df.columns)
        
        column = []
        for i in range(self.columns):
            column.append(str(i))

        if(self.parameters[1].get_model() != None):
            for i in range(len(column)-1):
                self.parameters[1].remove_column(self.parameters[1].get_column(0))
        
        self.store = Gtk.ListStore(*([float]*self.columns))
        self.parameters[1].set_model(self.store)
        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            print(tuple_of_row)
            self.store.append(list(tuple_of_row))
        self.parameters[1].set_model(self.store)

        renderer = Gtk.CellRendererText()
        for i, col in enumerate(column):
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.parameters[1].append_column(column)
