def prime(x): # Definimos primeiramente uma função que informa se um número é primo ou não
    if(x<2):
        return(False)
    if(x>=2):
        for a in range(2,int(1+x**0.5)):
            if(x%a==0):
                return(False)
    return(True)

a=0
b=1
while a<10000:
    if prime(b):
        a+=1
    b+=2
    
print(b-2)