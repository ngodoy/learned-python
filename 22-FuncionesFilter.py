def filtro(elem):
    return (elem>0)  
    
l =[1,-3,2,-7,-8,-9,10]
print "la lista ",l

lr = filter(filtro, l)

print lr 

def filtro1(elem):
    return (elem=='a')  

s ="hola"
print "la lista ",s

lr = filter(filtro1, s)
print lr 
print type(lr)
