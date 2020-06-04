from sympy import *

def derivate_function(function):
    x = Symbol('x')
    dif = diff(function,x)
    return str(dif)
