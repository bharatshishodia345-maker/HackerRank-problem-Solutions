#!/bin/python3

import os

def hurdleRace(k, height):
    max_height = max(height)
    return max(0, max_height - k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, k = map(int, input().rstrip().split())
    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')
    fptr.close()