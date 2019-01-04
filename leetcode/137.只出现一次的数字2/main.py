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
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

很好的思路，按位进行比较，每一位不是0就是1，如果该位出现了3n次，那么说明那个单独的数字该位不是1，否则该位就是1，
如 1，1，1，2 对应二进制则是 01,01,01,10，第一位有3个1，第二位只有1个1
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            s = 0
            for num in nums:
                if (num >> i) & 1:
                    s += 1
            if s % 3 == 1:
                res |= (1 << i)

        # python的坑，1 << 32 在c/c++中按照位运算定义会溢出 变成一个负数，但是python里面没有这个限制，
        # 因此这里做下判断，int的范围应该是 -2^31 - 2^31-1，所以当超过2^31次方后应该要减回来
        if res >= 2 ** 31:
            res -= 2 ** 32

        return res


if __name__ == '__main__':
    print Solution().singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
