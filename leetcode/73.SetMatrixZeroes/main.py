# coding=utf-8

class Solution(object):
    """
    给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

    示例 1:

    输入: 
    [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
    输出: 
    [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]
    示例 2:

    输入: 
    [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
    输出: 
    [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
    ]
    进阶:

    一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
    一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
    你能想出一个常数空间的解决方案吗？
    """
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()

        for i in xrange(0, m):
            for j in xrange(0, n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for col in xrange(0, n):
                matrix[row][col] = 0

        for col in cols:
            for row in xrange(0, m):
                matrix[row][col] = 0

    def setZeroes2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 更慢
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()

        for i in xrange(0, m):
            for j in xrange(0, n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                elif i in rows or j in cols:
                    matrix[i][j] = 0
                else:
                    p = i + 1
                    q = j + 1
                    while p < m:
                        if matrix[p][j] == 0:
                            matrix[i][j] = 0
                            cols.add(j)
                            break
                        p += 1

                    while q < n:
                        if matrix[i][q] == 0:
                            matrix[i][j] = 0
                            rows.add(i)
                            break
                        q += 1


if __name__ == '__main__':
    a = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(a)
    print a
