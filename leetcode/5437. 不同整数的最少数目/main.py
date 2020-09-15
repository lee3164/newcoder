#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k == len(arr):
            return 0
        if k == len(arr) - 1:
            return 1

        d = {}
        for n in arr:
            d.setdefault(n, 0)
            d[n] += 1

        items = sorted(d.items(), key=lambda i: i[1])

        i = 0
        while i < len(items):
            item = items[i]
            x = min(item[1], k)
            k -= x
            if x == item[1]:
                i += 1

            if k == 0:
                break

        return len(items) - i


if __name__ == '__main__':
    print Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3)
