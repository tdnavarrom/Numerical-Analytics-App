import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .functions.functionsUI import function_user_interface as fui

class NonLinealMenu(Gtk.Notebook):

    def __init__(self):
        self.notebook = self.create_ui()


    def create_ui(self):

        notebook = Gtk.Notebook()
        page1 = Gtk.Box()
        page1.set_border_width(10)
        page1.add(fui().grid)
        notebook.append_page(page1, Gtk.Label('Incremental Search'))

        page2 = Gtk.Box()
        page2.set_border_width(10)
        page2.add(Gtk.Label('Plain Text'))
        notebook.append_page(page2, Gtk.Label('Bisection Method'))


        page3 = Gtk.Box()
        page3.set_border_width(10)
        page3.add(Gtk.Label('The other'))
        notebook.append_page(page3, Gtk.Label('Plain Title'))


        page4 = Gtk.Box()
        page4.set_border_width(10)
        page4.add(Gtk.Label('The other one'))
        notebook.append_page(page4, Gtk.Label('Plain Title'))


        page5 = Gtk.Box()
        page5.set_border_width(10)
        page5.add(Gtk.Label('The last one'))
        notebook.append_page(page5, Gtk.Label('Plain Title'))

        return notebook
