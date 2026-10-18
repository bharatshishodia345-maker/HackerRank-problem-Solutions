#!/bin/python3

import os

def designerPdfViewer(h, word):
    max_height = 0

    for letter in word:
        index = ord(letter) - ord('a')
        max_height = max(max_height, h[index])

    return max_height * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))
    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')
    fptr.close()