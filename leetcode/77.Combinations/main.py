# coding=utf-8
import copy

class Solution(object):
    """
    给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

    示例:

    输入: n = 4, k = 2
    输出:
    [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
    ]
    """
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        r = []

        def dfs(s, nums, r):
            if k == len(nums):
                r.append(copy.copy(nums))
                return
            for i in xrange(s, n + 1):
                nums.append(i)
                dfs(i + 1, nums, r)
                nums.pop()

        # 从1开始排列
        dfs(1, [], r)
        return r


if __name__ == '__main__':
    print Solution().combine(4, 2)
