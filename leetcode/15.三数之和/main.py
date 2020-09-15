#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums = sorted(nums)
        if nums[0] > 0 or nums[-1] < 0:
            return []

        r = []
        i = 0
        while i <= len(nums) - 3 and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                if k != len(nums) - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue

                s = nums[j] + nums[k] + nums[i]
                if s == 0:
                    r.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

            i += 1

        return r


if __name__ == '__main__':
    print Solution().threeSum([0, 0, 0, 0])
