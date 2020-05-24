#!/usr/bin/env python
# coding=utf-8

"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

链接：https://leetcode-cn.com/problems/minimum-window-substring

1。子串开头结尾必定是T中的一个字符；

"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c_count_dict = {}
        for c in t:
            c_count_dict.setdefault(c, 0)
            c_count_dict[c] += 1

        r = ""
        c_idx_list = {}
        count = 0
        for i, c in enumerate(s):
            if c not in t:
                continue

            c_idx_list.setdefault(c, [])
            if len(c_idx_list[c]) == c_count_dict[c]:
                count -= 1
                c_idx_list[c].pop(0)

            count += 1
            c_idx_list[c].append(i)

            if count == len(t):
                mi = i
                for _, idx_list in c_idx_list.iteritems():
                    mi = min(mi, idx_list[0])

                if r == "":
                    r = s[mi:i + 1]
                elif i + 1 - mi < len(r):
                    r = s[mi:i + 1]
        return r


if __name__ == '__main__':
    print Solution().minWindow("aa", "aa")
