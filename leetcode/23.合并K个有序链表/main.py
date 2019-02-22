# coding=utf-8
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


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


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


def generate_list(nums):
    p = q = ListNode(-1)
    for num in nums:
        q.next = ListNode(num)
        q = q.next
    return p.next


def print_list(node):
    while node:
        print node.val
        node = node.next


from collections import defaultdict, deque
from copy import copy
import string
import heapq


class Solution(object):
    """
    题目的思想就是每次得出k个链表头部最小的那个，如何得出最小的是个问题，
    第一种方式线性比较（6000ms+），第二种构建最小堆（70ms+）
    速度差别100倍左右
    """
    def get_min(self, lists):
        idx = -1
        m = 100000
        for i, node in enumerate(lists):
            if node and node.val < m:
                idx = i
                m = node.val
        return idx

    def mergeKLists(self, lists):
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        a = b = ListNode(-1)
        while True:
            idx = self.get_min(lists)
            if idx == -1:
                return a.next
            b.next = lists[idx]
            b = b.next
            lists[idx] = lists[idx].next

    def mergeKLists2(self, lists):
        a = b = ListNode(-1)
        h = [(m.val, i) for i, m in enumerate(lists) if m]
        heapq.heapify(h)
        while h:
            _, i = heapq.heappop(h)
            b.next = lists[i]
            b = b.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))

        return a.next


if __name__ == '__main__':
    a = generate_list([1, 4, 5])
    b = generate_list([2, 3, 6])
    c = generate_list([0, 9])
    d = Solution().mergeKLists2([a, b, c])
    print_list(d)
