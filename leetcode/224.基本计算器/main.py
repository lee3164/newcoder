#!/usr/bin/env python
# coding=utf-8

"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

解析：
本题目中没有 * / ， 利用栈来处理符号和数字，每次数字进栈前先 比较前一个符号，如果是+-，则需要和之前的结果进行运算；
如果是(，则直接进栈，因为(优先级高，需要把后面的结果算完之后再与前面的进行计算，遇到 )的时候，弹出 符号栈，此时一定是一个 (，
因为+，-理论上都会被数字消耗掉，否则语法就有问题。此时符号栈如果还有符号，说明（之前还有运算，继续之前的运算
"""


class Solution(object):

    def add_or_sub(self, a, b, op):
        if op == '+':
            return a + b
        else:
            return a - b

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
            if '0' <= c <= '9':
                j = i + 1
                while j < len(s) and '0' <= s[j] <= '9':
                    j += 1

                n = int(s[i:j])
                if not signs or signs[-1] == '(':
                    nums.append(n)
                else:
                    op = signs.pop()
                    a = nums.pop()
                    nums.append(self.add_or_sub(a, n, op))

                i = j

            elif c in ('(', '+', '-'):
                signs.append(c)
                i += 1
            elif c == ')':
                i += 1
                signs.pop()
                if not signs or signs[-1] == '(':
                    pass
                else:
                    a = nums.pop()
                    b = nums.pop()
                    op = signs.pop()
                    nums.append(self.add_or_sub(b, a, op))
            else:
                i += 1

        return nums[-1]


if __name__ == '__main__':
    print Solution().calculate("0")
