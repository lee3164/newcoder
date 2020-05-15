#!/usr/bin/env python
# coding=utf-8

"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

链接：https://leetcode-cn.com/problems/subarray-sum-equals-k

前缀和问题：假设s[i] 代表 nums[0]~nums[i] 的和，那么  s[i,j]也就是 nums[i]~nums[j] 的和应该等于 s[j]-s[i-1]
对于一个数组而言，前缀和可以一遍遍历就可以求出来，o(n)的时间复杂度。对于要求以j为结尾的连续子数组和为k的情况，我们可以通过求
可以通过 求 s[i-1] == k - s[j]，也就是看 j前面的数字中有多少个 前缀和 == k-s[j]的。j前面的数字的前缀和对应的个数我们可以通过
一个map存下来，每次只需要查 k-s[j]在 map中出现的个数即可，可以在o(n)的时间复杂度完成。
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = {0: 1}
        s = 0
        r = 0
        for num in nums:
            s = s + num
            if s - k in dp:
                r += dp[s - k]
            dp.setdefault(s, 0)
            dp[s] += 1
        return r
