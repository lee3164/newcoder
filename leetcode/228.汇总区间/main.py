#!/usr/bin/env python
# coding=utf-8

"""
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。

示例 1:

输入: [0,1,2,4,5,7]
输出: ["0->2","4->5","7"]
解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
示例 2:

输入: [0,2,3,4,6,8,9]
输出: ["0","2->4","6","8->9"]
解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。

链接：https://leetcode-cn.com/problems/summary-ranges

将起始数字记录，循环比较当前数字和前一个数字，如果不是连续，则输出区间，否则继续
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        r = []
        s = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1] + 1:
                i += 1
                continue

            if nums[i - 1] == s:
                r.append("{}".format(nums[i - 1]))
            else:
                r.append("{}->{}".format(s, nums[i - 1]))
            s = nums[i]
            i += 1

        if s == nums[-1]:
            r.append("{}".format(s))
        else:
            r.append("{}->{}".format(s, nums[-1]))

        return r


if __name__ == '__main__':
    print Solution().summaryRanges([0])
