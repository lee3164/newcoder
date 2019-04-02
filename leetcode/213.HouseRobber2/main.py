# coding=utf-8
class Solution(object):
    """
    同 HouseRobber，不过这里的数组是环状的，不允许0和n-1同时出现，
    分解成0~n-2 和 1~n-1的问题,
    如果不偷0， 那么1~n-1可以随便，退化成HouseRobber问题，
    如果偷0，那么n-1肯定不能，退化成 0~n-2问题
    """
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        D = [0 for _ in nums]
        for index,num in enumerate(nums):
            if index == 0:
                D[index] = num
            elif index == 1:
                D[index] = max(D[index-1],num)
            else:
                D[index] = max(D[index-2]+num,D[index-1])
        return D[-1]
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        return max(self.rob2(nums[1:]), self.rob2(nums[:-1]))
        