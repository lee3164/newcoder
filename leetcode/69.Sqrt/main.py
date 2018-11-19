# coding=utf-8

class Solution(object):
    """
    实现 int sqrt(int x) 函数。

    计算并返回 x 的平方根，其中 x 是非负整数。

    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

    示例 1:

    输入: 4
    输出: 2
    示例 2:

    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

     使用类似二分查找的方式，开方结果必定在1-x之间（0，1特殊，可单独处理）
    """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l, r = 1, x
        while l < r:
            m = (l + r) / 2
            y = m * m
            if y == x:
                return m
            if y > x:
                r = m - 1
            else:
                l = m + 1

        if r * r <= x:
            return r
        return r - 1


if __name__ == '__main__':
    print Solution().mySqrt(26)
