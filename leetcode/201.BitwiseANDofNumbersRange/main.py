#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 下午1:45
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


class Solution(object):
    """
    给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
    示例 1:
    输入: [5,7]

    输出: 4
    示例 2:
    输入: [0,1]
    输出: 0

    0000
    0001
    0010
    0011
    0100
    0101
    0110
    0111
    1000
    1001
    1010
    1011
    1100
    1101
    1110
    1111
    可以观察出第0位，每2个数字一个周期，比如
    第1位，没4个数字一个周期，第2位，每8个数字一个周期
    得出第i为，每2 ** (i + 1)一个周期，在每个周期内，前面2**i都是0，后面2**i都是1
    因此 当前数字 % 2 **i 可以得出当前数字在 2 ** i 个数字里面的位置idx，
    根据 n - m得到diff，如果 idx + diff >= 2 ** i ,说明有0,1交替，相与之后肯定是0
    """
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0

        diff = n - m
        res = 0
        # 1.确定每一位是0还是1,
        # 2.确定当前的位置
        for i in xrange(0, 32):
            val = (m >> i) & 1
            idx = m % (2 ** i)
            if val == 1 and idx + diff < (2 ** i):
                res |= (1 << i)

        return res


if __name__ == '__main__':
    print Solution().rangeBitwiseAnd(5, 7)
