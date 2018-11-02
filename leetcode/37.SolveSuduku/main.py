# coding=utf-8

class Solution(object):
    """
    编写一个程序，通过已填充的空格来解决数独问题。

    一个数独的解法需遵循如下规则：

    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
    空白格用 '.' 表示。

    示例 1:
    输入:
    [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    输出: true

    示例 2:
    输入:
    [
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    输出: false
    解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
         但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。

    说明:
    给定的数独序列只包含数字 1-9 和字符 '.' 。
    你可以假设给定的数独只有唯一解。
    给定数独永远是 9x9 形式的。

    利用回溯法，找到一个就ok ；
    """

    def get_grid_index(self, i, j):
        return i / 3 * 3 + j / 3

    def find_numbers(self, i, j, row, col, grid):
        nums = []
        for num in xrange(1, 10):
            if not row[i][num] and not col[j][num] and not grid[self.get_grid_index(i, j)][num]:
                nums.append(num)
        return nums

    def get_next_i_j(self, board, i, j):
        while board[i][j] != '.':
            if 0 <= j < 8:
                j += 1
            else:
                i += 1
                j = 0
            if i == 9:
                break
        return i, j

    def solve(self, board, i, j, row, col, grid):
        if i == 9:
            return True

        nums = self.find_numbers(i, j, row, col, grid)
        if not nums:
            return False
        for num in nums:
            num = int(num)
            row[i][num] = True
            col[j][num] = True
            grid[self.get_grid_index(i, j)][num] = True
            board[i][j] = str(num)

            p, q = self.get_next_i_j(board, i, j)
            if self.solve(board, p, q, row, col, grid):
                return True
            row[i][num] = False
            col[j][num] = False
            grid[self.get_grid_index(i, j)][num] = False
            board[i][j] = '.'

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """
        row = [[False for _ in xrange(0, 10)] for _ in xrange(0, 9)]
        col = [[False for _ in xrange(0, 10)] for _ in xrange(0, 9)]
        grid = [[False for _ in xrange(0, 10)] for _ in xrange(0, 9)]

        for i in xrange(0, 9):
            for j in xrange(0, 9):
                num = board[i][j]
                if num == '.':
                    continue
                num = int(num)
                print i, j, num
                row[i][num] = True
                col[j][num] = True
                grid[self.get_grid_index(i, j)][num] = True

        i, j = self.get_next_i_j(board, 0, 0)
        self.solve(board, i, j, row, col, grid)


if __name__ == '__main__':
    a = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(a)
    import json
    for row in a:
        print json.dumps(row)