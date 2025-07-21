DIGITS = 3

def to_digits(number):
    digits = []

    while(number > 0):
        digits.append(number % 10)
        number = number // 10

    return digits

def is_palindrome(number):
    digits = to_digits(number)
    mid = len(digits) // 2

    for a, b in zip(digits[:mid], reversed(digits[mid:])):
        if a != b:
            return False

    return True

highest = 0

for x in range(10 ** (DIGITS - 1), 10 ** DIGITS ):
    for y in range(x, 10 ** DIGITS):
        product = x * y
        if product >= highest and is_palindrome(product):
            highest = product


print(highest)
