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


class Solution(object):
    """
    给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

    dfs遍历，每次返回包含 节点的最大路径和（root+left 或者 root+right，因为一条路径不能分叉），
    和该节点中的最大路径和（可能包含该节点，也可能不包含）
    """
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root):
            if not root:
                return -float("inf"), -float("inf")

            l1, l2 = dfs(root.left)
            r1, r2 = dfs(root.right)
            m = n = root.val
            if l1 > 0:
                n += l1
            if r1 > 0:
                n += r1

            return max(m, m + l1, m + r1), max(n, l2, r2)

        return dfs(root)[1]


if __name__ == '__main__':
    root = generate_tree([-10, 9, 20, None, None, 15, 7])
    print Solution().maxPathSum(root)
