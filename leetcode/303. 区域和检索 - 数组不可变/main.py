# coding=utf-8
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        f = {-1: 0}
        for i, num in enumerate(nums):
            if i == 0:
                f[0] = num
            else:
                f[i] = f[i-1] + num
        self.f = f
    
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.f[j] - self.f[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)