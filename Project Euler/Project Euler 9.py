print('calculando')
a=0
b=0
c=(a**2+b**2)**.5
abc=a*b*c
for d in range(1,1000):
    for e in range(1,1000):
        if (d+e+(d**2+e**2)**.5==1000):
            a,b=d,e
print('a=%i'%a)
print('b=%i'%b)
print('c=%i'%c)
print('a.b.c=%i'%abc)
