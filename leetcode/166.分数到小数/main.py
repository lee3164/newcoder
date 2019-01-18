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
    给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

难度不大，唯一需要注意的是 负数情况，因此都转化成绝对值在算
    """
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator / denominator)

        s = {}
        r1 = []
        if numerator * denominator < 0:
            r1.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        r1.append(str(numerator / denominator))
        r1.append(".")
        a = numerator % denominator
        i = len(r1)
        while True:
            s[a] = i
            i += 1
            r1.append(str(a * 10 / denominator))
            a = a * 10 % denominator
            if a == 0:
                break
            if a in s:
                r1.insert(s[a], "(")
                r1.append(")")
                break

        return "".join(r1)


if __name__ == '__main__':
    print Solution().fractionToDecimal(-50, 8)
