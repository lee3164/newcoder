#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        re = []
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, n - 1
        u, d = 0, m - 1

        i, j = 0, 0

        while l <= r and u <= d:
            while j <= r:
                re.append(matrix[i][j])
                j += 1
            u += 1
            i, j = u, r

            if not (l <= r and u <= d):
                break

            while i <= d:
                re.append(matrix[i][j])
                i += 1
            r -= 1
            i, j = d, r

            if not (l <= r and u <= d):
                break

            while j >= l:
                re.append(matrix[i][j])
                j -= 1
            d -= 1
            i, j = d, l

            if not (l <= r and u <= d):
                break

            while i >= u:
                re.append(matrix[i][j])
                i -= 1
            l += 1
            i, j = u, l

        return re


if __name__ == '__main__':
    print Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
