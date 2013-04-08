class Humano:
    def __init__(self,edad=25):
        self.edad =edad
        print "Soy nuevo objecto"
        
    def hablar(self,mensaje):
        print self.edad
        print mensaje

pedro = Humano(26)
raul = Humano()

print 'Soy Pedro y tengo ', pedro.edad
print 'Soy Raul y tengo ', raul.edad

pedro.hablar("hola")
raul.hablar("hola pedro")
