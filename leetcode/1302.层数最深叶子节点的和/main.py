#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。

示例：

输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15

链接：https://leetcode-cn.com/problems/deepest-leaves-sum

层次遍历，没啥好说的
"""


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        while q:
            new_q = []
            s = 0
            for n in q:
                s += n.val
                if n.left:
                    new_q.append(n.left)
                if n.right:
                    new_q.append(n.right)
            if not new_q:
                return s
            q = new_q
