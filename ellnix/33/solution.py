def to_digits(n):
    digits = []

    while n > 0:
        digits.append(n % 10)
        n //= 10

    return digits


digit_cancelling_fractions = []

for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        numerator_digits = to_digits(numerator)
        denominator_digits = to_digits(denominator)
        overlap =  set(numerator_digits).intersection(set(denominator_digits))

        if len(overlap) == 1:
            digit_cancelling_fractions.append((numerator, denominator, overlap))



non_trivial_fractions = []

for (num, den, overlap) in digit_cancelling_fractions:
    left_diff = set(to_digits(num)).difference(overlap)
    right_diff = set(to_digits(den)).difference(overlap)

    if len(right_diff) == 1 and len(left_diff) == 1:
        divisor = right_diff.pop()
        if divisor > 0:
            cancelled_res = left_diff.pop() / divisor
            regular_res = num / den

            if cancelled_res == regular_res and num % 10 != den % 10:
                non_trivial_fractions.append((num, den))
                print(f"{num}/{den} -- {cancelled_res} vs {regular_res}")

def gcd(num, den):
    s_term = min(num, den)

    for n in range(s_term, 0, -1):
        if num % n == 0 and den % n == 0:
            return n

def simplify(num, den):
    while (gc := gcd(num, den)) > 1:
        num //= gc
        den //= gc

    return (num, den)

unsimplified_den = 1
unsimplified_num = 1

for (num, den) in non_trivial_fractions:
    unsimplified_num *= num
    unsimplified_den *= den

print(simplify(unsimplified_num, unsimplified_den))
