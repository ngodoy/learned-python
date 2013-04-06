l = [2, "tres", True, [1,"dos",3]]
print "lista l =",l
l2 = l[1];
print "el segundo de la lista = ",l2
l3 = l[3][1]

print "lista de lista l[3][1] =",l3
l3 = l[3][1]=2
print "reaccion lista de lista l[3][1] =",l3
l4 = l[0:3]
print "un segmenteo de la lista l[0:3] =",l4
l5 = l[0:3:2]
print "un segmenteo de lista con intervalo l[0:3] =",l5
l6 = l[0::2]
print "un segmenteo de la lista l[0::2] =",l6
l7 = l[1::2]
print "un segmenteo de la lista l[1::2] =",l7
l[0:2]=[4,3]
print "asignacio de una lista l[0:2]=[4,3] =",l
l[0:2]=[4]
print "asignacio de una lista l[0:2]=[4,3] =",l
l9=l[-1]
print "indices invervios l9=l[-1] =",l9


