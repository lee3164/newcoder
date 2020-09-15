#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        left_res = self.binaryTreePaths(root.left)
        right_res = self.binaryTreePaths(root.right)

        res = []
        for r in left_res + right_res:
            res.append("{}->{}".format(root.val, r))

        if not res:
            res.append("{}".format(root.val))

        return res
