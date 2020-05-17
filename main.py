import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from NonLinearEquations.NonLinearEquationsUI import Handler


class App:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("Prueba.glade")

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('main.css')
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        go = self.builder.get_object
        
        self.window = go("window1")
        self.method = go("Method")
        self.error = go("Error")
        self.help = go("Help")
        self.function = go("Function")
        self.gfunction = go("GFunction")
        self.iterations = go("Iterations")
        self.increment = go("Increment")
        self.initial = go("Initial")
        self.superior = go("Superior")
        self.result = go("Result")
        self.tolerance = go("Tolerance")

        self.parameters = self.method, self.error, self.help, self.function, self.gfunction, self.iterations, self.increment, self.initial, self.superior, self.result, self.tolerance
        self.builder.connect_signals(Handler(self.parameters))

        self.window.show()


if __name__ == '__main__':
    try:
        gui = App()
        Gtk.main()
    except KeyboardInterrupt:
        pass
