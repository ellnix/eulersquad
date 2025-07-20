firstNum = 1
secondNum = 2
sum = 0
total = 2
while sum <= 4000000:
    sum = firstNum + secondNum
    if sum % 2 == 0:
        total += sum
    firstNum = secondNum
    secondNum = sum

print(total)
