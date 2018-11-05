# coding=utf-8
import copy


class Solution(object):
    def next_permutation(self, nums):
        nums = copy.copy(nums)
        i = len(nums) - 1
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

    def permuteUnique(self, nums):
        """
        这种解法有bug，还不清楚bug在哪里
        :param nums:
        :return:
        """
        r = []
        nums = sorted(nums)

        def dfs(nums, s, arr):
            arr = copy.copy(arr)
            if s == len(nums):
                r.append(arr)
                return

            # i = s
            # used_num = set()
            # while i < len(nums):
            #     if nums[i] in used_num:
            #         i += 1
            #         continue
            #     arr.append(nums[i])
            #     nums[i], nums[s] = nums[s], nums[i]
            #     dfs(nums, s + 1, arr)
            #     nums[i], nums[s] = nums[s], nums[i]
            #     arr.pop()
            #     used_num.add(nums[i])
            #     i += 1

            i = s
            prev = None
            while i < len(nums):
                if i != s and (nums[i] == prev or nums[i] == nums[s]):
                    i += 1
                    continue
                arr.append(nums[i])
                nums[i], nums[s] = nums[s], nums[i]
                dfs(nums, s + 1, arr)
                nums[i], nums[s] = nums[s], nums[i]
                arr.pop()
                prev = nums[i]
                i += 1

        dfs(nums, 0, [])
        return r


if __name__ == '__main__':
    print Solution().permuteUnique([0, 1, 0, 0, 9])
