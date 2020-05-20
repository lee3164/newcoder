#!/usr/bin/env python
# coding=utf-8

"""
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 

提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。

链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts

解析见链接答案
"""


class Solution(object):
    def findTheLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = ('a', 'e', 'i', 'o', 'u')
        size = len(s)
        dp = {
            'a': [[0 for _ in xrange(size)] for _ in xrange(size)],
            'e': [[0 for _ in xrange(size)] for _ in xrange(size)],
            'i': [[0 for _ in xrange(size)] for _ in xrange(size)],
            'o': [[0 for _ in xrange(size)] for _ in xrange(size)],
            'u': [[0 for _ in xrange(size)] for _ in xrange(size)]
        }

        i = 0
        r = 0
        while i < size:
            j = i
            while j >= 0:
                c = s[j]
                if c in l:
                    if i == j:
                        dp[c][j][i] = 1
                    else:
                        dp[c][j][i] = dp[c][j + 1][i] + 1

                for c in l:
                    if j < i and c != s[j]:
                        dp[c][j][i] = dp[c][j + 1][i]

                valid = True
                for c in l:
                    if dp[c][j][i] % 2 != 0:
                        valid = False
                        break

                if valid:
                    r = max(i - j + 1, r)

                j -= 1

            i += 1

        return r

    def findTheLongestSubstring(self, s):
        pos = [-1 for _ in xrange(1 << 5)]
        pos[0] = 0
        status = 0
        r = 0
        for i, c in enumerate(s):
            if c == 'a':
                status ^= 1 << 0
            elif c == 'e':
                status ^= 1 << 1
            elif c == 'i':
                status ^= 1 << 2
            elif c == 'o':
                status ^= 1 << 3
            elif c == 'u':
                status ^= 1 << 4

            if pos[status] != -1:
                r = max(r, i + 1 - pos[status])
            else:
                pos[status] = i + 1

        return r


if __name__ == '__main__':
    print Solution().findTheLongestSubstring("leetcodeisgreat")
