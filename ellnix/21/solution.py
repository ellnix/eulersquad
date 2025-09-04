
def divisor_sum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum

sum = 0

for a in range(1, 10000):
    b = divisor_sum(a)
    db = divisor_sum(b)
    if (a == db and b != a):
        sum += a

print(sum)
