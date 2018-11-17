# coding=utf-8
import copy


class Solution(object):
    """
    给定两个二进制字符串，返回他们的和（用二进制表示）。
    输入为非空字符串且只包含数字 1 和 0。

    示例 1:
    输入: a = "11", b = "1"
    输出: "100"
    
    示例 2:
    输入: a = "1010", b = "1011"
    输出: "10101"
    """
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r = []
        c = '0'
        a = list(reversed(a))
        b = list(reversed(b))
        for i in xrange(0, max(len(a), len(b))):
            num_of_1 = 1 if c == '1' else 0
            if i < len(a) and a[i] == '1':
                num_of_1 += 1
            if i < len(b) and b[i] == '1':
                num_of_1 += 1

            if num_of_1 == 3:
                r.append('1')
                c = '1'
            elif num_of_1 == 2:
                r.append('0')
                c = '1'
            elif num_of_1 == 1:
                r.append('1')
                c = '0'
            else:
                r.append('0')
                c = '0'

        if c == '1':
            r.append('1')

        return "".join(reversed(r))


if __name__ == '__main__':
    print Solution().addBinary("1010", "1011")
