#!/usr/bin/env python
# coding=utf-8

"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

 

示例 1：

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：

输出：["b==a","a==b"]
输入：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：

输入：["a==b","b==c","a==c"]
输出：true
示例 4：

输入：["a==b","b!=c","c==a"]
输出：false
示例 5：

输入：["c==c","b==d","x!=z"]
输出：true

链接：https://leetcode-cn.com/problems/satisfiability-of-equality-equations
"""

from collections import defaultdict


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        m = {}

        for e in equations:
            i, j = e[0], e[3]
            op = e[1:3]

            m.setdefault(i, i)
            m.setdefault(j, j)

            if op == "!=":
                continue

            while i != m[i]:
                i = m[i]

            while j != m[j]:
                j = m[j]

            m[i] = j

        for e in equations:
            i, j = e[0], e[3]
            op = e[1:3]
            if op == "==":
                continue

            while i != m[i]:
                i = m[i]

            while j != m[j]:
                j = m[j]

            if i == j:
                return False

        return True


if __name__ == '__main__':
    print Solution().equationsPossible(["a==b","b!=a"])
