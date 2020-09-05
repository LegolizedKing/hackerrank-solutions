#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    d={}
    flag=1
    for item in magazine: 
        if (item in d): 
            d[item] += 1
        else: 
            d[item] = 1
    for item in note:
        if (item in d):
                d[item]-=1
                if d[item]==0:
                        d.pop(item)
        else:
                flag=0
    if flag==1:
        print("Yes")
    else:
        print("No")        

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

