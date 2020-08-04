def prime(x):
    if(x<2):
        return(False)
    if(x>=2):
        if x%2==0 and x!=2:
            return (False)
        else:
            for a in range(3,int(1+x**0.5)):
                if(x%a==0):
                    return(False)
            return(True)
while(0==0):
    a=int(input('N:'))
    b=2
    for x in reversed(range(1,1+a,2)):
        if prime(x) and a%x==0 and x>b:
            b=x
            break
    print(b)