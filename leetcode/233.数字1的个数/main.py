#!/usr/bin/env python
# coding=utf-8

"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

链接：https://leetcode-cn.com/problems/number-of-digit-one

213.0

001 011 021 031 041 051 061 ... 211 => 22

01x 11x 21x  => 20+4

01xx => 100

设N = abcde ,其中abcde分别为十进制中各位上的数字。
    如果要计算百位上1出现的次数，它要受到3方面的影响：百位上的数字，百位以下（低位）的数字，百位以上（高位）的数字。
    如果百位上数字为0，百位上可能出现1的次数由更高位决定。比如：12013，则可以知道百位出现1的情况可能是：100~199，1100~1199,2100~2199，
    ，...，11100~11199，一共1200个。可以看出是由更高位数字（12）决定，并且等于更高位数字（12）乘以 当前位数（100）。注意：高位数字不包括当前位
    如果百位上数字为1，百位上可能出现1的次数不仅受更高位影响还受低位影响。比如：12113，则可以知道百位受高位影响出现的情况是：
    100~199，1100~1199,2100~2199，，....，11100~11199，一共1200个。和上面情况一样，并且等于更高位数字（12）乘以 当前位数（100）。
    但同时它还受低位影响，百位出现1的情况是：12100~12113,一共14个，等于低位数字（13）+1。 注意：低位数字不包括当前数字
    如果百位上数字大于1（2~9），则百位上出现1的情况仅由更高位决定，比如12213，则百位出现1的情况是：100~199,1100~1199，2100~2199，
    ...，11100~11199,12100~12199,一共有1300个，并且等于更高位数字+1（12+1）乘以当前位数（100）
*/
"""


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        base = 1  # 保存位数，从各位开始
        num = n
        while n > 0:
            i = n % 10  # 当前数字
            if i == 0:
                r += base * (n / 10)
            elif i == 1:
                r += base * (n / 10) + (num % base) + 1
            else:
                r += base * (n / 10 + 1)
            n /= 10
            base *= 10
        return r


if __name__ == '__main__':
    print Solution().countDigitOne(213)
