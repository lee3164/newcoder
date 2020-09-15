#!/usr/bin/env python
# coding=utf-8
"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45

链接：https://leetcode-cn.com/problems/qiu-12n-lcof
"""


class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        return n + self.sumNums(n - 1)
