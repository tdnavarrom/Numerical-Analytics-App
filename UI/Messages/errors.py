from gi.repository import Gtk, Gdk
import gi

gi.require_version('Gtk', '3.0')


class Errors:
    def non_lineal_errors(self, list_error):
        """
        list_error[0]:     Function
        list_error[1]:     GFunction
        list_error[2]:     Iterations
        list_error[3]:     Increments
        list_error[4]:     Initial
        list_error[5]:     Superior
        list_error[6]:     Tolerance
        """
        
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text(self.messages(list_error))
        dialog.run()
        dialog.destroy()
    
    def messages(self,list_error):
        """
        list_error[0]:     Function
        list_error[1]:     GFunction
        list_error[2]:     Iterations
        list_error[3]:     Increments
        list_error[4]:     Initial
        list_error[5]:     Superior
        list_error[6]:     Tolerance
        """
        text = "Ingrese:"
        if list_error[0]  == 1 :
            text += '\n - Function.'
        if list_error[1]  == 1 :
            text += '\n - GFunction.'
        if list_error[2]  == 1 :
            text += '\n - Iterations value.'
        if list_error[3]  == 1 :
            text += '\n - Increments value.'
        if list_error[4]  == 1 :
            text += '\n - Initial value.'
        if list_error[5]  == 1 :
            text += '\n - Superior value.'
        if list_error[6]  == 1 :
            text += '\n - Tolerance.'
        return text
    
    def lineal_errors(self, list_errors):
        """
        list_errors[0]:      variables
        """
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text(self.messages2(list_errors))
        dialog.run()
        dialog.destroy()
    
    def messages2(self,list_error):
        """
        list_error[0]:    Variables
        """
        text = "Ingrese:"
        if list_error[0]  == 1 :
            text += '\n - Number of variables.'
        return text
    
    def div_0(self):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text("División por 0")
        dialog.run()
        dialog.destroy()
    
    def determinante_0(self):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text("La determinante es igual a 0, por lo tanto tiene infinitas soluciones, o ninguna.")
        dialog.run()
        dialog.destroy()

    def negativeRoot(self):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text("Un elemento de la matriz es negativo, por lo que no se puede calcular la raiz")
        dialog.run()
        dialog.destroy()

    def invalidIter(self):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text("El valor ingresado para las iteraciones es invalido. Por favor ingrese un numero entero positivo.")
        dialog.run()
        dialog.destroy()

    def invalidTol(self):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text("El valor ingresado para la tolerancia es invalido. Por favor ingrese un numero entre 0 y 1. ")
        dialog.run()
        dialog.destroy()

    def invalidLambda(self):
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Error")
        dialog.format_secondary_text("El valor ingresado para la relajacion es invalido. Por favor ingrese un numero mayor o igual a 0")
        dialog.run()
        dialog.destroy()
        
          

class ZeroDeterminantException(Exception):
    """Raised when The determinant of a matrix A is zero"""
    pass

class InvalidIterException(Exception):
    """ Raised when the value given for iterations is <1 or not a positive integer"""
    pass

class InvalidToleranceException(Exception):
    """ Raised when the value given for a tolerance is not between 0 and 1"""
    pass

class InvalidLambdaException(Exception):
    """Raised when the value given for Lambda is not a positive number"""
    pass

class NegativeRoot(Exception):
    """ Raised when attempting to calculat ethe root of a negative number, 0"""
    pass