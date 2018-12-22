# coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


import copy


class Solution(object):
    """
    给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
    一个字符串的一个子序列是指，通过删除一些（也可以不删除）
    字符且不干扰剩余字符相对位置所组成的新字符串。
    （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

    示例 1:
    输入: S = "rabbbit", T = "rabbit"
    输出: 3
    解释:
    如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
    (上箭头符号 ^ 表示选取的字母)
    rabbbit
    ^^^^ ^^
    rabbbit
    ^^ ^^^^
    rabbbit
    ^^^ ^^^

    示例 2:
    输入: S = "babgbag", T = "bag"
    输出: 5
    解释:
    如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
    (上箭头符号 ^ 表示选取的字母)
    babgbag
    ^^ ^
    babgbag
    ^^    ^
    babgbag
    ^    ^^
    babgbag
    ^  ^^
    babgbag
        ^^^

    典型的动态规划，设f[i][j] 长度为i的t子串和j的s子串中符合这个条件的个数
    当 t[i] == s[j]的时候，如果使用当前字符，那么f[i][j] += f[i-1][j-1]，
    如果不用的话，那么f[i][j] += f[i][j-1]
    注意 f[i][0] = 0
    f[0][j] = 1 因为空串总和空串匹配
    """
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        f = [[0 for _ in xrange(len(s) + 1)] for _ in xrange(len(t) + 1)]
        i = 0
        while i <= len(t):
            f[i][0] = 0
            i += 1
        j = 0
        while j <= len(s):
            f[0][j] = 1
            j += 1
        i = 1
        while i <= len(t):
            j = i
            while j <= len(s):
                f[i][j] = f[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    f[i][j] += f[i - 1][j - 1]
                j += 1
            i += 1

        return f[-1][-1]


if __name__ == '__main__':
    print Solution().numDistinct("babgbag", "bag")
