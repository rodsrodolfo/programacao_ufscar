while True:
        a=[]
        b=[]
        c=[]
        d=[a,b,c]
        e=[]
        f=0
        x=input('Nível: ')
        if x.isdigit():
            if int(x)>0:
                x=int(x)
                for q in reversed(range (0,x)):
                    d[0].append(q+1)
                    e.append(q+1)
                    d[1].append(0)
                    d[2].append(0)
                for q in reversed(range(0,x)):
                    print(a[q], b[q], c[q])
                while c!=e:
                    y=input('Jogada (0 para desistir): ')
                    if y=='0':
                        break
                    elif y.isdigit() and len(y)==2:
                        if y[0]!=y[1] and (int(y[0]) in [1,2,3]) and (int(y[1]) in [1,2,3]):
                            if d[int(y[0])-1].count(0)!=x:
                                if d[int(y[1])-1].count(0)==x or d[int(y[0])-1][(x-1)-(d[int(y[0])-1][1:(x)].count(0))]<d[int(y[1])-1][(x-1)-(d[int(y[1])-1].count(0))]:
                                    d[int(y[1])-1][(x)-(d[int(y[1])-1].count(0))],d[int(y[0])-1][(x-1)-(d[int(y[0])-1][1:(x)].count(0))]=d[int(y[0])-1][(x-1)-(d[int(y[0])-1][1:(x)].count(0))],0
                                    f=f+1
                                else:
                                   print('Jogada inválida (não se pode colocar um número maior em cima de um menor)') 
                            else:
                                print('Jogada inválida (sem números na coluna '+str(y[0])+')')
                        else:
                            print('\'Jogada\' deve ser um número de 2 algarismos distintos, sendo eles entre 1 e 3, ou \'desistir\'')
                    else:
                        print('\'Jogada\' deve ser um número de 2 algarismos distintos, sendo eles entre 1 e 3, ou \'desistir\'')
                    for q in reversed(range(0,x)):
                            print(a[q], b[q], c[q])
                if c==e:
                    print('***\n***Parabéns, você resolveu em '+str(f)+' movimentos, sendo que o mínimo era '+str((2**x)-1)+' movimentos***\n***\nEscolha o nível novamente')
                else:
                    print('Escolha o nível novamente')
            else:
                print('\'Nível\' deve ser um número positivo')
        else:
            print('\'Nível\' deve ser um número positivo')
