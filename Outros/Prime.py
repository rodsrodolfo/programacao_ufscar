def prime(x):
    if(x<2):
        return('NOT prime')
    if(x>=2):
        for a in range(2,int(1+x**0.5)):
            if(x%a==0):
                return('NOT prime')
    return('prime')
while(0==0):
    x=int(input('Your number:'))
    print(x,'is',prime(x))
    print('**********')