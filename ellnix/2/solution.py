def fibonacci(x = 1, y = 2):
    yield x
    yield from fibonacci(y, x + y)

sum = 0

for n in fibonacci():
    if n >= 4_000_000:
        break
    elif n % 2 == 0:
        sum += n

print(sum)
