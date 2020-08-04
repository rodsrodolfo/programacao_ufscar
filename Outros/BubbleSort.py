import random

lis=[]

for a in range (0,10):
    lis.append(random.choice(range(0,100)))
    
print(lis)

for c in range (0,10):
    for b in range (0,9):
        if lis[b]>lis[b+1]:
            lis[b],lis[b+1]=lis[b+1],lis[b]
        
print(lis,lis[0],lis[9])
