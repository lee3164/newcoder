# coding=utf-8

class Solution(object):
    """
    编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
    示例 1:

    输入:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 3
    输出: true
    示例 2:

    输入:
    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 13
    输出: false

    简单的二分查找，只不过每次要算出坐标取值比较
    """
    def get_row_col(self, idx, n):
        return idx / n, idx % n

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        s = 0
        e = m * n - 1
        while s <= e:
            m = (s + e) / 2
            i, j = self.get_row_col(m, n)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                s = m + 1
            else:
                e = m - 1

        return False


if __name__ == '__main__':
    a = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print Solution().searchMatrix(a, 3)
