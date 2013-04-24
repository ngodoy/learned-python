class Pruebas(object):
    def __init__(self):
        self.publico ="soy variable publico"
        self.__privado = "soy variable privado"
        
    def mentodoPublico(self):
        return "soy metodo publico"
    
    def metodoPrivado(self):
        return "soy metodo privado"
    
    def getPrivado(self):
         return self.__privado
        
    def setPrivado(self,valor):
          self.__privado =valor
     
obj=Pruebas()

#print obj.publico
#print obj.__privado
print obj.mentodoPublico()
print obj.getPrivado()

#print obj.__privado