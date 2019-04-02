#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 上午10:02
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals

import copy
import random
import unittest


def bubble_sort(nums):
    for i in reversed(xrange(0, len(nums))):
        for j in xrange(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


class TestSort(unittest.TestCase):

    def test_sort(self):
        sort_funcs = [bubble_sort]

        for i in xrange(0, 100):
            origin_nums = [i for i in xrange(random.randint(0, 100))]  # 随机产生一个已经排序的序列

            for sort_func in sort_funcs:
                test_nums = copy.copy(origin_nums)
                random.shuffle(test_nums)  # 随机打乱该序列
                sort_func(test_nums)  # 排序
                self.assertEqual(test_nums, origin_nums)  # 比较


if __name__ == '__main__':
    unittest.main()
