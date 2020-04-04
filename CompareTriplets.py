#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
#a=(a[0],a[1],a[2]) = (1,2,3)
#b=(b[0],b[1],b[2]) = (3,2,1)
def compareTriplets(a, b):
    totalA = 0
    totalB = 0
    if (a[0] > b[0]):
        totalA += 1
    elif (a[0] > b[0]):
        totalB += 1

    if(a[1] > b[1]):
        totalA += 1
    elif (a[1] > b[1]):
        totalB += 1

    if(a[2] > b[2]):
        totalA += 1
    elif (a[2] > b[2]):
        totalB += 1
    return(totalA,totalB)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
