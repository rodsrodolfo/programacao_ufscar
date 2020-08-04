import numpy as np
import matplotlib.pyplot as plt

MAX=800
SIZE=800

geracao=np.zeros(SIZE)
novageracao=np.zeros(SIZE)

evolucao=np.zeros((MAX,SIZE))

geracao[SIZE//2]=1.

for i in range(MAX):   
    evolucao[i,:]=geracao

    for j in range(SIZE):
        #aplicar regra 30
        if geracao[j-1]==0 and geracao[j]==0 and geracao[(j+1)%SIZE]==0:
            novageracao[j]=0
        if geracao[j-1]==0 and geracao[j]==0 and geracao[(j+1)%SIZE]==1:
            novageracao[j]=1
        if geracao[j-1]==0 and geracao[j]==1 and geracao[(j+1)%SIZE]==0:
            novageracao[j]=1
        if geracao[j-1]==0 and geracao[j]==1 and geracao[(j+1)%SIZE]==1:
            novageracao[j]=1
        if geracao[j-1]==1 and geracao[j]==0 and geracao[(j+1)%SIZE]==0:
            novageracao[j]=1
        if geracao[j-1]==1 and geracao[j]==0 and geracao[(j+1)%SIZE]==1:
            novageracao[j]=0
        if geracao[j-1]==1 and geracao[j]==1 and geracao[(j+1)%SIZE]==0:
            novageracao[j]=0
        if geracao[j-1]==1 and geracao[j]==1 and geracao[(j+1)%SIZE]==1:
            novageracao[j]=0
            
    geracao=novageracao.copy()

plt.figure(1)    
plt.imshow(evolucao, cmap='gray', interpolation='none')
plt.show()
