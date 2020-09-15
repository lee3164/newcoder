#!/usr/bin/env python
# coding=utf-8

"""
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。

 

示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

链接：https://leetcode-cn.com/problems/best-sightseeing-pair

暴力解法是很简单，但是需要o(n2)的时间复杂度
对于任意位置j，我们想要求最大值，需要遍历所有的i（0<=i<j）,得到出最大值
那么有什么办法能够一趟遍历就可以搞定呢？
求分的公式为 f[i][j] = A[i]+A[j]+i-j，稍微变下位置
f[i][j] = A[i]+i + A[j]-j，其中对于位置j，A[j]-j是固定的，因此要找最大值
我们只需要找 A[i]+i的最大值即可。而A[i]+i的最大值可以在遍历的同时进行维护。
"""

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        r = 0
        m = A[0]
        i = 1
        while i < len(A):
            r = max(r, m + A[i] - i)
            m = max(m, A[i] + i)
            i += 1

        return r
