#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

from multiprocessing import Process, Lock, Pool, Queue
import os
import time

L = [1, 2, 3]


def add(q, lock, a, b):
    lock.acquire()
    L1 = range(a, b)
    lock.release()
    q.put(L1)
    print L1

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    p1 = Process(target=add, args=(q, lock, 20, 30))
    p2 = Process(target=add, args=(q, lock, 30, 40))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    L += q.get() + q.get()
    print L

