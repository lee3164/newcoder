#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        r = []
        q = []
        i = 1
        while i < len(arr):
            while q and arr[q[-1]] < arr[i]:
                q.pop()
            q.append(i)
            i += 1

        for i, num in enumerate(arr):
            if q and q[0] == i:
                q.pop(0)
            if q:
                r.append(arr[q[0]])
            else:
                r.append(-1)

        return r

    def replaceEmelemts2(self, arr):
        """
        逆向遍历即可
        """
        n = len(arr)
        ans = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans


if __name__ == '__main__':
    print Solution().replaceElements([17, 18, 5, 4, 6, 1])
