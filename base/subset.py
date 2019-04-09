#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 上午10:10
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals

import copy


def subset(nums):
    """
    求子集
    """
    r = []

    def dfs(r, t, i):
        r.append(copy.copy(t))
        for j in xrange(i, len(nums)):
            if j != i and nums[j] == nums[j - 1]:
                continue
            t.append(nums[j])
            dfs(r, t, j + 1)
            t.pop()

    nums.sort()
    dfs(r, [], 0)
    return r


if __name__ == '__main__':
    print subset([1, 2, 2])
