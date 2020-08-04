n = 600851475143
answer = 0
for prime in range (2,1000000):
    if n % prime == 0:
        answer = prime
    while n % prime == 0:
        n = n/prime
print(answer)
