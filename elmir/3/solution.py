import math

number = 600851475143
biggestNum = 0

def isPrime(n):
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime


for i in range(2, int(math.sqrt(number) + 1)):
    if number % i == 0:
        if isPrime(i):
            biggestNum = i


print(biggestNum)