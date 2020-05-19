#!/bin/python3

import math
import os
import random
import re
import sys



def gradingStudents(grades):
    # Write your code here
    l=len(grades)
    for i in range(l):
        if grades[i] < 38:
            continue
        else:
            j=grades[i]%5
            if j>=3:
                grades[i] += (5-j)
    return grades
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

