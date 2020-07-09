# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 上午11:01
# @Author  : chaos
# @FileName: class_decorated_profiled_fib.py
# @Software: PyCharm
import time


class ProfilingDecorateor(object):
    def __init__(self, f):
        print("Profiling decorator initiating...")
        self.f = f

    def __call__(self, *args):
        start_time = time.time()
        result = self.f(*args)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(*args, end_time - start_time))

        return result

class ToHtmlDecorator(object):
    def __init__(self, f):
        print("HTML wrapper initiating...")
        self.f = f

    def __call__(self, *args):
        print("ToHtmlDecorator called")
        with open("status.log", "w") as log:
            log.write("Fibonacci number for n = {}: {}".format(*args, self.f(*args)))

        return 'Success'


@ToHtmlDecorator
@ProfilingDecorateor
def fib(n):
    print("Inside fib")
    if n < 2:
        return

    fib_prev = 1
    fib = 1
    for num in range(2, n):
        fib_prev, fib = fib, fib + fib_prev

    return fib


if __name__ == "__main__":
    n = 77
    print("Fibonacci number for n = {}: {}".format(n, fib(n)))