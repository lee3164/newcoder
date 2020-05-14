#!/usr/bin/env python
# coding=utf-8

"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree

解1：这个比较简单，回想下二叉搜索树的特性就能想到。如果p,q分布在两侧，那么公共节点一定是root，如果p,q分布在左或右，
那么公共节点一定在左或右里面，可以递归。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


if __name__ == '__main__':
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


    print Solution().lowestCommonAncestor(generate_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 8)
