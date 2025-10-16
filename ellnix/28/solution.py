GRID_SIZE = 1001

sum = 1
n = 1

for i in range(1, (GRID_SIZE + 1) // 2):
    coefficient = i * 2

    for _ in range(0, 4):
        n += coefficient
        sum += n
        print(n)

print(sum)
