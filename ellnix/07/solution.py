primes = [2]

n = 3
while len(primes) <= 10000:
    if not any(n % prime == 0 for prime in primes):
        primes.append(n)

    n += 2

print(n - 2)
