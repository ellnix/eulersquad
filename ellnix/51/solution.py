import itertools
import math

REQUIRED_SIZE = 8

def primes():
    primes = [2]
    yield 2
    n = 3

    while True:
        if not any(n % prime == 0 for prime in primes):
            primes.append(n)
            yield n

        n += 2


def to_digits(n):
    digits = []

    while n > 0:
        digits.append(n % 10)
        n //= 10

    return digits


def from_digits(digits):
    n = 0

    for i, d in enumerate(digits):
        n += d * 10 ** i

    return n


def relevant_digit_positions(digits):
    groups = [[], []]

    for i, d in enumerate(digits):
        if d == 0:
            groups[0].append(i)
        elif d == 1:
            groups[1].append(i)

    return groups


def digit_position_combinations(group):
    combinations = [group]

    for length in range(1, len(group)):
        combinations.extend(itertools.combinations(group, length))

    return combinations


def is_prime(n):
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime


def family_size(digits, pos):
    if len(pos) < 1:
        return 0

    size = 1

    while True:
        for p in pos:
            digits[p] += 1

            if digits[p] > 9 or size - digits[p] < REQUIRED_SIZE - 10:
                break
        else:
            if is_prime(from_digits(digits)):
                size += 1

            continue

        break

    return size


for prime in primes():
    digits = to_digits(prime)

    positions = relevant_digit_positions(digits)

    for d, pos in enumerate(positions):
        for comb in digit_position_combinations(pos):
            fam_size = family_size(digits.copy(), comb)
            if fam_size >= REQUIRED_SIZE:
                print(prime)
                exit()
