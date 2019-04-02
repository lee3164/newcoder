class Solution(object):
    """
    在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4

设f[i,j]表示以i,j为右下角的能够成正方形的边长，
    """
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        f = [[0 for _ in xrange(n)] for _ in xrange(m)]
        t = 0
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    f[i][j] = int(matrix[i][j])
                else:
                    f[i][j] = min(int(f[i - 1][j]), int(f[i][j - 1]), int(f[i - 1][j - 1])) + 1
                t = max(t, f[i][j])
        return t * t