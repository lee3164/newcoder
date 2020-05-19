#!/usr/bin/env python
# coding=utf-8
from collections import defaultdict

"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

链接：https://leetcode-cn.com/problems/valid-palindrome-ii

f[i, j] == f[i+1, j-1] and s[i]==s[j]
           f[i+1, j] 删除 s[i] and d[i+1, j] == 0
           f[i, j-1] 删除 s[j] and d[i, j-1] == 0
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        动态规划反而复杂了
        """
        size = len(s)
        d = [[0 for _ in xrange(size)] for _ in xrange(size)]
        f = [[0 for _ in xrange(size)] for _ in xrange(size)]
        i = size - 1
        while i >= 0:
            j = i
            while j <= size - 1:
                if i == j:
                    f[i][j] = 1
                    d[i][j] = 0
                elif s[i] == s[j] and (i + 1 >= j - 1 or f[i + 1][j - 1] == 1):
                    f[i][j] = 1
                    d[i][j] = d[i + 1][j - 1]
                elif f[i + 1][j] == 1 and d[i + 1][j] == 0 or f[i][j - 1] == 1 and d[i][j - 1] == 0:
                    f[i][j] = 1
                    d[i][j] = 1
                else:
                    f[i][j] = 0

                j += 1
            i -= 1
        return bool(f[0][len(s) - 1])

    def validPalindrome2(self, s):
        """
        用递归的方式更清晰，但是会产生栈溢出
        """
        i = 0
        j = len(s) - 1
        deleted = False

        checkpoint = None

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif not deleted and (s[i] == s[j - 1] or s[i + 1] == s[j]):
                deleted = True
                if s[i] == s[j - 1]:
                    if s[i + 1] == s[j]:
                        checkpoint = (i + 2, j - 1)
                    i += 1
                    j -= 2
                else:
                    i += 2
                    j -= 1
            elif checkpoint:
                i, j = checkpoint
                checkpoint = None
            else:
                return False

        return True


if __name__ == '__main__':
    s = "ebcbbececabbacecbbcbe"
    print Solution().validPalindrome2(s)
