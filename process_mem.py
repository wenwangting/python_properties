#!/usr/bin/env python
#! -*- coding:utf-8 -*-
import resource


def memUsage():
    list_test = []
    for i in range(0, 1000*10000):
        list_test.append('abcdefg')
        if len(list_test) % 1000000 == 0:
            print(len(list_test), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
    print(resource.getrusage(resource.RUSAGE_SELF))


if __name__ == "__main__":
    memUsage()
