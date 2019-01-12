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
    给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

    示例 1:
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。

    示例 2:
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
    
    动态规划思想，因为存在负数，比如[-1，-1]这个序列，最大是1。
    因此我们需要用两个dp数组，一个保存当前乘积的最大值，一个保存当前乘积的最小值
    """
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f1 = [num for num in nums]
        f2 = [num for num in nums]
        m = f1[0]
        for i in xrange(1, len(nums)):
            a = f1[i - 1] * nums[i]
            b = f2[i - 1] * nums[i]

            f1[i] = max(a, b, nums[i])
            f2[i] = min(a, b, nums[i])

            m = max(m, f1[i])
        return m


if __name__ == '__main__':
    print Solution().maxProduct([2,-5,-2,-4,3])
