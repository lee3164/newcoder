#!/usr/bin/env python
# coding=utf-8

"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

链接：https://leetcode-cn.com/problems/find-the-duplicate-number

1. 不能排序
2. 不能用map
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        什么时候能用二分查找；
        单调有序
        但是这个数组并不是有序的，所以不能用二分查找；
        题目特意提示了 数字范围在 1-n，并且有至少一个重复的数字，假设重复的数字是j
        如果按照位置去放数字的话，比如1放在第一位，2放在第二位，那么j位置有多个数字
        设 cnt[i] 代表 i位置 <= i的数字个数，
        那么 cnt[i] <= i (i < j)
            cnt[i] > i (i >= j)
        如果数字刚好重复一个，满足上述条件
        如果重复多个的话，那么多的那个数字可以看做是将其中一个数字变成了j，
        如果是将j之前的某个数字变成j，假设是i, 那么 cnt[k] = k, (k < i)
        cnt[k] = k - 1 (i <= k < j) 因为少了个i, cnt[k] > k (k >= j)

        如果将j之后的某个数字变成j，那么 cnt[k] = k (k < j)
        cnt[k] > k （k >= j）这部分还是没变的，因为cnt表示的是i位置小于等于i的数字个数
        移到前的数字i 会累积在 j上，而 i > j，这部分会重新累积到 i上面

        所以此题目中 cnt[i]这个数组始终递增，我们要找的是 第一个 cnt[i] > i的数字，这个数字就是重复数字

        1,2,2,3,4
        """

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            cnt = 0
            for num in nums:
                if num <= m:
                    cnt += 1
            if cnt <= m:
                l = m + 1
            else:
                r = m

        return l
