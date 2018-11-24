# coding=utf-8

class Solution(object):
    """
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。

    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

    示例:
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    给定 word = "ABCCED", 返回 true.
    给定 word = "SEE", 返回 true.
    给定 word = "ABCB", 返回 false.
    """

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        vis = [[False for _ in xrange(0, n)] for _ in xrange(0, m)]

        def dfs(vis, i, j, idx):
            if idx == len(word):
                return True

            vis[i][j] = True
            # up down left right
            for (p, q) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= p < m and 0 <= q < n and not vis[p][q] and word[idx] == board[p][q]:
                    ret = dfs(vis, p, q, idx + 1)
                    if ret:
                        return ret
            vis[i][j] = False
            return False

        for i in xrange(0, m):
            for j in xrange(0, n):
                if word[0] == board[i][j] and dfs(vis, i, j, 1):
                    return True
        return False


if __name__ == '__main__':
    print Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "SEE")
