# coding=utf-8

class Solution(object):
    """
    给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = {0: 0}
        x = 1
        for i in xrange(1, n + 1):
            if i == x ** 2:
                x += 1
                f[i] = 1
            else:
                f[i] = min([1 + f[i - j ** 2] for j in xrange(1, x)])
        return f[n]