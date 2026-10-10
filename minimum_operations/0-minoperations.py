#!/usr/bin/python3
"""Module that calculates the fewest operations to reach n characters."""


def minOperations(n):
    """Return the fewest number of operations needed to get exactly
    n 'H' characters in the file.

    The operations are 'Copy All' and 'Paste'. The answer is the sum
    of the prime factors of n. Return 0 if n is impossible to achieve.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
