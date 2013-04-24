l = [1, "dos",3,"cuatros"]
a=1
b=5
c=3
print "esta ",a," en ",l, " ", a in l
print "esta ",b," en ",l, " ", b in l

print "donde esta  ",b," en ",l

if b in l:
    print l.index(b)
else:
    print "no esta ",b," en  la lista"

print l 
print "agregar nuevo"
l.append("nuevo")
print "agregar 5"

l.append(5)
print l 


print "contar cuantos ",c, "hay : " ,l.count(c)

print "agregar en lugar 3 la palabra nuevo tres"
l.insert(2, "nuevo tres")
print l
l2="candena"
print "extender lista "
l.extend(l2)
print l

print l.pop()
print l.pop()
print l.pop()
print l.pop()
print l.pop()
print l.pop()
print l.pop()
print l.pop(2)



print l 

l.remove(5)

print l
l.reverse()
print l
