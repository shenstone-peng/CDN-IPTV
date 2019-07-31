#!/usr/boin/python
def open(n):
    a=[0]*n
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j%i==0:
                a[j-1]=0 if a[j-1]==1 else 1
    for i in a:
        print i

open(3)
#开灯，算法五分钟
