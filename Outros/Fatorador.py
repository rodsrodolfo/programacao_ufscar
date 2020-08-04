def prime(x):
    if(x<2):
        return(False)
    if(x>=2):
        for a in range(2,int(1+x**0.5)):
            if(x%a==0):
                return(False)
    return(True)
while True:
    x=int(input('n: '))
    h=x
    p=[]
    for a in range (2,int(h/2)+1):
        if prime(a):
            p.append(a)
    i=[]
    for c in range(0,len(p)):
        i.append(0)
        while h%(p[c])==0:
            h=h/(p[c])
            i[c]+=1
    while 0 in i:
        p.remove(p[i.index(0)])
        i.remove(0)
    if p==[]:
        print('{}^1'.format(x))
    else:
        r=''
        for d in range(0,len(p)):
            r=r+'{}^{} x '.format(p[d],i[d])
        print(r[0:len(r)-2])