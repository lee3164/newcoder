#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

链接：https://leetcode-cn.com/problems/reverse-nodes-in-klast_tail-group

# 单纯的模拟执行即可，需要注意的是需要保存上次的尾结点和下次的头结点。每k次需要翻转长度为k的链表，因此需要翻转 n/k 次
每次翻转的时间复杂度为k，因此总体时间复杂度是 o(n), 空间复杂度 o(1)
"""


class Solution(object):
    def reverse(self, start, end):
        tail = start
        last = None
        while start != end:
            next = start.next
            start.next = last
            last = start
            start = next
        return last, tail

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = None
        last_tail = None
        t = head
        while t:
            i = 0
            p = t
            while i < k and p:
                p = p.next
                i += 1

            if p:
                s, e = self.reverse(t, p)
            else:
                s, e = t, None

            t = p

            if not new_head:
                new_head = s

            if last_tail:
                last_tail.next = s
                last_tail = e

        return new_head
