# exp(X**2), 0,1  M4 76e
# sin(4x+exp(3x)) 0,pi/4



from matplotlib import pyplot as plt
import numpy as np

def F(F, x):
    return(eval(F.replace('X',str(x))))
    
def Par(x):
    x = abs(x)
    if x/2 == int(x/2):
        return(1)
    else:
        return(0)
        
def SR(l,h):
    ly = l
    sr = 0
    sr = sr + ly[0] + ly[-1] + 4*ly[-2]
    ly = ly[1:-2]
    while ly != []:
        sr += 4*ly[0]
        sr += 2*ly[1]
        ly = ly[2:]
    sr *= h/3
    return(sr)

while 1:
    M4_ = 0
    print('_ - _ - _ - _ - _')
    
    funcao_ = int(input('\nInput função (1) ou tabela (0)? \n'))
    
    if not funcao_:
        arquivo = input('\nNome do arquivo txt contendo a tabela: \n') + '.txt'
        data = open(arquivo , 'r')
        lx = []
        ly = []
    
        for line in data.readlines():
            lx.append(float(line.split()[0]))
            ly.append(float(line.split()[1]))
            
        h = lx[1] - lx[0]
        
        data.close()
    
    
    if funcao_:
        f = input('\nFunção em notação np e X como variável: \n')
        x0 = eval(input('\nx0: \n'))
        xn = eval(input('\nxn: \n'))
            
        M4_ = int(input('\nM4 é conhecido? (0) ou (1) \n'))       
        if M4_:
            M4 = eval(input('\nM4: \n'))
            
            E_ = int(input('\nFornecer n (0) ou E (1)? \n'))            
            if E_:
                E = eval(input('\nE: \n'))
                
                n = 1 + int(((((xn - x0)**5)*M4)/(180*E))**(1/4))
                
                if not Par(n):
                    n += 1
                    
            if not E_:
                n = int(input('\nn par: \n'))
                
                E = float((((xn - x0)**5)*M4)/(180*(n**4)))
                
        if not M4_:
            n = int(input('\nn par: \n'))
                

        h = (xn - x0)/n
        lx = []
        ly = []
            
        for i in range(n+1):
            x = x0 + i*(xn - x0)/n
            lx.append(x)
            ly.append(F(f,x))
            
            
    S = SR(ly, h)
    print('\nA integral da sua função calculada por 1/3 de Simpson repetido é: \n{0}\n'.format(S))
    if M4_:
        print('\nCom erro menor ou igual a: \n{0}\n'.format(E))
        
    plt.plot(lx, ly, 'bo')
    plt.show()  