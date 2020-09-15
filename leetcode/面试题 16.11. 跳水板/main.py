#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if shorter == longer:
            return shorter * k

        r = []

        def dfs(last, k, s):
            if k == 0:
                r.append(s)
                return

            items = [shorter, longer]
            if last == longer:
                items = [longer]

            for i in items:
                dfs(i, k - 1, s + i)

        dfs(shorter, k, 0)
        return r

    def divingBoard2(self, shorter, longer, k):
        # 每次减少一个s，增加一个l，就是个等差数列
        if k == 0:
            return []

        if shorter == longer:
            return [shorter * k]

        r = [shorter * k]
        while k >= 1:
            r.append(r[-1] + longer - shorter)
            k -= 1
        return r


if __name__ == '__main__':
    print Solution().divingBoard(1, 2, 4)
