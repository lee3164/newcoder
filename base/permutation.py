#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 下午8:04
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals

import copy


def next_permutation(nums):
    """
    这里面有两个while循环，分别解释下条件
    1.第一个是要从后往前找出递增序列中最大的那个，比如1，2，5，4，3，找到的就是5这个位置
    为什么是 <= ，主要是为了跳过重复元素，让重复元素只被算一次，比如 1，2，5，5，4，3这个
    序列，从后往前有两个5。
    2.第二个循环条件是从末尾找到第一个比i-1的位置大的数，首先i > 0，否则i-1就越界了。
    然后条件为啥是 <= ，同样，比如1,2,5,2,0这个，如果是 < 的情况下，符合这个条件的时候
    j在第二个2的位置，此时nums[i-1] == nums[j]，交换两个同样的数没啥意义，因为2在这个位置肯定
    已经被计算过了，此时应该跳过
    """
    i = len(nums) - 1
    while i > 0 and nums[i] <= nums[i - 1]:
        i -= 1

    if i > 0:
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
    nums[i:] = nums[::-1][:len(nums) - i]


def full_permutation(nums):
    r = []
    while not r or r[0] != nums:
        r.append(copy.copy(nums))
        next_permutation(nums)
    return r


def full_permutation2(nums):
    """
    非去重全排列
    """
    r = []

    def dfs(r, i):
        if i == len(nums):
            r.append(copy.copy(nums))
            return

        for j in xrange(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            dfs(r, i + 1)
            nums[i], nums[j] = nums[j], nums[i]

    dfs(r, 0)
    return r


def full_permutation3(nums):
    """
    去重全排列
    """
    r = []

    def dfs(r, i):
        if i == len(nums):
            r.append(copy.copy(nums))
            return

        # 这里意思是把 i~len(nums)-1的位置的数字依次换到i位置上，一个个试，
        # 但是要做去重处理，比如 1,1,2，针对i=0的时候，第0位和第1位都是1，
        # 那么j=0和j=1是一样的效果，因此需要做去重处理
        for j in xrange(i, len(nums)):
            # 这个去重处理是正确的吗？看上去是对的，如果j==i，肯定不用做去重的，否则
            # 和前一个比较，如果一样就去重，但是我们默认这里的nums是有序的，实际上并不是
            # 比如 0,0,1,3 可以得到 3,0,1,0，此时递归i=1的时候，序列等于是0,1,0，就已经失序了，所以这里不能这么判断
            # 因此这里理论上应该和前面所有的数字进行比较
            # if j != i and nums[j - 1] == nums[j]:
            #     continue

            ok = True
            for k in xrange(i, j):
                if nums[k] == nums[j]:
                    ok = False
                    break

            if not ok:
                continue

            nums[i], nums[j] = nums[j], nums[i]
            dfs(r, i + 1)
            nums[i], nums[j] = nums[j], nums[i]

    nums.sort()
    dfs(r, 0)
    return r


if __name__ == '__main__':
    a = [0, 1, 0, 3]
    print full_permutation3(a)
