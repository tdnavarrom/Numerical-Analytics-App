from scitools.StringFunction import StringFunction

class Function:
    def __init__(self,entrada):
        self.function=StringFunction(entrada)
    
    def evaluate(self,valor):
       return self.function(valor)









