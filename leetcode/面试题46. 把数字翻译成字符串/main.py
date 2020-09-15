#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def translateNum(self, num):
        """
        dfs的思想，时间复杂度有点高
        """
        if num == 0:
            return 1

        r = 0
        t = 0
        base = 1
        while num > 0:
            # 这里还要考虑 类似 501这样的，中间有个0，01是不能算数的
            if base > 1 and num % 10 == 0:
                break

            t = base * (num % 10) + t
            num /= 10
            base *= 10

            if t > 25:
                break

            if num > 0:
                r2 = self.translateNum(num)
                r += r2
            else:
                r += 1

        return r

    def translateNum2(self, num):
        """
        动态规划思想，对于一个数字来说，从0-i位能产生多少个划分和前面的划分有关系
        首先第i为肯定能单独划分,数字肯定是在0-9之间，第i-1~i位不一定能划分，如果
        范围在10~25之间是能够划分的，所以表达式如下
        f[i] = f[i-1] + f[i-2](有f[i-2]的条件是s[i-1:i+1]的这个数字的范围在10-25)
        因为只涉及到前两位，可以只用两个变量即可
        """
        numStr = str(num)
        p, q = 1, 1
        i = 1
        while i < len(numStr):
            r = 0
            r += p
            if "10" <= numStr[i - 1:i + 1] <= "25":
                r += q

            q = p
            p = r
            i += 1

        return p


if __name__ == '__main__':
    print Solution().translateNum2(12258)
