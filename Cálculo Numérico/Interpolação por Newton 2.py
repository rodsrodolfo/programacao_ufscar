from matplotlib import pyplot as plt

while 1:

    filename = '{0}.txt'.format(input('#######################################################\nNome do arquivo txt a ser criado para input dos pontos: '))
    try:
        file = open(filename,'r')
        file.close()
        run = 1
        while run:
            pergunta = input('Já existe um arquivo chamado {0}. Deseja usá-lo (0) ou sobrescrevê-lo (1)? '.format(filename))
            if pergunta == '0':
                break
            if pergunta == '1':
                while run:
                    pergunta2 = input('Tem certeza que deseja sobrescrever o arquivo {0}? S ou N: '.format(filename))
                    if pergunta2 == 'N':
                        break
                    if pergunta2 == 'S':
                        run = 0
                        file = open(filename, 'w+')
                        file.close()
                        ok = input('Um aquivo chamado {0} foi criado.\nPor linha, digite o x e o y de um ponto separados por um espaço.\nSalve as alterações do arquivo e digite enter para a interpolação.\n'.format(filename))
                    else:
                        print('resposta inválida\n')
            else:
                print('resposta inválida\n')

    except:
        file = open(filename,'w+')
        file.close()
        ok = input('Um aquivo chamado {0} foi criado.\nPor linha, digite o x e o y de um ponto separados por um espaço.\nSalve as alterações do arquivo e digite enter para a interpolação.\n'.format(filename))

    data = open(filename , 'r')
    points = []
    n = 0
    
    for line in data.readlines():
        if line[0] != '#':
            point = [float(line.split()[0]),float(line.split()[1])]
            points.append(point)
            n += 1
        
    points = sorted(points, key = lambda index : index[0])
    
    lx = []
    ly = []


    for point in points:
        lx.append(point[0])
        ly.append(point[1])

    data.close()

    valido = 1
    if lx == [] or ly == []:
        print('arquivo inválido')
        valido = 0

    #######################################
    if valido:
        TDD = []
        TDD.append(ly)

        for k in range(1,n):
            ordemk = []
            for i in range(n-k):
                f = TDD[k-1][i+1] - TDD[k-1][i]
                f /= lx[i+k] - lx[i]
                ordemk.append(f)
            TDD.append(ordemk)

        ld = []
        for ordem in TDD:
            ld.append(ordem[0])

        #######################################

        if ld[0] > 0:
            p = '\n+ %.4f\n' % ld[0]
        if ld[0] < 0:
            p = '\n- %.4f\n' % ld[0]
        if ld[0] == 0:
            p = '\n'
        m = ''
        for k in range (n-1):
            if lx[k] > 0:
                m += '(x - %.4f)' % abs(lx[k])
            if lx[k] < 0:
                m += '(x + %.4f)' % abs(lx[k])
            if lx[k] == 0:
                m += '(x)'
            if ld[k+1] > 0:
                p += '+ %.4f' %abs(ld[k+1]) + m +'\n'
            if ld[k+1] < 0:
                p += '- %.4f' %abs(ld[k+1]) + m +'\n'

        def pn(x,lx,ld):
            p = ld[0]
            m = 1
            for k in range(len(lx)-1):
                m *= x - lx[k]
                p += m*ld[k+1]
            return(p)

        lx2 = []
        ly2 = []

        x = lx[0]

        while x < lx[-1]:
            lx2.append(x)
            ly2.append(pn(x,lx,ld))
            x += 0.01

        #########################################

        plt.plot(lx, ly, 'bo', lx2, ly2, 'r--')
        print('p{0}(x) = {1}'.format(n-1,p))
        plt.show()

        run = 1
        while run:
            add = input('Deseja adicionar a expressão de p no arquivo {0}? S ou N: '.format(filename))
            if add == 'N':
                break
            if add == 'S':
                file = open(filename, 'a')
                num = []
                file.write(p)
                file.close()
                run = 0
            else:
                print ('resposta inválida')

        data.close()

