GRID_SIZE = 20

def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n-1)



grid_factorial = factorial(GRID_SIZE)
res = factorial(GRID_SIZE * 2) / (grid_factorial * grid_factorial)

print(int(res))
