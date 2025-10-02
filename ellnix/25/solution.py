
DIGITS = 1000

divisor = 10 ** (DIGITS - 1)

a = b = 1
i = 2

while (a // divisor) == 0:
    i += 1
    a, b = a + b, a

print(i, a)
