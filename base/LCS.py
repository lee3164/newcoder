#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 下午6:32
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


def lcs(str1, str2):
    """
    什么是最长公共子序列呢?好比一个数列 S，如果分别是两个或多个已知数列的子序列，且是所有符合此条件序列中最长的，则S 称为已知序列的最长公共子序列。
    举个例子，如：有两条随机序列，如 1 3 4 5 5 ，and 2 4 5 5 7 6，则它们的最长公共子序列便是：4 5 5。
    """
    m, n = len(str1), len(str2)
    dp = [[0] for _ in xrange(m) for _ in xrange(n)]
    for i in xrange(0, m):
        dp[i][0] = 1 if str1[i] == str2[0] else 0
    for j in xrange(0, n):
        dp[0][j] = 1 if str1[0] == str2[j] else 0

    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

    return dp[m - 1][n - 1]
