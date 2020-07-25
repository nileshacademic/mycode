#!/usr/bin/python3.6
#longest bi valued slice in python

#A=[0,5,4,4,5,12]
#A=[4,2,2,4,2]
#A=[1,2,3,2]
#A=[4,4]
A=[4,5,5,3,3,7,1,3,3,3,3,3]

def solution(A):
    c=[]
    b=set()
    d=[]
    while A:
        for a in A:
            if len(b)==2:
                continue
            else:
                b.add(a)
        for a in A:
            if a in b:
                c.append(a)
            else:
                break
        A.pop(0)
        d.append(len(c))
        c=[]
        b=set()
    return max(d)

print (solution(A))
