#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 下午11:56
# @Email   : lixiaoyu@bytedance.com
from __future__ import absolute_import, unicode_literals
from base.util import ListNode

class Solution(object):
    """
    删除链表中等于给定值 val 的所有节点。

    示例:

    输入: 1->2->6->3->4->5->6, val = 6
    输出: 1->2->3->4->5

    """
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = q = ListNode(-1)
        p.next = head
        while head:
            if head.val == val:
                p.next = head.next
            else:
                p = p.next
            head = head.next
        return q.next