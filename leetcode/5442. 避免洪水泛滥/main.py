#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        r = [-1 for rain in rains]
        l = []
        d = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                l.append(i)
                continue

            if rain not in d:
                d[rain] = i
                continue

            j = d[rain]
            k = 0
            while k < len(l):
                if l[k] > j:
                    break
                k += 1

            if k == len(l):
                return []

            r[l.pop(k)] = rain
            d[rain] = i

        for i in l:
            r[i] = 1

        return r


if __name__ == '__main__':
    print Solution().avoidFlood([1, 2, 3, 4])
