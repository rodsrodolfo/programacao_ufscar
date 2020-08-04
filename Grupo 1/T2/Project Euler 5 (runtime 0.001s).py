def prime(x): # Definimos primeiramente uma função que informa se um número é primo ou não
    if(x<2):
        return(False)
    if(x>=2):
        for a in range(2,int(1+x**0.5)):
            if(x%a==0):
                return(False)
    return(True)

while 1:
    
    X=int(input('n: '))#o problema em questão pede o mmc!(20) 
    
    f={}   #dicionário que vai armazenar a fatoração dos números de 1 a 20 a fatoração de 15, por exemplo,
           #será {2:0,3:1,5:1,7:0,11:0,13:0,17:0,19:0}, pois 15 é 2**0 * 3**1 * 5**1 * 7**0 * 11**0 * 13**0 * 17**0 * 19**0
    
    p=[]  #lista com os primos de 1 a 20 - possiveis divisores dos números de 1 a 20 para fatoração
    
    for a in range (X+1): #loop que testa os possiveis divisores primos dos números de 1 a 20 e os adiciona na lista p
        if prime(a):
            p.append(a)
    
    x=[]   #vai armazenar o maior expoente a qualcada primo é elevado. Para que o número desejado seja divisível por todos os números de 1 a 20,
           #ele deve ser a multiplicação dos primos que fatoram tais números elevados à maior potência entre as fatorações
    
    for a in range(1,X+1):  #esse loop fatora os números de 1 a 20 e armazena os dados no dicionário
        c=a
        f[a]={}
        for b in p:
            f[a][b]=0
            while c//b>=1 and a%b==0: #a fatoração está de fato aqui
                f[a][b]+=1
                c=c/b
    
    c=0
    for a in p:   #vai pegar o maior expoente a qual cada primo é elevado, para o cálculo da resposta do problema
        x.append(0)
        for b in range(1,X+1):
            if f[b][a]>x[c]:
                x[c]=f[b][a]
        c+=1

    n=1
    for a in range(len(p)):  #faz a conta da resposta com base na lista p de primos e x de expoentes
        n=n*(p[a]**x[a])
    
    
    print(n)
