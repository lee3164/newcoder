#!/usr/bin/env python
# coding=utf-8

"""
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2
示例 2:

输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        signs = []
        nums = []

        i = 0
        for j, c in enumerate(input):
            if c in ("+", "-", "*"):
                signs.append(c)
                nums.append(int(input[i:j]))
                i = j + 1
        nums.append(int(input[i:]))

        def helper(nums, signs):
            if len(nums) == 1:
                return nums

            r = []
            i = 0
            while i < len(signs):
                sign = signs[i]
                r1 = helper(nums[0:i + 1], signs[0:i])
                r2 = helper(nums[i + 1:], signs[i + 1:])
                for n1 in r1:
                    for n2 in r2:
                        if sign == "+":
                            r.append(n1 + n2)
                        elif sign == "-":
                            r.append(n1 - n2)
                        elif sign == "*":
                            r.append(n1 * n2)
                i += 1
            return r

        return helper(nums, signs)


if __name__ == '__main__':
    print Solution().diffWaysToCompute("2*3-4*5")
