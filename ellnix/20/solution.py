def fac(n):
    if n < 2:
        return n

    return n * fac(n-1)


print(sum(int(x) for x in list(str(fac(100)))))
