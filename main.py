import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from NonLinearEquations.NonLinearEquationsUI import Handler


class App:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file("Prueba.glade")

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

        self.variables = go("VariablesM")
        self.generate_button = go("generate_button")
        self.initialValues = go("initialValues")
        self.initialValues_button = go("initialValues_button")
        self.matrixMethods = go("matrixMethods")
        self.evalOptions = go("evalOptionsID")
        self.tolerance = go('tolerance')
        self.iterations = go('iterations')
        self.lambda = go('lambda')
        self.resultMatrix = go("resultMatrixID")
        self.evaluateMatrix = go("evaluateMatrixID")

        self.parameters2 = self.variables, self.generate_button, self.initialValues, self.initialValues_button, self.matrixMethods, self.evalOptions, self.tolerance, self.iterations, self.lambda, self.resultMatrix, self.evaluateMatrix

        self.builder.connect_signals(Handler(self.parameters, self.parameters2))

        self.window.connect("destroy", Gtk.main_quit)
        gtk_style()
        self.window.show_all()


def gtk_style():

    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path("main.css")
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


if __name__ == '__main__':
    try:
        gui = App()
        Gtk.main()
    except KeyboardInterrupt:
        pass
