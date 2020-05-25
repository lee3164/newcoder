#!/usr/bin/env python
# coding=utf-8

"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。



示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""


class Solution(object):

    def findKthInSortedArrays(self, k, nums1, nums2):
        # type: (int, list, list) -> float
        """
        查找两个有序数组的第k个元素，比较nums1和nums2的第 k/2个元素，
        如果 nums1[k/2] < nums2[k/2]，那么 nums1前k/2个元素都可以排除
        为什么？
        1. 数组有序
        2. 假设此时 nums2的前k/2-1个元素比nums1的第1个都要小，那么 比num1[k/2]小的有
         k/2-1(nums2的前k/2-1个)+k/2-1(num1的前k/2-1)个，即 k-2个，
         nums[k/2]最多是第 k-1小的元素，不是第k小的

        因此 nums1的前 k/2个都可以排除，因此我们只需要在剩下的数组里面找第 k-k/2小的元素
        需要注意临界问题，有的数组长度不够，达不到 k/2个，那么取到它的最长为止
        """
        i, j = 0, 0

        while True:

            if i >= len(nums1):
                return nums2[j + k - 1]
            if j >= len(nums2):
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])

            i1 = min(len(nums1) - i, k / 2)
            j1 = min(len(nums2) - i, k / 2)

            if nums1[i + i1 - 1] <= nums2[j + j1 - 1]:
                i = i + i1
                k -= i1
            else:
                j = j + j1
                k -= j1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_size = len(nums1) + len(nums2)
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.findKthInSortedArrays(total_size / 2 + 1, nums1, nums2)
        else:
            m = self.findKthInSortedArrays(total_size / 2, nums1, nums2)
            n = self.findKthInSortedArrays(total_size / 2 + 1, nums1, nums2)
            return (m + n) / 2.0

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        如果能够找到两个数，i,j分别将nums1和nums2划分成两部分，如下

        A0，A1...Ai-1 | Ai...An
        B0，B1...Bj-1 | Bj...Bm

        如果m+n是偶数
          满足 i+j == n-i+1+m-j+1 => i+j = (m+n+2) / 2 => j = (m+n+2)/2 - i
          且 Bj > Ai-1 && Ai > Bj-1, 通俗点说就是 左边最大的都小于右边最小的
          此时中位数应该是 (max(Ai-1, Bj-1) + min(Ai, Bj)) / 2

        如果m+n是奇数
          满足 i+j-1 = n-i+1+m-j+1 =>  j = (m+n+3) / 2 - i
          且 Bj > Ai-1 && Ai > Bj-1, 通俗点说就是 左边最大的都小于右边最小的
          此时中位数应该是 max(Ai-1, Bj-1)

        其中j和i的关系表达式，可以统一表达为  j = (m + n) / 2 + 1 - i
        因为 2 / 2 == 3 / 2 == 1

        因此 确定了i就可以确定j，我们可以通过2分法来 尝试i的位置，看看是否满足条件，然后不断调整
        直到最终满足条件
        """


if __name__ == '__main__':
    # print Solution().findKthInSortedArrays(7, [1, ], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print Solution().findMedianSortedArrays([2], [1, 3, 4])
