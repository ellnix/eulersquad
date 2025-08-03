for x in range(1, 1000):
    for y in range(x, 1000):
        for z in range(y, 1000):
            if x * x + y * y == z * z and x + y + z == 1000:
                res = x * y * z
                print(res)
                exit()

