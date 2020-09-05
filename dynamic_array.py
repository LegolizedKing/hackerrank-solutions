#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seq=[]
    result=[]
    lastans=0
    for i in range(n):
        seq.append([])
    for i in range(len(queries)):
        x,y=queries[i][1],queries[i][2]
        if queries[i][0]==1:
            index=(x^lastans)%n
            seq[index].append(y)
        elif queries[i][0]==2:
            index=(x^lastans)%n
            size=y % len(seq[index])
            lastans=seq[index][size]
            result.append(lastans)
    return result

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

