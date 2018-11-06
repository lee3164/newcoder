# coding=utf-8

class Solution(object):
    """
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。

    示例 1:
    输入: 2.00000, 10
    输出: 1024.00000

    示例 2:
    输入: 2.10000, 3
    输出: 9.26100

    示例 3:
    输入: 2.00000, -2
    输出: 0.25000
    解释: 2-2 = 1/22 = 1/4 = 0.25

    说明:
    -100.0 < x < 100.0
    n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
    """
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        r = 1
        while True:
            a = x
            i = 1
            while i * 2 <= n:
                a *= a
                i *= 2

            r *= a
            if n - i == 0:
                break
            n = n - i
        return r

    def myPow2(self, x, n):
        """
        2 ^ 10 = 2^(2^3) * 2^(2^2)，可以看出，每次乘的时候，n的该位必须为1，其他时候都只是在累计算该位应该乘的值
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow2(x, -n)

        r = 1
        while n > 0:
            if n & 1:
                r *= x
            x *= x
            n >>= 1
        return r


if __name__ == '__main__':
    print Solution().myPow2(2.0, 10)
