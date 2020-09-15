#!/usr/bin/env python
# coding=utf-8

"""
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"
（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。
编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：

输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：

输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：

输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：

0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。

链接：https://leetcode-cn.com/problems/pattern-matching-lcci
"""


class Solution(object):
    def patternMatching(self, pattern, value):
        """
        :type pattern: str
        :type value: str
        :rtype: bool
        """
        ac, bc = 0, 0
        for p in pattern:
            if p == 'a':
                ac += 1
            else:
                bc += 1
        t = len(value)

        ab_dict = {}

        def dfs(pattern, value):
            if not pattern and not value:
                return True

            if not pattern:
                return False

            p = pattern[0]

            if p not in ab_dict:
                i = 0
                while i <= len(value):
                    ab_dict[p] = value[:i]

                    a, b = ab_dict.get('a'), ab_dict.get('b')
                    if a == b:
                        i += 1
                        continue

                    if a is not None and b is not None and len(a) * ac + len(b) * bc != t:
                        i += 1
                        continue

                    if dfs(pattern[1:], value[i:]):
                        return True
                    i += 1
                ab_dict.pop(p)
            elif ab_dict[p] == value[:len(ab_dict[p])]:
                return dfs(pattern[1:], value[len(ab_dict[p]):])

            return False

        return dfs(pattern, value)


if __name__ == '__main__':
    print Solution().patternMatching("abba",
                                     "catdogdogcat")
