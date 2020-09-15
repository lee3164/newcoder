#!/usr/bin/env python
# coding=utf-8

"""
bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
f = [10, 10, 9, 9, 8, 8, 7, 7, 6]
f = [9, 9, 10, 10, 8, 8, 7, 7, 6]
"""


class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1

        f = {}
        i = k - 1
        while i < len(bloomDay):
            f[i] = max(bloomDay[i - k + 1: i + 1])

        dp = [[-1 for _ in f] for _ in f]

        def helper(i, j):
            pass