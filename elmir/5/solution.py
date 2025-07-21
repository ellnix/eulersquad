number = 20

while True:
    number += 20
    num_check = 0

    for num in range(11, 20):
        if number % num != 0:
            break
        else:
            num_check += 1

    if num_check >= 9:
        break

print(number)