from PIL import Image
import random
import winsound


def rulebin(x):
    z=bin(x)[2:len(bin(x))]
    while len(z)<8:
        z='0'+z
    return (z)
def rule(x,y):
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

img = Image.new( 'RGB', (501,500))
pixels = img.load()

while True:
    Dur=150
    jogo=''
    jogofinal=[]
    jogofinal2=[]
    while len(jogo)<501:
        jogo+=random.choice(['1','0'])
    h=input('Regra ')
    if h.isdigit():
        h=int(h)
        hh=rulebin(h)
        if h<=255 and 0<=h:
            for l in range (0,500):
                for b in range (int((len(jogo)-501)/2),int(((len(jogo)-501)/2)+501)):
                    if jogo[b]=='0':
                        jogofinal.append((255,255,255))
                        jogofinal2.append(0)
                    else:
                        jogofinal.append((84,84,84))
                        jogofinal2.append(1)
                nex=''
                for a in range(0,(len(jogo)-2)):
                        nex=nex+(rule(jogo[a:3+a],hh))
                nex=(nex[0])*2+nex+(nex[len(nex)-1])*2
                jogo=nex
            img.putdata(jogofinal)
            img.show('501x500_regra'+str(h))
        else:
            print('input inválido')
    else:
        print('input inválido')
    for a in range(len(jogofinal2)):
        if jogofinal2[a-1]==0 and jogofinal2[a]==0 and jogofinal2[(a+1)%len(jogofinal2)]==0:
            winsound.Beep(261,Dur)
        if jogofinal2[a-1]==0 and jogofinal2[a]==0 and jogofinal2[(a+1)%len(jogofinal2)]==1:
            winsound.Beep(293,Dur)
        if jogofinal2[a-1]==0 and jogofinal2[a]==1 and jogofinal2[(a+1)%len(jogofinal2)]==0:
            winsound.Beep(329,Dur)
        if jogofinal2[a-1]==0 and jogofinal2[a]==1 and jogofinal2[(a+1)%len(jogofinal2)]==1:
            winsound.Beep(349,Dur)
        if jogofinal2[a-1]==1 and jogofinal2[a]==0 and jogofinal2[(a+1)%len(jogofinal2)]==0:
            winsound.Beep(392,Dur)
        if jogofinal2[a-1]==1 and jogofinal2[a]==0 and jogofinal2[(a+1)%len(jogofinal2)]==1:
            winsound.Beep(440,Dur)
        if jogofinal2[a-1]==1 and jogofinal2[a]==1 and jogofinal2[(a+1)%len(jogofinal2)]==0:
            winsound.Beep(493,Dur)
        if jogofinal2[a-1]==1 and jogofinal2[a]==1 and jogofinal2[(a+1)%len(jogofinal2)]==1:
            winsound.Beep(523,Dur)
