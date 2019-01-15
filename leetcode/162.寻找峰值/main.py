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
    峰值元素是指其值大于左右相邻值的元素。

    给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

    数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

    你可以假设 nums[-1] = nums[n] = -∞。

    示例 1:

    输入: nums = [1,2,3,1]
    输出: 2
    解释: 3 是峰值元素，你的函数应该返回其索引 2。
    示例 2:

    输入: nums = [1,2,1,3,5,6,4]
    输出: 1 或 5 
    解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6
     感觉这题没啥意义
    """
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def find(s, e):
            if s > e:
                return -1
            m = (s + e) / 2
            if (m == 0 and nums[m] > nums[m + 1]) or (m == len(nums) - 1 and nums[m] > nums[m - 1]) or \
                    (nums[m] > nums[m - 1] and nums[m] > nums[m + 1]):
                return m

            i = find(s, m - 1)
            if i != -1:
                return i
            return find(m + 1, e)

        return find(0, len(nums) - 1)


if __name__ == '__main__':
    print Solution().findPeakElement([1, 2])
