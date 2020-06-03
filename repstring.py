#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
        l=s.count('a')
        l1=len(s)
        a=n//l1
        b=n%l1
        c=[]
        if b>0:
            for i in range(b):
                c.append(s[i])
        d=c.count('a')
        return (l*a) + d
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
