# coding=utf-8

class Solution(object):
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    注意：给定 n 是一个正整数。

    示例 1：
    输入： 2
    输出： 2
    解释： 有两种方法可以爬到楼顶。
    1.  1 阶 + 1 阶
    2.  2 阶

    示例 2：
    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶
    """
    f = {
        1: 1,
        2: 2
    }

    def climbStairs(self, n):
        """
        基于记忆的递归，如果单纯的递归容易超时，因为很多都是重复计算
        """
        if n in self.f:
            return self.f[n]
        if n - 1 not in self.f:
            self.f[n - 1] = self.climbStairs(n - 1)
        if n not in self.f:
            self.f[n - 2] = self.climbStairs(n - 2)

        return self.f[n - 1] + self.f[n - 2]

    def climbStairs2(self, n):
        """
        非递归实现
        """
        if n in (1, 2):
            return n

        x, y = 1, 2
        i = 3
        while i <= n:
            x, y = y, x + y
            i += 1

        return y


if __name__ == '__main__':
    print Solution().climbStairs2(35)
