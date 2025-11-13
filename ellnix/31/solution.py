SUM = 200
COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def combinations(remaining_sum, coins):
    if len(coins) == 1:
        return 1

    r = remaining_sum
    next_coin = coins[0]
    running_sum = 0

    while r >= 0:
        running_sum += combinations(r, coins[1:])
        r -= next_coin

    return running_sum

print(combinations(SUM, COINS))
