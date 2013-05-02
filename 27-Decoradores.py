
class Decorador(object):
    def __init__(self,f):
        self.f=f
    def __call__(self,*args,**kwargs):
        print "funcion ejecutada", self.f.__name__
        self.f(*args,**kwargs)

        
@Decorador
def  resta(n,m):
    print n-m

#decorador
#resta(5,3)
#docorador(resta)(5,3)
 
#docorada =docorador(resta)
#docorada(5,3)

#docorador
resta(5, 3)