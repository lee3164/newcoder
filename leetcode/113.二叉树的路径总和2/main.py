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

import copy
class Solution(object):
    """
    给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        def helper(root, sum, r, l):
            # 不管如何，每次都需要append当前节点的值
            l.append(root.val)
            if root.val == sum and not root.left and not root.right:
                r.append(copy.copy(l))

            # 下面的两个判断条件如果是叶子节点是不会进入的，也就是说，
            # 如果sum条件满足也进入不到下面
            if root.left:
                helper(root.left, sum - root.val, r, l)
            if root.right:
                helper(root.right, sum - root.val, r, l)
            l.pop()

        r = []
        helper(root, sum, r, [])
        return r


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)

    p = TreeNode(-2)
    q = TreeNode(-3)
    p.right = q
    print Solution().hasPathSum(p, -5)
