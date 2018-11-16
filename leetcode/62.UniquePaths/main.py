# coding=utf-8
import copy


class Solution(object):
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。
    问总共有多少条不同的路径？
    说明：m 和 n 的值均不超过 100。

    示例 1:
    输入: m = 3, n = 2
    输出: 3
    解释:
    从左上角开始，总共有 3 条路径可以到达右下角。
    1. 向右 -> 向右 -> 向下
    2. 向右 -> 向下 -> 向右
    3. 向下 -> 向右 -> 向右
   
    示例 2:
    输入: m = 7, n = 3
    输出: 28
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 简单动态规划，没啥好说的，边上的点 步数都是1，先初始化下
        f = [[1 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[m - 1][n - 1]


if __name__ == '__main__':
    print Solution().uniquePaths(7, 3)
