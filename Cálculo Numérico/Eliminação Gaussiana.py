while 1:
    print('\nExemplo de input:\n\nLine: 1 0 0 1 ;\n\nLine: 1 1 0 1 ;\n\nLine: 1 1 1 1\n\nSeu input:\n')
    acabou = 0
    A = []
    while acabou == 0:
        novalinha = input('Line: ').split()
        A.append([])
        if novalinha[-1] == ';':
            for a in novalinha[:-1]:
                A[-1].append(float(a))
        else:
            acabou = 1
            for a in novalinha:
                A[-1].append(float(a))
    print('\n') 
    for linha in A:
        print(linha)
    print('\n')
    
    n = len(A)
    
    for k in range (n-1):
        #pivoteamento
        listapivo = []
        for pivo in A[k:]:
            listapivo.append(abs(pivo[k]))
        A[k], A[k+listapivo.index(max(listapivo))] = A[k+listapivo.index(max(listapivo))], A[k]
        
        for i in range(k+1,n):
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1,n+1):
                A[i][j] = A[i][j] - A[k][j] * m
    print('\n') 
    for linha in A:
        print(linha)
    print('\n')
       
    resposta = []
    for a in range(n):
        resposta.append(0)
    for k in reversed(range(n)):                         # para k de n a 1
        xk = A[k][-1]                                    # xk = Bk
        for i in range(k,n):                             # para i de k a n
            xk -= A[k][i] * resposta[i]                  # xk -= Aki * Bi
        xk /= A[k][k]                                    # xk /= Akk
        resposta[k] = xk
    for a in range(len(A)):
        print('x{0} = {1}'.format(a+1, resposta[a]))