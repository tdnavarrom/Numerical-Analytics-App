import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from NonLinearEquations.NonLinearEquationsUI import NonLinealMenu as nleMenu

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Change Analytics")
        self.set_border_width(5)

        self.notebook = Gtk.Notebook()
        self.notebook.set_show_border(True)
        self.notebook.set_tab_pos(Gtk.PositionType(0))

        self.add(self.notebook)

        nleNotebook = nleMenu().notebook

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(nleNotebook)
        self.notebook.append_page(self.page1, Gtk.Label('Non Linear Equations') )

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('Otra Vuelta'))
        self.notebook.append_page(self.page2, Gtk.Label('Otro Menu'))

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
