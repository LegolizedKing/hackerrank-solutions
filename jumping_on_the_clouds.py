#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
        j=0
        i=0
        while i<n-1:
                if c[i]==1:
                        i+=1
                        continue
                else:
                        if c[i+1]==0:
                                if i+2==n:
                                        i+=1
                                        j+=1
                                        continue
                                if c[i+2]==0:
                                        j+=1
                                        i+=2
                                else:
                                        j+=1
                                        i+=1
                        else:
                                j+=1
                                i+=2
                                continue
        return j

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
