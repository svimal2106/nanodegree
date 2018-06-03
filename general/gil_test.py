#!/usr/bin/python
import threading
import time


class CountDownThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            self.count -= 1

def count(num):
    while num > 0:
        num -= 1


def sequential_execution():
    start_time = time.time()
    count(100000)
    count(100000)
    end_time = time.time()
    print "Sequential Execution time => ", end_time - start_time


def threaded_execution():
    start_time = time.time()
    o1 = CountDownThread(100000)
    o2 = CountDownThread(100000)
    o1.start()
    o2.start()
    o1.join();
    o2.join()
    end_time = time.time()
    print "Threaded execution time => ", end_time - start_time


if __name__ == "__main__":
    sequential_execution()
    threaded_execution()
