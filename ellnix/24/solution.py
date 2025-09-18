DIGIT_COUNT = 10
digits = list(range(0, DIGIT_COUNT))

seek = 1_000_000 - 1
result = []

def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n-1)

while len(result) < 10:
    step, seek = divmod(seek, factorial(len(digits) - 1))
    result.append(digits[step])
    digits.pop(step)

print("".join(str(x) for x in result))
