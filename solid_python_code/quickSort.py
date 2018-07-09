#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

def quick_sort(array):
    less = []
    greator = []

    if len(array) <= 1:
        return array

    pivot = array.pop()

    for item in array:
        if item < pivot:
            less.append(item)
        else:
            greator.append(item)

    return quick_sort(less) + [pivot] + quick_sort(greator)
