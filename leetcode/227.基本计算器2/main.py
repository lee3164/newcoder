#!/usr/bin/env python
# coding=utf-8

"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

链接：https://leetcode-cn.com/problems/basic-calculator-ii

*/立即计算，+-延迟计算，可以将-改为 +，结尾直接sum即可，如 1-2 == 1 + -2
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        signs = []

        i = 0
        while i < len(s):
            c = s[i]
            if c == ' ':
                i += 1
                continue

            if c.isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                n = int(s[i:j])
                i = j

                if not nums or not signs or signs[-1] in ('+', '-'):
                    nums.append(n)
                else:
                    op = signs.pop()
                    n2 = nums.pop()
                    if op == '*':
                        nums.append(n2 * n)
                    else:
                        nums.append(n2 / n)
            else:
                signs.append(c)
                i += 1

        r = nums.pop(0)
        while signs:
            op = signs.pop(0)
            if op == '+':
                r = r + nums.pop(0)
            else:
                r = r - nums.pop(0)

        return r

    def calculate2(self, s):
        sign = '+'
        s += "+"
        stack = []
        num = 0
        for ch in s:
            if ch >= '0' and ch <= '9':
                num = 10 * num + int(ch)
                continue

            if ch == " ":
                continue

            if sign == '+':
                stack.append(num)

            if sign == '-':
                stack.append(-num)

            if sign == "*":
                pre = stack.pop()
                stack.append(pre * num)

            if sign == '/':
                pre = stack.pop()
                stack.append(int(pre / num))

            sign = ch
            num = 0

        return sum(stack)


if __name__ == '__main__':
    s = " 3/2 "
    print Solution().calculate(s)
