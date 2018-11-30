# coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
    你应当保留两个分区中每个节点的初始相对位置。

    示例:
    输入: head = 1->4->3->2->5->2, x = 3
    输出: 1->2->2->4->3->5

    分成两个链表，其中一个存小于的，一个存大于等于的，然后合起来
    """
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        l = ListNode(-1)
        r = ListNode(-1)
        lh, rh = l, r

        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next

        l.next = rh.next

        # 前面的都不是太复杂，这一句尤为重要，举个例子，1，4，3，2，5，2，执行到这里的情况
        # l链表，1，2，2，r链表，4，3，5
        # l链表的最后的2肯定是指向None的，因为是最后一位，但是r链表的5却还是指向2，那么此时就有了问题，
        # 本来5应该是最后一位的
        e.next = None
        return lh.next


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    f = ListNode(2)
    # g = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # f.next = g
    Solution().partition(a, 3)
