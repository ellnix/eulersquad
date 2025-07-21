def isPalindrome(number):
    reversed_number = int(str(number)[::-1])

    if reversed_number == number:
        return True
    else:
        return False

biggest_palindrome = 0

for first in range(1, 1000):
    for second in range(first, 1000):
        product = first * second
        if isPalindrome(product) and product > biggest_palindrome:
            biggest_palindrome = product

print(biggest_palindrome)