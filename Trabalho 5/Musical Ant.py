import numpy as np
import matplotlib.pyplot as plt
import winsound as ws


def nex(a,b,c): #define a nova posição da formiga baseado na sua posição atual e em sua orientação
    x=b
    y=c
    if a=='u':
        x-=1
    if a=='l':
        y-=1
    if a=='d':
        x+=1
    if a=='r':
        y+=1
    return x,y
    
def newori(a,b): #atualiza a orientação da formiga baseado em sua orientação atual e o estado da célula da qual a mesma se encontra
    if a=='u':
        if b=='l':
            return 'l'
        if b=='r':
            return 'r'
            
    if a=='l':
        if b=='l':
            return 'd'
        if b=='r':
            return 'u'
            
    if a=='d':
        if b=='l':
            return 'r'
        if b=='r':
            return 'l'
            
    if a=='r':
        if b=='l':
            return 'u'
        if b=='r':
            return 'd'

def freq(a,b): #setup das frequências
    if a==0:
        ws.Beep(int(((2**((28-49)/12))*440)*(2**b)),300)
    if a==1:
        ws.Beep(int(((2**((30-49)/12))*440)*(2**b)),300)
    if a==2:
        ws.Beep(int(((2**((32-49)/12))*440)*(2**b)),300)
    if a==3:
        ws.Beep(int(((2**((33-49)/12))*440)*(2**b)),300)
    if a==4:
        ws.Beep(int(((2**((35-49)/12))*440)*(2**b)),300)
    if a==5:
        ws.Beep(int(((2**((37-49)/12))*440)*(2**b)),300)
    if a==6:
        ws.Beep(int(((2**((39-49)/12))*440)*(2**b)),300)

            
#setup da primeira geração do autômato (aleatória)
al=3
lg=7

a=np.random.randint(2, size=(al,lg))

p=plt.imshow(a, cmap='gray', interpolation='none')


posx=lg//2
posy=al//2

ori='u'


while 1:
    
    
    a[posy,posx] = not a[posy,posx]  #troca o estado da célula

    if a[posy,posx]:
        ori=newori(ori,'l')
                                #comanda a formiga
    if not a[posy,posx]:
        ori=newori(ori,'r')
    
    posy, posx = nex(ori,posy,posx)[0]%al, nex(ori,posy,posx)[1]%lg  #deixa as coordenadas dentro dos limites (wrap)

    freq(posx,posy)  #toca a nota
        
    p.set_data(a)   #anima o autômato
    plt.pause(.00000000000000000001)
