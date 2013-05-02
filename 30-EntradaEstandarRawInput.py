try:

    valor = raw_input("Escriba un numero o una palabra para lansar el error ")
    print type(valor)
    valor = int(valor)
    print type(valor)
except :
    print "Error al intrudir datos"
else:
    print valor
