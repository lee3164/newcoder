# coding=utf-8
import copy


class Solution(object):
    """
    给定一个没有重复数字的序列，返回其所有可能的全排列。

    示例:

    输入: [1,2,3]
    输出:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]

    1.用全排列标准方法
    2.用回溯法
    """

    def next_permutation(self, nums):
        nums = copy.copy(nums)
        i = len(nums) - 1
        # 首先从后往前找到一个 最高点，如 6 2 5 4 3 1, 第一个应该找到5
        # 然后应该考虑 让 5后面的数字和前面某一个进行交换，如上，如果把1交换到前面，只会更小，所以要吧5后面的最后
        # 一个大于2的数字移到前面去，变成 6 3 5 4 2 1，此时5后面的数字仍然有序且是倒序，然后反转5后面的序列
        # 得到 6 3 1 2 3 4 5，每一个数字能够得到其下一轮的数字，知道重复为止
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i > 0:
            j, k = i - 1, i
            while k + 1 < len(nums) and nums[k + 1] > nums[j]:
                k += 1
            nums[j], nums[k] = nums[k], nums[j]
        nums[i:] = nums[::-1][:len(nums) - i]
        return nums

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        nums = sorted(nums)
        r.append(nums)
        a = self.next_permutation(nums)
        while a != nums:
            r.append(a)
            a = self.next_permutation(a)
        return r

    def permute2(self, nums):
        """
        每次回溯该位置能够用的数字，如第一位可以用n个数字，so，每次用到了这个数字就把他放前面来，
        然后start+1，进入下一轮回溯，
        """
        r = []

        def dfs(nums, s, arr):
            arr = copy.copy(arr)
            if s == len(nums):
                r.append(arr)
                return

            i = s
            while i < len(nums):
                arr.append(nums[i])
                nums[i], nums[s] = nums[s], nums[i]  # 把该轮用到的数字放到前面来
                dfs(nums, s + 1, arr)
                nums[i], nums[s] = nums[s], nums[i]  # 用完了放回去
                arr.pop()
                i += 1

        dfs(nums, 0, [])
        return r


if __name__ == '__main__':
    print Solution().permute2([1, 2, 3, 4])
