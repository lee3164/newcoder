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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(root):
            if not root:
                return True, 0

            left_is_balanced, left_height = helper(root.left)
            right_is_balanced, right_height = helper(root.right)
            if left_is_balanced and right_is_balanced and 0 <= abs(left_height - right_height) <= 1:
                return True, max(left_height, right_height) + 1
            return False, -1

        ret, _ = helper(root)
        return ret


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)
    a.left = b
    a.right = c
    c.left = d
    c.right = e

    p = TreeNode(1)
    q = TreeNode(2)
    p.left = q
    print Solution().isBalanced(p)
