def docorador(f):
    def funcionDecorador(*args,**kwargs):
        print "funcion ejecutada", f.__name__
        f(*args,**kwargs)
        
    return funcionDecorador
@docorador
def  resta(n,m):
    print n-m

#decorador
#resta(5,3)
#docorador(resta)(5,3)
 
#docorada =docorador(resta)
#docorada(5,3)

#docorador
resta(5, 3)