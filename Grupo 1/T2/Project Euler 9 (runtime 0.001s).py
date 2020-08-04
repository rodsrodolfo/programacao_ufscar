# Pelo Teorema de Pitágoras, c = (a**2 + b**2)**.5, e por otimização tal
# variável foi omitida

for a in range (2, 500):
# Ver comentário final acerca do intervalo do range
# Da condição inicial do problema, temos a equação
# a + b + (a**2 + b**2)**.5 = 1000
# Isolando-se b, obtemos a fórmula
    b = 1000*(500-a)/(1000-a)
# Checamos se b é inteiro e, enfim, se satisfaz a + b + c = 1000
    if b == int(b):
        if a+b+((a**2 + b**2)**.5)==1000:
            print('Trina pitagórica que resolve o problema: '+str((a,int(b),int((a**2+b**2)**.5))))
            print('Multiplicação de seus elementos: '+str(int(a*b*((a**2 + b**2)**.5))))
            break
        
# O break foi aqui inserido para evitar que a resposta (b,a) fosse printada
# também, já que se (a,b) é resposta da equação, (b,a) também deve ser, pois
# a equação permite comutações (para nós a ordem das variáveis não importa,
# pois a*b*c = b*a*c.)
            
#PS: A variável 'a' não pode ser maior que 499 (500 - 1) pois, substituindo
# a = 500 na fórmula obtida de b, obtemos b = 0, um número não natural positivo
