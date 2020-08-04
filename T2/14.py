coseq={}

#5:[5,16,8,4,2,1]


for a in range(1,1000001):
    c=a
    b=[a]
    while a!=1 and b[len(b)-1]!=1:
        if a in coseq:
            b+=coseq[a][1:]
        else:
            if a%2==0:
                a=int(a/2)
            else:
                a=int(3*a)+1
            b.append(a)
    coseq[c]=b.copy()

b=0
for a in coseq:
    if len(coseq[a])>b:
        c=a
        b=len(coseq[a])

print (c)
