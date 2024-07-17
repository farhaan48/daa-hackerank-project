#!/bin/python3

import os
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    # Initialize the dp array where dp[i] means the maximum sum we can achieve with capacity i
    dp = [0] * (k + 1)
    
    # Iterate through all capacities from 1 to k
    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                dp[i] = max(dp[i], dp[i - num] + num)
    
    return dp[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()
        
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        
        arr = list(map(int, input().rstrip().split()))
        
        result = unboundedKnapsack(k, arr)
        
        fptr.write(str(result) + '\n')

    fptr.close()
