import gi
import math
import numpy as np
import pandas as pd
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .functions.Function import Function
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import FigureCanvas
from matplotlib.backends.backend_gtk3 import (
        NavigationToolbar2GTK3 as NavigationToolbar)

def graphic(funcion, initial_value, iterations):
    function = Function(funcion)

    win = Gtk.Window()
    win.connect("destroy", lambda x: Gtk.main_quit())
    win.set_default_size(640, 480)
    win.set_title("Embedding in GTK")

    vbox = Gtk.VBox()
    win.add(vbox)

    increment = 0.01
    final_value = math.fabs(initial_value+math.fabs(increment*100))

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    x = np.arange(-50, 3, 0.01)
    y = [function.evaluate2(i) for i in x]
    ax.plot(x, y)

    canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
    vbox.pack_start(canvas, True, True, 0)
    toolbar = NavigationToolbar(canvas, win)
    vbox.pack_start(toolbar, False, False, 0)

    win.show_all()
    Gtk.main()
