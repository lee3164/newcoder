#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 下午9:36
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


class Solution(object):
    """
    给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
    你可以假设网格的四个边均被水包围。

示例 1:
输入:
11110
11010
11000
00000

输出: 1

示例 2:
输入:
11000
11000
00100
00011

输出: 3

    也可以不用visited集合，每次访问到1就将当前的值改成0
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        visited = set()
        num = 0
        m, n = len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if (i, j) in visited or grid[i][j] == '0':
                    continue
                num += 1
                q = [(i, j)]
                while q:
                    new_q = []
                    for x, y in q:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and (x, y) not in visited:
                            visited.add((x, y))
                            new_q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
                    q = new_q

        return num


if __name__ == '__main__':
    a = [
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "1"]
    ]
    print Solution().numIslands(a)
