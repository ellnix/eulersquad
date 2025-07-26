DIVISORS = [11, 12, 13, 14, 15, 16, 17, 18, 19]


def is_divisible(n):
    for d in DIVISORS:
        if n % d != 0:
            return False

    return True

n = 20

while not is_divisible(n):
    n += 20

print(n)
