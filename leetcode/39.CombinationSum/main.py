# coding=utf-8
import copy

class Solution(object):
    """
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的数字可以无限制重复被选取。

    说明：

    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。 
    示例 1:

    输入: candidates = [2,3,6,7], target = 7,
    所求解集为:
    [
    [7],
    [2,2,3]
    ]
    示例 2:

    输入: candidates = [2,3,5], target = 8,
    所求解集为:
    [
    [2,2,2,2],
    [2,3,3],
    [3,5]
    ]
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        vec = []
        candidates = sorted(candidates)
        self.solve(candidates, target, 0, res, vec)
        return res

    def solve(self, candidates, target, sum, res, vec):
        if sum == target:
            res.append(copy.copy(vec))
            return
        for c in candidates:
            if vec and c < vec[-1]:
                continue
            if c > target - sum:
                return
            vec.append(c)
            sum += c
            self.solve(candidates, target, sum, res, vec)
            vec.pop()
            sum -= c


if __name__ == '__main__':
    print Solution().combinationSum([8, 7, 4, 3], 11)
