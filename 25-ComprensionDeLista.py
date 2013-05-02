l=[-2,-1,0,1,2,3]
l2=[num for num in l if num>0]

print l
print l2
l=[1,2,3,4]
s="hola mundo"
l3=[c * num for c in s 
                for num in l
                    if num >0]

print l3