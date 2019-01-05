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
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

设f[i] 是 i金额下的最小兑换次数，那么对于所有的面值coin，一个个看f[i-coin]是否存在最小兑换次数，
找到所有的coins中f[i-coin]最小的就能确定f[i]
    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = {0: 0}
        coins = sorted(coins, reverse=True)
        for i in xrange(coins[-1], amount + 1):
            for coin in coins:
                left = i - coin
                if left >= 0 and left in f:
                    if i not in f:
                        f[i] = f[left] + 1
                    else:
                        f[i] = min(f[left] + 1, f[i])

        return f.get(amount, -1)


if __name__ == '__main__':
    print Solution().coinChange([186, 419, 83, 408],
                                6249)
