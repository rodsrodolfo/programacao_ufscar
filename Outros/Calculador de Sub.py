while True:
    notas=input('Escreva suas 3 notas até agora (P1, P2, P3) separadas por espaço \n')
    sub=18-sum(float(x) for x in notas.split())+min(float(x) for x in notas.split())
    print('Sua nota na SUB deve ser no mínimo %f' %sub)
