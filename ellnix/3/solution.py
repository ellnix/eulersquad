from math import floor, sqrt

input = 600_851_475_143

def isprime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


for n in reversed(range(floor(sqrt(input)) + 1)):
    if input % n == 0 and isprime(n):
        print(n)
        break
