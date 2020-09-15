#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0 for _ in nums]
        r = [0 for _ in nums]

        l[0] = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == 0:
                l[i] = 0
            else:
                l[i] = l[i - 1] + 1
            i += 1

        r[-1] = nums[-1]
        i = len(nums) - 2
        while i >= 0:
            if nums[i] == 0:
                r[i] = 0
            else:
                r[i] = r[i + 1] + 1
            i -= 1

        ma = -1
        i = 0
        while i < len(l):
            if l[i] != 0:
                i += 1
                continue

            if i == 0:
                ma = max(r[i + 1], ma)
            elif i == len(l) - 1:
                ma = max(l[i - 1], ma)
            else:
                ma = max(l[i - 1] + r[i + 1], ma)

            i += 1

        if ma == -1:
            return len(l) - 1

        return ma


print Solution().longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1])
