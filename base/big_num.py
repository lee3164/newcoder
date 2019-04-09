#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 下午6:53
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


def big_num_add(num1, num2):
    c = 0
    i, j = len(num1) - 1, len(num2) - 1
    r = []
    while i >= 0 and j >= 0:
        s = int(num1[i]) + int(num2[j]) + c
        c = s / 10
        r.append(str(s % 10))
        i -= 1
        j -= 1

    while i >= 0:
        s = int(num1[i]) + c
        c = s / 10
        r.append(str(s % 10))
        i -= 1

    while j >= 0:
        s = int(num2[j]) + c
        c = s / 10
        r.append(str(s % 10))
        j -= 1

    if c == 1:
        r.append('1')

    return "".join(reversed(r))


def big_num_mul(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    r = "0"
    i = len(num1) - 1
    while i >= 0:
        l = ['0' for _ in xrange(len(num1) - 1 - i)]
        c = 0
        j = len(num2) - 1
        while j >= 0:
            s = int(num2[j]) * int(num1[i]) + c
            c = s / 10
            l.append(str(s % 10))
            j -= 1
        if c > 0:
            l.append(str(c))

        r = big_num_add(r, "".join(reversed(l)))
        i -= 1

    return r


if __name__ == '__main__':
    print big_num_mul("9", "9")
