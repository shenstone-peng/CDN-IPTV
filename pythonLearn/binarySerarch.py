#!/usr/bin/python
# -*-coding:utf-8 -*-
def binarySearch(alist,target):
    left=0
    right=len(alist)-1
    mid=(left+right)/2
    while left<=right:
        mid=(left+right)/2
        #print(left)
        #print(mid)
        #print(right)
        if alist[mid]<target:
            left=mid+1
        elif alist[mid]>target:
            right=mid-1
        else:
            print(mid)
            break
a=[1,3,4,5,31,32,45,64,321,333,343,444]
target=321
binarySearch(a,target)
#二分查找
