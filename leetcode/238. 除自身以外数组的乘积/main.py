#!/usr/bin/env python
# coding=utf-8

"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

 

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

链接：https://leetcode-cn.com/problems/product-of-array-except-self

dp思想，L[i]代表i左侧数字乘积，R[i]代表i右侧数字乘积，那么f[i]=L[i]*R[i]
其中L[0]=R[len(nums)-1]=1，我们可以同时计算i左侧的乘积和j=len(num)-1-i右侧的乘积，分别用两个变量保存
即代码中的left和right，然后乘 r[i]和对应的r[j]，r每个对应的位置都会分别乘上左侧的乘积和右侧的乘积，一遍就可以遍历完成
时间复杂度o(n)，空间复杂度o(1)
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = [1 for _ in xrange(len(nums))]
        i = 0
        left = right = 1
        while i < len(nums):
            r[i] *= left
            left *= nums[i]

            r[len(nums) - 1 - i] *= right
            right *= nums[len(nums) - 1 - i]

            i += 1
        return r
