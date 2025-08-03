primes = list(range(2, 2_000_000))

for i, n in enumerate(primes):
    if n == 0:
        continue

    a = i
    while a + n < len(primes):
        a += n
        primes[a] = 0

print(sum(primes))
