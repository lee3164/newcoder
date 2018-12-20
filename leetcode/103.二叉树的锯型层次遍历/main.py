# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
    没啥好说的，逻辑很清晰，和普通层次遍历差别就多了一个方向控制位
    """
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        r = []
        queue = [root]
        left_order = True
        while queue:
            if left_order:
                r.append([n.val for n in queue])
            else:
                r.append([n.val for n in reversed(queue)])
            new_queue = []
            for n in queue:
                if n.left:
                    new_queue.append(n.left)
                if n.right:
                    new_queue.append(n.right)
            queue = new_queue
            left_order = not left_order
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
