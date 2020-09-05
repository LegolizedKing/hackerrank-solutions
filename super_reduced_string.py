#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    a=[]
    for i in range(len(s)):
        if not a or s[i]!=a[-1]:
            a.append(s[i])
        else:
            a.pop()
    if a:
        return ''.join(a)
    else:
        return 'Empty String'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

