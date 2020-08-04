while(0==0):
    notas=input('Digite suas 4 notas (P1, P2, P3, SUB) separadas por espaço \n')
    media=(sum(float(x) for x in notas.split())-min(float(x) for x in notas.split()))/3
    if media>=6:
        print('Aprovado com média %f' %media)
    else:
        print('Reprovado com média %f' %media)
