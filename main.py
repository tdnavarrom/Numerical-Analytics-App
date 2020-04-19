from NonLinearEquations.NonLinearEquationsUI import NonLinealMenu as nleMenu
from NonLinearEquations.NonLinearEquationsUI2 import NonLinealMenu2 as nleMenu2
from Welcome import Welcome
from Guide import Guide

from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')


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
        self.page1.add(Welcome().grid)
        self.notebook.append_page(self.page1, Gtk.Label('Welcome'))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Guide().grid)
        self.notebook.append_page(self.page2, Gtk.Label('Non-Linear Equations'))


        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.add(nleMenu2().grid)
        self.notebook.append_page(self.page3, Gtk.Label('Equations\' System'))

        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        self.page4.add(Gtk.Label('Otro Menu'))
        self.notebook.append_page(self.page4, Gtk.Label('Interpolation'))

        self.page5 = Gtk.Box()
        self.page5.set_border_width(10)
        self.page5.add(Gtk.Label('Otro Menu'))
        self.notebook.append_page(self.page5, Gtk.Label('Differentiation And Numeric Integration'))

        self.page6 = Gtk.Box()
        self.page6.set_border_width(10)
        self.page6.add(Guide().grid)
        self.notebook.append_page(self.page6, Gtk.Label('Guide'))


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
