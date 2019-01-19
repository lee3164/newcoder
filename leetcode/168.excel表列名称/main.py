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
    给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

N = A(n)*26^n + A(n-1)*26^n-1 + ... + A(0)*26^0
取余可以得到最后一位，然后看他在1-26的第几个位置，因为要取26余数，且A-Z => 1-26,所以要先减一
取余完成之后 N = N / 26 = A(n)*26^n + A(n-1)*26^n-1 + ... + A(1)*26^0
重复上述过程
    """
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = []
        while n != 0:
            n -= 1
            a = n % 26
            r.append(chr(ord('A') + a))
            n /= 26
        return "".join(reversed(r))


if __name__ == '__main__':
    print Solution().convertToTitle(17576)
