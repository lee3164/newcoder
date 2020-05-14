#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

链接：https://leetcode-cn.com/problems/palindrome-linked-list

解1：找到链表中点位置，然后反转中点位置，依次序比较前半段和后半段。
解2：链表如果都是小于10的数字的话，可以看做是两个数字正反比较，如果是一样的，则是回文
"""


class Solution(object):
    def reverse(self, head):
        last = None
        cur = head
        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next

        return last

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        0,1,2,3,4,5,6
        0,1,2,3,4,5
        """
        t = head
        count = 0
        while t:
            t = t.next
            count += 1

        if count <= 1:
            return True

        i = 0
        t = head
        while i != (count + 1) / 2:
            i += 1
            t = t.next

        s = head
        t = self.reverse(t)

        i = 0
        while i < count / 2:
            if s.val != t.val:
                return False
            i += 1
            s = s.next
            t = t.next

        return True

    def isPalindrome2(self, head):
        n1 = n2 = 0
        t = 1
        while head:
            n1 = 10 * n1 + head.val
            n2 = head.val * t + n2
            t *= 10
            head = head.next

        return n1 == n2


if __name__ == '__main__':
    def generate_list(nums):
        p = q = ListNode(-1)
        for num in nums:
            q.next = ListNode(num)
            q = q.next
        return p.next


    print Solution().isPalindrome2(generate_list([1, 1, 2, 1]))
