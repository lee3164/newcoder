# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_tree(nums):
    if not nums:
        return None
    nodes = []
    for num in nums:
        if num is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(num))

    p_idx = 0
    c_idx = 1
    while c_idx < len(nodes):
        if nodes[p_idx]:
            nodes[p_idx].left, nodes[p_idx].right = nodes[c_idx:c_idx + 2]
        p_idx += 1
        c_idx += 2

    return nodes[0]


from collections import defaultdict
from copy import copy
import string


class Solution(object):
    """
    给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        visited = set()
        i = 0
        m, n = len(board), len(board[0])
        while i < m:
            j = 0
            while j < n:
                q = [(i, j)]
                l = []
                flag = True
                while q:
                    new_q = []
                    for x, y in q:
                        if (x, y) in visited or board[x][y] == "X":
                            continue
                        visited.add((x, y))
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            flag = False
                        if x > 0:
                            new_q.append((x - 1, y))
                        if x < m - 1:
                            new_q.append((x + 1, y))
                        if y > 0:
                            new_q.append((x, y - 1))
                        if y < n - 1:
                            new_q.append((x, y + 1))
                        l.append((x, y))
                    q = new_q
                if flag:
                    for x, y in l:
                        board[x][y] = "X"
                j += 1
            i += 1


if __name__ == '__main__':
    b = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]]
    print Solution().solve(b)
    print b
