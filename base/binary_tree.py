#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 下午5:20
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals


def pre_order(root):
    r = []
    st = []
    while root or st:
        if not root:
            root = st.pop()
        else:
            r.append(root.val)
            st.append(root.right)
            root = root.left
    return r


def pre_order2(root):
    if not root:
        return []
    r = []
    st = [root]
    while st:
        node = st.pop()
        r.append(node.val)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)


def in_order(root):
    r = []
    st = []
    while root or st:
        if not root:
            root = st.pop()
            r.append(root.val)
            root = root.right
        else:
            st.append(root)
            root = root.left

    return r


def post_order(root):
    """
    后序遍历是 左右根，也就是 根右左 反过来
    """
    if not root:
        return []
    r = []
    st = [root]
    while st:
        node = st.pop()
        r.append(node.val)
        if node.left:
            st.append(node.left)
        if node.right:
            st.append(node.right)

    return r[::-1]


def post_order2(root):
    """
    正常的，用一个 pre保存上一个遍历的对象，如果是当前的子节点，那么说明子节点已经遍历过了，说明
    不需要继续遍历了，可以将当前的节点pop出去
    """
    pre = None
    r = []
    st = [root]
    while st:
        node = root[-1]
        if (node.left is None and node.right is None) or (pre is not None and (node.left == pre or node.right == pre)):
            r.append(node.val)
            st.pop()
            pre = node
        else:
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
    return r
