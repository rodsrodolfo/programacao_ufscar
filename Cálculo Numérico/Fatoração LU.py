while 1:
    print('\nExemplo de input:\n\nLine: 1 0 0 ;\n\nLine: 1 1 0 ;\n\nLine: 1 1 1\n\nMatriz A:\n')
    acabou = 0
    A = []
    L = []
    while acabou == 0:
        novalinha = input('Line: ').split()
        A.append([]) 
        L.append([])
        if novalinha[-1] == ';':
            for a in novalinha[0:-1]:
                A[-1].append(float(a))
                L[-1].append(0)
        else:
            acabou = 1
            for a in novalinha:
                A[-1].append(float(a))
                L[-1].append(0)
    print('\nA\n') 
    for linha in A:
        print(linha)
    
    n = len(A)
    perm = []
    for k in range (n-1):
        
        listapivo = []
        for pivo in A[k:]:
            listapivo.append(abs(pivo[k]))
        A[k], A[k+listapivo.index(max(listapivo))] = A[k+listapivo.index(max(listapivo))], A[k]
        perm.append(k+listapivo.index(max(listapivo)))
    
        for i in range(k+1,n):
            m = A[i][k] / A[k][k]
            A[i][k] = m
            for j in range(k+1,n):
                A[i][j] = A[i][j] - A[k][j] * m
                
    U = A.copy()
    for j in range(n):
        L[j][j] = 1
        for i in range(j):
            U[j][i], L[j][i] = 0, U[j][i]
            
    print('\nU\n')
    for line in U:
        print(line)
        
    print('\nL\n')
    for line in L:
        print(line)
        
    novoB = 1
    
    while novoB:
        LB = []
        for line in L:
            LB.append(line.copy())
        b = input('\nMatriz B: \n\n').split()
        for bk in range(len(b)):
            LB[bk].append(float(b[bk]))
            
        for p in range(len(perm)):
            LB[p][-1], LB[perm[p]][-1] = LB[perm[p]][-1], LB[p][-1]
            
        UY = []
        for line in U:
            UY.append(line.copy())
        for k in range(n):                                   # para k de 1 a n
            yk = LB[k][-1]                                    # xk = Bk
            for i in range(k):                               # para i de 1 a k-1
                yk -= LB[k][i] * UY[i][-1]                         # xk -= Aki * Bi
            yk /= LB[k][k]                                    # xk /= Akk
            UY[k].append(yk)
            
        x = []
        for k in range(n):
            x.append(0)
        for k in reversed(range(n)):                         # para k de n a 1
            xk = UY[k][-1]                                    # xk = Bk
            for i in range(k,n):                             # para i de k a n
                xk -= UY[k][i] * x[i]                  # xk -= Aki * Bi
            xk /= UY[k][k]                                    # xk /= Akk
            x[k] = xk
        
        print('\n')
        for a in range(len(A)):
            print('x{0} = {1}'.format(a+1, x[a]))
        
        if int(input('\nOutro B? 0 ou 1: \n')) == 0:
            novoB = 0