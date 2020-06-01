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
        
