#!/usr/bin/env python
# coding=utf-8

"""
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = {}
        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                last[num] = num - 1

        r = 0
        for num in nums:
            if num in last:
                continue

            l = 1
            n = num
            while n + 1 in last:
                n += 1
                l += 1
            r = max(l, r)

        return r


print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
