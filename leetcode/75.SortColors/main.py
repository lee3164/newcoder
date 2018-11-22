# coding=utf-8

class Solution(object):
    """
    0,1,2三种颜色排序后输出
    """
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = [0, 0, 0]
        for num in nums:
            a[num] += 1

        i = 0
        for idx, count in enumerate(a):
            nums[i:i + count] = [idx for _ in xrange(count)]
            i += count

    def sortColors(self, nums):
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1


if __name__ == '__main__':
    a = [2, 0, 2, 1, 1, 0, 1, 1, 1, 2, 0, 0, 2, 1, 2]
    print Solution().sortColors(a)
    print a
