# coding=utf-8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = {}
        f[0] = nums[0]
        m = f[0]
        i = 1
        while i < len(nums):
            if f[i - 1] + nums[i] > nums[i]:
                f[i] = f[i - 1] + nums[i]
            else:
                f[i] = nums[i]

            if f[i] > m:
                m = f[i]

            i += 1

        return m


if __name__ == '__main__':
    print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
