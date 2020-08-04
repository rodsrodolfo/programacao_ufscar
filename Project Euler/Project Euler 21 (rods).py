def d(x):    #define-se a função como o enunciado do problema
    a=0
    for g in range(1,int(x/2)+1):
        if x%g==0:
            a=a+g
    return(a)

print('calculando')

w=0
for y in range(1,10001):
    if d(d(y))==y and d(y)!=y:
        w=w+y                   #para cada dupla amigável encontrada, soma-se apenas um dos números porque um número é amigável do outro. Assim, o
                                #que não foi adicionado na primeira vez será adicionado quando novamente essa dupla for achada, dessa vez por causa do
        print(y)                #segundo número
print('********')
print('soma:',w)
