#!/usr/bin/env python
# coding=utf-8
"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

链接：https://leetcode-cn.com/problems/power-of-two

如果是2的幂次方，那么二进制上只有一个1，且为最高位。那么n-1就除了最高位全是1，因此 n&(n-1)==0应该要成立
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0
