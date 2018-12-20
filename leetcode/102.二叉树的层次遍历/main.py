# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        r = []
        queue = [root]
        while queue:
            r.append([n.val for n in queue])
            new_queue = []
            for n in queue:
                if n.left:
                    new_queue.append(n.left)
                if n.right:
                    new_queue.append(n.right)
            queue = new_queue
        return r


if __name__ == '__main__':
    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(15)

    d = TreeNode(10)
    e = TreeNode(5)
    f = TreeNode(15)
    a.left = b
    a.right = c

    d.left = e
    e.right = f
    print Solution().isSymmetric(a)
