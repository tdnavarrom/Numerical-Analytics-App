from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')

class Guide(Gtk.Grid):

    def __init__(self):
        self.grid = Gtk.Grid()
        self.grid = self.create_ui()


    def create_ui(self):
        grid = Gtk.Grid()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        welcome_label = Gtk.Label()
        welcome_label.set_markup("<big>Guide</big>")
        welcome_label.set_line_wrap(True)
        vbox.pack_start(welcome_label, True, True, 0)

        introductory_text = Gtk.Label()

        introductory_text.set_markup(
            "This is the Guide for the application. Please <b>follow the syntax</b> listed below for the equations.\n"
            'e^n ==> exp(n)\n'
            'x^n ==> x**n\n'
            'ln(x) ==> log(x)\n'
            'cos(x) ==> cos(x)\n'
            'sin(x) ==> sin(x)\n'
        )

        introductory_text.set_line_wrap(True)
        vbox.pack_start(introductory_text, True, True, 0)

        grid.attach(vbox, 0, 0, 2, 2)

        return grid
