from itertools import permutations

ALL_DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
DIGITS_SET = set(ALL_DIGITS)


def to_digits(number):
    digits = []

    while(number > 0):
        digits.append(number % 10)
        number = number // 10

    return digits


def has_repetition(digits):
    return len(digits) != len(set(digits))


def from_digits(digits):
    n = 0

    for i, d in enumerate(digits):
        n += d * 10 ** i

    return n


def find_multiplicants(n, digits):
    n_digit_set = set(digits)
    remaining_digits = DIGITS_SET.difference(n_digit_set)
    cnt = len(remaining_digits)

    for x_len in range(1, cnt + 1):
        y_len = cnt - x_len

        for x_digits in permutations(remaining_digits, x_len):
            x = from_digits(x_digits)

            for y_digits in permutations(remaining_digits.difference(set(x_digits)), y_len):
                y = from_digits(y_digits)

                if (x * y) == n:
                    return [x, y]

    return None


filtered = []

for i in range(1_000, 100_000):

    digits = to_digits(i)

    if 0 in digits or has_repetition(digits):
        continue

    multiplicants = find_multiplicants(i, digits)
    if (multiplicants != None):
        filtered.append(i)
        print(i, multiplicants)
        print("SUM: ", sum(filtered))


