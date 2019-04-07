#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 下午4:15
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals

import bisect
import unittest


def binary_search(nums, target):
    """
    最基本的二分查找，没有重复元素的
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) / 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1


def first_e(nums, target):
    """
    第一个等于target
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) / 2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return r + 1


def last_e(nums, target):
    """
    最后一个等于target
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) / 2
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l - 1


def first_ge(nums, target):
    """
    第一个大于等于target，即lower_bound
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) / 2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1

    return l


def first_g(nums, target):
    """
    第一个大于target，即upper_bound
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) / 2
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return l


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        nums = [i for i in xrange(0, 10)]
        for i, num in enumerate(nums):
            self.assertEqual(binary_search(nums, num), i)

    def test_first_e(self):
        nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9]
        for num in set(nums):
            self.assertEqual(first_e(nums, num), nums.index(num))

    def test_last_e(self):
        nums = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9]
        reversed_nums = list(reversed(nums))
        for num in set(nums):
            last_e_idx = len(nums) - reversed_nums.index(num) - 1
            self.assertEqual(last_e(nums, num), last_e_idx)

    def test_first_ge(self):
        nums = [i for i in xrange(0, 10)]
        for num in nums:
            self.assertEqual(first_ge(nums, num), bisect.bisect_left(nums, num))

    def test_first_g(self):
        nums = [i for i in xrange(0, 10)]
        for num in nums:
            self.assertEqual(first_g(nums, num), bisect.bisect_right(nums, num))
