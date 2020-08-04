def prime(x): # Definimos primeiramente uma função que informa se um número é primo ou não
    if(x<2):
        return(False)
    if(x>=2):
        for a in range(3,int(1+x**0.5),2):
            if(x%a==0):
                return(False)
    return(True)

# Testamos agora quais são os fatores primos do número informado, selecionando
# o maior 
x=600851475143
g,h=0,0
for a in reversed(range(2,int(1+x**0.5))):
    if prime(a):
        if (x%a==0):
            h=a
            if h>g:
                g,h=h,0

print(g)
