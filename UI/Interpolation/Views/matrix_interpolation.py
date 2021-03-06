import gi
import pandas as pd
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class Matrix_View_Interpolation:

    def __init__(self, original_matrix):

        self.builder = Gtk.Builder()
        self.builder.add_from_file('UI/Interpolation/Views/MatrixInterpolation.glade')
        go = self.builder.get_object

        self.original_matrix = original_matrix

        self.window = go("Window3")
        self.original_matrix_view = go("matrixInterpolation")        

        self.show_original_matrix()

        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()
    
    def show_original_matrix(self):
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        #self.add(self.grid)
        
        scrollTree = Gtk.ScrolledWindow(hexpand=True, vexpand=True)
        scrollTree.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scrollTree.add(self.original_matrix_view)


        df = pd.DataFrame(self.original_matrix)
        columns = len(df.columns)

        column = []
        for i in range(columns):
            column.append(str(i))

        if(self.original_matrix_view.get_model() != None):
            for i in len(column):
                self.original_matrix_view.remove_column(self.original_matrix_view.get_column(0))
        
        self.store = Gtk.ListStore(*([float]*columns))
        self.original_matrix_view.set_model(self.store)
        for i, j in df.iterrows():
            # i es el index del DataFrame
            # J es la tupla donde esta el valor de x & y
            # los dos son un row del DataFrame
            tuple_of_row = j
            self.store.append(list(tuple_of_row))
        self.original_matrix_view.set_model(self.store)

        renderer = Gtk.CellRendererText()
        for i, col in enumerate(column):
            column = Gtk.TreeViewColumn(col, renderer, text=i)
            column.set_resizable(True)
            column.set_expand(True)
            self.original_matrix_view.append_column(column)

def gtk_style():
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path("main.css")
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

