class Humano:
    def __init__(self,edad=25):
        self.edad =edad
               
    def hablar(self,mensaje):
        print self.edad
        print mensaje
        
class IngSistemas(Humano):
    def __init__(self):
        Humano.__init__(self,10)
        
    def programar(self,lenguaje):
        print 'voy programa en',lenguaje
        
class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print 'debo estudiar el caso de ',de
            

pedro = IngSistemas()
raul = LicDerecho()

pedro.hablar("hola")
pedro.programar("Python")

raul.hablar("hola pedro")
raul.estudiarCaso("pedro")
