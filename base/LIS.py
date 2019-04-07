#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 下午6:18
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals
"""
最长递增子序列LIS
"""

def lis(nums):
    f = [1 for _ in xrange(len(nums))]
    m = 1
    for i in xrange(1, len(nums)):
        for j in xrange(0, i):
            if nums[i] >= nums[j]:
                f[i] = max(f[i], f[j] + 1)
        m = max(m, f[i])
    return m
