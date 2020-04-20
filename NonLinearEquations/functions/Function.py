from scitools.StringFunction import StringFunction
from math import *

class Function:
    def __init__(self,input):
        self.function=StringFunction(input)
        self.input = input

    def evaluate(self,value):
       return self.function(value)

    def evaluate2(self,value):
        x = value
        return eval(self.input)