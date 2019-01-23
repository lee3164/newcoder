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


from collections import defaultdict, deque
from copy import copy
import string


class Solution(object):
    """
    给定一个整数 n，返回 n! 结果尾数中零的数量。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.

    怎么才会产生0，2和5相乘，本质上这个题目就是找n阶乘中2*5的个数，根据观察很容易得到5的数目比2的数目少，所以题目
    本质上是找n阶乘中有多少个5，首先如果是5的倍数会产生1个5，25的倍数2个5，
    对于5^i会产生i个5，因此需要去不断找5^i的个数，第一种写法就是这样，很容易理解，第二种是一个变体，和一本质一样
    """
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        tot = 0
        i = 1
        while 5 ** i <= n:
            tot += (n / 5 ** i)
            i += 1

        return tot

    def trailingZeroes2(self, n):
        tot = 0
        while n > 0:
            n = n / 5
            tot += n
        return tot

if __name__ == '__main__':
    print Solution().trailingZeroes2(100)
