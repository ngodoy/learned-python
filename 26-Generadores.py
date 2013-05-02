from sqlite3.test import factory
l=[1,2,3,4]
s="hola mundo"
l3=(c * num for c in s 
                for num in l
                    if num >0)

print l3.next()
for letra in l3:
    print letra 
    
def factorial(n):
    i =1
    while n >1 :
         i =n*i
         yield i
         n-=1
    
for e in factorial(5):
    print (e)