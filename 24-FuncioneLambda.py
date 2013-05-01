s = ('h','o','l','a','-''m','u','n','d','o')

l = [1,2,3,4,5,6,7,8,9]
def concatenar(a,b):
    return  a+b

sr = reduce(concatenar, s)
print  sr


sr = reduce(concatenar, l)
print  sr

