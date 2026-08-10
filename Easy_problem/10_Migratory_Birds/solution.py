#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
       
    max = 0
    ans = 0
    for bird, count in freq.items():
        if count > max:
            max = count
            ans = bird 
    
        elif count == max and bird < ans:
        
            ans = bird
    return ans
        
    
    
    return freq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
