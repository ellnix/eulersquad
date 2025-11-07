UPPER_BOUND = 1_000_000

def to_digits(number):
    digits = []

    while(number > 0):
        digits.append(number % 10)
        number = number // 10

    return digits

filtered = []

for i in range(2, UPPER_BOUND):
    digits = to_digits(i)
    sum_of_powers_of_5 = sum(x ** 5 for x in digits)
    if i == sum_of_powers_of_5:
        filtered.append(i)

print(filtered)
print(sum(filtered))
