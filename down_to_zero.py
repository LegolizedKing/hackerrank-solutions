#!/bin/python3

import os
import sys

#
# Complete the downToZero function below.
#
m=10**6
res=list(range(m+1))
for i in range(2,m+1):
    curr=res[i]
    prev=res[i-1]
    if curr>prev+1:
        res[i]=prev+1
        curr=res[i]
    for j in range(2,i+1):
        multiple=i*j
        if multiple>m:
            break
        init=res[multiple]
        if init > curr+1:
            res[multiple]=curr+1

def downToZero(n,res):
    #
    # Write your code here.
    #
    if n<=3:
        return n
    return res[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n,res)

        fptr.write(str(result) + '\n')

    fptr.close()

