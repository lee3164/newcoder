# coding=utf-8


class Solution(object):
    """
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
    必须原地修改，只允许使用额外常数空间。
    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    """

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1

        if i == 0:
            nums[0:] = list(reversed(nums))
            return

        j = i - 1
        while i < len(nums):
            if nums[i] <= nums[j]:  # 此处，应该找 <= 的数字，特殊例子，1，5，1，下一个应该是 5，1，1
                break
            i += 1

        nums[j], nums[i - 1] = nums[i - 1], nums[j]
        nums[j + 1:] = list(reversed(nums[j + 1:]))


if __name__ == '__main__':
    a = [1, 2, 3]
    i = 10
    while i > 0:
        print a
        Solution().nextPermutation(a)
        i -= 1
