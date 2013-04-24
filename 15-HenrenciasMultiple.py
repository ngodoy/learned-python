class Humano:
    def __init__(self,edad=25):
        self.edad =edad
               
    def hablar(self,mensaje):       
        print mensaje       
        
class IngSistemas(Humano):
    def __init__(self):
        print "hola"
        Humano.__init__(self,10)
        
    def programar(self,lenguaje):
        print 'voy programa en',lenguaje
        
class LicDerecho(Humano):
    def __init__(self,escuala):
        print "hola soy LicDerecho y estudio en la escula de ",escuala
        Humano.__init__(self,10)
        
    def estudiarCaso(self,de):
        print 'debo estudiar el caso de ',de
            
class Estudios(IngSistemas,LicDerecho):
    pass 

class Estudios2(LicDerecho,IngSistemas):
    pass 

pp =Estudios()
pp.hablar("soy estoydiosos")
pp.programar("java")
pp.estudiarCaso("Juan")

pp1 =Estudios2("luz")
pp1.hablar("soy estoydiosos 2")
pp1.programar("java")
pp1.estudiarCaso("Juan")
