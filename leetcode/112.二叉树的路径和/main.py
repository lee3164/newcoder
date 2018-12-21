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
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

理解清楚题意的情况下进行优化，不一定全是正数，可能是都有，如果当前节点已经大于等于sum，
也要继续往下层，因为可能存在负数。还有注意是到叶子节点的和
    """
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        q = [root]
        while q:
            new_q = []
            for n in q:
                if n.val == sum and not n.left and not n.right:
                    return True
                if n.left:
                    n.left.val += n.val
                    new_q.append(n.left)
                if n.right:
                    n.right.val += n.val
                    new_q.append(n.right)
            q = new_q
        return False

    def hasPathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root==None:
            return False
        elif root.left==None and root.right==None:
            return root.val==sum
        elif root.left==None:
            return self.hasPathSum(root.right, sum-root.val)
        elif root.right==None:
            return self.hasPathSum(root.left, sum-root.val)
        else:
            return self.hasPathSum(root.right, sum-root.val) or self.hasPathSum(root.left, sum-root.val)
        


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
