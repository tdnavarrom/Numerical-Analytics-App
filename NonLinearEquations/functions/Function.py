from scitools.StringFunction import StringFunction

class Function:
    def __init__(self,input):
        self.function=StringFunction(input)

    def evaluate(self,value):
       return self.function(value)
