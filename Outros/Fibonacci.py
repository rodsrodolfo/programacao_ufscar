def fibonacci(x):
    if(x<=0):
        return('invalid input')
    else:
        a,b=1,1
        y=1
        while(y<x):
            a,b=b,(a+b)
            y=y+1
        return(a,b/a)
while(0==0):
    x=int(input('x='))
    print(fibonacci(x))
    print('**********')