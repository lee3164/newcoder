# coding=utf-8

class Solution(object):
    """
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。

    示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]

    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]

    解析：两个二分查找，一个查左边界，一个查右边界，注意边界条件
    """

    def search_left(self, nums, target):
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) / 2

            # 两种情况，一是target在最左边，此时nums[m-1]不不存在，另外一个就是正常情况，存在且target比它大
            if nums[m] == target and ((m > 0 and nums[m] > nums[m - 1]) or m == 0):
                return m

            # 如果nums[m] == target 不是在最左边，那么进入下面判断
            if nums[m] >= target:
                e = m - 1
            else:
                s = m + 1
        return -1

    def search_right(self, nums, target):
        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) / 2
            if nums[m] == target and ((m < len(nums) - 1 and nums[m] < nums[m + 1]) or m == len(nums) - 1):
                return m
            if nums[m] <= target:
                s = m + 1
            else:
                e = m - 1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.search_left(nums, target), self.search_right(nums, target)]


if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8, 10], 6)
