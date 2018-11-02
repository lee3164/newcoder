# coding=utf-8
import copy
import heapq


class Solution(object):
    """
    给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

    示例 1:

    输入: [1,2,0]
    输出: 3
    示例 2:

    输入: [3,4,-1,1]
    输出: 2
    示例 3:

    输入: [7,8,9,11,12]
    输出: 1
    说明:

    你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

    一个 nums的长度 为 len，则1-len的数字极端情况下每个都出现，此时 len+1就是最小的，如果只要有一个没出现，从1-len开始找，找到没出现的那个最小的
    首先便利数组，发现范围是1-len的就做标记，表示是否出现。最后遍历这个标记数组。貌似不是常数空间，可以在原数组进行 bitmap存储
    """
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 1
        bitmap = [False for _ in xrange(len(nums) + 2)]  # 为什么要 +2，因为 0站一位，len(nums) + 1站一位，
        for num in nums:
            if 0 < num <= len(nums):
                bitmap[num] = True

        for i, exist in enumerate(bitmap):
            if i == 0:
                continue
            if not exist:
                return i

    def solve2(self, nums):
        if not nums:
            return 1

        i = 0
        # 如果 nums[i] - 1 代表的是 nums[i] 在 nums应该排的位置，如 [3,2,1]，对于3，在nums应该排 3-1=2第2个位置，从0开始算，
        # 如果两个数不等，就交换，得到[1,2,3]，此时继续算1应该排的位置，如此重复，直到所有在1-len范围的数字都排到了指定位置上
        while i < len(nums):
            while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1



if __name__ == '__main__':
    print Solution().firstMissingPositive([1])
