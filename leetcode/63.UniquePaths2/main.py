# coding=utf-8
import copy


class Solution(object):
    """
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

    网格中的障碍物和空位置分别用 1 和 0 来表示。

    说明：m 和 n 的值均不超过 100。

    示例 1:
    输入:
    [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    输出: 2
    解释:
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右
    """
    def uniquePaths(self, obstacleGrid):
        # 如果第一个就是障碍物，不用继续算了
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        f = [[1 for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(0, m):
            for j in xrange(0, n):
                # 如果遇到障碍物，当前位置直接是0
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                    continue

                # 第一个元素是障碍物在前面已经处理了，此处直接赋值
                if i == 0 and j == 0:
                    f[i][j] = 1
                elif i == 0:
                    f[i][j] = f[i][j - 1] # 最上面的行
                elif j == 0:
                    f[i][j] = f[i - 1][j] # 最左边的列
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]  # 一般情况

        return f[m - 1][n - 1]


if __name__ == '__main__':
    print Solution().uniquePaths([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ])
