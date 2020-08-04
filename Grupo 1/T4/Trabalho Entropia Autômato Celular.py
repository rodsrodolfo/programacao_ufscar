import numpy as np
import matplotlib.pyplot as plt

while 1:
    #geração máxima
    MAX = 500
    
    #tamanho
    SIZE = 1000
    
    #regra
    REGRA = int(input('Qual regra? '))
    a = REGRA
    l = []
    while a > 0:
        l.append(a%2)
        a = a//2
    while len(l) != 8:
        l.append(0)
    
    #vetor de células
    alpha=input('Geração inicial aletatória ou individual? (colocar 1 para aleatório e 0 para individual) ')
    if alpha=='0':
        geracao = np.zeros(SIZE)
        geracao[SIZE//2]=1
    if alpha=='1':
        geracao = np.random.randint(2,size=SIZE)
    novageracao = np.zeros(SIZE)
    
    #matriz para armazenar as interações do sistema
    evolucao = np.zeros((MAX, SIZE))
    
    #contar a quantidade de zeros
    countzero = 0
    for b in range (SIZE):
        if geracao[b] ==  0:
            countzero += 1
    
    #acumulador
    holder = []
    
    #entropia da primeira linha
    H1 = -((countzero/1000) * np.log((countzero/1000)) + (1-(countzero/1000)) * np.log((1-(countzero/1000))))
    holder.append(H1)
    
    ## LAÇO PRINCIPAL ##
    for i in range(MAX): 
        evolucao[i,:] = geracao
        for j in range(SIZE):
            # Aplicar regra nas células j
            # Regra dada
            if geracao[j-1]==0 and  geracao[j]==0 and  geracao[(j+1)%SIZE]==0:
                novageracao[j]=l[0]
            elif geracao[j-1]==0 and geracao[j]==0 and geracao[(j+1)%SIZE]==1:
                novageracao[j]=l[1]
            elif geracao[j-1]==0 and geracao[j]==1 and geracao[(j+1)%SIZE]==0:
                novageracao[j]=l[2]
            elif geracao[j-1]==0 and geracao[j]==1 and geracao[(j+1)%SIZE]==1:
                novageracao[j]=l[3]
            elif geracao[j-1]==1 and geracao[j]==0 and geracao[(j+1)%SIZE]==0:
                novageracao[j]=l[4]
            elif geracao[j-1]==1 and geracao[j]==0 and geracao[(j+1)%SIZE]==1:
                novageracao[j]=l[5]
            elif geracao[j-1]==1 and geracao[j]==1 and geracao[(j+1)%SIZE]==0:
                novageracao[j]=l[6]
            else:
                novageracao[j]=l[7]    
        geracao = novageracao.copy()
        #Calcular a entropia da linha
        count = 0
        for a in range (SIZE):
            if geracao[a] ==  0:
                count += 1
        H = -((count/1000) * np.log((count/1000)) + (1-(count/1000)) * np.log((1-(count/1000))))
        holder.append(H)
            
    #Plotando os resultados
    plt.figure(1)
    plt.imshow(evolucao, cmap = "gray", interpolation='none')
    plt.show()
    
    plt.figure(2)
    plt.plot(holder)
    plt.ylabel('Entropia')
    plt.xlabel('Geração')
    plt.show()
    print('**********')
