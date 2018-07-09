#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

"""有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"""
import time
t1 = time.time()
d = []
for i in range(1, 5):
    for j in range(1,5):
        for k in range(1,5):
            if i != k and i != j and j != k:
                print d.append([i, j, k])

print len(d)
print d
t2 = time.time()
print t2-t1


list_num = [1,2,3,4]

list  = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if (j != i and k != j and k != i)]

print (list)
print len(list)

from itertools import permutations

print permutations('123', 2)