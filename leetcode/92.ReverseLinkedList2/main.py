# coding=utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

    说明:
    1 ≤ m ≤ n ≤ 链表长度。

    示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL

    先反转 m-n位置的链表，然后重新连接下 这部分的头尾
    """
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if n == m:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = head
        for _ in xrange(0, m - 1):
            p = p.next
            q = q.next

        i = q
        j = q.next
        k = q.next.next
        idx = 0
        while idx < (n - m) and j is not None:
            j.next = i
            i = j
            j = k
            k = k.next if k else None
            idx += 1

        p.next.next = j
        p.next = i
        return dummy.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    print Solution().reverseBetween(a, 2, 5)
