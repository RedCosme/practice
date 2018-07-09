import time
import multiprocessing

def worker(d, key, value):
    d[key] = value

if __name__ == "__main__":
    print time.strftime('%y-%m-%d %H:%M:%S',  time.localtime())
    mgr = multiprocessing.Manager()
    d = mgr.dict()

    jobs = [ multiprocessing.Process(target=worker, args=(d, i, i*2))
             for i in range(10)
           ]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print ('Results:' )
    for key in dict(d):
       print "%s->%s" % (key, d[key])