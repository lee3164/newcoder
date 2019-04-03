#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 上午10:02
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals

import copy
import random
import time
import unittest


def bubble_sort(nums):
    for i in reversed(xrange(0, len(nums))):
        for j in xrange(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def insert_sort(nums):
    for i in xrange(1, len(nums)):
        j = i
        num = nums[j]
        while j > 0 and num < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = num


def merge_sort(nums):
    def merge_sort_impl(nums, start, end):
        if start >= end:
            return
        mid = (start + end) / 2
        merge_sort_impl(nums, start, mid)
        merge_sort_impl(nums, mid + 1, end)
        merge(nums, start, mid, end)

    def merge(nums, start, mid, end):
        tmp = []
        i, j = start, mid + 1
        while i <= mid and j <= end:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1

        while i <= mid:
            tmp.append(nums[i])
            i += 1

        while j <= mid:
            tmp.append(nums[j])
            j += 1

        for i, num in enumerate(tmp):
            nums[start + i] = num

    merge_sort_impl(nums, 0, len(nums) - 1)


def quick_sort(nums):
    def quick_sort_impl(nums, left, right):
        if left >= right:
            return

        mid = partition(nums, left, right)
        quick_sort_impl(nums, left, mid - 1)
        quick_sort_impl(nums, mid + 1, right)

    def partition(nums, left, right):
        """
        这个Partition写法通过两个指针，一个往后遇见比自己大的停下，一个往前遇见比自己小的停下，
        然后交换，注意 条件一定是 i <= j； 这样可以确保最终结果中i - j = 1，此时nums[i]肯定大于
        pivot，nums[j]肯定小于pivot，如果条件是 i < j ，最终停下来的时候，i == j，不能确定那个位置的
        num和pivot的关系
        """

        # 采用 左 中 右 三数取中的方式确定pivot，避免划分的特别不均匀
        mid = (left + right) / 2
        if nums[left] < nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]
        if nums[right] < nums[mid]:
            nums[right], nums[mid] = nums[mid], nums[right]
        if nums[right] < nums[right]:
            nums[right], nums[left] = nums[left], nums[right]

        pivot = left
        i = left + 1
        j = right
        while i <= j:
            while i <= j and nums[i] < nums[pivot]:
                i += 1
            while i <= j and nums[j] >= nums[pivot]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[j], nums[pivot] = nums[pivot], nums[j]
        return j

    def partition2(nums, left, right):
        pivot = nums[left]
        i = left
        j = right

        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] < pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        return i

    quick_sort_impl(nums, 0, len(nums) - 1)


def heap_sort(nums):
    def sift_down(nums, idx, size):
        while 2 * idx + 1 < size:
            l = 2 * idx + 1
            m = l
            if l + 1 < size and nums[l] < nums[l + 1]:
                m = l + 1
            if nums[idx] >= nums[m]:
                break
            nums[idx], nums[m] = nums[m], nums[idx]
            idx = m

    def make_heap(nums):
        for i in reversed(xrange(0, len(nums) / 2)):
            sift_down(nums, i, len(nums))

    make_heap(nums)
    for i in reversed(xrange(1, len(nums))):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, 0, i)


class TestSort(unittest.TestCase):

    def test_sort(self):
        TEST_COUNT = 10
        TEST_RANGE = 1000
        sort_funcs = [bubble_sort, insert_sort, merge_sort, quick_sort, heap_sort]
        time_dict = {sort_func.func_name: 0 for sort_func in sort_funcs}

        for i in xrange(0, TEST_COUNT):
            origin_nums = [i for i in xrange(random.randint(0, TEST_RANGE))]  # 随机产生一个已经排序的序列

            for sort_func in sort_funcs:
                test_nums = copy.copy(origin_nums)
                random.shuffle(test_nums)  # 随机打乱该序列
                s = time.time()
                sort_func(test_nums)  # 排序
                e = time.time()
                self.assertEqual(test_nums, origin_nums, "sort_func={}".format(sort_func.func_name))  # 比较
                time_dict[sort_func.func_name] += (e - s)

        for func_name, total_time in time_dict.iteritems():
            print func_name, total_time


if __name__ == '__main__':
    unittest.main()
