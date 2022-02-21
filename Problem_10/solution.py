# Day 10
# Problem 10
# Date 21 Feb 2021
# Time 6:50 PM

import time


def hello():
    print("Hello")


def scheduler(f, n):
    time.sleep(n/1000)
    f()


scheduler(hello, 0)
scheduler(hello, 1000)
scheduler(hello, 2000)
