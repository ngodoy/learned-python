def operador(n,m):
    if n==None or m==None:
        return 0
    
    return n+m

l1 =[1,2,3,4]
t1 =(9,8,7,6)

lt= map(operador,l1,t1)
print "sumar ",l1," con ",t1," = ",lt

t2 =(9,8,7)
lt= map(operador,l1,t2)
print "sumar ",l1," con ",t2," = ",lt

s1="hola"
s2="mundo"
lt= map(operador,s1,s2)
print "sumar ",s1," con ",s2," = ",lt

