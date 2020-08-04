coseq={}  #dicionário que guardará em suas chaves todos os números de 1 a 1000000 e em seus valores
           #armazena uma lista, cujo conteúdo é a sequência de Collatz do número da chave correspondente

           #exemplo: colseq[5]=[5,16,8,4,2,1]


for a in range(1,1000001):  #calcula todas as sequências correspondentes aos números de 1 a 1000000
    c=a
    b=[a]
    while a!=1 and b[len(b)-1]!=1: #calcula a sequência até chegar no 1o 1 da mesma e para, senão o cálculo entraria em um loop
        if a in coseq:
            b+=coseq[a][1:]  #parte inteligente do código: se o programa no meio do cálculo da sequência se depara com um número cuja sequência já foi calculada,
        else:                           #o cálculo da sequência atual congela e a sequência já calculada é adicionada como continuação. Isso otimiza o código
            if a%2==0:
                a=int(a/2)
            else:
                a=int(3*a)+1
            b.append(a)
    coseq[c]=b.copy()        #ao final adiciona-se ao dicionário o número e sua respectiva sequência

b=0

for a in coseq:              #ao final do cálculo de todas as sequências, compara-se todas e escolhe-se a chave cujo valor é de maior tamanho (intuito do problema)
    if len(coseq[a])>b:
        c=a
        b=len(coseq[a])

print (c)
