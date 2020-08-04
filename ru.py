import urllib.request

cardapio = []

response = urllib.request.urlopen('http://www2.ufscar.br/restaurantes-universitario')
for line_number, line in enumerate(response):
    if line_number in range(206,233) or line_number in range(248,274) and line != b'                  <div>\n' and line != b'            \n':
        a = (str(line, 'utf-8').split('<')[1].split('>')[1])
        if len(a) > 2:
            cardapio.append(a)
            
    elif line_number > 274:
        break

print('Almoço:')
for a in range(0,14,2):
    print(cardapio[a]+cardapio[a+1])
print('')
print('Jantar:')
for a in range(14,len(cardapio)-1,2):
    print(cardapio[a]+cardapio[a+1])
