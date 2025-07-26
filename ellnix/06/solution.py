def square_of_sum(n):
    return sum(range(1, n+1)) ** 2

def sum_of_squares(n):
    return sum(x * x for x in range(1, n+1))

print( square_of_sum(100) - sum_of_squares(100) )
