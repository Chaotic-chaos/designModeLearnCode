# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 上午11:22
# @Author  : chaos
# @FileName: function_decorated_fib.py
# @Software: PyCharm
import time


def profiling_decorator(f):
    def wrapped_f(n):
        start_time = time.time()
        result = f(n)
        end_time = time.time()
        print("[Time elapsed for n = {}]: {}".format(n, end_time-start_time))

        return result
    return wrapped_f

@profiling_decorator
def fib(n):
    print("Inside fib")
    if n<2 :
        return

    fib_prev = 1
    fib = 1

    fib_prev, fib = fib, fib+fib_prev

    return fib

if __name__ == "__main__":
    n = 77
    print("Fibonacci number for n = {}: {}".format(n, fib(n)))