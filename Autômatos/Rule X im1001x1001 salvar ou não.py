from PIL import Image

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

img = Image.new('RGB', (1001,1001))

while True:
    jogo='1'
    jogofinal=[]
    h=input('Regra ')
    if h.isdigit():
        h=int(h)
        hh=rulebin(h)
        if h<=255 and 0<=h:
            while len(jogo)<1001:
                jogo='0'+jogo+'0'
            for l in range (0,1001):
                for b in range (int((len(jogo)-1001)/2),int(((len(jogo)-1001)/2)+1001)):
                    if jogo[b]=='0':
                        jogofinal.append((255,255,255))
                    else:
                        jogofinal.append((84,84,84))
                nex=''
                for a in range(0,(len(jogo)-2)):
                        nex=nex+(rule(jogo[a:3+a],hh))
                nex=(nex[0])*2+nex+(nex[len(nex)-1])*2
                jogo=nex
            img.putdata(jogofinal)
            img.show()
            c=False
            while not c:
                salvar=input("salvar a imagem? (s ou n): ")
                if salvar=='s':
                    img.save("regra"+str(h)+".png", "PNG")
                    c=True
                elif salvar=='n':
                    c=True
                else:
                    print('input inválido')
        else:
            print('input inválido')
    else:
        print('input inválido')
