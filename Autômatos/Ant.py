import numpy as np
import matplotlib.pyplot as plt


def nex(a,b,c):
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
    
def newori(a,b):
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
            

al=40
lg=40

#a=np.random.randint(2, size=(al,lg))
a=np.ones((al,lg),dtype=int)
a[0,0]=0

p=plt.imshow(a, cmap='gray', interpolation='none')


posx=lg//2
posy=al//2

ori='u'


while 1:
    
    a[posy,posx] = not a[posy,posx]

    if a[posy,posx]:
        ori=newori(ori,'l')

    if not a[posy,posx]:
        ori=newori(ori,'r')
    
    posy, posx = nex(ori,posy,posx)[0]%al, nex(ori,posy,posx)[1]%lg
        
    p.set_data(a)
    plt.pause(.00000000000000000001)
