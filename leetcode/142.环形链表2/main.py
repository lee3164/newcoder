class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


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


from collections import defaultdict
from copy import copy
import string


class Solution(object):
    """
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    说明：不允许修改给定的链表。

    设起始位置到入环的长度为a，环长度为b，设环起点到相逢位置为c
    则相逢的时候slow走了 a+c步，而fast速度是两倍，即走了2(a+c)，而另一点可以得出，相逢的时候
    fast比slow多走了一圈，因此走了a+b+c，可以推出 2(a+c) = a+b+c => a = b - c，
    当fast和slow相遇的时候，slow正好走了在环上走了c步，正好在走 b-c步就走了一圈，也就是到了环的起点，
    而链表起点到环起点是a=b-c步，此时设置另外一个指针，同时走，相遇的时候就是环起点
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast != slow:
                continue
            a = head
            b = slow
            while a != b:
                a = a.next
                b = b.next

            return a
        return None


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    Solution().detectCycle(a)
