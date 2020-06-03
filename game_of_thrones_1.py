#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
        l=list(s)
        m=[]
        for x in l:
            if x not in m:
                m.append(x)
        d={}
        for i in m:
            a=l.count(i)
            d[i]=a
        flag=0
        for j in d:
            if d[j]%2 ==0:
                a='YES'
            else:
                flag+=1
        if flag>1:
            return 'NO'
        else:
            return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

