#!/usr/bin/env python
# coding=utf-8

"""
给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。

请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。

树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
"""


class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        self.parent = parent
        self.cache = {}

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        if (node, k) in self.cache:
            return self.cache[(node, k)]

        origin_node = node
        origin_k = k
        while k > 0 and node != -1:
            node = self.parent[node]
            k -= 1
            self.cache[(origin_node, origin_k - k)] = node

        return node


if __name__ == '__main__':
    t = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print t.getKthAncestor(3, 1)
    print t.getKthAncestor(5, 2)
    print t.getKthAncestor(6, 3)
