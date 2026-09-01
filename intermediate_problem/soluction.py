#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    
    remainder = [0] * k

    # Har number ka remainder count karo
    for num in s:
        remainder[num % k] += 1

    ans = 0

    # Remainder 0 se maximum 1 element
    if remainder[0] > 0:
        ans += 1

    # r aur k-r mein se jiski frequency zyada hai, usko lo
    for r in range(1, (k + 1) // 2):
        ans += max(remainder[r], remainder[k - r])

    # Agar k even hai, k/2 remainder se maximum 1 element
    if k % 2 == 0 and remainder[k // 2] > 0:
        ans += 1

    return ans
    
    ans = 0
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            q = s[i] + s[j]
            if q % k != 0:
                count +=1
        if ans < count:
            ans += 1
    return ans                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
