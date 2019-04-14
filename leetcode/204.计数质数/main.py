#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 上午12:10
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


class Solution(object):
    """
    统计所有小于非负整数 n 的质数的数量。
    示例:
    输入: 10
    输出: 4

    解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
    这题搜到一个算法,叫做厄拉多塞筛法. 比如说求20以内质数的个数,首先0,1不是质数.2是第一个质数,然后把20以内所有2的倍数划去.
    2后面紧跟的数即为下一个质数3,然后把3所有的倍数划去.3后面紧跟的数即为下一个质数5,再把5所有的倍数划去.以此类推.
    """
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        non_primes = {0, 1}
        for i in xrange(2, int(n ** 0.5) + 1): # 这里直接判断是否是小于n开方
            if i in non_primes:
                continue
            j = i ** 2
            while j < n:
                non_primes.add(j)
                j += i
        return n - len(non_primes)


if __name__ == '__main__':
    print Solution().countPrimes(101111111)
