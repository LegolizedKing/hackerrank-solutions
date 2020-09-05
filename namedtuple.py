
from collections import namedtuple
n=int(input())
a=0
f=input().split()
for i in range(n):
    students=namedtuple('student',f)
    MARKS, CLASS, NAME, ID = input().split()
    b=students(MARKS, CLASS, NAME, ID)
    a+=int(b.MARKS)
av=a/n
print("%2f"%av)
