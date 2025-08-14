POWER = 1000

def to_digits(n):
    digits = []

    while n > 0:
        digits.append(n % 10)
        n //= 10

    return digits

n = 2 ** POWER
print(sum(to_digits(n)))
