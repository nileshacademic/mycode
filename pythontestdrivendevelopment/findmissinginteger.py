1. MissingInteger
Find the smallest positive integer that does not occur in a given sequence.

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

///

#!/usr/bin/python3
A=[1,2,3]
A=[-1,-3]
A = [1, 3, 6, 4, 1, 2]
A=[-3,-4,1,2,3,9,7]
A=[-3,-1]
A=[1,2,3]

def solution(A):
    # write your code in Python 3.6
#   A.sort()
    c=[]
    d=[]
    rangecreation=max(A)+2

    if rangecreation <= 1:
        rangecreation=2

    for a in range(1,rangecreation):
        c.append(a)

    for a in c:
        if a not in A:
            d.append(a)

    minimum=min(d)
    print (minimum)
    return minimum

solution(A)

///
