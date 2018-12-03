# coding=utf-8

class Solution(object):
    """
    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

    说明:

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    示例:

    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    输出: [1,2,2,3,5,6]

    如果从前往后排，需要考虑移动位置，当nums2的数比nums1的数字小的时候移动过来肯定要将后面所有的数字都移动一遍
    所以这种可能需要移动位置的可以考虑从后往前排
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        i, j = m - 1, n - 1
        while idx >= 0:
            # 如果 两者都没遍历完，且 nums1的数字大于nums2的数字  或者 nums2遍历完了，那么都去取nums1的数字填充
            # 否则用 nums2的数字填充
            if (i >= 0 and j >= 0 and nums1[i] >= nums2[j]) or (i >= 0 and j < 0):
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 10, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 4, nums2, 3)
    print nums1
