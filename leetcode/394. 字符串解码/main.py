#!/usr/bin/env python
# coding=utf-8

"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

链接：https://leetcode-cn.com/problems/decode-string
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        b = 0
        m = 0
        r = []
        n = 0
        while i < len(s):
            c = s[i]
            if '0' <= c <= '9' and n == 0:
                b = 10 * b + int(c)
            elif c == '[':
                if n == 0:
                    m = i + 1
                n += 1
            elif c == ']':
                n -= 1
                if n == 0:
                    substr = s[m:i]
                    r.append(b * self.decodeString(substr))
                    b = 0
            elif b == 0:
                r.append(c)

            i += 1

        return "".join(r)

    def decodeString2(self, s):
        st = []
        count = 0
        for i, c in enumerate(s):
            if '0' <= c <= '9':
                count = count * 10 + int(c)
            elif c == '[':
                st.append(count)
                count = 0
            elif c == ']':
                t = []
                while st:
                    j = st.pop()
                    if isinstance(j, int):
                        st.append("".join(j * t))
                        break
                    else:
                        t.insert(0, j)
            else:
                st.append(c)

        return st.pop()


if __name__ == '__main__':
    print Solution().decodeString2("3[a2[c]]")
