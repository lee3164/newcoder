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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while head:
            next = head.next
            p = dummy
            c = dummy.next
            while c and head.val >= c.val:
                c = c.next
                p = p.next
            p.next = head
            head.next = c
            head = next
        return dummy.next


if __name__ == '__main__':
    a = ListNode(5)
    b = ListNode(4)
    c = ListNode(3)
    a.next = b
    b.next = c

    print Solution().insertionSortList(a)
