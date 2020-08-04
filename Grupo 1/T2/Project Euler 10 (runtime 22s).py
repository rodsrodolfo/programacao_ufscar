# Definimos primeiramente uma função que informa se um número é primo ou não
def prime(x):
    if(x<2):
        return(False)
    if(x>=2):
        for a in range(3,int(1+x**0.5),2):
            if(x%a==0):
                return(False)
    return(True)

# Calculamos, assim, a soma de todos os primos menores que 2.000.000
c = 0
for b in range(3, 2 * 10**6 + 1, 2): #observações a respeito do ',2' ao final
    if prime(b):
        c=c+b
        
print(c+2)

# O 2 é adicionado ao final para que o range do b seja menor, pulando de dois
# em dois (uma vez que sabemos que pares, com excessão do 2, não são primos, não
#tem porque testá-los)
