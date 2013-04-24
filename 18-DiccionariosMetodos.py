diccionario ={
"redes_socioales":["Twitter","Facebook","LidenIn"],
3:"Tres",
"hola":"Mundo"
}


print  "ver diccionario: \n",diccionario


print "existe hola :",diccionario.has_key("hola")

print "ver en forma de lista :\n",diccionario.items()

print "ver lista de key :\n",diccionario.keys()

print "ver lista de los valores :\n",diccionario.values()

diccionario2 = diccionario.copy()
print  "copiar ha  diccionario2: \n",diccionario2

diccionario["hola2"]="adios"
print  "agregar 1 elemento  al   diccionario: \n",diccionario2


print "sacar la key 3 : ",diccionario.pop(3)

print "sacar la key 3  otra vez : ",diccionario.pop(3,"no existe 3")

print "borrar key  hola"
del diccionario["hola"]

print  "ver diccionario: \n",diccionario

print  "vaciar el diccionario\n"
diccionario.clear()

print  "ver diccionario: \n",diccionario


