"""Lottery Lucky Dip Number Generator v2 Write a function that will return
random numbers for a lottery.

The lottery will draw 8 balls labeled 1 to 20.
The balls will be picked out of a bag and if the number rules below are valid
we will accept that number as part of the lottery numbers and return the ball
back in the bag.  We will do this until we get 8 lottery numbers.
Rules are:
- The same number can appear more than once
- No number can appear more times than its value

Examples valid draws:
1, 2, 3, 4, 5, 6, 7, 8
1, 2, 2, 3, 4, 6, 7, 8

Example not allowed:
1, 1, 2, 2, 3, 3, 7, 8      (because of 1 having duplicates)
"""
import random
from collections import defaultdict


def lottery_generator():
    results = []
    appearance = defaultdict(int)

    while True:
        if len(results) == 8:
            break
        value = random.randint(1, 20)
        if appearance[value] >= value:
            continue
        else:
            appearance[value] += 1
            results.append(value)
    return sorted(results)
