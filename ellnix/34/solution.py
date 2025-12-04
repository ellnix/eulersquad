def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


def to_digits(n):
    digits = []

    while n > 0:
        digits.append(n % 10)
        n //= 10

    return digits


factorial_cumulative = 0

for n in range(3, 100_000_000):
    n_digits = to_digits(n)
    sum_of_digit_facs = sum(factorial(digit) for digit in n_digits)
    if sum_of_digit_facs == n:
        factorial_cumulative += n

    if (n % 1000 == 0):
        print(f"So far {n} with a sum of {factorial_cumulative}")


