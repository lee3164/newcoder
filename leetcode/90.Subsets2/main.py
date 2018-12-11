# coding=utf-8
from copy import copy


class Solution(object):
    """
    给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。

    示例:
    输入: [1,2,2]
    输出:
    [
        [2],
        [1],
        [1,2,2],
        [2,2],
        [1,2],
        []
    ]
    依次是DP的方法，先 排序一下，然后 针对 重复元素如1，2，2这样的
    如果2使用过一次了就不应该在继续用了，如何判断使用过，当前和前面的数比较，一样的代表使用过，
    但是 需要判断是否是这一轮第一次使用，如果是第一次使用，不用比较
    
    """
    def subsetsWithDup(self, nums):
        """
        :type nums: list[int]
        :rtype: list[list[int]]
        """
        nums.sort()
        def dfs(r, l, i):
            # type: (list[int], list[int], int) -> None
            r.append(copy(l))
            j = i
            while j < len(nums):
                if j != i and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                l.append(nums[j])
                dfs(r, l, j + 1)
                l.pop()
                j += 1
        r = []
        dfs(r, [], 0)
        return r


if __name__ == '__main__':
    print Solution().subsetsWithDup([1, 3, 2])
