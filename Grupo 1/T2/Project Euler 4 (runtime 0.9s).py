# Definimos todos os produtos possíveis para dois números de três dígitos
h = 0
for x in range (100,1000):
    for y in range (100,1000):
# Convertemos o inteiro x*y em uma string, pois assim pode ser invertido
# para a checagem palindrômica. Após isso, selecionamos o maior x*y que
# satisfaz tal condição
        b = str(x*y)
        c = b[::-1]
        if b==c and h < x*y:
            h=x*y
print(h)