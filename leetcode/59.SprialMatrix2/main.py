# coding=utf-8

class Solution(object):
    """
    给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

    示例:

    输入: 3
    输出:
    [
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
    ]

    这题 和 螺旋矩阵1没啥区别，先生成矩阵，然后按照顺序输出数字即可
    """
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        a = [0, 0]
        b = [n - 1, n - 1]
        matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]
        c = 1
        while True:
            i, j = a[0], a[1]
            while j <= b[1]:
                matrix[i][j] = c
                c += 1
                j += 1

            a[0] += 1
            if a[0] > b[0]:
                break

            i, j = a[0], b[1]
            while i <= b[0]:
                matrix[i][j] = c
                c += 1
                i += 1

            b[1] -= 1
            if a[1] > b[1]:
                break

            i, j = b[0], b[1]
            while j >= a[1]:
                matrix[i][j] = c
                c += 1
                j -= 1
            b[0] -= 1
            if a[0] > b[0]:
                break

            i, j = b[0], a[1]
            while i >= a[0]:
                matrix[i][j] = c
                c += 1
                i -= 1
            a[1] += 1
            if a[1] > b[1]:
                break

        return matrix

if __name__ == '__main__':
    print Solution().generateMatrix(0)
