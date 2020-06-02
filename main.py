import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from UI.UIHandler import Handler


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
        self.tolerance = go("tolerance")
        self.iterations = go("iterations")
        self.lambd = go("lambda")
        self.resultMatrix = go("resultMatrixID")
        self.evaluateMatrix = go("evaluateMatrixID")
        self.helpMatrix = go("HelpMatrix")

        self.parameters2 = self.variables, self.generate_button, self.initialValues, self.initialValues_button, self.matrixMethods, self.tolerance, self.iterations, self.lambd, self.resultMatrix, self.evaluateMatrix, self.helpMatrix

        self.interpolationMethods = go("interpolationMethods")
        self.initialValuesInterpolation = go("initialValuesInterpolation")
        self.initialValuesInterpolation_button = go("insertInitialValues")
        self.functionInterpolation = go("functionInterpolation")
        self.xvalues_interpolation = go("xValues")
        self.xvalues_button = go("insertXValues")
        self.fx_values_interpolation = go("fxValues")
        self.fx_values_button = go("insertFXValues")
        self.result_interpolation = go("result_interpolation")
        self.evaluate_interpolation = go("evaluateInterpolation")
        self.helpInterpolation = go("helpInterpolation")

        self.parameters3 = self.interpolationMethods, self.initialValuesInterpolation, self.initialValuesInterpolation_button, self.functionInterpolation, self.xvalues_interpolation, self.xvalues_button, self.fx_values_interpolation, self.fx_values_button, self.result_interpolation, self.evaluate_interpolation, self.helpMatrix

        self.builder.connect_signals(Handler(self.parameters, self.parameters2, self.parameters3))

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
