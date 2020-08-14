#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    digits = [int(x) for x in str(n)]
    d=0
    n=int(n)
    for i in range(len(digits)):
        if digits[i]!=0:
            if n%digits[i]==0:
                d+=1
    return d
   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

