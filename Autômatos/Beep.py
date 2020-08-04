import winsound as ws
import numpy as np

def binn(x):   #converte um número decimal em um binário de 8 dígitos
    z=bin(x)[2:len(bin(x))]
    while len(z)<8:
        z='0'+z
    return (z)
    
def rule(x,y):   #aplica a regra na trina de células
    if x=='111':
        return (y[0])
    if x=='110':
        return (y[1])
    if x=='101':
        return (y[2])
    if x=='100':
        return (y[3])
    if x=='011':
        return (y[4])
    if x=='010':
        return (y[5])
    if x=='001':
        return (y[6])
    if x=='000':
        return (y[7])

while 1:

    #configurações de input
    cel,gen,reg,ran=input('células por geração, número de gerações, regra e random input ou não (1 ou 0), separados por espaço:\n').split()
    cel,gen,reg,ran=int(cel),int(gen),int(reg),int(ran)
    jogo=np.zeros(shape=(gen,cel),dtype='int')
    if ran:
        jogo[0]=np.random.randint(2,size=cel)
    else:
        jogo[0]=np.zeros(cel,dtype=int)
        jogo[0,cel//2]=1

    #aplica a rega à geração atual
    for a in range(1,gen):
        for b in range(cel):
            jogo[a,b]=rule('{}{}{}'.format(jogo[a-1,b-1],jogo[a-1,b],jogo[a-1,(b+1)%cel]),binn(reg))

    #analisa as trina celulares e atribui frequências sonoras à elas
    for a in range(cel):
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='000':
            fr=523
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='001':
            fr=587
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='010':
            fr=659
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='011':
            fr=698
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='100':
            fr=783
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='101':
            fr=880
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='110':
            fr=987
        if '{}{}{}'.format(jogo[gen-1,a-1],jogo[gen-1,a],jogo[gen-1,(a+1)%cel])=='111':
            fr=1046
        ws.Beep(fr, 300)

