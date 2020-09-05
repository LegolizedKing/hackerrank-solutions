#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    hstack,pstack=[],[]
    maxarea=0
    h.append(0)
    for i in range(len(h)):
        lastwidth=len(h)+1
        while len(hstack)!=0 and hstack[-1]>h[i]:
            lastwidth=pstack[-1]
            width=i-pstack.pop()
            height=hstack.pop()
            area=width*height
            maxarea=max(area,maxarea)
        if len(hstack)==0 or hstack[-1]<h[i]:
            hstack.append(h[i])
            pstack.append(min(lastwidth,i))
    return maxarea
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

