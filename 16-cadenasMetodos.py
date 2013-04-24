s ="Hola Mundo Como Estas"
print s
print 'tengo ', len(s), ' caracteres'

print 'Contar las "o"', s.count('o')

print 'Contar las "o" de 0 a 10 ' , s.count('o',0,10)

print 'Contar las "o" de 0  ' , s.count('o',0)

print 'Contar las "O"', s.count('O')

print s,' en mayusculas \n', s.upper()

print s,' en minusculas \n', s.lower()

print s,'enreemplazar las "o" por las "x" \n', s.replace('o', 'x')

print s,'enreemplazar las "o" por las "x" solo 2 veces \n', s.replace('o', 'x',2)

print s,' los vamos dividir donde esta "" \n', s.split()
print s,' los vamos dividir donde esta a \n', s.split('a')
print s,' los vamos dividir donde esta s \n', s.split('s')

print s,' los vamos dividir solo 1 vez \n', s.split('o',1)
print s,' los vamos dividir solo 2 vez \n', s.split('o',1)

print s,' \n vamos ha buscar la primer ocurrencia "o" \n', s.find('o')
print s,' \n vamos ha buscar la ultima  ocurrencia "o" \n', s.rfind('o')

t = ("H","O","L","A")
s=";"
print (s.join(t))
print type(s.join(t))