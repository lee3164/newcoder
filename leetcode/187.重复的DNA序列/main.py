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
    所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

    编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。

    示例:

    输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

    输出: ["AAAAACCCCC", "CCCCCAAAAA"]
    """
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        str_count = {}
        for i in xrange(0, len(s) - 9):
            str_count.setdefault(s[i:i + 10], 0)
            str_count[s[i:i + 10]] += 1

        return [k for k, v in str_count.iteritems() if v > 1]


if __name__ == '__main__':
    print Solution().findRepeatedDnaSequences("AAAAAAAAAAA")