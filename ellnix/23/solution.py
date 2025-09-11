import math

def is_abundant(n):
    divisor_sum = 0

    for m in range(1, math.floor(n/2+1)):
        if n % m == 0:
            divisor_sum += m

    return divisor_sum > n



abundants = dict()

total = 0

for i in range(1, 28123):
    if is_abundant(i):
        abundants[i] = True

    cond = False

    for a in abundants:
        try:
            cond = abundants[i-a]
            break
        except KeyError:
           continue

    if not cond:
        total += i

print(total)
