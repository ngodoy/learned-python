def mi_funciones(num1=0,num2=0):
    print num1 + num2

mi_funciones(1, 2)
mi_funciones()
mi_funciones(3)

def mi_funciones2(cad,v=2):
    print cad*v

mi_funciones2("Python")
mi_funciones2("Python",5)
#funciones con tuplas
def mi_funciones3(cad,v=2,*algomas):
    print cad*v
    for cadena in algomas:
        print cadena
    
#funciones con tuplas
mi_funciones3("Python",5,"hola","adios", "como estas")
#funciones con diccionario
def mi_funciones4(cad,v=2,**algomas):
    print cad*v
    print algomas['Cadena1']
    print algomas['Cadena2']
    print algomas['Cadena3']

        
mi_funciones4("Python",5,Cadena1="hola",Cadena2="adios",Cadena3="como estas")

#funciones con return
def mi_funciones5(num1=0,num2=0):
    return num1 + num2
print mi_funciones5(1, 2)

    