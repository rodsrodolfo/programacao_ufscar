import random
import time

def BubbleSort(x):
    for i in range (len(x)-1,0,-1):
        for j in range (i):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
                
def SelectionSort(x):
    for i in range (len(x)): 
        menor = i # identifica o menor elemento do conjunto
        for k in range (i+1, len(x)):
            if x[k] < x[menor]:
                menor = k
        x[menor],x[i]=x[i],x[menor]
        
def InsertionSort(x):
    for i in range (1, len(x)):
        k = i
        while k > 0 and x[k] < x[k-1]:
            x[k],x[k-1]=x[k-1],x[k]
            k -= 1
            
def TesteDeVelocidade(n):
    l = []
    li = []
    lis = []
    for a in range(n):
        l.append(random.choice(range(max(1,n))))
        li.append(random.choice(range(max(1,n))))
        lis.append(random.choice(range(max(1,n))))     
    print(n, 'Entradas Randômicas')
    begin = time.time()
    BubbleSort(l)
    end = time.time()
    B = end - begin
    print('BubbleSort    %.6f segundos'%(B))
    begin = time.time()
    SelectionSort(li)
    end = time.time()
    S = end - begin
    print('SelectionSort %.6f segundos'%(S))
    begin = time.time()
    InsertionSort(lis)
    end = time.time()
    I = end - begin
    print('InsertionSort %.6f segundos'%(I))
    if B == min(B,I,S):
        print('O melhor algoritmo foi o BubbleSort.')
    elif S == min(B,I,S):
        print('O melhor algoritmo foi o SelectionSort.')
    else:
        print('O melhor algoritmo foi o InsertionSort.')
    if B == max(B,I,S):
        print('O pior algoritmo foi o BubbleSort.')
    elif S == max(B,I,S):
        print('O pior algoritmo foi o SelectionSort.')
    else:
        print('O pior algoritmo foi o InsertionSort.')
    print()    
    print(n, 'Entradas em Rol') 
    begin = time.time()
    BubbleSort(l)
    end = time.time()
    B = end - begin
    print('BubbleSort    %.6f segundos'%(B))
    begin = time.time()
    SelectionSort(li)
    end = time.time()
    S = end - begin
    print('SelectionSort %.6f segundos'%(S)) 
    begin = time.time()
    InsertionSort(lis)
    end = time.time()
    I = end - begin
    print('InsertionSort %.6f segundos'%(I))
    if B == min(B,I,S):
        print('O melhor algoritmo foi o BubbleSort.')
    elif S == min(B,I,S):
        print('O melhor algoritmo foi o SelectionSort.')
    else:
        print('O melhor algoritmo foi o InsertionSort.')
    if B == max(B,I,S):
        print('O pior algoritmo foi o BubbleSort.')
    elif S == max(B,I,S):
        print('O pior algoritmo foi o SelectionSort.')
    else:
        print('O pior algoritmo foi o InsertionSort.')
    print()    
    print(n, 'Entradas em Rol Invertido')
    begin = time.time()
    BubbleSort(l[::-1])
    end = time.time() 
    B = end - begin
    print('BubbleSort    %.6f segundos'%(B))
    begin = time.time()
    SelectionSort(li[::-1])
    end = time.time()
    S = end - begin
    print('SelectionSort %.6f segundos'%(S))
    begin = time.time()
    InsertionSort(lis[::-1])
    end = time.time()
    I = end - begin
    print('InsertionSort %.6f segundos'%(I))
    if B == min(B,I,S):
        print('O melhor algoritmo foi o BubbleSort.')
    elif S == min(B,I,S):
        print('O melhor algoritmo foi o SelectionSort.')
    else:
        print('O melhor algoritmo foi o InsertionSort.')
    if B == max(B,I,S):
        print('O pior algoritmo foi o BubbleSort.')
    elif S == max(B,I,S):
        print('O pior algoritmo foi o SelectionSort.')
    else:
        print('O pior algoritmo foi o InsertionSort.')
    print()    
    
TesteDeVelocidade(1000)
print()
TesteDeVelocidade(5000)
print()
TesteDeVelocidade(10000)
