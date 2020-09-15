#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        i = len(arr1) - 1
        j = len(arr2) - 2
        r = []
        t = 0
        f = True
        while i >= 0 and j >= 0:
            p = arr1[i]
            q = arr2[j]
            if f:
                p+q-t