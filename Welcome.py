from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')

class Welcome(Gtk.Grid):

    def __init__(self):
        self.grid = Gtk.Grid()
        self.grid = self.create_ui()


    def create_ui(self):
        grid = Gtk.Grid()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        welcome_label = Gtk.Label()
        welcome_label.set_markup("<big>Welcome</big>")
        welcome_label.set_line_wrap(True)
        vbox.pack_start(welcome_label, True, True, 0)

        introductory_text = Gtk.Label()

        introductory_text.set_markup(
            "This application is made for the <b>Numeric Analytics Course</b> "
            "from <b>EAFIT University</b>. It has many algorithmic soluctions to solve equations."
            'It was made with <a href="https://www.gtk.org" title="GTK Web">Gtk3</a> and Python'
        )

        introductory_text.set_line_wrap(True)
        vbox.pack_start(introductory_text, True, True, 0)

        grid.attach(vbox, 0, 0, 2, 2)

        return grid
