#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        nums = [c for c in num]
        sort_nums = sorted(nums)
        if nums == sort_nums:
            return num

        r = []
        kth_nums = sorted((n, i) for i, n in enumerate(nums))

        while nums and k > 0:
            mi = kth_nums[0][1]
            k -= mi
            r.append(nums[mi])
            del nums[mi]

            if r + nums == sort_nums:
                break

            new_kth_nums = []
            for n, idx in kth_nums[1:]:
                if idx > mi:
                    idx -= 1
                if idx <= k:
                    new_kth_nums.append((n, idx))

            kth_nums = new_kth_nums

        return "".join(r + nums)


if __name__ == '__main__':
    print Solution().minInteger("294984148179", 11)
