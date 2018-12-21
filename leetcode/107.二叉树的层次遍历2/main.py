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


class Solution(object):
    """
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
    没啥意义的题目，得到层次遍历然后反转一下
    """
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        r = []
        while q:
            r.append([n.val for n in q])
            new_q = []
            for n in q:
                if n.left:
                    new_q.append(n.left)
                if n.right:
                    new_q.append(n.right)
            q = new_q

        return [i for i in reversed(r)]

if __name__ == '__main__':
    pass
