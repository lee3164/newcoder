#!/usr/bin/env python
# coding=utf-8
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor_list = defaultdict(list)
        st = [root]
        p_found = False
        q_found = False
        while st:
            n = st.pop()
            ancestor_list[n.val].append(n)

            if n.val == p.val:
                p_found = True
            elif n.val == q.val:
                q_found = True

            if p_found and q_found:
                break

            l = n.left
            r = n.right

            if r:
                ancestor_list[r.val].extend(ancestor_list[n.val])
                st.append(r)
            if l:
                ancestor_list[l.val].extend(ancestor_list[n.val])
                st.append(l)

        p_list = ancestor_list[p.val]
        q_list = ancestor_list[q.val]

        last = None
        i = 0
        while i < len(p_list) and i < len(q_list):
            if p_list[i] != q_list[i]:
                break
            last = p_list[i]
            i += 1

        return last


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
