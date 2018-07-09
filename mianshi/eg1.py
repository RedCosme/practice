#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'
# 1. python如何实现单例模式
# Python有两种方式可以实现单例模式
# 下面两个例子使用了不同的方式实现单例模式
"""面试题
"""


class Singleton(object):
    """单例模式"""
    _instance = "1"

    def __new__(cls, *args):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args)
        return cls._instance

class MyClass(Singleton):
    a = 1
########################################################

from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyDecoratorClass(object):
    a = 1


class MSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MMyClass(object):
    __metaclass__ = MSingleton


# 2.什么是lambda函数
# lambda是python定义匿名函数的语法
# 定义lambda函数的形式如下: lambda参数



def Partition(arr,firstIndex,lastIndex):
    i=firstIndex-1
    for j in range(firstIndex,lastIndex):
        if arr[j]>=arr[lastIndex]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[lastIndex]=arr[lastIndex],arr[i+1]
    return i

def QuickSort(arr,firstIndex,lastIndex):

    if firstIndex<lastIndex:
        divIndex=Partition(arr,firstIndex,lastIndex)
        print divIndex
        QuickSort(arr,firstIndex,divIndex)
        QuickSort(arr,divIndex+1,lastIndex)
    else:
        return


arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]

print("initial array:\n",arr)
QuickSort(arr,0,len(arr)-1)
print("result array:\n",arr)
