def fibonacci(x):
    if(x<=0):
        return('invalid input')
    else:
        a,b=1,1
        y=1
        while(y<x):
            a,b=b,(a+b)
            y=y+1
        return(a)
def pandigital(x):
    listida=sorted(x[0:9])
    listvolta=sorted(x[len(x)-9:len(x)])
    listideal=['1','2','3','4','5','6','7','8','9']
    if len(x)<18:
        return (False)
    else:
        if listida==listideal and listvolta==listideal:
            return(True)
        else:
            return(False)
c=1
a,b=1,1
while not pandigital(str(a)):
    a,b=b,(a+b)
    c=c+1
print (c)