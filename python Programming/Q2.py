print("Sahil Tapas")
x, y = 3, 100 
primes = [True] * (y + 1)
primes[0], primes[1], primes[2] = False, False, False

for i in range(2, int(y ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, y + 1, i):
            primes[j] = False

res = [i for i in range(x, y + 1) if primes[i]]
print(res if res else "No")