#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    n = len(p)
    m = len(y)
    
    towns = sorted(zip(x, p))
    clouds = sorted(zip(y, r))
    
    # Number of people in towns that are always sunny
    sunny_population = 0
    town_pop = [0] * n  # Population of each town
    cloud_cover = [0] * m  # Number of towns each cloud covers
    cloud_pop = [0] * m  # Population covered by each cloud

    # Determine population of each town
    for i in range(n):
        town_pop[i] = towns[i][1]

    # Calculate the effect of each cloud
    cloud_ranges = [(clouds[i][0] - clouds[i][1], clouds[i][0] + clouds[i][1]) for i in range(m)]

    i = 0  # Index for towns
    for j in range(m):
        while i < n and towns[i][0] < cloud_ranges[j][0]:
            sunny_population += towns[i][1]
            i += 1
        while i < n and towns[i][0] <= cloud_ranges[j][1]:
            cloud_cover[j] += 1
            cloud_pop[j] += towns[i][1]
            i += 1

    while i < n:
        sunny_population += towns[i][1]
        i += 1

    # Find maximum sunny population by removing one cloud
    max_population = sunny_population
    for j in range(m):
        if cloud_cover[j] > 0:
            max_population = max(max_population, sunny_population + cloud_pop[j])

    return max_population
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
