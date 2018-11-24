# coding=utf-8
import copy


class Solution(object):
    """
    求子集
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        size = len(nums)

        r = []
        while i < 2 ** size:
            p = i
            j = 0
            k = []
            while p > 0:
                if p & 1 == 1:
                    k.append(nums[j])
                j += 1
                p >>= 1
            r.append(k)
            i += 1
        return r


if __name__ == '__main__':
    print Solution().subsets([1, 2])
