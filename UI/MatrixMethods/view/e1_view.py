import gi
import pandas as pd
from .matrix_handler import Matrix_Handler
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class Matrix_View2:

    def __init__(self, matrix_l, matrix_u, vector_z, vector_x):

        self.builder = Gtk.Builder()
        self.builder.add_from_file('UI/MatrixMethods/view/factorizacion_view.glade')
        go = self.builder.get_object

        self.matrix_l = matrix_l
        self.matrix_u = matrix_u
        self.vector_z = vector_z
        self.vector_x = vector_z
        
        self.window = go("")
        self.matrix_l_view = go("LMatrix")
        self.matrix_u_view = go("UMatrix")
        self.vector_z_view = go("ZVector")
        self.vector_x_view = go("XVector")
    
        self.show_matrix_l()
        self.show_matrix_u()
        self.show_vector_x()
        self.show_vector_z()
        #self.builder.connect_signals()

        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()
    

    def show_matrix_l(slef):
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        #self.add(self.grid)
        
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scrollTree.add(self.matrix_l_view)


        df = pd.DataFrame(self.matrix_l)
        columns = len(df.columns)

        column = []
        for i in range(columns):
            column.append(str(i))

        if(self.matrix_l_view.get_model() != None):
            for i in len(column):
                self.matrix_l_view.remove_column(self.matrix_l_view.get_column(0))
        
        self.store = Gtk.ListStore(*([float]*columns))
        self.matrix_l_view.set_model(self.store)
        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))
        self.matrix_l_view.set_model(self.store)

        renderer = Gtk.CellRendererText()
        for i, col in enumerate(column):
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.matrix_l_view.append_column(column)
        
    def show_matrix_u(self):
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        #self.add(self.grid)
        
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scrollTree.add(self.matrix_u_view)


        df = pd.DataFrame(self.matrix_u)
        columns = len(df.columns)

        column = []
        for i in range(columns):
            column.append(str(i))

        if(self.matrix_u_view.get_model() != None):
            for i in len(column):
                self.matrix_u_view.remove_column(self.matrix_u_view.get_column(0))
        
        self.store = Gtk.ListStore(*([float]*columns))
        self.matrix_u_view.set_model(self.store)
        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))
        self.matrix_u_view.set_model(self.store)

        renderer = Gtk.CellRendererText()
        for i, col in enumerate(column):
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.matrix_u_view.append_column(column)
            
    def show_vector_x(self):
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        #self.add(self.grid)
        
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scrollTree.add(self.vector_x_view)


        df = pd.DataFrame(self.vector_x)
        columns = len(df.columns)

        column = []
        for i in range(columns):
            column.append(str(i))

        if(self.vector_x_view.get_model() != None):
            for i in len(column):
                self.vector_x_view.remove_column(self.vector_x_view.get_column(0))
        
        self.store = Gtk.ListStore(*([float]*columns))
        self.vector_x_view.set_model(self.store)
        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))
        self.vector_x_view.set_model(self.store)

        renderer = Gtk.CellRendererText()
        for i, col in enumerate(column):
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.vector_x_view.append_column(column)

    def show_vector_z(self):
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        #self.add(self.grid)
        
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scrollTree.add(self.vector_z_view)


        df = pd.DataFrame(self.vector_z)
        columns = len(df.columns)

        column = []
        for i in range(columns):
            column.append(str(i))

        if(self.vector_z_view.get_model() != None):
            for i in len(column):
                self.vector_z_view.remove_column(self.vector_z_view.get_column(0))
        
        self.store = Gtk.ListStore(*([float]*columns))
        self.vector_z_view.set_model(self.store)
        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))
        self.vector_z_view.set_model(self.store)

        renderer = Gtk.CellRendererText()
        for i, col in enumerate(column):
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.vector_z_view.append_column(column)