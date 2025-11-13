from functools import reduce

SUM = 200
COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def combinations(remaining_sum, coins):
    if len(coins) == 1:
        return 1

    return sum(combinations(r, coins[1:]) for r in range(remaining_sum, -1, -coins[0]))


print(combinations(SUM, COINS))
