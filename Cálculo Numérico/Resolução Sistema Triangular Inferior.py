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
    resposta = []
    for k in range(n):                                   # para k de 1 a n
        xk = A[k][-1]                                    # xk = Bk
        for i in range(k):                               # para i de 1 a k-1
            xk -= A[k][i] * resposta[i]                  # xk -= Aki * Bi
        xk /= A[k][k]                                    # xk /= Akk
        resposta.append(xk)
    for a in range(len(A)):
        print('x{0} = {1}'.format(a+1, resposta[a]))