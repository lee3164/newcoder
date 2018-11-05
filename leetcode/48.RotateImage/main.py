# coding=utf-8
import copy


class Solution(object):
    """
    给定一个 n × n 的二维矩阵表示一个图像。
    将图像顺时针旋转 90 度。

    说明：
    你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

    示例 1:
    给定 matrix = 
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    原地旋转输入矩阵，使其变为:
    [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    示例 2:
    给定 matrix =
    [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ], 
    原地旋转输入矩阵，使其变为:
    [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]

    这题主要找旋转规律
    """
    def find_next_position(self, n, i, j):
        return j, n - 1 - i

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rotated_pos = set()
        num = len(matrix)
        for i in xrange(0, num):
            for j in xrange(0, num):
                if (i, j) in rotated_pos:
                    continue
                val = matrix[i][j]
                p, q = i, j
                while True:
                    m, n = self.find_next_position(num, p, q)
                    rotated_pos.add((m, n))
                    # 开始是这样写的，本意是想把 m，n的值保存到val，然后把上一轮的val赋值给p,q
                    # val = matrix[m][n]
                    # matrix[m][n] = val

                    t = matrix[m][n]
                    matrix[m][n] = val
                    val = t
                    if (m, n) == (i, j):
                        break
                    p, q = m, n

    def rotate2(self, matrix):
        """
        1  2  3           1  4  7          7  4  1
        4  5  6    ==>    2  5  8   ==>    8  5  2
        7  8  9           3  6  9          9  6  3
        第一步，根据对角线，找对应位置，互换两个数字的值。
        第二步，对每一行数字，根据中线左右翻转。
        """
        n = len(matrix)
        for i in xrange(1, n):  # 从第一行开始
            for j in xrange(0, i):  # 对角线是 n,n
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in xrange(0, n):
            matrix[i] = list(reversed(matrix[i]))


if __name__ == '__main__':
    a = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    Solution().rotate2(a)
    print a
