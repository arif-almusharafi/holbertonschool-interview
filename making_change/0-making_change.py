#!/usr/bin/python3
"""Making change module"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Return 0 if total is 0 or less.
    Return -1 if total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    coins = sorted(coins)
    impossible = total + 1
    dp = [0] + [impossible] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin > amount:
                break
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    if dp[total] == impossible:
        return -1
    return dp[total]
