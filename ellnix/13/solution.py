

cache = dict()

def collatz(n):
    if n == 1:
        return 0

    if not n in cache:
        cache[n] = collatz(n / 2 if n % 2 == 0 else 3 * n + 1) + 1

    return cache[n]


max_val = 1
max_n = 1

for i in range(2, 1_000_000):
    new_val = collatz(i)

    if new_val > max_val:
        max_val = new_val
        max_n = i

print(max_n)
print(max_val)
