print "bienvenido"

try:
    print l
    #print 1/0
    #print n/0
    print "listo"

except (TypeError, NameError):
    print "Erro tipo de dato"
except ZeroDivisionError:
    print "No se puede divir entre cero"
except NameError:
    print "Variable no existe"
else:
    print "Sin errores"
finally:
    print "me ejecuto pase lo que pase"
    
print "Fin"


print "Uso de mis Errores"

class misErrores(Exception): 
    def __init__(self,valor):
        self.valor=valor
    def __str__(self, *args, **kwargs):
        return "No se puede hacer eso "

n=5         

if(True):
    raise misErrores(n)

    
print "Adios"

