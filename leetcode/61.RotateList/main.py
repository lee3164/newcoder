# coding=utf-8
import copy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

    示例 1:
    输入: 1->2->3->4->5->NULL, k = 2
    输出: 4->5->1->2->3->NULL
    解释:
    向右旋转 1 步: 5->1->2->3->4->NULL
    向右旋转 2 步: 4->5->1->2->3->NULL
    
    示例 2:
    输入: 0->1->2->NULL, k = 4
    输出: 2->0->1->NULL
    解释:
    向右旋转 1 步: 2->0->1->NULL
    向右旋转 2 步: 1->2->0->NULL
    向右旋转 3 步: 0->1->2->NULL
    向右旋转 4 步: 2->0->1->NULL

    """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        l = 0
        p = head
        while p.next:
            l += 1
            p = p.next

        p.next = head
        step = (l + 1) - k % (l + 1)

        # 这里是根据头结点算，找到了头结点还要遍历一遍才能找到尾部节点 
        while step > 0:
            head = head.next
            step -= 1

        p = head
        while l > 0:
            p = p.next
            l -= 1

        p.next = None
        return head

    def rotateRight2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        l = 0
        p = head
        while p.next:
            l += 1
            p = p.next

        p.next = head
        step = (l + 1) - k % (l + 1)

        # 此处变为 找 尾部节点，因为 尾部节点找到了就能找到头节点
        while step > 0:
            p = p.next
            step -= 1

        head = p.next
        p.next = None
        return head


if __name__ == '__main__':
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)

    a.next = b
    b.next = c
    c.next = None

    print Solution().rotateRight2(a, 4)
    # Solution().next_permutation([1,4,3,2])
