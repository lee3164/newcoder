# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    给定一个二叉树，判断其是否是一个有效的二叉搜索树。

    假设一个二叉搜索树具有如下特征：

    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
    """
    def isValidBST(self, root):
        """
        二叉搜索树中序遍历结果一定是升序
        """
        if not root:
            return True

        def helper(root, r):
            if root.left:
                helper(root.left, r)
            r.append(root.val)
            if root.right:
                helper(root.right, r)

        r = []
        helper(root, r)
        i = 1
        while i < len(r):
            if r[i] <= r[i - 1]:
                return False
            i += 1
        return True

    def isValidBST2(self, root):
        """
        完全根据性质来做。二叉树的左边所有节点都应该小于根节点，右边所有的都应该大于
        这个解法很简洁，
        """
        def helper(node, min, max):
            if not node:
                return True
            if min < node.val < max:
                return helper(node.left, min, node.val) and helper(node.right, node.val, max)
            return False

        return helper(root, min=-2 ** 63, max=2 ** 63 - 1)


if __name__ == '__main__':
    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(15)
    d = TreeNode(6)
    e = TreeNode(20)
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    print Solution().isValidBST2(a)
