#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    for i in range(len(grid)):
        l=sorted(list(grid[i]))
        grid[i]=''.join(l)
    flag=True
    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if grid[j][i]>grid[j+1][i]:
                flag=False
    if flag:
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

