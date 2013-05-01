def suma(a,b):
    return a+b
def multi(a,b):
    return a*b

def filtar(a):
    return (a=='o')

li =[1,-2,1,-4]
lo =[5,3,6,7]
s ="hola mundo"
print "sin lambda"
print map(suma,li,lo)
print filter(filtar,s)
print reduce(multi, lo)
print "con lambda"

print map(lambda a,b:a+b,li,lo)
print filter(lambda a: a=='o',s)
print reduce(lambda a,b: a*b, lo)

c1=lambda a,b:a+b
c2=lambda a: a=='o'
c3=lambda a,b: a*b

#print c1(1,2)
#print c2('o')
#print c3(1,2)


print "variables lambda"

print map(c1,li,lo)
print filter(c2,s)
print reduce(c3, lo)
