# coding=utf-8

class Solution(object):
    """
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。

    示例 1:
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4

    示例 2:
    输入: nums = [4,5,6,7,0,1,2], target = 3
    输出: -1
    """

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or nums[-1] < target < nums[0]:
            return -1

        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) / 2
            if nums[m] == target:
                return m
            if nums[s] == target:
                return s
            if nums[e] == target:
                return e

            if nums[s] <= nums[m]:
                if nums[s] < target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
                    e = e - 1
            elif nums[m] < nums[e]:
                if nums[m] < target <= nums[e]:
                    s = m + 1
                else:
                    s = s + 1
                    e = m - 1
        return -1


if __name__ == '__main__':
    print Solution().search([5,1,3], 0)
