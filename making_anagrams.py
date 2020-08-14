#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    l1=list(a)
    l2=list(b)
    l=len(l1)
    d=0
    for i in range(l):
        t=l1[i]
        if t in l2:
            l2.remove(t)
            d+=1
    f=len(l2) + (len(l1)-d)
    return f

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

