# coding=utf-8

class Solution(object):
    """
    编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

每个丑数都是由另一个丑数乘2，3，5而来，每个丑数乘2，3，5都会得到另一丑数，维护3个idx，
    """
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1 for _ in xrange(n)]
        x2 = x3 = x5 = 0

        i = 1
        while i < n:
            f[i] = min(f[x2] * 2, f[x3] * 3, f[x5] * 5)
            if f[i] == f[x2] * 2:
                x2 += 1
            if f[i] == f[x3] * 3:
                x3 += 1
            if f[i] == f[x5] * 5:
                x5 += 1
            i += 1
        return f[n - 1]