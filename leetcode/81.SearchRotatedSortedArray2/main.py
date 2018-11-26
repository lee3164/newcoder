# coding=utf-8
class Solution(object):
    """
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。

    ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

    编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

    示例 1:

    输入: nums = [2,5,6,0,0,1,2], target = 0
    输出: true
    示例 2:

    输入: nums = [2,5,6,0,0,1,2], target = 3
    输出: false
    进阶:

    这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
    这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

    最主要的问题就是 如果 nums[m] == nums[l] == nums[r]的情况下无法确定m在左半部分还是右，这种情况下只能退化为线性查找
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if target == nums[m]:
                return True
            if target == nums[l]:
                return True
            if target == nums[r]:
                return True

            if nums[m] > nums[l]:
                if nums[l] < target < nums[m]:
                    l = l + 1
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] < target < nums[r]:
                    l = m + 1
                    r = r - 1
                else:
                    r = m - 1
            else:
                # 极端情况 如 1,1,1,1,3,1,1,1,1无数个1，此时nums[m] == 1，无法确定m在左还是右，只能退化为线性查找
                l += 1
                r -= 1
        return False


if __name__ == '__main__':
    print Solution().search([1, 2, 3, 4, 5, 6, 7, -1, 0], 4)
