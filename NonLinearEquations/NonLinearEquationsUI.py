import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .functions.Incremental_Search_UI import incremental_search_ui as isui
from .functions.Bisection_Search_UI import bisection_search_ui as bsui
from .functions.FalseRule_Search_UI import falseRule_search_ui as fsui

class NonLinealMenu(Gtk.Notebook):

    def __init__(self):
        self.notebook = self.create_ui()


    def create_ui(self):

        notebook = Gtk.Notebook()
        page1 = Gtk.Box()
        page1.set_border_width(10)
        page1.add(isui().grid)
        notebook.append_page(page1, Gtk.Label('Incremental Search'))

        page2 = Gtk.Box()
        page2.set_border_width(10)
        page2.add(bsui().grid)
        notebook.append_page(page2, Gtk.Label('Bisection Search'))


        page3 = Gtk.Box()
        page3.set_border_width(10)
        page3.add(fsui().grid)
        notebook.append_page(page3, Gtk.Label('False-Rule Search'))


        page4 = Gtk.Box()
        page4.set_border_width(10)
        page4.add(Gtk.Label('The other one'))
        notebook.append_page(page4, Gtk.Label('Plain Title'))


        page5 = Gtk.Box()
        page5.set_border_width(10)
        page5.add(Gtk.Label('The last one'))
        notebook.append_page(page5, Gtk.Label('Plain Title'))

        return notebook
