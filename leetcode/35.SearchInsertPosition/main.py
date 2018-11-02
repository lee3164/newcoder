# coding=utf-8

class Solution(object):
    """
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。

    示例 1:
    输入: [1,3,5,6], 5
    输出: 2

    示例 2:
    输入: [1,3,5,6], 2
    输出: 1

    示例 3:
    输入: [1,3,5,6], 7
    输出: 4

    示例 4:
    输入: [1,3,5,6], 0
    输出: 0
    """

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 先判断下边界条件，简单的预处理，对于很小或很大的数字不用浪费时间去搜索，直接插入指定位置
        if not nums or nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        s, e = 0, len(nums) - 1

        while s <= e:
            m = (s + e) / 2
            if nums[m] == target or nums[m - 1] < target < nums[m]:
                return m

            if nums[m] < target:
                s = m + 1
            else:
                e = m - 1


if __name__ == '__main__':
    print Solution().searchInsert([1, 3], 2)
