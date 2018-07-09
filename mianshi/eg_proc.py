#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

from multiprocessing import Process, Pool, Lock
import os
import time

lock = Lock()

def run_proc(name):
    for i in range(5):
        lock.acquire()
        time.sleep(0.2)
        print "Run child process %s (%s)" % (name, os.getpid())
        lock.release()

if __name__ == "__main__":
    print "Run the main process (%s)." % (os.getpid())
    mainStart = time.time()
    p = Pool(8)
    for i in range(16):
        p.apply_async(run_proc, args=('Process' + str(i),))

    print "Waiting for all subprocessing done ..."
    p.close()
    p.join()
    print "All subprocessing done"
    mainEnd = time.time()
    print 'All process run %0.2f seconds.' % (mainEnd - mainStart)


