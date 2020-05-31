#!/usr/bin/env python
# coding=utf-8

"""
给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，
数组的和最接近  target （最接近表示两者之差的绝对值最小）。

如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。

请注意，答案不一定是 arr 中的数字。



示例 1：

输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
示例 2：

输入：arr = [2,3,5], target = 10
输出：5
示例 3：

输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361
"""

import bisect


class Solution(object):
    def findBestValue(self, arr, target):
        """
        首先思考下结果value的边界，最大值肯定是max(*arr)，即arr中的最大值，因为如果大于了这个值之后
        无论value在如何增大，结果都不会在变化。
        那么最小值呢，也是min(*arr)
        设S(n) = a(1) + ...+ a(n)
        如果S(n) <= target，那么value=max(*arr)，因为这个value在变小会让S(n)变的越来越小，
        更加远离target。

        如果S(n) > target，
        假设大于value的arr中的数字有i个，那么就是求 S(n-i)+i*value-target最接近0的一个，可以看出来
        随着value减小，这个表达式也是递减的，因为是整数，最接近0的那个一个可能是正数，一个可能是负数，
        比较二者绝对值，最小的即可。这两个数字关系肯定是正数比负数大1，我们只需要找到那个正数对应的value
        就可以找到那个负数对应的value

        如何快速找出比value小的数字的和，预先排序
        那么我们可以根据lower_bound快速找到大于等于value的数字的小标，将后面的数字都改成value，
        可以快速得到结果和target比较。

        -1 -1 -1, -1
        """
        s = sum(arr)
        if s <= target:
            return max(*arr)

        arr = sorted(arr)

        s = {-1: 0}
        for i, n in enumerate(arr):
            s[i] = arr[i] + s[i - 1]

        l, r = 0, arr[-1]
        ans = r
        a2 = a2 = 0
        while l <= r:
            m = (l + r) / 2
            i = bisect.bisect_left(arr, m)
            if s[i - 1] + (len(arr) - i) * m - target >= 0:
                ans = m
                a1 = s[i - 1] + (len(arr) - i) * m - target
                r = m - 1
            else:
                l = m + 1

        i = bisect.bisect_left(arr, ans - 1)
        a2 = s[i - 1] + (len(arr) - i) * (ans - 1) - target

        if -a2 <= a1:
            return ans - 1

        return ans


if __name__ == '__main__':
    print Solution().findBestValue([48772, 52931, 14253, 32289, 75263], 40876)
