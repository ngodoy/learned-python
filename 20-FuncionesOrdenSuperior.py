def prueba(f):
    return f()

def porEnviar():
    return 2+2

print  "ejemplo 1 :",prueba(porEnviar)

def seleccion(operecion):
    def suma(n,m):
        return n+m
    
    def multiplacion(n,m):
        return n*m
    
    
    if operecion =="suma":
        return suma
    elif operecion =="multiplacion":
        return multiplacion
    
fguardar= seleccion("suma")

print  "ejemplo 2 :",fguardar(2,6)

print  "ejemplo 3 :",fguardar

fguardar= seleccion("multiplacion")

print  "ejemplo 4 :",fguardar
