# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    给定一个已排序链表，删除所有的重复节点，只保留原始链表中独特的数字。

    例如， 
    给定 1->2->3->3->4->4->5, 返回 1->2->5. 
    给定 1->1->1->2->3, 返回 2->3.

    此类需要保留parent指针的单链表感觉都可以插入一个头部虚拟节点来达到目的，谨记
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 插入一个虚拟节点，无论头部怎么变化，dummy.next一定是头
        dummy = ListNode(-1)
        dummy.next = head

        # p是parent节点，q是待查看是否重复的节点
        p = dummy
        q = head
        while q:

            # 通过s检查重复，如果s==q，说明没有重复，这个节点不需要去掉，因此将p=q，下次q就是父节点
            # 否则，移除所有的相同节点
            s = q
            while s.next and s.next.val == s.val:
                s = s.next

            if s == q:
                p = q
            else:
                p.next = s.next

            q = s.next

        return dummy.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(3)
    f = ListNode(3)
    g = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    Solution().deleteDuplicates(a)
