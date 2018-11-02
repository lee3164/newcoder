# coding=utf-8
import copy


class Solution(object):
    """
    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的每个数字在每个组合中只能使用一次。

    说明：

    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。 
    示例 1:

    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
    ]
    示例 2:

    输入: candidates = [2,5,2,1,2], target = 5,
    所求解集为:
    [
    [1,2,2],
    [5]
    ]
    """
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        vec = []
        self.dfs(candidates, target, 0, res, vec)
        return res

    def dfs(self, candidates, target, idx, res, vec):
        if target == 0:
            res.append(copy.copy(vec))
            return

        while idx < len(candidates):
            if target < candidates[idx]:
                return
            vec.append(candidates[idx])
            self.dfs(candidates, target - candidates[idx], idx + 1, res, vec)
            vec.pop()

            # 此处很重要，类似[1,2,2,2,5] 这样的，如果不加这一行会出现几个 1，2，2，
            # 此处的含义是如果下一个和上一个相同，那么不用重复加入
            idx += 1
            while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                idx += 1


if __name__ == '__main__':
    print Solution().combinationSum2([2, 5, 2, 1, 2], 5)
