#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    s1=sum(h1)
    s2=sum(h2)
    s3=sum(h3)
    while not(s1==s2 and s2==s3):
        if s1>s2 or s1>s3:
            t=h1[0]
            h1.remove(h1[0])
            s1-=t
        if s2>s1 or s2>s3:
            t=h2[0]
            h2.remove(h2[0])
            s2-=t
        if s3>s1 or s3>s2:
            t=h3[0]
            h3.remove(h3[0])
            s3-=t
    return s1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

