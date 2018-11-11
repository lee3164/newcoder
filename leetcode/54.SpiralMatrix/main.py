# coding=utf-8

class Solution(object):
    """
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

    示例 1:
    输入:
    [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]
    输出: [1,2,3,6,9,8,7,4,5]

    示例 2:
    输入:
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    输出: [1,2,3,4,8,12,11,10,9,5,6,7]
    """
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        a = [0, 0]  # 记录左上角的坐标
        b = [len(matrix) - 1, len(matrix[0]) - 1]  # 记录右下角的坐标
        r = []

        while True:

            # 遍历最上面的行
            i, j = a[0], a[1]
            while j <= b[1]:
                r.append(matrix[i][j])
                j += 1

            # 遍历完成后将a[0] + 1，因为已经遍历过了
            # 并判断当前是否要退出
            a[0] += 1
            if a[0] > b[0]:
                break

            # 遍历最右边的列
            i, j = a[0], b[1]
            while i <= b[0]:
                r.append(matrix[i][j])
                i += 1

            b[1] -= 1
            if b[1] < a[1]:
                break

            # 遍历最下面的行
            i, j = b[0], b[1]
            while j >= a[1]:
                r.append(matrix[i][j])
                j -= 1

            b[0] -= 1
            if b[0] < a[0]:
                break

            # 遍历最左边的列
            i, j = b[0], a[1]
            while i >= a[0]:
                r.append(matrix[i][j])
                i -= 1

            a[1] += 1
            if a[1] > b[1]:
                break

        return r


if __name__ == '__main__':
    a = [
        [2, 5, 8],
        [4, 0, 1]
    ]
    print Solution().spiralOrder(a)
