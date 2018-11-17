# coding=utf-8
import copy


class Solution(object):
    """
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
    最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。

    示例 1:
    输入: [1,2,3]
    输出: [1,2,4]
    解释: 输入数组表示数字 123。

    示例 2:
    输入: [4,3,2,1]
    输出: [4,3,2,2]
    解释: 输入数组表示数字 4321。
    """
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 这个加上，大多数情况 不用进位
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        c = 1
        i = len(digits) - 1
        while i >= 0:
            s = digits[i] + c
            digits[i] = s % 10
            c = s / 10
            i -= 1

        if c > 0:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    print Solution().plusOne([9, 9, 9, 9])
