#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not dependencies:
            return n / k if n % k == 0 else n / k + 1

        d1 = {}
        d2 = {}

        i = 1
        while i <= n:
            d1.setdefault(i, set())
            d2.setdefault(i, set())
            i += 1

        for (i, j) in dependencies:
            d1.setdefault(i, set())
            d1.setdefault(j, set())
            d1[j].add(i)

            d2.setdefault(i, set())
            d2.setdefault(j, set())
            d2[i].add(j)

        r = 0
        while d1:
            r += 1
            t = []
            for i, s in d1.iteritems():
                if not s:
                    t.append([i, len(d2[i])])

            t = sorted(t, key=lambda x: x[1], reverse=True)

            for (i, _) in t[0:k]:
                for j in d2[i]:
                    d1[j].remove(i)
                d1.pop(i)

        return r


if __name__ == '__main__':
    print Solution().minNumberOfSemesters(9,
                                          [[4, 8], [3, 6], [6, 8], [7, 6], [4, 2], [4, 1], [4, 7], [3, 7], [5, 2],
                                              [5, 9], [3, 4], [6, 9], [5, 7]],
                                          2)
