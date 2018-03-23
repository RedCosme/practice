#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

arr = [8, 7, 4, 4, 6, 7, 4 ,6]
dic = {}
for item in arr:
    if item in dic.keys():
        dic[item] += 1
    else:
        dic[item] = 1

print dic


# 二叉树深度
import Queue

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def treeDepth(tree):
    if tree==None:
        return 0

    leftDepth = treeDepth(tree.left)
    rightDepth = treeDepth(tree.right)
    if leftDepth > rightDepth:
        return leftDepth + 1
    if rightDepth >= leftDepth:
        return rightDepth + 1

def treeWidth(tree):
    curwidth = 1
    maxwidth = 0
    q = Queue.Queue()
    q.put(tree)
    while not q.empty():
        n = curwidth
        print n
        print q.qsize()
        q.get()
        for i in range(curwidth):
            tmp = q.get()
            curwidth-=1
            if tmp.left:
                q.put(tmp.left)
                curwidth+=1
            if tmp.right:
                q.put(tmp.right)
                curwidth+=1
        if curwidth > maxwidth:
            maxwidth=curwidth
    return maxwidth

root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
depth = treeDepth(root)
print depth
width = treeWidth(root)
print width
