# Day 14
# Problem 14
# Date 23 Feb 2022
# Time 3:45 PM

from random import random

rad = 2


def estimate(n):
    counter = 0
    r2 = rad ** 2
    for _ in range(n):
        x = random() * rad
        y = random() * rad
        if (x ** 2) + (y ** 2) < r2:
            counter += 1

    return 4 * counter / n


print(round(estimate(100000000), 3))
