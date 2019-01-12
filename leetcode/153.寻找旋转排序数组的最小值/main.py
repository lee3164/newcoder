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
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。

    (例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2])。

    请找出其中最小的元素。

    你可以假设数组中不存在重复元素。

    示例 1:

    输入: [3,4,5,1,2]
    输出: 1
    示例 2:

    输入: [4,5,6,7,0,1,2]
    输出: 0

    特殊情况 [7,0]这样的
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while True:
            m = (l + r) / 2
            if nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m
            else:
                return nums[l]


if __name__ == '__main__':
    print Solution().findMin([7, 0])
