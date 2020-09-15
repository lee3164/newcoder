# coding=utf-8
import bisect


class Solution(object):
    """
    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

    """

    def minSubArrayLen(self, s, nums):
        """
        双指针
        """
        i, j = 0, 0
        c = 0
        m = len(nums) + 1
        while i < len(nums):
            c += nums[i]
            if c >= s:
                while j <= i:
                    if c < s:
                        # 这里两行为什么 不需要，因为满足这个条件的时候，上一轮循环肯定是c>=s
                        # j -= 1
                        # c += nums[j]
                        break
                    else:
                        m = min(m, i - j + 1)
                        c -= nums[j]
                        j += 1
            i += 1
        return 0 if m == len(nums) + 1 else m

    def minSubArrayLen2(self, s, nums):
        """
        前缀和+二分查找
        """
        d = [0 for _ in xrange(len(nums) + 1)]
        r = len(nums) + 1
        for i, n in enumerate(nums):
            d[i + 1] = d[i] + n
            if d[i + 1] >= s:
                j = bisect.bisect_right(d[:i + 1], d[i + 1] - s)
                r = min(r, i - j + 2)

        return r if r <= len(nums) else 0


if __name__ == '__main__':
    print Solution().minSubArrayLen2(7, [2, 3, 1, 2, 4, 3])
