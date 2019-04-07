#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 下午6:32
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


def lcs(str1, str2):
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
