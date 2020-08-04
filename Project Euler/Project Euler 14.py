def collatz(x):
    a=x
    b=0
    while(a!=1):
        if a%2==0:
            a=(a/2)
        else:
            a=(3*a)+1
        b=(b+1)
    return(b)
print('calculando')
s,t=0,0
for x in range (1,1000000):
    if collatz(x)>s:
        s,t=collatz(x),x
print(s,t)
