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
    给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。


    比较字符串的数字 a+b和b+a哪个更大

    当所有的数字都是0的时候是比较坑的，需要注意，不能返回 '00'这种
    """

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not any(nums):
            return '0'

        nums = [str(num) for num in nums]

        def sort_cmp_func(num1, num2):
            if num1 == num2:
                return 0
            if num1 + num2 > num2 + num1:
                return 1
            return -1

        nums.sort(cmp=sort_cmp_func, reverse=True)
        return "".join(nums)

    def largestNumber2(self, nums):
        """
        非常简洁的写法，mark一下
        """
        nums = map(str, nums)
        nums.sort(cmp=lambda a, b: 1 if a + b < b + a else -1)
        nums = ''.join(nums)
        return '0' if nums[0] == '0' else nums


if __name__ == '__main__':
    print Solution().largestNumber([3, 30, 34, 5, 9])
    print Solution().largestNumber([0, 0, 0])
    print Solution().largestNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print Solution().largestNumber([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247])
