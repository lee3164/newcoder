#!/usr/bin/env python
# coding=utf-8

"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

链接：https://leetcode-cn.com/problems/majority-element-ii

摩尔投票发的变种，超过n/3的数字最多两个，因此可以设定x,y分别计数，如果n没出现过，x,y的count都抵消掉一个，
最后得出两个可能是 超过n/3的数字，最后还需要验证下
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x, x_count, y, y_count = 0, 0, 0, 0
        for n in nums:
            if n == x:
                x_count += 1
            elif n == y:
                y_count += 1
            elif x_count == 0:
                x = n
                x_count = 1
            elif y_count == 0:
                y = n
                y_count = 1
            else:
                x_count -= 1
                y_count -= 1

        r = []
        x_count = 0
        for n in nums:
            if n == x:
                x_count += 1

            if x_count > len(nums) / 3:
                r.append(x)
                break

        if x == y:
            return r

        y_count = 0
        for n in nums:
            if n == y:
                y_count += 1

            if y_count > len(nums) / 3:
                r.append(y)
                break

        return r


if __name__ == '__main__':
    print Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2])
