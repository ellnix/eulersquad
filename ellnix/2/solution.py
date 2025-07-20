from itertools import takewhile

def fibonacci(x = 1, y = 2):
    yield x
    yield from fibonacci(y, x + y)

result = sum(filter(lambda x: x % 2 == 0, takewhile(lambda x: x < 4_000_000, fibonacci())))

print(result)
