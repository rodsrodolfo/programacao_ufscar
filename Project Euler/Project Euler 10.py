def prime(x):
    if(x<2):
        return(False)
    if(x>=2):
        for a in range(2,int(1+x**0.5)):
            if(x%a==0):
                return(False)
    return(True)
print('calculando')
a=0
for x in range (0,2000001):
    if prime(x):
        a=a+x
print(a)