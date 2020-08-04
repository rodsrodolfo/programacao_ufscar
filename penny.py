import numpy as np

pp1=0
pp2=0

while 1:
    
    p=[0,0]
    p1=input('player 1: ')
    p2=input('player 2: ')
    while p[0]<3 and p[1]<3:
        jogo=''
        while jogo[len(jogo)-3:]!=p1 and jogo[len(jogo)-3:]!=p2 or len(jogo)<3:
            jogo+=np.random.choice(('h','t'))
        if jogo[len(jogo)-3:]==p1:
            p[0]+=1
        if jogo[len(jogo)-3:]==p2:
            p[1]+=1
    if p[0]==3:
        pp1+=1
        print()
        print('player 1 won')
        print()
    if p[1]==3:
        pp2+=1
        print()
        print('player 2 won')
        print()
